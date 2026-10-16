# Wrangler dan konfigurasi

## Isi

- Dasar proyek
- Binding dan environment
- Secret
- Perintah operasi
- Validasi

## Dasar proyek

Gunakan Wrangler lokal yang dikunci lockfile. Pakai npx wrangler agar versi konsisten. Periksa help versi terpasang sebelum memakai subcommand baru.

Preferensikan wrangler.jsonc pada proyek baru. Pertahankan TOML proyek lama bila berfungsi. Jangan membuat dua konfigurasi yang berbeda.

    {
      "$schema": "./node_modules/wrangler/config-schema.json",
      "name": "aplikasi-contoh",
      "main": "src/index.ts",
      "compatibility_date": "2026-10-16",
      "workers_dev": true,
      "vars": { "APP_ENV": "development" },
      "observability": { "enabled": true }
    }

Ganti tanggal contoh dengan tanggal pembuatan. Jangan menambah compatibility_flags tanpa kebutuhan. Generate tipe setelah binding berubah.

    npx wrangler types
    npx tsc --noEmit

## Binding dan environment

Nama binding case-sensitive. ID berbeda dari nama tampilan. Ambil ID dari hasil create/list atau dashboard akun yang tepat.

    {
      "d1_databases": [{
        "binding": "DB",
        "database_name": "aplikasi-db",
        "database_id": "<ID-DATABASE>",
        "migrations_dir": "migrations"
      }],
      "kv_namespaces": [{ "binding": "CACHE", "id": "<ID-KV>" }],
      "r2_buckets": [{ "binding": "FILES", "bucket_name": "aplikasi-files" }]
    }

Gabungkan fragmen ke config proyek. Tambah hanya resource yang perlu. Jangan mengganti resource lama dengan resource kosong tanpa kebutuhan.

Gunakan env.staging dan env.production sesuai proyek. Banyak binding dan vars tidak diwariskan. Deklarasikan ulang pada environment tujuan dan periksa schema Wrangler terkini.

Gunakan --env yang sama pada types, migration, secret, dry-run, tail dan deploy untuk named environment. Pisahkan database, namespace dan bucket staging dari produksi.

## Secret

Simpan non-secret pada vars. Simpan rahasia lokal pada .dev.vars atau env lokal yang didukung. Jangan commit .dev.vars, .env, file token dan backup pelanggan.

    npx wrangler secret put TELEGRAM_BOT_TOKEN
    npx wrangler secret put TELEGRAM_WEBHOOK_SECRET
    npx wrangler secret list

Put meminta nilai lewat input. List memeriksa nama secret. Tambahkan --env production jika itu target konfigurasi. Jangan menaruh nilai secret sebagai argumen CLI.

| Nama | Pemakaian |
| --- | --- |
| TELEGRAM_BOT_TOKEN | Token BotFather |
| TELEGRAM_WEBHOOK_SECRET | Nilai acak untuk header webhook |
| TURNSTILE_SECRET_KEY | Verifikasi Turnstile backend |
| QWEN_API_KEY | Key provider Qwen |
| DEEPSEEK_API_KEY | Key provider DeepSeek |
| SESSION_SIGNING_SECRET | Penandatangan sesi bila diperlukan |
| CLOUDFLARE_API_TOKEN | Administrasi/CI, bukan akses binding aplikasi |

Webhook secret bukan API key yang dibeli. Generate dengan sumber acak kriptografi. Nonaktifkan setup endpoint atau rotasi secret bootstrap setelah dipakai.

## Perintah operasi

    npx wrangler whoami
    npx wrangler dev
    npx wrangler deploy --dry-run
    npx wrangler deploy
    npx wrangler tail
    npx wrangler kv namespace create CACHE
    npx wrangler d1 create aplikasi-db
    npx wrangler r2 bucket create aplikasi-files
    npx wrangler d1 migrations create aplikasi-db initial
    npx wrangler d1 migrations apply aplikasi-db --local
    npx wrangler d1 migrations apply aplikasi-db --remote
    npx wrangler d1 export aplikasi-db --remote --output backup.sql
    npx wrangler deployments list
    npx wrangler versions list

Create, migration remote, deploy dan secret put mengubah state. Jalankan pada target yang ditentukan. Ekspor mengandung data dan perlu disimpan privat.

## Validasi

1. Periksa akun, Worker, environment, route dan ID binding.
2. Pastikan assets berisi hasil build dan tidak memuat rahasia.
3. Generate tipe, typecheck, test lalu dry-run.
4. Baca warning dan perubahan trigger/route.
5. Ingat dry-run tidak memverifikasi secret remote, DNS atau izin akun.

Dokumentasi CLI dapat berubah. Jangan menerapkan sintaks cf CLI pada proyek Wrangler atau memigrasikan CLI saat perbaikan tanpa kebutuhan.

Sumber: https://developers.cloudflare.com/workers/wrangler/configuration/
Sumber: https://developers.cloudflare.com/workers/wrangler/commands/
Sumber: https://developers.cloudflare.com/workers/configuration/secrets/
Sumber: https://developers.cloudflare.com/workers/wrangler/environments/
