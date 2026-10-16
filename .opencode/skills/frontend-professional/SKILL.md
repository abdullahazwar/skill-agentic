---
name: frontend-professional
description: Panduan Markdown untuk AI agent OpenCode atau agent coding dalam merancang, membangun, memperbaiki dan mengaudit frontend profesional. Gunakan untuk UI/UX, portofolio, bisnis, company profile, landing page, dashboard penjualan/admin, toko online, SaaS, blog, dokumentasi, booking dan web responsif. Mencakup desain sesuai konteks tanpa AI slop, berbagai stack frontend, design system, aksesibilitas, state, integritas data, performance, SEO, pengujian browser serta sumber open source dengan lisensi. Paket hanya instruksi, tanpa kode, script atau konfigurasi akun.
---

# Frontend Profesional

Hasilkan frontend yang membantu pengguna menyelesaikan tugas, punya identitas beralasan dan mudah dirawat programmer berikutnya. Paket ini hanya instruksi Markdown. Tidak ada template kode, config, script, installer, workflow, custom agent atau integrasi akun.

## Alur kerja

1. Tentukan hasil dan batas tugas. Baca AGENTS.md, status, struktur source, manifest/lockfile, route, komponen, token dan test yang relevan. Jangan membuka secret atau menjalankan script repo tanpa meninjau isinya.
2. Tetapkan audiens, tugas utama, jenis website, konten nyata, target perangkat, backend dan acceptance criteria melalui [discovery dan brief](references/discovery-dan-brief.md). Jika cukup jelas, nyatakan asumsi singkat dan lanjutkan.
3. Pertahankan sistem visual untuk perubahan kecil. Untuk proyek baru/redesign, susun [brief desain](references/brief-desain.md) dan pilih satu arah berdasarkan produk.
4. Baca [playbook jenis website](references/jenis-website.md). Untuk dashboard, baca [integritas data](references/dashboard-dan-data.md). Gunakan [arah visual](references/arah-visual.md) dan [design system](references/design-system.md) untuk keputusan komposisi.
5. Jika tugasnya implementasi aplikasi, kerjakan pada repo aplikasi yang diminta, memakai stack yang ada. Selesaikan satu alur utama: semantik, konten, responsive, aksi, validasi dan state. Baca [arsitektur](references/arsitektur-dan-stack.md), [interaksi](references/interaksi-dan-state.md) dan [kontrak state](references/kontrak-state.md).
6. Periksa [aksesibilitas](references/aksesibilitas.md), [performance/SEO/security](references/performance-seo-security.md) serta [validasi browser](references/validasi-browser.md). Jalankan cek terkait, uji alur dan keyboard, lihat screenshot desktop/mobile jika browser tersedia, lalu perbaiki temuan.
7. Tinjau [checklist](references/checklist-review.md), diff dan scope. Laporkan perubahan, tes nyata dan batas tersisa sesuai [handoff](references/handoff-dan-git.md). Push/deploy hanya jika termasuk tugas.

## Standar desain dan fungsi

- Dahulukan konten spesifik, hierarki, ritme, keterbacaan dan fungsi. Jangan memakai susunan hero, logo cloud, bento, testimonial, glow dan gradient yang sama untuk semua jenis produk.
- Efek, warna dan library tidak dilarang mutlak. Gunakan bila membantu identitas atau tugas. Desain khas berasal dari alasan, bukan dekorasi acak.
- Pertahankan design system dan stack yang berjalan. Jangan mengganti seluruh framework, font atau komponen untuk satu perbaikan.
- Gunakan kontrol native untuk hal sederhana dan primitive matang untuk interaksi kompleks. Pelajari [sumber open source](references/sumber-open-source.md) sebagai pola, dengan meninjau lisensi dan asal aset.
- Jangan mengarang klien, testimoni, rating, sertifikasi, dampak bisnis, harga, stock atau pendapatan. Data demo memiliki label yang jelas.
- Kontrol bekerja sesuai label. Integrasi yang belum ada dijelaskan jujur; jangan membuat sukses palsu atau tombol dekoratif.
- Dashboard memiliki sumber, definisi metrik, periode, timezone, mata uang dan izin. Filter memengaruhi ringkasan, tabel, grafik dan ekspor secara konsisten.
- Screenshot, lint atau contrast checker bukan bukti tunggal kualitas, kepatuhan WCAG atau ketiadaan AI slop.

## Peta panduan

| Kebutuhan | Referensi |
| --- | --- |
| Pemasangan dan terminal OpenCode | [Pemasangan dan terminal OpenCode](references/mulai-opencode.md) |
| Discovery dan acceptance criteria | [Discovery dan acceptance criteria](references/discovery-dan-brief.md) |
| Arah visual dan orisinalitas | [Arah visual dan orisinalitas](references/arah-visual.md) |
| Typography, token, responsive dan motion | [Typography, token, responsive dan motion](references/design-system.md) |
| Playbook berbagai website | [Playbook berbagai website](references/jenis-website.md) |
| Dashboard, tabel, filter dan uang | [Dashboard, tabel, filter dan uang](references/dashboard-dan-data.md) |
| Interaksi, form dan lifecycle | [Interaksi, form dan lifecycle](references/interaksi-dan-state.md) |
| Semantik, keyboard dan contrast | [Semantik, keyboard dan contrast](references/aksesibilitas.md) |
| Pilihan stack, state dan komponen | [Pilihan stack, state dan komponen](references/arsitektur-dan-stack.md) |
| Performance, SEO dan keamanan | [Performance, SEO dan keamanan](references/performance-seo-security.md) |
| Browser dan bukti validasi | [Browser dan bukti validasi](references/validasi-browser.md) |
| Repo upstream dan lisensi | [Repo upstream dan lisensi](references/sumber-open-source.md) |
| Brief yang dapat diisi | [Brief yang dapat diisi](references/brief-desain.md) |
| Kontrak perilaku | [Kontrak perilaku](references/kontrak-state.md) |
| Checklist review | [Checklist review](references/checklist-review.md) |
| Handoff, git dan publikasi | [Handoff, git dan publikasi](references/handoff-dan-git.md) |

## Batas paket

Pertahankan seluruh file distribusi sebagai .md. Metadata nama/deskripsi pada SKILL.md hanya untuk discovery, bukan config akun. Jangan menyertakan source aplikasi, JSON/JSONC/TOML, YAML workflow, SQL, script, installer, environment file atau nilai identitas/kredensial pengguna.

Memasang dokumen tidak memerlukan perubahan model/provider/permission atau login Cloudflare. Jika aplikasi memakai Cloudflare, baca skill cloudflare-opencode-terminal sebagai pelengkap hanya ketika tugas menyentuh platform itu. Membuat skill frontend tidak memberi izin operasi akun.

Hasil panduan berupa langkah serta kriteria verifikasi tertulis. Kemampuan implementasi dijalankan kelak pada repo aplikasi yang memang diminta pengguna.
