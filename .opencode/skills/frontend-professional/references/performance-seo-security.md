# Performance, SEO dan keamanan

## Ukur sesuai konteks

Target baik Core Web Vitals saat rujukan diperiksa: LCP paling lama 2.5 detik, INP paling lama 200 ms, CLS paling besar 0.1, pada persentil ke-75 pengguna dan dipisah mobile/desktop. Lighthouse lokal adalah diagnosis lab, bukan bukti field INP atau pengalaman semua pengguna. Verifikasi rujukan terkini bila metrik berubah.

Budget mengikuti halaman, perangkat, jaringan dan kebutuhan. Jangan mengarang skor 100. Catat kondisi, production/development build, data dan cache.

## Praktik berdampak

- Tetapkan dimensi/aspect-ratio media. Pakai ukuran responsif dan format tepat. Jangan lazy-load gambar LCP secara membabi buta; lazy-load bagian bawah fold jika sesuai.
- Minimalkan JavaScript dan pisahkan bagian berat. Jangan menambah chart, animation atau seluruh icon library untuk dekorasi kecil.
- Ukur sebelum optimasi render/long task. Pagination/virtualisasi mengikuti ukuran data. Debounce bukan pengganti API yang tepat.
- Muat font secukupnya; periksa lisensi, subset, fallback dan layout shift. Hindari request pihak ketiga tanpa kebutuhan.
- Cache mengikuti sensitivitas data. Jangan cache response privat secara publik untuk mengejar skor.

## SEO publik

Atur title, description, heading, canonical, metadata share, sitemap/robots dan 404 sesuai arsitektur. Structured data hanya memuat fakta terlihat dan benar, tanpa rating palsu. Rendering mengikuti kebutuhan konten/crawler.

Dashboard privat berbeda dari blog. noindex bukan kontrol akses. Jangan bocorkan PII, token, draft atau data internal lewat HTML, metadata, URL, source map publik dan analytics.

## Keamanan frontend

Jangan masukkan secret ke environment publik, bundle, localStorage atau fixture. Prefix NEXT_PUBLIC/VITE menandai data client, bukan tempat secret; rujuk framework yang terpasang.

Escape teks tidak tepercaya. Jika rich HTML diperlukan, gunakan sanitizer tepat pada batas jelas. Hindari innerHTML/dangerouslySetInnerHTML dari input tanpa pengendalian. Validasi URL/redirect. Jangan memperlakukan input sebagai JavaScript atau shell.

Backend menegakkan auth, otorisasi, transaksi, CSRF sesuai model session, rate limit dan aturan bisnis. Tombol disabled bukan proteksi. Gunakan provider auth/pembayaran proyek.

## Privasi

Kumpulkan data seperlunya, jelaskan penggunaan dan hindari isi form dalam analytics. Ikuti kebutuhan izin/consent proyek tanpa mengklaim kepatuhan hukum yang belum diverifikasi. Demo tidak memerlukan credential atau pengiriman data pribadi.

Sumber: [Web Vitals](https://web.dev/articles/vitals), [MDN performance](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Performance/JavaScript).
