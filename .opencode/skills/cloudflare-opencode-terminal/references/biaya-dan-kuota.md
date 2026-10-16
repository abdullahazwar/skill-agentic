# Biaya dan kuota

## Hitung metrik yang tepat

| Layanan | Metrik penting |
| --- | --- |
| Workers | Request/invocation, CPU, paket dan fitur cache |
| Static Assets/Pages | Jalur aset murni dibanding pemicu kode |
| D1 | Rows read, rows written, storage |
| KV | Read, write, delete, list dan storage |
| R2 | Storage, class operasi, fitur media |
| DO | Request, durasi aktif, storage/operasi |
| Queues | Operasi dan retry |
| Workflows | Eksekusi, langkah, durasi sesuai model billing |
| Workers AI | Model, input/output, unit model dan paket |
| Browser Rendering | Sesi/waktu dan batas produk |
| Provider eksternal | Token, request, file dan fitur provider |

Jangan menyamakan satu klik dengan satu read atau satu query dengan satu row. Kuota aplikasi multi-user dapat berbagi akun/namespace yang sama.

## Verifikasi harga

Sebelum menyebut angka, buka pricing dan limits resmi produk. Catat tanggal, paket, periode reset, scope kuota, biaya tambahan dan aktivasi yang diperlukan. Dashboard billing akun menjadi rujukan pemakaian aktual.

Jangan memakai nilai lama seperti batas neurons, request harian atau CPU dari ingatan. Jangan menjanjikan tidak ada biaya hanya karena paket akun tertulis Free.

Periksa apakah caching yang dipakai ialah Cache API, KV atau fitur Workers Cache terkini. Semantik dan billing berbeda. Pada dokumentasi yang diperiksa, fitur Workers Cache dapat mengenakan request rate pada jalur yang tanpa fitur itu biasanya gratis. Jangan menyamaratakan semua cache.

## Proyeksi

Perkiraan traffic HTTP harian:

    user aktif × aksi per user × API request per aksi

Perkiraan cron:

    1.440 / interval menit

Dengan satu cron tiap lima menit, ada 288 tick per hari meskipun tidak ada jadwal. Tick tidak identik dengan request HTTP browser. Billing setiap jenis event tetap perlu diperiksa terpisah.

Contoh penggunaan alat estimasi:

    python3 scripts/estimasi.py --users 20 --actions 15 --api-per-action 1 \
      --cron-minutes 5 --kv-reads 1 --d1-rows-read 5 --days 30

Alat mengestimasi volume. Alat tidak mengonversi ke Rupiah dan tidak menanam batas free tier. Input harus mencerminkan pola nyata. Tambahkan monitor, retry, subrequest dan operasi tick bila ada.

## Urutan penghematan

1. Hilangkan loop, retry tanpa batas dan polling yang tidak berguna.
2. Pindahkan bot ke webhook jika masih polling tanpa kebutuhan.
3. Hentikan kerja downstream ketika cron kosong.
4. Gunakan due query berindeks, pagination dan batas batch.
5. Kurangi write yang tidak perlu, seperti last_seen setiap endpoint.
6. Gunakan Static Assets secara tepat agar aset publik tidak selalu memicu kode.
7. Batasi AI, gunakan parser manual dan konfirmasi terstruktur.
8. Ukur manfaat cache dan sampling log.
9. Buat alert sesuai produk yang mendukungnya dan pantau billing.

Jangan menghapus data pelanggan atau mematikan pengingat sebagai penghematan tanpa memastikan kebutuhan bisnis.

Sumber: https://developers.cloudflare.com/workers/platform/pricing/
Sumber: https://developers.cloudflare.com/workers/platform/limits/
Sumber: https://developers.cloudflare.com/workers/static-assets/billing-and-limitations/
Sumber: https://developers.cloudflare.com/workers/cache/
Sumber: https://developers.cloudflare.com/d1/platform/pricing/
Sumber: https://developers.cloudflare.com/kv/platform/pricing/
Sumber: https://developers.cloudflare.com/r2/pricing/
Sumber: https://developers.cloudflare.com/workers-ai/platform/pricing/
