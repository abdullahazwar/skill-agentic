# Workers, Static Assets dan Pages

## Handler

Gunakan module Worker dengan fetch untuk HTTP. Tambahkan scheduled/queue jika diperlukan. Generate Env dari Wrangler. Jangan menyimpan state pengguna dalam global mutable.

Urutkan route, metode, autentikasi, validasi, aturan bisnis, data, respons. Pakai request ID dan kode error stabil. Jangan mengirim stack trace atau pesan database mentah.

Streaming cocok untuk payload besar. Batasi ukuran sebelum mem-buffer body. Tetapkan timeout provider. Tunggu promise penting. Memakai void tidak membuat pekerjaan tahan gangguan.

## Routing aset dan API

Rancang pemisahan route API, health dan aset. Periksa jalur mana yang benar-benar menjalankan Worker agar proteksi tidak dilewati.

Untuk SPA, pilih mode fallback SPA pada konfigurasi aplikasi secara privat setelah menguji navigasi. Pertahankan Worker-first untuk API agar API salah tidak menjadi HTML 200. Daftarkan callback autentikasi yang harus masuk Worker.

Jika HTML privat, pola API saja tidak cukup. Jalankan Worker pada halaman privat atau lindungi hostname dengan Access. Middleware Worker tidak melindungi aset yang disajikan langsung.

Gunakan binding aset yang didukung runtime untuk meneruskan request fallback. Hindari fetch ke URL aplikasi sendiri karena dapat membuat loop.

| Respons | Penanganan |
| --- | --- |
| JSON privat | Cache-Control: no-store |
| Mutasi sukses | ID dan state final yang tersimpan |
| API tidak dikenal | JSON 404 |
| Metode salah | 405 dan Allow |
| OPTIONS lintas origin | Allowlist dan preflight |
| Error internal | Kode umum dan request ID |

## Frontend mobile

Gunakan viewport, label form, fokus keyboard, kontras, tombol sentuh yang cukup besar dan state loading. Grid dua kolom sesuai untuk katalog selama nama/harga terbaca. Tambahkan pencarian.

Sesudah mutasi, perbarui komponen terkait. Hindari reload seluruh halaman. Pertahankan scroll, filter, isi form dan navigasi. Cegah respons lama menimpa state baru.

Rollback UI optimistis jika server gagal. Untuk pembayaran/stok, konfirmasi akhir berasal dari server. Uji tap ganda, jaringan putus, retry dan pergantian halaman.

Jangan menaruh API key pada JavaScript frontend. Variabel build publik tetap terlihat pengunjung.

## Pages yang sudah berjalan

Periksa root directory, build command, output directory, branch produksi, env, Functions dan binding. Deploy hasil build yang benar.

Gunakan nama proyek hasil inventaris. Pisahkan preview dan produksi. Bila migrasi ke Workers, pindahkan route, redirect/header rules, assets behavior, binding, domain dan CI secara terencana.

## Pengujian

Unit test berbasis Node tidak membuktikan routing platform atau binding nyata. Tambahkan test runtime Workers untuk perubahan spesifik platform.

Uji di browser: login, input, simpan, kembali, scroll, gambar, refresh manual dan pemulihan offline. Periksa /api/typo secara langsung serta lewat fetch.

Sumber: https://developers.cloudflare.com/workers/static-assets/routing/worker-script/
Sumber: https://developers.cloudflare.com/workers/static-assets/routing/single-page-application/
Sumber: https://developers.cloudflare.com/pages/configuration/build-configuration/
Sumber: https://developers.cloudflare.com/workers/testing/
