# Memakai skill di OpenCode

## Isi paket

Repo skill-agentic membagikan skill Markdown di direktori .opencode/skills. cloudflare-opencode-terminal dan frontend-professional merupakan folder sejajar. Setiap folder memiliki SKILL.md dan referensi tertulis. Paket tidak menyertakan installer, kode aplikasi, custom agent, command otomatis atau konfigurasi provider.

## Pemasangan proyek

Salin hanya folder skill yang diperlukan ke direktori .opencode/skills pada proyek tujuan. Pertahankan nama folder dan SKILL.md. Jangan mengganti AGENTS.md atau konfigurasi proyek yang sudah ada.

Jika skill bernama sama sudah ada, bandingkan instruksi dan gabungkan perubahan yang diperlukan secara sadar. Jangan menimpa versi pengguna. Menyalin dokumen tidak membutuhkan kredensial Cloudflare.

## Pemasangan global

Menurut dokumentasi OpenCode, direktori global yang umum adalah ~/.config/opencode/skills. Lokasi bisa berbeda bila instalasi mengatur direktori konfigurasi lain. Periksa dokumentasi versi yang digunakan. Pilih satu lokasi agar tidak ada nama duplikat.

Tidak perlu menambahkan provider, model, API key, izin bash atau koneksi Cloudflare untuk membaca skill.

## Memulai sesi

Buka terminal OpenCode pada folder proyek yang dimaksud dan minta agent memuat cloudflare-opencode-terminal melalui tool skill. Minta agent membaca referensi yang relevan, bukan seluruh paket sekaligus.

Untuk belajar/audit/rancangan, sebutkan hasil itu agar agent tetap pada instruksi. Untuk implementasi aplikasi kelak, sebut repo aplikasi, perubahan yang diminta dan batas operasinya. Paket skill-agentic sendiri tidak perlu dideploy.

## Jika tidak ditemukan

Periksa lokasi discovery, nama folder yang cocok dengan metadata name, huruf besar pada SKILL.md, nama duplikat serta permission skill yang aktif. Muat ulang sesi jika perlu. Jangan mematikan pembatasan alat atau mengganti konfigurasi global hanya untuk mengatasi discovery.

Sumber: https://opencode.ai/docs/skills/
