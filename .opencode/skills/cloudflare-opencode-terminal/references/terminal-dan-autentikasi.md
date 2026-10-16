# Terminal dan autentikasi

## Inspeksi

Pastikan folder kerja, aturan repo, status branch, file terkait dan versi toolchain. Periksa bantuan CLI terpasang sebelum memakai opsi dari dokumentasi. Batasi inventaris pada file yang diperlukan dan hindari dump environment/konfigurasi.

Repo skill adalah dokumen, bukan aplikasi yang perlu diinstal dependency atau dipublikasikan ke Cloudflare.

## Penggunaan shell kelak

Saat tugas aplikasi memang mencakup terminal, tinjau perintah dan argumen. Perlakukan path berspasi dengan benar. Jangan menggabungkan input bebas sebagai shell, mengevaluasi teks provider, atau menjalankan installer remote tanpa meninjau sumber.

Baca output dan status proses sebelum tindakan yang bergantung padanya. Hentikan dev server dan stream log setelah pengujian. Jangan menaruh secret pada argumen, URL atau file yang ikut git.

## Cloudflare

Membaca panduan tidak memerlukan login atau token. Pada operasi akun yang diminta kemudian, gunakan alur autentikasi resmi dan scope minimal. Tentukan akun/environment secara privat; jangan menyimpan identitasnya di paket skill.

Gunakan toolchain proyek agar versi konsisten. Simulasi publikasi tidak sama dengan deploy dan tidak membuktikan izin, DNS atau secret remote.

## GitHub

Push dilakukan hanya pada repo/branch yang diminta. Commit lokal berbeda dari hasil remote. Verifikasi hasil setelah publikasi. Jangan membaca token autentikasi atau menyalin remote berkredensial ke output.

## Dokumentasi dan MCP

MCP bersifat opsional; panduan dapat dibaca tanpa connector akun. MCP dokumentasi dan MCP administrasi memiliki kemampuan berbeda. Jangan menghubungkan akun, membuat resource atau menanam token dalam config hanya untuk memakai skill.

Sumber: https://opencode.ai/docs/cli/
Sumber: https://developers.cloudflare.com/workers/wrangler/commands/
