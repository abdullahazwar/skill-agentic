# Aksesibilitas

Rujuk WCAG 2.2 dan WAI-ARIA APG. Checklist dan axe saja tidak membuktikan kepatuhan seluruh standar.

## Struktur dan nama

Gunakan lang, title unik, landmark, urutan heading logis, skip link, serta urutan DOM sesuai alur baca. Nama kontrol jelas. Ikon dekoratif tidak perlu dibaca; tombol ikon tetap memiliki accessible name.

Utamakan HTML native sebelum role. Jangan memakai aria-label yang menghilangkan label visual penting. Teks link menjelaskan tujuan dalam konteks.

## Keyboard dan fokus

Uji Tab, Shift+Tab, Enter, Space, Escape, dan panah sesuai widget. Semua aksi dapat dicapai, urutan logis, tidak ada trap, dan focus-visible terlihat. Sticky header/banner/footer tidak menutupi fokus.

Periksa focus saat dialog dibuka/ditutup. Error submit mengarah ke ringkasan/field sesuai konteks tanpa menghapus input. Live announcement seperlunya; jangan umumkan seluruh tabel tiap ketikan.

## Contrast dan warna

WCAG AA meminta 4.5:1 untuk teks normal dan 3:1 untuk teks besar, dengan pengecualian seperti logo/teks insidental. Teks besar setidaknya 18pt reguler atau 14pt bold. Non-text/component yang memenuhi kriteria terkait memerlukan 3:1.

Periksa rasio contrast dari pasangan warna yang benar-benar dirender. Uji warna yang benar-benar dirender. Perhitungan dua warna saja tidak memperhitungkan gradient, opacity, gambar, ukuran/font, hover atau pengecualian. Jangan membulatkan sebelum keputusan lulus. Status tidak bergantung pada warna saja.

## Reflow, zoom dan target

Uji zoom 200%, pembesaran teks, dan reflow setara 320 CSS px untuk konten yang berlaku. Jangan mengunci tinggi viewport sehingga konten hilang. Tabel dua dimensi boleh membutuhkan scroll; region diberi nama dan akses keyboard.

2.5.8 AA memakai target 24 kali 24 CSS px atau alternatif/pengecualian tertentu termasuk spacing. Sekitar 44 CSS px sering nyaman. Jangan menyatakan link inline gagal tanpa memahami pengecualiannya.

## Media dan gerak

Alt menjelaskan fungsi gambar, bukan nama file. Dekoratif memakai alt kosong. Audio/video perlu alternatif sesuai. Hormati reduced motion, hindari autoplay suara, parallax memaksa dan kilatan berbahaya.

## Pemeriksaan

Gunakan tool a11y yang tersedia dan cek manual. Uji alur keyboard serta screen reader bila lingkungan mendukung. Catat jika belum diperiksa. Jangan menyatakan WCAG compliant dari screenshot/lint.

Sumber: [WCAG Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/), [Target Size](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html), [APG](https://www.w3.org/WAI/ARIA/apg/).
