# Referensi open source dan dokumentasi

Tanggal pemeriksaan sumber: 17 Oktober 2026, Asia/Jakarta. Daftar ini kurasi pola engineering dari proyek upstream, bukan peringkat popularitas atau jaminan cocok untuk semua produk. Tidak ada kode/aset upstream yang disalin ke paket ini.

## Repo yang dipelajari

| Upstream | Pelajaran yang dapat diambil | Lisensi yang teramati |
| --- | --- | --- |
| [Radix Primitives](https://github.com/radix-ui/primitives) | Primitive aksesibel, composition, focus/keyboard terpisah dari styling | MIT |
| [shadcn/ui](https://github.com/shadcn-ui/ui) | Komponen yang dimiliki dan disesuaikan proyek, bukan desain akhir seragam | MIT |
| [Headless UI](https://github.com/tailwindlabs/headlessui) | Perilaku widget dengan gaya visual yang dapat disesuaikan | MIT |
| [React Spectrum / React Aria](https://github.com/adobe/react-spectrum) | Primitive/interaksi aksesibel dan kebutuhan input beragam | Apache-2.0 |
| [TanStack Table](https://github.com/TanStack/table) | Model tabel headless, sorting/filter/pagination sesuai kebutuhan | MIT |
| [TanStack Query](https://github.com/TanStack/query) | Lifecycle server state, cache, retry dan invalidation | MIT |
| [Astro](https://github.com/withastro/astro) | Situs konten, islands, contoh blog/portofolio sebagai studi struktur | MIT dengan notices upstream pada bagian tertentu |
| [Vercel Commerce](https://github.com/vercel/commerce) | Pemisahan katalog, produk, cart dan integrasi commerce | MIT |
| [GOV.UK Frontend](https://github.com/alphagov/govuk-frontend) | Semantik form, petunjuk, error dan pola layanan | MIT; periksa hak aset/branding secara terpisah |
| [Grafana](https://github.com/grafana/grafana) | Struktur ruang kerja dashboard, konteks data dan eksplorasi | Default AGPL-3.0-only; beberapa direktori berbeda |

Lisensi dibaca dari metadata repo upstream; file LICENSE Astro dan LICENSING Grafana diperiksa terpisah karena metadata tidak cukup. Untuk penggunaan aktual, buka file lisensi pada versi/path yang dipakai, termasuk dependency, font, logo dan gambar. Jangan menganggap lisensi root berlaku tanpa pengecualian.

## Cara mengambil pelajaran

1. Tentukan masalah produk lebih dulu, lalu pilih bagian relevan, bukan seluruh stack.
2. Baca dokumentasi resmi dan source pada versi yang dipakai proyek.
3. Catat pola yang dipelajari, sumber dan alasan pemilihan.
4. Gunakan implementasi yang sesuai stack. Jangan membawa React ke proyek Vue hanya untuk satu widget.
5. Jika kelak menyalin kode pada repo aplikasi, tinjau syarat atribusi/notices/lisensi pada path dan versi tersebut. Paket skill ini tetap tidak menyertakan salinan kode.
6. Gunakan Grafana untuk mempelajari kebutuhan dashboard secara konseptual; jangan mengambil source/aset tanpa meninjau lisensi bagian yang dipakai.
7. Jangan menyalin identitas dagang, logo, screenshot produk atau testimoni seolah milik pengguna.

## Dokumentasi primer

- [Radix introduction](https://www.radix-ui.com/primitives/docs/overview/introduction)
- [TanStack Table](https://tanstack.com/table/latest/docs/introduction)
- [TanStack Query](https://tanstack.com/query/latest/docs/framework/react/overview)
- [React Aria](https://react-spectrum.adobe.com/react-aria/)
- [Astro LICENSE](https://github.com/withastro/astro/blob/main/LICENSE)
- [Grafana LICENSING](https://github.com/grafana/grafana/blob/main/LICENSING.md)
- [WCAG 2.2 Quick Reference](https://www.w3.org/WAI/WCAG22/quickref/)
- [WAI-ARIA APG](https://www.w3.org/WAI/ARIA/apg/)
- [Web Vitals](https://web.dev/articles/vitals)
- [Playwright](https://playwright.dev/docs/test-assertions)
- [Testing Library](https://testing-library.com/docs/queries/about/)
- [OpenCode skills](https://opencode.ai/docs/skills/)

Halaman latest/main dapat berubah. Periksa dokumentasi versi terpasang saat implementasi. Tidak semua tautan indeks telah ditinjau baris demi baris.
