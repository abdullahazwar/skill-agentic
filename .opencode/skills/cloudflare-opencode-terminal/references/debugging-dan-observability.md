# Debugging dan observability

## Isi

- Bukti awal
- Log yang berguna
- Diagnosis error
- Performa
- Pengujian dan penutupan

## Bukti awal

Catat waktu dengan zona, deployment aktif, route, metode, status HTTP dan request ID. Reproduksi sekali dengan input aman. Tentukan apakah request mencapai Worker sebelum mengubah kode.

    npx wrangler tail
    npx wrangler tail --status error

Gunakan environment yang benar. Log real-time bukan arsip lengkap. Sampling dapat menyembunyikan event yang tidak terpilih.

## Log

Gunakan event terstruktur dengan request_id, component, action, duration_ms, status dan error_code tersanitasi. Hindari body mentah, cookie, token, prompt privat serta nilai keuangan yang tidak perlu.

Pisahkan durasi parse, auth, database, AI dan Telegram. Untuk job, gunakan job_id dan attempt. Catat jenis pemicu agar cron tidak tertukar dengan HTTP.

Konfigurasi observability harus seimbang dengan kebutuhan dan biaya:

    {
      "observability": {
        "enabled": true,
        "head_sampling_rate": 1
      }
    }

Sampling 1 ialah contoh pencatatan penuh untuk diagnosis. Evaluasi kembali setelah masalah teratasi. Periksa retensi dan biaya aktual.

## Diagnosis

| Gejala | Langkah awal |
| --- | --- |
| Binding undefined | Nama, config environment, types dan resource |
| 401/403 provider | Key, izin, endpoint dan header, tanpa mencetak secret |
| 429 | Kuota, rate limit, retry_after dan backoff |
| Exception Worker | Log exception dan jalur input |
| CPU/memory limit | Profil, payload, loop, JSON besar dan dependency |
| Hanya produksi gagal | Config/secret, runtime, resource dan tanggal kompatibilitas |
| API mengembalikan HTML | Routing Static Assets/SPA |
| Data setelah edit masih lama | Cache key, KV consistency, respons frontend lama |
| Duplikat transaksi | Retry, idempotency key dan atomic claim |
| Pesan bot tidak terkirim | Webhook info, Telegram response, chat permission |
| Test lokal lolos, domain timeout | DNS/jaringan/route dan log masuk |

Jangan menambal dengan catch yang selalu membalas 200. Tindakan itu dapat menghentikan retry tetapi kehilangan pekerjaan.

## Performa

Bandingkan p50 dan p95 pada beban yang serupa, bukan satu request. Bedakan CPU time dari wall-clock menunggu jaringan.

Kurangi round trip dengan batch SQL, pilih kolom, indeks, payload kecil dan binding langsung. Parallelkan operasi independen. Pertahankan operasi yang bergantung atau harus berurutan.

Cache setelah menentukan sumber kebenaran dan toleransi stale. Optimasi UI dengan update komponen, request cancellation dan menjaga scroll. Jangan menambah polling sebagai obat data basi.

Untuk web, periksa LCP, INP, CLS, ukuran gambar, script dan request berulang. Gunakan perangkat/viewport yang sesuai pengguna, terutama HP.

## Pengujian

- Unit: parsing nominal, validasi, perubahan state dan perhitungan.
- Integrasi lokal: D1 SQL, binding, routing Worker dan asset.
- Konflik: request ganda, stok bersamaan, lease dan retry.
- Otorisasi: dua pengguna dan rute bypass.
- Produksi: health dan smoke read-only setelah deploy.

Jalankan test yang sesuai perubahan. Jangan menambah test yang hanya menyalin implementasi. Setelah lolos, perluas hanya jika ada risiko yang belum terjawab.

## Penutupan

Laporkan penyebab dengan bukti, perubahan, pengujian, deployment/commit, dan metrik sesudah perbaikan. Jika observasi jangka waktu tertentu belum dilakukan, sebutkan dengan jujur. Jangan mengklaim request idle hilang hanya dari satu dry-run.

Sumber: https://developers.cloudflare.com/workers/observability/
Sumber: https://developers.cloudflare.com/workers/observability/metrics-and-analytics/
Sumber: https://developers.cloudflare.com/workers/observability/logs/real-time-logs/
Sumber: https://developers.cloudflare.com/workers/testing/
