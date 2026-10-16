# KV dan cache

## Pilih data yang sesuai

KV cocok untuk konfigurasi jarang berubah, cache ringkasan, dan data yang boleh terlambat terlihat lintas lokasi. Jangan jadikan KV satu-satunya sumber saldo, stok, lock atau deduplikasi atomik.

State percakapan sementara dapat memakai KV jika keterlambatan/kehilangan dapat ditangani. Untuk urutan kuat, gunakan D1 dengan kontrol konflik atau Durable Objects.

## Bedakan masa berlaku

| Konsep | Arti | Menghapus data utama? |
| --- | --- | --- |
| cacheTtl pada get | Masa cache hasil baca jaringan KV | Tidak |
| expirationTtl pada put | Masa berlaku key sejak ditulis | Ya, key kedaluwarsa |
| Retensi bisnis | Kebijakan umur transaksi/jadwal | Jika diimplementasikan |

Pada verifikasi 17 Oktober 2026, minimum cacheTtl ialah 30 detik dan default 60 detik. Minimum expirationTtl ialah 60 detik. Periksa ulang saat dipakai. Jangan tertukar karena namanya mirip.

Key memakai versi, pemilik dan periode. Identitas berasal dari server. Jangan memakai satu key ringkasan untuk semua user.

## Cache-aside

1. Validasi user dan parameter.
2. Baca cache.
3. Saat miss, hitung dari D1.
4. Kembalikan hasil dan simpan cache bila bermanfaat.
5. Sesudah mutasi, invalidate key terkait dan kembalikan state final D1.

Delete cache tidak menjamin seluruh lokasi segera membaca data baru. Negative lookup juga dapat tersimpan. Jangan menguji KV dengan asumsi konsistensi langsung di semua lokasi. Untuk hasil edit seketika, kirim state final pada respons mutasi atau bypass cache pada alur itu.

Tambahkan schema version bila bentuk value berubah. Perlakukan JSON rusak/lama sebagai miss. Kegagalan cache tidak boleh menggagalkan transaksi yang sudah tersimpan.

## Kurangi operasi

Hindari get/list/put semua user pada setiap tick. Jangan update last_seen tiap endpoint jika cukup per sesi. Ukur hit rate dan jumlah operasi, bukan hanya latensi.

Get lalu put jika kosong bukan atomic claim. Dua invocation dapat lolos bersama. TTL tidak membuat pola tersebut menjadi lock.

## Auto hapus

Periksa opsi put terlebih dahulu. Key tanpa expiration tidak memiliki retensi aplikasi otomatis hanya karena sudah lama. Data D1 tetap ada saat cache habis. Log observability mempunyai retensi tersendiri.

Untuk cleanup, tentukan jenis data, umur, pengecualian, backup, batch dan audit. Jangan menghapus transaksi keuangan untuk mengurangi request.

Sumber: https://developers.cloudflare.com/kv/concepts/how-kv-works/
Sumber: https://developers.cloudflare.com/kv/api/read-key-value-pairs/
Sumber: https://developers.cloudflare.com/kv/api/write-key-value-pairs/
Sumber: https://developers.cloudflare.com/changelog/post/2026-01-30-kv-reduced-minimum-cachettl/
