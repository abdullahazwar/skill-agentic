# Discovery dan brief

## Baca repo sebelum mengubah UI

1. Temukan AGENTS.md root dan direktori yang diubah. Periksa git status agar perubahan pengguna tidak tertimpa.
2. Baca manifest dan lockfile. Cari route, layout, CSS global, theme, komponen bersama, API client, locale, test, dan asset pipeline dengan rg.
3. Pada tugas aplikasi yang memang diminta, jalankan halaman sesuai proses proyek setelah meninjau perintahnya. Catat alur yang sudah berjalan, bahasa visual, breakpoint, dan masalah konkret.
4. Inventarisasi token, komponen native/library, ikon, ilustrasi, font berlisensi, dan konten yang tersedia. Jangan memuat seluruh monorepo ke konteks.

Discovery adalah inspeksi terarah, bukan audit keamanan otomatis atau quality score.

## Brief minimum

Catat audiens, masalah, tugas utama, jenis halaman, konten yang tersedia, CTA utama, dan bukti kepercayaan yang benar-benar ada. Bedakan situs publik dengan aplikasi operasional berulang. Catat backend, transaksi, login, target mobile, bahasa, dan environment.

Untuk proyek baru tanpa merek, pilih arah sesuai audiens dan nyatakan asumsi. Untuk proyek yang punya design system, gunakan sistem itu. Jangan menghentikan implementasi hanya karena pengguna belum memberi palet atau font.

## Acceptance criteria yang bisa diperiksa

- Portofolio: pengunjung menemukan karya relevan, memahami peran pemilik, membaca detail proyek, dan menemukan kontak.
- Bisnis: layanan, wilayah, proses, harga atau cara meminta estimasi, serta kontak jelas. Klaim kepercayaan memiliki bukti.
- Dashboard: periode dan mata uang jelas, ringkasan cocok dengan sumber, filter/empty/error bekerja, tabel bisa dipakai dengan keyboard.
- E-commerce: pilihan varian, stok, harga total, cart, dan status checkout sesuai integrasi.

Tetapkan alur utama dan 2 sampai 4 kondisi tepi berdampak. Hindari kriteria “modern, premium, smooth” tanpa perilaku atau bukti konkret.

## Batas scope

Jangan mengganti backend, auth, navigasi global, atau dependency besar untuk tugas kecil. Jika integrasi belum tersedia, buat batas adapter dan label demo. Tanyakan hanya pilihan yang tidak bisa disimpulkan dan mengubah transaksi, akses, atau hasil utama. Lanjutkan bagian lain yang tidak bergantung pada jawaban.
