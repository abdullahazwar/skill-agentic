# Aturan repo skill-agentic

Repo ini membagikan instruksi Markdown untuk AI agent. Repo ini bukan aplikasi frontend atau Cloudflare yang perlu dijalankan atau dideploy.

## Skill yang tersedia

- [Cloudflare untuk OpenCode](.opencode/skills/cloudflare-opencode-terminal/SKILL.md): platform, data, bot, operasi dan batas akun.
- [Frontend Profesional](.opencode/skills/frontend-professional/SKILL.md): desain dan engineering untuk portofolio, bisnis, dashboard, toko serta berbagai web.

Kedua folder berada sejajar di .opencode/skills. Muat SKILL.md yang relevan, lalu baca referensi sesuai kebutuhan. Gunakan agent/model yang sudah dimiliki pengguna. Paket tidak menyertakan primary agent khusus atau slash command.

## Batas isi

Pertahankan hanya file .md. Jangan menambahkan kode, script, installer, JSON/JSONC/TOML, YAML konfigurasi/workflow, SQL, package/lockfile, environment file, atau template aplikasi. Metadata name/description pada SKILL.md hanya untuk discovery.

Jangan menaruh credential, Account ID, Zone ID, resource ID, hostname deployment pribadi, endpoint privat atau data pelanggan. Jelaskan konsep dengan prose tanpa nilai akun dan tanpa blok kode/config siap jalan.

Membuat atau memperbarui repo skill tidak memberi izin login, membuat resource Cloudflare, mengubah DNS/billing, mengirim pesan atau deploy aplikasi. Implementasi aplikasi dilakukan pada repo aplikasi dalam tugas yang jelas.

## Penyuntingan

Gunakan bahasa Indonesia sederhana. Baca aturan, status branch dan diff. Pertahankan perubahan pengguna. Tinjau dokumentasi resmi bila detail teknis, lisensi, API, harga atau batas diperlukan.

## Validasi

Periksa bahwa seluruh file distribusi Markdown, frontmatter valid, nama cocok dengan folder, tautan lokal ada, dan referensi tidak mengarah ke kode/config yang sudah dihapus. Tinjau nilai sensitif tanpa menampilkannya.

Commit/push hanya pada repo/branch yang diminta dan verifikasi hasil remote. Jangan force-push atau mengklaim penghapusan pada commit baru telah membersihkan riwayat lama.
