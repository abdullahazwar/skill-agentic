# Konfigurasi dan izin OpenCode

## Pertahankan konfigurasi

Paket tidak menerbitkan contoh konfigurasi. Membaca skill tidak memerlukan perubahan model, provider, endpoint, MCP, default agent, atau permission global.

Jika masalah berada pada konfigurasi aplikasi pengguna, baca hanya bagian yang diperlukan secara privat dan rujuk dokumentasi versi terpasang. Jangan menyalin config lengkap ke chat, issue, log atau repo skill.

## Tiga lapisan

1. Instruksi pengguna menentukan scope tugas.
2. Permission OpenCode menentukan alat yang boleh berjalan.
3. Izin akun provider menentukan operasi yang diterima.

Skill tidak menambah hak pada lapisan mana pun. Jika alat menolak, jelaskan tindakan dan aturan yang teramati. Jangan mengganti deny/ask menjadi allow atau memakai jalur lain untuk melewatinya.

## Izin terminal

Pattern izin shell bukan sandbox lengkap. Package script dan program perantara dapat menjalankan operasi tambahan. Baca efek perintah sebelum menjalankan, terutama dari repo tidak tepercaya.

Jangan mengaktifkan persetujuan otomatis sebagai solusi umum. Jika headless terhalang prompt yang wajib, lanjutkan melalui alur resmi yang sesuai atau laporkan batasnya.

## Autentikasi

Login model, GitHub dan Cloudflare terpisah. Memasang skill tidak melakukan login. Jangan membuka auth store, cookie atau environment asli hanya untuk mengecek status. Gunakan status resmi yang tidak menampilkan secret jika memang diperlukan untuk tugas yang diizinkan.

Sumber: https://opencode.ai/docs/config/
Sumber: https://opencode.ai/docs/permissions/
