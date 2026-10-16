# Troubleshooting OpenCode

| Gejala | Pemeriksaan |
| --- | --- |
| Skill tidak terlihat | Lokasi discovery, nama folder/metadata, SKILL.md, permission, duplikasi |
| Referensi tidak dibaca | Muat skill dan gunakan base directory aktual |
| Agent/command lama hilang | Paket sekarang hanya skill Markdown; gunakan agent biasa dan instruksi langsung |
| Opsi CLI tidak dikenal | Bantuan versi binary terpasang |
| Model tidak tersedia | Nama provider/model dari daftar resmi instalasi |
| Provider menolak akses | Alur autentikasi, endpoint dan scope tanpa mencetak secret |
| Terminal ditolak | Permission aktif, bukan alasan mematikan pembatasan |
| Konfigurasi invalid | Schema versi yang dipakai, tanpa menerbitkan config pengguna |
| Headless berhenti | Prompt izin, login, provider, timeout atau batas iterasi |
| Runtime lokal gagal | Bedakan batas OS/jaringan dengan bug source |
| Data sensitif muncul | Hentikan penyebaran dan tangani paparan yang benar-benar terjadi |

## Versi dan provider

Jangan menebak flag atau endpoint router/model lokal. Provider ID, alias model dan model upstream bisa berbeda. Baca bantuan serta dokumentasi instalasi yang benar. Jangan menimpa setup yang sudah berfungsi.

Model lokal tetap membutuhkan resource mesin dan dukungan tool calling. Uji kemampuan memakai artefak tidak sensitif. Jangan memakai credential produksi untuk mencoba provider yang belum dipercaya.

## Discovery tanpa tugas model

Jika CLI menyediakan fungsi daftar/debug skill, gunakan untuk memeriksa discovery tanpa menjalankan tugas model. Hindari output config penuh. Discovery membuktikan dokumen ditemukan, bukan kualitas penalaran atau keberhasilan aplikasi.

Jika CLI belum ada, periksa nama/frontmatter/tautan secara lokal dan nyatakan integrasi belum diuji. Paket ini tidak membutuhkan installer, YAML agent atau file JSON tambahan.

Sumber: https://opencode.ai/docs/cli/
Sumber: https://opencode.ai/docs/skills/
Sumber: https://opencode.ai/docs/troubleshooting/
