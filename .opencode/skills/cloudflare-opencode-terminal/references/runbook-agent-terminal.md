# Runbook agent terminal

## Membuat aplikasi baru

1. Tentukan folder tujuan dan kontrak fitur.
2. Pilih starter aset paket atau generator Cloudflare resmi. Jangan menulis proyek pada folder skill.
3. Tetapkan Worker name dan tanggal kompatibilitas.
4. Tambahkan binding yang diperlukan. Gunakan resource lama jika memang diminta.
5. Generate tipe, implementasi, test, build dan dry-run.
6. Buat atau pilih resource remote hanya dalam scope.
7. Isi secret dengan prompt resmi. Jalankan migrasi yang telah diuji.
8. Deploy, verifikasi URL dan catat versi.

Jika diminta lokal saja atau rancangan saja, berhenti pada hasil itu. Jangan menambah deployment.

## Memperbaiki proyek lama

1. Baca aturan repo, status git dan konfigurasi produksi yang relevan.
2. Reproduksi atau temukan bukti log tanpa membuka data privat.
3. Identifikasi modul penyebab dan kontrak yang harus dipertahankan.
4. Buat perubahan sekecil kebutuhan. Jangan mengganti seluruh Worker hanya karena satu handler bermasalah.
5. Uji jalur gagal, jalur normal dan regresi yang terkait.
6. Deploy atau push bila diminta, lalu periksa hasil remote.

## Memperbaiki bot idle

Bedakan invocation cron dari HTTP, outbound API dan KV/D1. Periksa handler yang memanggil AI sebelum memeriksa pekerjaan. Gunakan due query berindeks dan early return. Pertahankan pengingat yang memang diperlukan.

Gunakan inbox durable dan atomic claim untuk update/job. Jangan mengakui webhook sukses sebelum menerima pekerjaan secara tahan gangguan. Uji duplicate, crash, lease dan retry.

## Migrasi data

Inventaris tabel, foreign key, jumlah baris dan versi. Backup privat, migrasi tambahan, uji lokal/staging, lalu apply pada environment benar. Jangan memulihkan snapshot lama secara otomatis setelah deploy kode gagal.

Simpan keputusan penghapusan relasi. Riwayat harga penjualan perlu snapshot. Cache tidak menjadi sumber kebenaran untuk saldo atau stok.

## Ketika sesi panjang

Catat checkpoint ringkas dalam catatan proyek yang memang ditujukan untuk pekerjaan:

    Tujuan:
    Scope yang telah diizinkan:
    Repo/branch/Worker/environment:
    Perubahan dan commit:
    Test yang sudah lulus:
    Bukti error yang belum selesai:
    Langkah berikutnya:
    Jangan ulangi:

Jangan menyimpan token atau data pelanggan dalam checkpoint. Setelah compaction atau resume, baca catatan, status git dan file yang berubah. Jangan mengulang create resource yang mungkin sudah berhasil.

## Headless dan exit status

Opencode run menggerakkan agent, bukan menggantikan semua test. Tinjau hasil tool dan exit code. Format JSON event membantu integrasi jika CLI mendukung, tetapi struktur event dapat berubah.

Jangan menganggap jawaban model "selesai" sebagai bukti deploy. Verifikasi branch SHA, deployment ID, health dan data sesuai perubahan. Untuk tindakan tidak dapat dibuktikan, tulis status belum terverifikasi.

## Hasil akhir

Berikan hasil konkret lebih dahulu. Sebutkan perubahan, alasan, pengujian, commit atau URL. Nyatakan blocker spesifik. Hindari laporan kronologi perintah yang panjang.
