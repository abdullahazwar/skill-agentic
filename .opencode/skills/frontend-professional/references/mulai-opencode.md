# Memakai skill frontend di OpenCode

## Struktur sejajar

Skill frontend-professional berada di .opencode/skills/frontend-professional, sejajar dengan cloudflare-opencode-terminal. SKILL.md merupakan pintu masuk; references berisi panduan sesuai tugas. Tidak ada file kode, konfigurasi atau installer yang perlu dijalankan.

## Pemasangan proyek atau global

Salin folder frontend-professional ke direktori skill proyek yang didukung OpenCode. Lokasi proyek yang umum adalah .opencode/skills. Lokasi global yang umum adalah ~/.config/opencode/skills, kecuali konfigurasi instalasi memilih direktori lain.

Pertahankan nama folder dan metadata name. Jika versi bernama sama sudah ada, bandingkan instruksi dahulu. Jangan menimpa AGENTS.md, provider, model atau permission pengguna. Tidak perlu menghubungkan Cloudflare/GitHub untuk membaca skill.

## Penggunaan

Buka OpenCode pada proyek yang dituju dan minta agent memuat frontend-professional melalui tool skill. Sebut jenis website, tujuan, batas perubahan dan hasil yang diminta.

Untuk portofolio, berikan karya serta peran yang nyata. Untuk bisnis, berikan layanan dan informasi praktis. Untuk dashboard, jelaskan sumber data, metrik, periode serta tugas operator. Jika belum tersedia, agent menyatakan asumsi dan melabeli demo.

Skill bukan slash command otomatis dan tidak menyediakan primary agent khusus. Gunakan agent/model yang sudah aktif. Untuk audit saja, nyatakan read-only agar tidak ada edit atau instalasi.

## Discovery

Jika tidak muncul, periksa lokasi, nama folder/frontmatter, SKILL.md, permission skill, nama duplikat dan sesi. Gunakan dokumentasi versi OpenCode yang dipakai, tanpa menambahkan config akun ke repo panduan.

Sumber: https://opencode.ai/docs/skills/
