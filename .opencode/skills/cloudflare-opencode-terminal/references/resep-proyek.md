# Resep proyek dan latihan

## Belajar bertahap

| Tahap | Hasil yang dibuat | Bukti selesai |
| --- | --- | --- |
| 1 | Worker health dan web | Lokal 200, API salah 404 |
| 2 | Deploy pertama | URL aktual dapat dibuka |
| 3 | CRUD D1 | Data bertahan dan input buruk ditolak |
| 4 | Identitas pengguna | Akun A tidak membaca akun B |
| 5 | File R2 | Upload, tampil, ganti dan hapus konsisten |
| 6 | Cache ringkasan | Hit/miss diukur, edit tetap terlihat |
| 7 | Webhook Telegram | Duplicate tidak menggandakan data |
| 8 | Pengingat | Due terkirim, kosong tidak memicu AI |
| 9 | GitHub CI | Commit teruji dan deploy target benar |
| 10 | Operasi | Backup, restore uji, log dan budget |

## POS angkringan mobile

Gunakan Worker + Static Assets + D1. Tambahkan R2 untuk foto menu. Tambahkan KV hanya untuk ringkasan yang boleh stale.

Modelkan produk, recipe/produksi, ingredient, pembelian, stock ledger, penjualan, sale item dan pengeluaran. Simpan harga/modal snapshot pada sale item. Jangan menghitung histori memakai harga master terbaru.

Definisikan satuan pcs, batch, gram atau botol beserta konversinya. Tambah produksi harian ialah stock movement baru, bukan mengganti jumlah awal tanpa jejak.

Transaksi checkout harus menolak pembayaran ganda dan stok negatif jika bisnis memakai stok. Bila owner memilih penjualan tanpa stok, jangan menambahkan blokir stok pada checkout.

UI memuat katalog dua kolom, pencarian, keranjang, bayar dan riwayat. Pertahankan scroll saat stok/menu diperbarui. Foto disimpan sebagai object key, bukan base64 pada baris menu.

Tentukan penghapusan master terhubung secara eksplisit. Hapus data draft yang memang diminta, tetapi pertahankan audit penjualan sesuai kebijakan. Test nama yang dipakai ulang setelah penghapusan.

## Dashboard galon dan LPG

Gunakan model pelanggan, produk, kurir, pesanan, detail item, pembayaran dan pengeluaran. Satu pelanggan dapat memiliki air dan gas dalam pesanan sama.

Tampilkan qty selesai per item dengan tombol tambah/kurang yang memanggil API tervalidasi. Cegah nilai negatif dan perubahan melebihi pesanan. Simpan audit siapa mengubah.

Laporan laba per produk, kurir dan pelanggan memakai snapshot modal/harga. Margin dihitung dengan pembagi yang jelas dan nol penjualan ditangani. Jangan memakai lokasi GPS jika kebutuhan pengguna memang menghapusnya.

## Bot keuangan

Gunakan webhook, parser nominal, draft konfirmasi, transaksi D1 dan wallet ledger. Pisahkan transfer internal dari pemasukan/pengeluaran. Pakai kategori milik user dan default Lainnya.

Gunakan idempotency key untuk update Telegram dan tindakan simpan. Batasi riwayat dengan pagination. Cache laporan jika perlu, tetapi saldo final berasal dari ledger/database.

Kriteria selesai: 200 rb benar, transfer ke teman keluar, antar wallet seimbang, dua user terisolasi, duplicate aman dan idle tidak memanggil AI.

## Bot kampus

Gunakan jadwal matkul mingguan, occurrence, validasi dosen malam sebelumnya, kegiatan pribadi dan tugas kelompok. Simpan course_id untuk relasi.

Jadwal pribadi singkat dapat meminta nama kegiatan, tanggal/waktu dan konfirmasi. Tanya jika "jam 8" ambigu atau tanggal sudah lewat. Validasi dosen hanya berlaku untuk occurrence yang dipilih.

Kriteria selesai: zona waktu benar, tidak mengirim matkul yang dibatalkan, tugas dekat tenggat ditampilkan sesuai hubungan, cron kosong berhenti cepat.

## Bot warung

Gunakan kategori, produk dan alias pencarian. Tambah produk dapat memakai wizard nama, kategori, harga/satuan, konfirmasi. State wizard terpisah per user.

Search memprioritaskan exact/alias lalu prefix atau fuzzy terbatas. AI opsional hanya saat pencocokan deterministik gagal. Edit pesanan perlu ID dan ownership, bukan hanya teks nama.

## Bot makalah PDF

Gunakan job durable untuk data cover, outline, penulisan, sitasi, review dan render. Jangan menghasilkan sumber palsu. Review mempunyai batas revisi dan status yang menjelaskan tahap.

Simpan output di R2 dan kirim attachment setelah validasi. Cegah tombol ulang membuat beberapa job aktif untuk permintaan yang sama.

Semua resep ialah pola implementasi, bukan klaim keadaan proyek pengguna. Baca kode dan data terbaru sebelum melakukan perubahan nyata.
