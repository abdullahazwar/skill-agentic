# D1 dan desain data

## Isi

- Model data dan SQL
- Transaksi dan konflik
- Laporan dan performa
- Migrasi dan isolasi
- Penghapusan relasi

## Model data dan SQL

Gunakan D1 untuk data relasional. Simpan uang Rupiah sebagai integer dengan satuan jelas. Hindari floating point untuk saldo. Simpan waktu UTC dengan unit eksplisit, lalu format sesuai zona pengguna.

Gunakan ID stabil, UNIQUE, CHECK, foreign key dan indeks. Nama barang ialah label yang dapat berubah, bukan primary key.

Ambil verifiedUserId dari autentikasi server. Jangan percaya user_id client sebagai bukti kepemilikan. Bind input, batasi tanggal/halaman dan allowlist kolom ORDER BY.

## Transaksi dan konflik

Gunakan DB.batch untuk kelompok SQL yang commit/rollback bersama. Batch tidak menjadikan keputusan JavaScript sebelumnya atomik.

Pengurangan stok memerlukan SQL bersyarat dengan stok mencukupi. Periksa meta.changes. UPDATE nol baris bukan error SQL, sehingga tidak otomatis menggagalkan statement batch selanjutnya.

Untuk pesanan plus stok, rancang constraint, trigger, conditional insert atau koordinasi DO yang menjamin prasyarat. Uji stok satu dengan dua pembeli serentak. Jangan mengurangi angka cache.

Gunakan idempotency key unik per user dan transaksi. Simpan fingerprint payload untuk menolak key sama dengan payload berbeda. Gunakan outbox durable bagi efek eksternal. Transaksi database tidak mencakup panggilan Telegram.

## Laporan dan performa

1. Buat indeks menurut query nyata, misalnya (user_id, occurred_at).
2. Pakai EXPLAIN QUERY PLAN saat banyak baris dipindai.
3. Ambil kolom yang diperlukan.
4. Gunakan agregasi SQL untuk laporan dengan batas UTC hasil konversi zona pengguna.
5. Hindari membaca seluruh tabel ke Worker untuk menghitung total.
6. Ukur rows_read dan rows_written. Jumlah query berbeda dari jumlah baris.
7. Cache ringkasan sesuai toleransi stale. Hasil mutasi berasal dari data utama.

Untuk read-after-write dengan read replication, pelajari Sessions API dan bookmark. Jangan menganggap semua replica langsung melihat write terakhir.

## Migrasi dan isolasi

Buat migrasi baru. Jangan mengubah file yang sudah diterapkan. Uji lokal, backup produksi, lalu apply pada database/environment yang benar.

Rancang skema sesuai domain dan uji constraint serta kepemilikan pada data terisolasi.

Uji dua akun. Pastikan edit, hapus, laporan, ekspor, job dan cache menolak akses lintas pemilik. Gunakan constraint gabungan untuk relasi lintas tenant bila diperlukan.

## Penghapusan relasi

Tentukan kebijakan per relasi, bukan CASCADE untuk semua tabel.

| Data | Kebijakan yang lazim |
| --- | --- |
| Detail draft tanpa nilai audit | Cascade dapat sesuai |
| Master masih dipakai penjualan | Archive atau snapshot |
| Harga penjualan | Snapshot saat checkout |
| Belanja sementara | Hapus sesuai instruksi |
| Ledger keuangan | Koreksi/reversal dengan jejak |
| File R2 terkait | Cleanup terpisah dengan retry |

Untuk hapus permanen, identifikasi tabel anak, histori, backup dan retensi yang terdampak. Periksa row count dan konsistensi akhir. Jangan hapus massal untuk mengatasi konflik nama.

Sumber: https://developers.cloudflare.com/d1/worker-api/d1-database/
Sumber: https://developers.cloudflare.com/d1/worker-api/prepared-statements/
Sumber: https://developers.cloudflare.com/d1/reference/migrations/
Sumber: https://developers.cloudflare.com/d1/sql-api/foreign-keys/
Sumber: https://developers.cloudflare.com/d1/worker-api/sessions/
