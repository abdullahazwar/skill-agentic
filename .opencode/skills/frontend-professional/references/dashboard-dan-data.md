# Dashboard dan integritas data

## Definisikan metrik sebelum widget

Untuk setiap angka, catat nama, formula, sumber, rentang waktu, timezone, mata uang, status transaksi yang disertakan, waktu update, dan pembanding. Omzet kotor, pendapatan bersih, uang diterima, laba, serta nilai pesanan berbeda.

Contoh kontrak demo, bukan aturan semua bisnis:

- Penjualan dibayar = jumlah nilai pesanan paid dalam periode; pajak/refund di luar model dan dijelaskan.
- Pesanan dibayar = jumlah pesanan paid, bukan seluruh baris.
- Rata-rata pesanan = penjualan dibayar dibagi jumlah pesanan dibayar; denominator nol ditangani jelas.
- Perubahan persentase memerlukan pembanding setara. Baseline nol memakai “belum tersedia” atau perubahan absolut berlabel.

Gunakan unit terkecil integer atau decimal backend untuk uang. Intl.NumberFormat memformat, bukan memperbaiki hitung floating point. Jangan menjumlahkan mata uang berbeda tanpa definisi konversi.

## Susunan berdasarkan tugas

Letakkan judul/konteks, periode dan filter dengan jelas. Pilih metrik yang membantu keputusan. Beri unit, penjelasan istilah dan waktu update. Grafik menjawab pertanyaan; tabel mendukung penelusuran/tindakan.

Grafik perlu skala, unit, legenda, tooltip yang dapat dipakai, serta alternatif teks/tabel jika diperlukan. Hindari 3D, area dekoratif, sumbu menyesatkan dan merah/hijau tanpa label. Tidak semua dashboard memerlukan grafik.

## Filter, pagination dan server

Simpan filter yang layak dibagikan di URL, tanpa secret/PII. Perubahan filter memperbarui ringkasan, grafik, tabel, total, ekspor dan periode dari scope yang sama. Reset pagination saat filter mengubah set data. Sorting server tidak boleh hanya mengurutkan satu halaman seolah seluruh dataset.

Bedakan total dataset, total setelah filter, total halaman dan jumlah dipilih. Seleksi bulk lintas halaman harus eksplisit. Pembatalan request/sequence guard mencegah respons lama menimpa filter terbaru. Pertahankan data valid saat refetch bila dapat ditandai sedang diperbarui.

## Tabel dan mobile

Gunakan table, caption, th scope, serta aria-sort untuk kolom yang diurutkan. Aksi baris menyebut objek. Angka rata kanan/tabular; tanggal punya format dan timezone jelas. Status memiliki teks.

Pada mobile, pilih prioritas kolom, detail expandable, atau scroll region bernama. Jangan menghilangkan angka penting hanya agar muat. Virtualisasi dipakai untuk dataset besar terukur dan diuji kembali aksesibilitasnya.

## State dan izin

Tangani initial loading, refresh, dataset kosong, filter nol, error, partial, stale, permission denied dan session expired. Retry tidak boleh menyebabkan submit ganda.

Menyembunyikan tombol bukan otorisasi. Backend menegakkan izin. Ekspor/log tidak membuka data di luar akses. Untuk ekspor spreadsheet, mitigasi input tidak tepercaya yang dapat menjadi formula.

## Verifikasi

Gunakan fixture kecil yang bisa dihitung manual. Uji filter/reset, denominator nol, status/refund, nilai negatif, angka besar, locale, timezone dan empty/error. Cocokkan ringkasan, tabel dan ekspor. Label demo selalu terlihat pada contoh.
