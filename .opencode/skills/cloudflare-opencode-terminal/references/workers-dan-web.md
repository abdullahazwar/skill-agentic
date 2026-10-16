# Workers, Static Assets dan Pages

## Handler

Gunakan module Worker dengan fetch untuk HTTP. Tambahkan scheduled/queue jika diperlukan. Generate Env dari Wrangler. Jangan menyimpan state pengguna dalam global mutable.

Urutkan route, metode, autentikasi, validasi, aturan bisnis, data, respons. Pakai request ID dan kode error stabil. Jangan mengirim stack trace atau pesan database mentah.

Streaming cocok untuk payload besar. Batasi ukuran sebelum mem-buffer body. Tetapkan timeout provider. Tunggu promise penting. Memakai void tidak membuat pekerjaan tahan gangguan.

## Routing aset dan API

    {
      "assets": {
        "directory": "./public",
        "binding": "ASSETS",
        "run_worker_first": ["/api", "/api/*", "/healthz"]
      }
    }

API/health masuk Worker. Aset cocok dapat melewati jalur kode. Starter tidak memakai fallback SPA karena hanya satu halaman.

Untuk SPA, tambahkan not_found_handling: single-page-application setelah menguji navigasi. Pertahankan Worker-first untuk API agar API salah tidak menjadi HTML 200. Daftarkan callback autentikasi yang harus masuk Worker.

Jika HTML privat, pola API saja tidak cukup. Jalankan Worker pada halaman privat atau lindungi hostname dengan Access. Middleware Worker tidak melindungi aset yang disajikan langsung.

Gunakan env.ASSETS.fetch(request) untuk fallback. Hindari fetch ke URL aplikasi sendiri karena dapat membuat loop.

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

    npx wrangler pages deploy ./dist --project-name nama-proyek

Gunakan nama proyek hasil inventaris. Pisahkan preview dan produksi. Bila migrasi ke Workers, pindahkan route, redirect/header rules, assets behavior, binding, domain dan CI secara terencana.

## Pengujian

Unit test starter memakai Web APIs Node. Test itu tidak membuktikan routing platform atau binding nyata. Tambahkan test runtime Workers untuk perubahan spesifik platform.

Uji di browser: login, input, simpan, kembali, scroll, gambar, refresh manual dan pemulihan offline. Periksa /api/typo secara langsung serta lewat fetch.

Sumber: https://developers.cloudflare.com/workers/static-assets/routing/worker-script/
Sumber: https://developers.cloudflare.com/workers/static-assets/routing/single-page-application/
Sumber: https://developers.cloudflare.com/pages/configuration/build-configuration/
Sumber: https://developers.cloudflare.com/workers/testing/
