# Runbook agent terminal

## Panduan, rancangan atau audit

1. Pastikan hasil yang diminta dan batas read-only.
2. Baca aturan serta dokumen yang relevan.
3. Kumpulkan bukti secukupnya tanpa membuka credential/data pelanggan.
4. Jelaskan pilihan, sebab, dampak dan langkah validasi.
5. Jangan membuat file aplikasi, konfigurasi atau perubahan akun bila pengguna hanya meminta instruksi.

## Implementasi aplikasi yang diminta terpisah

1. Tentukan repo aplikasi dan scope yang telah diizinkan.
2. Baca status, kontrak dan toolchain yang ada.
3. Rancang perubahan terkecil yang menyelesaikan masalah.
4. Kerjakan di repo aplikasi, tanpa memasukkan identitas akun ke repo skill.
5. Uji jalur normal, kegagalan dan regresi yang terkait.
6. Push/deploy hanya jika termasuk scope, lalu verifikasi hasil.

Jangan membuat aplikasi di folder paket skill. Jangan membuat resource dua kali setelah timeout tanpa memeriksa hasil operasi sebelumnya.

## Diagnosis bot idle

Bedakan cron, request HTTP, outbound API serta operasi storage. Periksa apakah AI dipanggil sebelum ada pekerjaan. Rancang pencarian due berindeks dan berhenti ketika kosong tanpa menghapus pengingat yang diperlukan.

Tinjau durable inbox, claim atomik, retry, lease dan idempotensi. Jangan menjanjikan tepat satu kali pengiriman eksternal tanpa dukungan ujung ke ujung.

## Migrasi data

Inventaris skema dan jumlah data secara privat. Siapkan backup yang sesuai, migrasi kompatibel dan uji terisolasi. Restore snapshot tidak boleh dijalankan otomatis setiap deploy gagal. Cache bukan sumber saldo/stok.

## Pemulihan sesi

Simpan catatan ringkas tentang tujuan, scope, perubahan, tes, bukti error dan langkah berikutnya di tempat privat yang sesuai. Jangan memasukkan credential, identitas akun atau data pelanggan ke catatan publik. Saat melanjutkan, baca status dan diff agar pekerjaan tidak diulang.

## Pelaporan

Jawaban model “selesai” bukan bukti operasi. Laporkan perubahan dan tes yang nyata; bedakan belum dikerjakan, gagal, dan belum terverifikasi. Utamakan hasil konkret dan batas material.
