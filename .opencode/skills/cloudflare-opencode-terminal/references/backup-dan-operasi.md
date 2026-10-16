# Backup dan operasi data

## Kebijakan

Tentukan data apa yang dicadangkan, frekuensi, lokasi privat, umur simpan, akses dan cara restore. Git mencadangkan kode, bukan isi D1, KV atau R2 secara otomatis.

Pisahkan backup data pelanggan dari repo publik. Gunakan enkripsi dan penyimpanan yang sesuai sensitivitas data. Jangan mencetak isi dump pada percakapan.

## D1

Pastikan nama, ID dan environment benar. Catat waktu UTC, jumlah tabel/baris, versi skema dan checksum file. Periksa export selesai dan file bukan kosong.

Uji restore ke database baru/staging:

Untuk remote restore uji, target harus database isolasi yang secara jelas dipilih. Periksa sintaks/batas import dan jangan menimpa database produksi hanya untuk menguji.

Time Travel membantu pemulihan sesuai periode retensi produk/paket. Periksa waktu/bookmark yang tersedia dan konsekuensi restore. Jangan menganggap retensi sama untuk seluruh paket.

## KV dan R2

Ekspor KV memerlukan pagination list dan mengambil value/metadata/expiration yang relevan. Menyalin nama key saja bukan backup. Perhatikan bahwa export panjang tidak selalu satu snapshot konsisten saat aplikasi terus menulis.

Backup R2 mencakup object bytes dan metadata/relasi D1. Pertimbangkan object immutable/versioned key dan inventaris checksum. R2 tidak otomatis menjadi backup karena menyimpan file utama.

Dokumentasikan secret names untuk pemulihan. Jangan mengekspor nilai secret ke git. Isi ulang melalui secret manager atau mekanisme aman.

## Migrasi aman

1. Inventaris skema dan data sebenarnya.
2. Buat migrasi tambahan yang kompatibel dengan kode lama.
3. Backup sebelum perubahan berisiko.
4. Uji dengan data representatif dan foreign key.
5. Apply pada environment yang benar.
6. Deploy kode yang kompatibel.
7. Validasi jumlah data, laporan dan alur bisnis.
8. Hapus struktur lama hanya setelah jalur baru terbukti.

Rollback Worker tidak membatalkan migrasi. Jika perlu revert data, buat rencana dan batas kehilangan data yang jelas. Jangan restore snapshot lama secara otomatis setelah setiap deploy gagal.

## Retensi dan penghapusan

Pisahkan session, cache, log, draft, jadwal selesai, lampiran dan transaksi. Tetapkan umur per jenis data. Gunakan cleanup batch dengan indeks dan cursor agar tidak memindai semua data setiap menit.

Untuk permintaan hapus permanen, cakup tabel anak, metadata, R2, vektor, cache dan pekerjaan tertunda sesuai instruksi. Backup dapat menyimpan salinan sampai retensinya habis. Jangan menjanjikan hilang dari seluruh backup seketika jika tidak dilakukan.

Untuk kebijakan undang-undang/kontrak, verifikasi sumber resmi yang relevan sebelum memberi angka retensi. Jangan membuat angka bulan seolah berasal dari Cloudflare.

Sumber: https://developers.cloudflare.com/d1/best-practices/import-export-data/
Sumber: https://developers.cloudflare.com/d1/reference/time-travel/
Sumber: https://developers.cloudflare.com/kv/api/list-keys/
Sumber: https://developers.cloudflare.com/r2/buckets/object-lifecycles/
