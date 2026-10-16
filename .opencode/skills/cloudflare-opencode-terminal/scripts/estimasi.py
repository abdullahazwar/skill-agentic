#!/usr/bin/env python3
"""Proyeksi volume Cloudflare. Tidak menghitung tagihan atau menetapkan kuota."""
from __future__ import annotations

import argparse
import json
import math
from collections.abc import Mapping


def nonnegative(value: str) -> float:
    number = float(value)
    if not math.isfinite(number) or number < 0:
        raise argparse.ArgumentTypeError("Gunakan angka nonnegatif yang finite.")
    return number


def estimate(values: Mapping[str, float]) -> dict:
    actions = values["users"] * values["actions"]
    cron = math.ceil(1440 / values["cron_minutes"]) if values["cron_minutes"] else 0
    monitor = math.ceil(1440 / values["monitor_minutes"]) if values["monitor_minutes"] else 0
    api = actions * values["api_per_action"]
    retries = api * values["retry_percent"] / 100
    daily = {
        "actions": actions,
        "http_from_actions": api,
        "http_retry_estimate": retries,
        "http_monitor": monitor,
        "http_total_estimate": api + retries + monitor,
        "cron_invocations": cron,
        "external_subrequests_estimate": actions * values["external_calls"],
        "kv_reads_estimate": actions * values["kv_reads"] + cron * values["kv_reads_tick"],
        "kv_writes_estimate": actions * values["kv_writes"] + cron * values["kv_writes_tick"],
        "d1_rows_read_estimate": actions * values["d1_rows_read"] + cron * values["d1_rows_read_tick"],
        "d1_rows_written_estimate": actions * values["d1_rows_written"] + cron * values["d1_rows_written_tick"],
    }
    return {
        "days": values["days"],
        "daily": daily,
        "period": {key: amount * values["days"] for key, amount in daily.items()},
        "scope": (
            "Proyeksi dasar. HTTP dan cron dipisahkan. Operasi ulang akibat retry, traffic publik, "
            "CPU, storage, DO, queue, AI dan billing produk belum dimodelkan otomatis."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    options = {
        "users": (20, "User aktif per hari."),
        "actions": (15, "Aksi per user per hari."),
        "api-per-action": (1, "HTTP API per aksi."),
        "cron-minutes": (0, "Interval cron menit, 0 untuk tanpa cron."),
        "monitor-minutes": (0, "Interval monitor HTTP menit, 0 untuk tanpa monitor."),
        "retry-percent": (0, "Tambahan persen request HTTP akibat retry."),
        "external-calls": (0, "Subrequest provider per aksi."),
        "kv-reads": (0, "KV read per aksi."),
        "kv-writes": (0, "KV write per aksi."),
        "kv-reads-tick": (0, "KV read per tick cron."),
        "kv-writes-tick": (0, "KV write per tick cron."),
        "d1-rows-read": (0, "Baris D1 dibaca per aksi, bukan jumlah query."),
        "d1-rows-written": (0, "Baris D1 ditulis per aksi."),
        "d1-rows-read-tick": (0, "Baris D1 dibaca per tick cron."),
        "d1-rows-written-tick": (0, "Baris D1 ditulis per tick cron."),
        "days": (30, "Jumlah hari proyeksi."),
    }
    for name, (default, help_text) in options.items():
        parser.add_argument("--" + name, type=nonnegative, default=default, help=help_text)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = estimate(vars(args))
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return
    print(f'Proyeksi {result["days"]:g} hari')
    for key, amount in result["daily"].items():
        print(f'{key}: {amount:g}/hari, {result["period"][key]:g}/periode')
    print(result["scope"])


if __name__ == "__main__":
    main()
