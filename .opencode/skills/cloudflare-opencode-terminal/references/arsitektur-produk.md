# Arsitektur dan produk

## Tentukan kebutuhan

Catat pengguna, perangkat utama, alur tulis, volume file, jadwal, toleransi data basi, audit dan target biaya. Jangan mulai dengan daftar layanan yang semuanya harus dipasang.

## Peta layanan

| Kebutuhan | Pilihan | Pertimbangan |
| --- | --- | --- |
| API, webhook, frontend ringan | Workers + Static Assets | Satu deployment kode dan aset |
| Website yang sudah memakai Pages | Pages, Functions bila perlu | Pertahankan build yang berfungsi |
| Relasi, transaksi, laporan | D1 | SQL, migrasi, indeks |
| Cache ringkasan/konfigurasi | KV | Terima konsistensi eventual |
| Foto menu, PDF, ekspor | R2 | Simpan metadata kepemilikan di database |
| Koordinasi per chat atau entity | Durable Objects | State dan koordinasi per object |
| Pekerjaan async dengan retry | Queues | Consumer idempoten |
| Proses bertahap yang dapat dilanjutkan | Workflows | Step tahan gangguan |
| Pemicu berkala | Cron Triggers | Tetap berjalan saat tidak ada user |
| Inference AI | Workers AI/provider eksternal | Periksa model dan biaya |
| Retrieval vektor | Vectorize | Cocokkan dimensi embedding |
| Routing dan observasi AI | AI Gateway | Periksa retensi dan billing |
| PostgreSQL/MySQL yang sudah ada | Hyperdrive | Pooling dan jaringan |
| Login staf/internal tool | Access | Validasi identitas backend |
| Publikasi layanan lokal | Tunnel | Komputer asal tetap hidup |
| Perlindungan form | Turnstile | Verifikasi token di server |
| Filter traffic | WAF/rate limiting | Fitur bergantung paket |
| Rendering browser/PDF | Browser Rendering | Periksa kuota dan runtime |
| Binary/container khusus | Containers/Sandbox | Jika runtime Worker tidak cocok |
| Email masuk | Email Routing/Email Workers | Pisahkan routing dan pengiriman |
| Kirim email aplikasi | Email Service/provider resmi | Aktivasi, domain, reputasi |

## Default aplikasi ringan

Gunakan satu Worker untuk API dan aset. Tambahkan D1 bila ada data relasional. Tambahkan R2 bila ada upload. Tambahkan KV setelah menentukan manfaat dan toleransi stale.

Satu Worker dapat menangani fetch webhook dan scheduled. Durable Object class dapat berada pada deployment Worker yang sama. DO tidak otomatis memerlukan Worker kedua. Tambahkan binding dan migrasi class bila dipakai.

Pisahkan Worker jika kebutuhan isolasi akses, dependency, tim, beban, atau domain kegagalan mendukungnya. Pakai service binding untuk komunikasi internal.

## Bedakan kode, data dan file

| Bagian | Lokasi |
| --- | --- |
| HTML/CSS/JS hasil build | Static Assets atau Pages |
| API dan aturan bisnis | Worker |
| Pesanan, harga, stok, transaksi | D1 |
| Ringkasan sementara | KV |
| Foto/PDF | R2 |
| Token dan API key | Workers secrets |
| Kode sumber/migrasi | GitHub atau git proyek |

Frontend dapat berada pada Worker yang sama. Database dan file tetap resource terpisah. Menghapus deployment tidak identik dengan menghapus database.

## Rancang modul

Buat interface berdasarkan tindakan bisnis, misalnya catatTransaksi, terimaWebhook, klaimJadwalJatuhTempo. Simpan query, validasi nominal, ownership, retry dan pemetaan error di implementasinya. Inject adapter waktu, storage dan provider agar test tidak menyentuh produksi.

Handler langsung cukup untuk aplikasi sederhana. Hono berguna saat routing/middleware berkembang. Hindari framework besar tanpa kebutuhan.

## Batas runtime

Worker bukan VPS dengan daemon bebas. Jangan mengandalkan proses selalu hidup, file lokal permanen, atau timer proses untuk pengingat. Periksa dukungan library. Aktifkan nodejs_compat jika dependency memerlukan API Node yang didukung. Jangan menganggap semua modul Node dan binary native berjalan.

Sumber: https://developers.cloudflare.com/workers/static-assets/
Sumber: https://developers.cloudflare.com/workers/runtime-apis/bindings/
Sumber: https://developers.cloudflare.com/workers/runtime-apis/nodejs/
Sumber: https://developers.cloudflare.com/products/
