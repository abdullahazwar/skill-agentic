# Wrangler, binding dan environment

## Memahami proyek

Gunakan Wrangler lokal dari toolchain proyek dan periksa dokumentasi versi terpasang. Pertahankan format konfigurasi proyek yang sudah berfungsi. Paket skill ini tidak menyediakan atau menerbitkan konfigurasi.

Identifikasi entrypoint, nama aplikasi, tanggal kompatibilitas dan cara build secara privat di repo aplikasi. Jangan memperbarui tanggal/flag kompatibilitas tanpa menguji perilaku lama.

## Binding

Binding menghubungkan kode Worker dengan resource. Nama binding, nama tampilan resource dan ID adalah hal berbeda. Nama binding harus cocok dengan yang dipakai aplikasi. Jangan mengganti resource berisi data dengan resource kosong untuk menyelesaikan error penamaan.

Tentukan resource yang memang diperlukan. D1 untuk data relasional, KV untuk data yang boleh stale, dan R2 untuk object. Generate/periksa tipe lingkungan sesuai toolchain aplikasi setelah binding berubah.

## Environment

Bedakan pengembangan lokal, preview, staging dan produksi. Banyak binding serta variabel memerlukan deklarasi khusus per environment. Periksa aturan pewarisan pada schema/dokumentasi saat itu, bukan menganggap semua otomatis diwariskan.

Gunakan target environment konsisten untuk pengujian, migrasi, secret, build, log dan deploy. Pisahkan resource staging dari produksi bila tugas memerlukannya.

## Rahasia

Pisahkan variabel publik/non-secret dari secret. Isi nilai rahasia melalui antarmuka aman yang resmi. Jangan memasukkan nilainya ke file distribusi skill, argumen terminal, log, URL, commit atau percakapan.

Akses binding aplikasi berbeda dari credential administrasi akun. Jangan memasang token administrasi ke frontend atau mengirimkannya pada setiap operasi data Worker.

## Validasi sebelum operasi nyata

1. Pastikan pengguna memang meminta pekerjaan aplikasi/akun.
2. Verifikasi target secara privat dan tinjau perubahan terkecil.
3. Periksa tipe, test, build serta simulasi publikasi sesuai proyek.
4. Baca warning tentang route, trigger, binding dan environment.
5. Ingat simulasi lokal tidak membuktikan izin, secret, DNS atau resource remote.
6. Setelah operasi yang diizinkan, verifikasi hasil nyata dan laporkan bukti tanpa identitas sensitif.

Sumber: https://developers.cloudflare.com/workers/wrangler/configuration/
Sumber: https://developers.cloudflare.com/workers/wrangler/commands/
Sumber: https://developers.cloudflare.com/workers/configuration/secrets/
Sumber: https://developers.cloudflare.com/workers/wrangler/environments/
