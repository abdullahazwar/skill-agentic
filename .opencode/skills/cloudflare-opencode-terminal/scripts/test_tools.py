#!/usr/bin/env python3
"""Test lokal untuk parser, estimator dan constraint SQL bawaan."""
import argparse
import json
import sqlite3
import tempfile
import unittest
from pathlib import Path

from doctor import inspect, parse_jsonc
from estimasi import estimate, nonnegative

ROOT = Path(__file__).resolve().parents[1]


def inputs(**overrides):
    values = dict(users=20, actions=15, api_per_action=1, cron_minutes=0,
                  monitor_minutes=0, retry_percent=0, external_calls=0,
                  kv_reads=0, kv_writes=0, kv_reads_tick=0, kv_writes_tick=0,
                  d1_rows_read=0, d1_rows_written=0,
                  d1_rows_read_tick=0, d1_rows_written_tick=0, days=30)
    values.update(overrides)
    return values


class JsoncTests(unittest.TestCase):
    def test_comment_dan_url_dalam_string(self):
        source = '{"url":"https://example.test/a//b","x":1,// komentar\n}'
        self.assertEqual(parse_jsonc(source)["url"], "https://example.test/a//b")

    def test_block_escape_trailing_comma(self):
        source = '{"s":"a\\\"b,}","arr":[1,/* komentar */2,],}'
        parsed = parse_jsonc(source)
        self.assertEqual(parsed["s"], 'a"b,}')
        self.assertEqual(parsed["arr"], [1, 2])

    def test_invalid_tidak_diterima(self):
        for source in ('{"x":1 /*', '{"a":}', "[]"):
            with self.assertRaises(ValueError):
                parse_jsonc(source)

    def test_comment_tidak_menggabungkan_token(self):
        with self.assertRaises(ValueError):
            parse_jsonc('{"a":1/*x*/2}')


class DoctorTests(unittest.TestCase):
    def test_temuan_secret_tidak_membuka_nilai(self):
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp)
            (project / "src").mkdir()
            (project / "src/index.ts").write_text("export default {}")
            config = dict(name="test", main="src/index.ts",
                          compatibility_date="2026-01-01",
                          vars={"API_TOKEN": "SAMPLE_PRIVATE_VALUE"},
                          triggers={"crons": ["* * * * *"]})
            (project / "wrangler.jsonc").write_text(json.dumps(config))
            result = inspect(project)
            codes = {f["code"] for f in result["findings"]}
            self.assertIn("SECRET_IN_VARS", codes)
            self.assertIn("FREQUENT_CRON", codes)
            self.assertNotIn("SAMPLE_PRIVATE_VALUE", json.dumps(result))

    def test_config_tidak_ada(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(inspect(Path(tmp))["findings"][0]["code"], "CONFIG_MISSING")


class EstimateTests(unittest.TestCase):
    def test_cron_tetap_jalan_tanpa_user(self):
        daily = estimate(inputs(users=0, cron_minutes=5))["daily"]
        self.assertEqual(daily["http_total_estimate"], 0)
        self.assertEqual(daily["cron_invocations"], 288)

    def test_bedakan_http_storage_dan_subrequest(self):
        result = estimate(inputs(cron_minutes=60, monitor_minutes=10,
                                 retry_percent=10, external_calls=2,
                                 kv_reads=1, d1_rows_read_tick=3))
        daily = result["daily"]
        self.assertEqual(daily["http_total_estimate"], 474)
        self.assertEqual(daily["external_subrequests_estimate"], 600)
        self.assertEqual(daily["kv_reads_estimate"], 300)
        self.assertEqual(daily["d1_rows_read_estimate"], 72)
        self.assertEqual(result["period"]["cron_invocations"], 720)

    def test_angka_tidak_valid(self):
        for value in ("-1", "nan", "inf"):
            with self.assertRaises(argparse.ArgumentTypeError):
                nonnegative(value)


class SchemaTests(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect(":memory:")
        self.db.execute("PRAGMA foreign_keys=ON")
        self.db.executescript((ROOT / "assets/sql/0001_initial.sql").read_text())
        self.db.execute("INSERT INTO users(id,created_at) VALUES('a',1),('b',1)")

    def tearDown(self):
        self.db.close()

    def transaction(self, identity="t", user="a", key="key", amount=100):
        self.db.execute(
            "INSERT INTO transactions(id,user_id,kind,amount_rupiah,wallet,"
            "occurred_at,created_at,idempotency_key,payload_fingerprint)"
            "VALUES(?,?,'expense',?,'TUNAI',1,1,?,'fingerprint')",
            (identity, user, amount, key))

    def test_idempotensi_dibatasi_pemilik(self):
        self.transaction()
        with self.assertRaises(sqlite3.IntegrityError):
            self.transaction(identity="t2")
        self.transaction(identity="t3", user="b")
        row = self.db.execute(
            "SELECT id FROM transactions WHERE user_id=? AND id=?", ("b", "t")
        ).fetchone()
        self.assertIsNone(row)

    def test_nominal_dan_fk(self):
        with self.assertRaises(sqlite3.IntegrityError):
            self.transaction(amount=-1)
        with self.assertRaises(sqlite3.IntegrityError):
            self.transaction(user="tidak-ada")

    def test_conditional_claim_dan_index(self):
        self.db.execute(
            "INSERT INTO reminder_jobs(id,user_id,chat_id,title,due_at,next_attempt_at,created_at)"
            "VALUES('j','a','1','ingat',10,10,1)")
        sql = "UPDATE reminder_jobs SET status='processing',claim_token=? WHERE id='j' AND status='pending'"
        self.assertEqual(self.db.execute(sql, ("claim1",)).rowcount, 1)
        self.assertEqual(self.db.execute(sql, ("claim2",)).rowcount, 0)
        plan = self.db.execute(
            "EXPLAIN QUERY PLAN SELECT id FROM reminder_jobs "
            "WHERE status='pending' AND next_attempt_at<=10 ORDER BY next_attempt_at LIMIT 50"
        ).fetchall()
        self.assertTrue(any("idx_reminders_due" in str(row) for row in plan))


if __name__ == "__main__":
    unittest.main()
