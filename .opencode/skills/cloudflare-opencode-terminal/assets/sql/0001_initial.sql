-- Contoh awal. Jalankan pada database baru/lokal dan sesuaikan kebutuhan.
-- Semua waktu menggunakan epoch detik UTC, uang menggunakan integer Rupiah.
CREATE TABLE users (
  id TEXT PRIMARY KEY,
  timezone TEXT NOT NULL DEFAULT 'Asia/Jakarta',
  created_at INTEGER NOT NULL
);

CREATE TABLE transactions (
  id TEXT PRIMARY KEY,
  user_id TEXT NOT NULL REFERENCES users(id) ON DELETE RESTRICT,
  kind TEXT NOT NULL CHECK (kind IN ('income', 'expense')),
  amount_rupiah INTEGER NOT NULL CHECK (amount_rupiah > 0),
  wallet TEXT NOT NULL,
  category TEXT NOT NULL DEFAULT 'Lainnya',
  note TEXT NOT NULL DEFAULT '',
  occurred_at INTEGER NOT NULL,
  created_at INTEGER NOT NULL,
  idempotency_key TEXT NOT NULL,
  payload_fingerprint TEXT NOT NULL,
  UNIQUE (user_id, idempotency_key)
);
CREATE INDEX idx_transactions_user_time ON transactions(user_id, occurred_at);

CREATE TABLE webhook_inbox (
  bot_id TEXT NOT NULL,
  update_id INTEGER NOT NULL,
  status TEXT NOT NULL DEFAULT 'pending'
    CHECK (status IN ('pending', 'processing', 'done', 'failed')),
  payload_json TEXT NOT NULL,
  attempts INTEGER NOT NULL DEFAULT 0 CHECK (attempts >= 0),
  next_attempt_at INTEGER NOT NULL,
  lease_until INTEGER,
  claim_token TEXT,
  created_at INTEGER NOT NULL,
  completed_at INTEGER,
  PRIMARY KEY (bot_id, update_id)
);
CREATE INDEX idx_inbox_due ON webhook_inbox(status, next_attempt_at);
CREATE INDEX idx_inbox_lease ON webhook_inbox(status, lease_until);

CREATE TABLE reminder_jobs (
  id TEXT PRIMARY KEY,
  user_id TEXT NOT NULL REFERENCES users(id) ON DELETE RESTRICT,
  chat_id TEXT NOT NULL,
  title TEXT NOT NULL,
  due_at INTEGER NOT NULL,
  timezone TEXT NOT NULL DEFAULT 'Asia/Jakarta',
  status TEXT NOT NULL DEFAULT 'pending'
    CHECK (status IN ('pending', 'processing', 'sent', 'failed', 'cancelled')),
  attempts INTEGER NOT NULL DEFAULT 0 CHECK (attempts >= 0),
  next_attempt_at INTEGER NOT NULL,
  lease_until INTEGER,
  claim_token TEXT,
  sent_message_id TEXT,
  created_at INTEGER NOT NULL,
  sent_at INTEGER
);
CREATE INDEX idx_reminders_due ON reminder_jobs(status, next_attempt_at);
CREATE INDEX idx_reminders_lease ON reminder_jobs(status, lease_until);
CREATE INDEX idx_reminders_user_time ON reminder_jobs(user_id, due_at);
