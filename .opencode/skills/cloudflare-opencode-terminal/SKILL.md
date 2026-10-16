---
name: cloudflare-opencode-terminal
description: Instruksi Markdown bagi AI agent OpenCode di terminal untuk belajar, merancang, mengaudit dan memandu pekerjaan Cloudflare/claudflare, Wrangler, Workers, Pages, D1, KV, R2, Durable Objects, Queues, Workflows, bot Telegram, cron idle, DNS, secret, Workers AI dan GitHub. Mencakup discovery skill, AGENTS.md, permission, versi CLI serta batas autentikasi. Tidak menyertakan kode, config, installer, custom agent, workflow atau identitas akun.
---

# Cloudflare untuk OpenCode Terminal

Gunakan agent dan model yang sudah dikonfigurasi pengguna. Muat skill ini melalui tool skill lalu baca referensi dari base directory aktual. Paket tidak membutuhkan connector ChatGPT, login atau akses akun untuk dibaca.

## Batas utama

Baca [privasi dan batas paket](references/privasi-dan-batas-skill.md). Repo skill-agentic adalah kumpulan instruksi Markdown, bukan aplikasi Cloudflare. Jangan menerbitkan kode/config, credential, identitas akun, hostname pribadi atau data pelanggan.

Permintaan membuat skill tidak memberi izin membuat resource, mengubah DNS/billing, menghubungkan akun atau deploy. Paket tidak menyertakan script, installer, primary agent khusus atau slash command. Gunakan instruksi langsung kepada agent yang tersedia.

## Alur agent

1. Tentukan apakah pengguna meminta panduan, audit read-only, rancangan atau pekerjaan aplikasi yang berbeda.
2. Muat hanya referensi terkait. Periksa aturan AGENTS.md, folder kerja serta status repo yang berlaku.
3. Untuk panduan, berikan langkah dan kriteria verifikasi secara tertulis, tanpa menambahkan kode/config siap jalan ke repo skill.
4. Untuk tugas aplikasi yang kelak diizinkan, kerjakan pada repo aplikasi dan hormati batas pengguna. Pertahankan data serta perubahan lokal.
5. Periksa versi CLI/toolchain dan dokumentasi resmi sebelum memakai fitur atau opsi. Jangan menebak sintaks atau mencampur schema versi.
6. Pilih target akun, environment dan resource secara privat lewat hasil alat resmi. Jangan menyalin nilainya ke dokumen publik.
7. Hormati permission OpenCode dan akun. Jangan mengganti model/provider, menonaktifkan aturan atau memakai jalur lain untuk melewati penolakan.
8. Jalankan validasi yang sesuai hanya dalam scope, baca hasilnya dan bedakan simulasi lokal dari bukti runtime/remote.
9. Push/deploy hanya jika diminta dalam tugas aplikasi. Verifikasi hasil dan laporkan bukti tanpa data sensitif.

## Peta referensi

| Kebutuhan | Referensi |
| --- | --- |
| Dari nol dan pemasangan | [Dari nol dan pemasangan](references/mulai-dan-instalasi.md) |
| Discovery dan aturan OpenCode | [Discovery dan aturan OpenCode](references/opencode-agent-dan-skill.md) |
| Permission dan konfigurasi privat | [Permission dan konfigurasi privat](references/opencode-konfigurasi-dan-izin.md) |
| Terminal dan autentikasi | [Terminal dan autentikasi](references/terminal-dan-autentikasi.md) |
| Runbook dan pemulihan sesi | [Runbook dan pemulihan sesi](references/runbook-agent-terminal.md) |
| Diagnosis OpenCode | [Diagnosis OpenCode](references/opencode-troubleshooting.md) |
| Pemilihan layanan | [Pemilihan layanan](references/arsitektur-produk.md) |
| Wrangler, binding dan environment | [Wrangler, binding dan environment](references/wrangler-konfigurasi.md) |
| Workers, Static Assets dan Pages | [Workers, Static Assets dan Pages](references/workers-dan-web.md) |
| D1, relasi, stok dan transaksi | [D1, relasi, stok dan transaksi](references/d1-dan-data.md) |
| KV, cache dan TTL | [KV, cache dan TTL](references/kv-dan-cache.md) |
| R2, upload dan media | [R2, upload dan media](references/r2-dan-media.md) |
| Cron, DO, Queues dan Workflows | [Cron, DO, Queues dan Workflows](references/jadwal-dan-background.md) |
| Bot Telegram dan request saat idle | [Bot Telegram dan request saat idle](references/bot-telegram-dan-idle.md) |
| DNS, domain dan TLS | [DNS, domain dan TLS](references/domain-dns-dan-tls.md) |
| Secret, Access, WAF dan Turnstile | [Secret, Access, WAF dan Turnstile](references/keamanan-dan-akses.md) |
| AI, RAG, Vectorize dan Gateway | [AI, RAG, Vectorize dan Gateway](references/ai-dan-otomasi.md) |
| GitHub dan deployment terpisah | [GitHub dan deployment terpisah](references/github-dan-deploy.md) |
| Log, pengujian dan performance | [Log, pengujian dan performance](references/debugging-dan-observability.md) |
| Biaya dan kuota | [Biaya dan kuota](references/biaya-dan-kuota.md) |
| Backup, retensi dan pemulihan | [Backup, retensi dan pemulihan](references/backup-dan-operasi.md) |
| Resep proyek konseptual | [Resep proyek konseptual](references/resep-proyek.md) |
| Dokumentasi resmi | [Dokumentasi resmi](references/sumber-resmi.md) |
| Privasi dan batas publikasi | [Privasi dan batas publikasi](references/privasi-dan-batas-skill.md) |

## Penalaran teknis

Gunakan binding untuk operasi data dan tool administrasi untuk resource. D1/DO mendukung kebutuhan koordinasi yang tidak cocok untuk read-then-write KV. Bedakan cache, ledger, retensi dan backup.

Untuk bot, verifikasi webhook, durable inbox, idempotensi, claim, lease dan retry. Hentikan kerja downstream ketika tidak ada job tanpa mematikan pengingat yang diperlukan. Cron terpasang tetap dapat memicu invocation ketika data kosong.

Verifikasi kepemilikan server untuk baca/edit/hapus/ekspor/job/media. Jangan menganggap CORS, tombol tersembunyi atau frontend sebagai otorisasi. Harga, model, limit dan fitur diperiksa ulang pada sumber resmi.

## Hasil yang dapat dipercaya

Sebutkan temuan, alasan, langkah yang benar-benar dilakukan dan batas yang tersisa. Jangan mengaku login/deploy/push berhasil hanya dari teks model. Jangan menyamakan pemasangan dokumen dengan akses Cloudflare atau deployment aplikasi.

Untuk audit saja, laporkan temuan tanpa mengedit aplikasi, memasang dependency, mengirim pesan produksi atau mengubah resource.
