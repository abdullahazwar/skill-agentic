# Arsitektur dan pilihan stack

## Gunakan stack yang berjalan

Pertahankan framework, router, package manager, dan lockfile. Periksa versi terpasang dan dokumentasi resminya sebelum API baru. Jangan mencampur App Router/Pages Router atau contoh server/client beda versi. Jangan upgrade massal untuk memperbaiki UI.

Untuk proyek baru, pilih sesuai kebutuhan, host, tim dan integrasi. HTML/CSS dengan JavaScript secukupnya cocok untuk statis sederhana. Astro dapat cocok untuk konten dan islands. React/Vue/Svelte dengan tooling sesuai cocok untuk aplikasi interaktif. Next/Nuxt/SvelteKit membantu saat routing/server rendering dibutuhkan. Tidak ada pemenang universal.

## Komponen dan styling

Pisahkan page composition, domain component, primitive UI, dan adapter saat batasnya membantu. Jangan membuat file raksasa atau abstraksi generik untuk dua baris. Props menyatakan kebutuhan nyata; state tidak saling bertentangan.

Gunakan CSS modules, scoped CSS, utility CSS atau sistem repo secara konsisten. Tailwind tetap membutuhkan token; CSS biasa tetap membutuhkan sistem. Hindari inline style acak, !important bertumpuk dan perubahan global yang mematahkan halaman lain.

Gunakan primitive aksesibel yang terpasang untuk dialog/combobox/menu. Radix, React Aria dan Headless UI berbeda ekosistem; jangan memasang semua untuk satu kebutuhan. Kode shadcn dimiliki proyek dan tetap perlu penyesuaian/pemeliharaan.

## Data dan typing

Pisahkan server state, URL, form, serta state presentasi. Hindari hasil filter duplikat yang mudah tidak sinkron. TanStack Query/Table membantu bila caching/tabel memerlukannya; tabel kecil tidak selalu memerlukan dependency.

Gunakan tipe response, missing value, loading/error dan status domain. Validate data eksternal pada batas relevan. Hindari any menyeluruh serta non-null assertion untuk menyembunyikan kontrak. Tangani race lewat pembatalan atau mekanisme library.

Pada SSR, pisahkan server, credential dan client. Jangan menjadikan seluruh halaman client hanya karena satu kontrol. Otorisasi serta harga transaksi berasal dari backend.

## Dependency

Baca package script sebelum menjalankan. Gunakan lockfile dan instalasi reproducible sesuai package manager. Dependency baru harus memiliki kebutuhan, ukuran, lisensi, pemeliharaan dan kompatibilitas yang masuk akal. Jangan edit lockfile manual. Jangan membawa seluruh library icon/chart/animation untuk satu dekorasi.

## Cloudflare

Muat cloudflare-opencode-terminal saat aplikasi memang membutuhkan konfigurasi/deploy Cloudflare. Skill frontend tidak memberi izin baru untuk resource, DNS atau deployment. Repo skill-agentic adalah paket instruksi, bukan aplikasi produksi.
