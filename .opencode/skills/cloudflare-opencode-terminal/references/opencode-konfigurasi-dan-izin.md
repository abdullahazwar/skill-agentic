# Konfigurasi dan izin OpenCode

## Pertahankan konfigurasi pengguna

OpenCode dapat menggabungkan global, proyek, env dan pengaturan terkelola. Jangan mengganti seluruh opencode.json hanya untuk menambah skill Cloudflare. Baca field yang relevan dan merge perubahan terkecil.

Jangan mengubah model, provider, base URL 9Router, MCP atau default agent yang sudah berfungsi tanpa kebutuhan. Template minimal paket tidak mengunci provider/model.

Contoh opsional yang sesuai schema dokumentasi utama saat pemeriksaan:

    {
      "$schema": "https://opencode.ai/config.json",
      "permission": {
        "skill": {
          "cloudflare-opencode-terminal": "allow"
        }
      }
    }

Ini bukan konfigurasi lengkap semua instalasi. Periksa schema dan versi lokal sebelum menggabungkan. Dokumentasi dev/v2 dapat memakai field lain. Jangan mencampur permission dan permissions dari format berbeda.

## Tiga lapis yang berbeda

1. Instruksi pengguna menentukan scope pekerjaan.
2. Permission OpenCode mengatur alat yang boleh berjalan.
3. Izin akun Cloudflare/GitHub menentukan operasi yang diterima provider.

Skill tidak menambah hak pada lapisan kedua dan ketiga. Jika pengguna sudah meminta deploy, tidak perlu meminta persetujuan percakapan lagi hanya karena deployment ialah mutasi. Tetap hormati prompt alat yang muncul dari policy aktif.

Jika alat menolak, jelaskan action dan rule yang teramati. Jangan mengubah ask/deny menjadi allow atau menjalankan lewat program lain untuk melewatinya.

## Permission bertarget

Aturan bash dapat memakai pattern dan urutan yang memengaruhi hasil. Gunakan contoh resmi sesuai versi. Rule luas seperti npm * juga mengizinkan lifecycle script yang dapat menjalankan kode.

Tinjau package scripts sebelum memberi izin permanen. Jangan menyatakan pattern allowlist sebagai sandbox keamanan lengkap. Flag, shell chain dan script perantara dapat mengubah efek perintah.

Installer tidak memasang policy bash atau mengganti config. Custom agent hanya meminta akses memuat skill ini. Untuk operasi lain, agent mengikuti konfigurasi yang sudah ada.

## Secret dan konfigurasi model

Login provider OpenCode berbeda dari wrangler login. Login GitHub berbeda lagi. Masing-masing credential memiliki scope sendiri.

Jangan membuka auth.json, .dev.vars, .env asli atau cookie hanya untuk mengetahui apakah login tersedia. Gunakan status/list resmi yang tidak menampilkan secret dan minta pengisian melalui alur autentikasi resmi bila diperlukan.

Jangan mengunggah debug config penuh ke chat atau issue karena hasil konfigurasi dapat mengandung key hasil interpolasi env. Jika perlu inspeksi, simpan privat dan tampilkan hanya field yang sudah disanitasi.

## Mode non-interaktif

Untuk run dari script, pastikan tool yang diperlukan memang sudah diizinkan dan akun siap. Jangan mengaktifkan auto-approve sebagai solusi umum. Jika operasi memerlukan prompt alat yang tidak dapat ditangani mode headless, lanjutkan di TUI atau laporkan blocker.

Jangan menambahkan instruksi "abaikan semua konfirmasi" ke system prompt. Utamakan penyelesaian scope yang jelas dengan policy yang ada.

Sumber: https://opencode.ai/docs/config/
Sumber: https://opencode.ai/docs/permissions/
Sumber: https://opencode.ai/docs/agents/
