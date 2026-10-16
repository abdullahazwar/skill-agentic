# Design system dan responsive

## Mulai dari sistem yang ada

Temukan token warna, spacing, radius, type, elevation dan breakpoint. Pertahankan nama/konvensinya. Untuk sistem baru, definisikan sedikit token semantik: background, surface, text, muted text, border, accent, success, warning, danger, dan focus.

Gunakan token semantik sebagai fondasi yang disesuaikan terhadap produk. Uji pasangan foreground/background setelah perubahan theme, termasuk hover, disabled, dark mode, dan overlay.

## Typography

- Pilih font sesuai bahasa/identitas dan periksa lisensi. System font layak untuk produksi. Jangan menambah webfont hanya agar berbeda.
- Tetapkan hierarki judul, isi, label dan metadata. Mulai isi sekitar 1rem dengan line-height nyaman, lalu sesuaikan konteks. Jangan memakai teks sangat kecil untuk memuat dashboard.
- Batasi paragraf panjang sekitar 60 sampai 75ch sebagai titik awal. Gunakan angka tabular dan rata kanan untuk kolom angka.
- Gunakan fluid type dengan clamp jika berguna. Judul panjang harus membungkus. Hindari line break manual yang merusak layar kecil atau terjemahan.

## Layout dan spacing

Gunakan grid/flex sesuai hubungan konten, skala spacing terbatas, dan container sesuai tugas. Situs baca membutuhkan kolom lebih sempit daripada ruang kerja dashboard. Jangan memasukkan setiap blok ke card.

Mulai layar sempit lalu tambah kolom ketika isi memerlukan ruang. Pilih breakpoint ketika layout mulai gagal. Uji sekitar 360, 768, dan 1440 CSS px serta sisi breakpoint. Periksa 320 CSS px untuk reflow konten relevan.

Periksa min-width: 0 pada anak flex/grid, overflow-wrap untuk ID/URL, aspect-ratio media, dan ukuran intrinsik gambar. Jangan menyembunyikan overflow seluruh body untuk menutupi bug. Tabel dua dimensi boleh memakai scroll region bernama dan dapat difokuskan.

## Kontrol dan state

Samakan ukuran, padding, label, focus, disabled, loading, dan feedback. Warna status disertai teks/ikon. Target sentuh sekitar 44 CSS px sering nyaman; WCAG 2.2 AA 2.5.8 memakai minimum 24 kali 24 CSS px dengan alternatif/pengecualian. Jangan menyamakan keduanya.

## Motion dan theme

Gunakan motion untuk menjelaskan perubahan state/orientasi. Hindari scroll hijacking, cursor pengganti, animasi masuk berulang, dan parallax yang menghambat membaca. Hormati prefers-reduced-motion. Konten tetap terlihat bila JavaScript animasi gagal.

Sediakan dark mode jika dibutuhkan atau sudah ada. Definisikan pasangan token dark, uji contrast/chart, dan simpan pilihan sesuai arsitektur. Jangan otomatis membalik semua warna.

## Ketahanan konten

Uji label panjang, ID tanpa spasi, nilai nol, angka besar, bahasa Indonesia, timezone berbeda, dan missing image. Alt menjelaskan gambar informatif; dekoratif memakai alt kosong. Media mendukung subjek, bukan menutupi informasi yang belum ditulis.
