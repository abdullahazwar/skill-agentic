# Bot Telegram dan diagnosis request saat diam

## Isi

- Inventaris dan pengukuran
- Webhook yang andal
- Idempotensi
- Permintaan saat idle
- Interaksi dan banyak pengguna
- Pengujian penerimaan

## Inventaris dan pengukuran

Temukan Worker aktif, URL webhook, secret names, binding, triggers, version dan repositori. Periksa getWebhookInfo memakai jalur autentikasi yang tidak membocorkan token. Catat URL, pending_update_count, last_error_date dan last_error_message tanpa mencatat kredensial.

Telegram token berada pada URL API. Jangan menuliskan URL bertoken ke log, shell history atau output alat. Untuk script operasional, ambil secret dari env dan redaksi pesan error HTTP.

Ukur dua periode: tanpa interaksi dan dengan satu update. Bedakan invocation fetch/scheduled/queue/alarm, outbound subrequest, query D1 dan operasi KV. Jangan menyebut semua metrik sebagai request yang sama.

## Webhook

1. Terima hanya POST pada path webhook.
2. Validasi header X-Telegram-Bot-Api-Secret-Token dengan secret server.
3. Batasi ukuran dan validasi JSON/update_id.
4. Tentukan user/chat dari update Telegram yang diverifikasi.
5. Simpan durable inbox atau enqueue sebelum membalas sukses jika kerja dilanjutkan async.
6. Kembalikan respons cepat setelah penerimaan tahan gangguan berhasil.
7. Jalankan pemrosesan idempoten dengan retry terbatas.

Untuk operasi singkat, pemrosesan dapat ditunggu sebelum 2xx. Untuk AI atau PDF panjang, gunakan queue/workflow. Jangan membalas 200 sebelum simpan/enqueue berhasil lalu mengandalkan promise biasa. waitUntil sendiri tidak menggantikan durable delivery.

Gunakan setWebhook dengan URL HTTPS hasil deployment, secret_token dan allowed_updates yang sesuai. Jangan menjalankan getUpdates polling bersamaan. Jangan melakukan setWebhook pada setiap request atau cron.

Saat URL berubah, perbarui webhook dan verifikasi kembali. Token bot biasanya tetap sama. Jangan memakai drop_pending_updates kecuali memang diminta membuang antrean.

## Idempotensi

Gunakan key gabungan bot_id dan update_id. Unique insert D1 atau koordinasi DO mencegah klaim ganda. Status inbox harus mendukung recovery.

Baris inbox yang sudah ada belum tentu selesai. Bedakan done dari processing dengan lease aktif, pending yang harus dilanjutkan, serta failed yang dapat retry. Jangan mengakui semua duplicate sebagai selesai jika proses sebelumnya crash.

Efek database perlu idempotency key tersendiri. Pengiriman pesan eksternal mempunyai celah crash setelah send sukses. Simpan message_id hasil provider dan gunakan outbox, tetapi tetap jelaskan batas jaminannya.

## Diagnosis request idle

| Bukti | Dugaan | Perbaikan yang sesuai |
| --- | --- | --- |
| scheduled setiap menit | Cron aktif | Sesuaikan frekuensi, query due berindeks, early return |
| fetch dengan update_id sama | Retry Telegram | Periksa webhook timeout/non-2xx, inbox dan idempotensi |
| fetch dari monitor | Health check eksternal | Kurangi frekuensi yang tidak diperlukan |
| Fetch berulang dari browser | Polling/UI refresh | Refresh saat perlu, batalkan saat tab tersembunyi |
| Path sama memanggil diri sendiri | Self-fetch loop | Panggil fungsi internal atau service binding |
| Banyak operasi KV tanpa update | Scan/list semua user | Hapus scan kosong, baca key yang relevan |
| AI dipanggil dari health/cron kosong | Alur salah | Jalankan AI hanya untuk pekerjaan valid |
| Alarm terus dipasang ulang | Scheduler tanpa kerja | Jadwalkan hanya next due yang ada |

Jangan mematikan semua cron pada bot pengingat karena notifikasi bisa berhenti. Untuk bot pencatat keuangan tanpa fitur terjadwal, hapus trigger aplikasi yang tidak punya fungsi setelah memeriksa kebutuhan lain.

Bot tanpa update tidak perlu memanggil Telegram atau model AI. Endpoint publik masih dapat menerima scan internet. Cron idle yang terpasang tetap memiliki invocation. Tunjukkan penyebab dan hasil perbandingan metrik.

## Interaksi dan banyak pengguna

Pisahkan parser manual dari AI. Gunakan AI untuk ekstraksi terstruktur, lalu validasi nominal, dompet dan kategori. Tampilkan konfirmasi sebelum menyimpan bila ambigu. Transfer ke orang lain berbeda dari perpindahan saldo antar wallet sendiri.

Gunakan callback berisi ID dan action, lalu verifikasi pemilik di server. Callback data bukan otorisasi. Jawab callback segera agar indikator Telegram berhenti.

Edit keyboard pesan lama setelah action selesai. Simpan message_id terpisah untuk menu, grafik dan konfirmasi. Untuk aksi baru setelah grafik, kirim pesan baru bila edit media/caption akan menyembunyikan alur. Jangan mengedit sembarang pesan lama hanya karena memiliki ID.

Gunakan state percakapan per bot/chat/user yang tepat untuk private/group. TTL sesi tidak menghapus transaksi. Jangan menampilkan active users yang tidak dapat dihitung dari sumber nyata.

## Pengujian penerimaan

- Satu update menghasilkan satu perubahan data.
- Duplicate dan dua update serentak tidak menggandakan transaksi.
- Crash sebelum/sesudah enqueue dapat dipulihkan.
- User A tidak dapat menjalankan callback user B.
- Satu cron kosong tidak memanggil AI atau Telegram.
- Jadwal due terkirim dalam toleransi dan retry berhenti.
- Tombol setelah grafik melanjutkan alur yang terlihat.
- Secret salah ditolak tanpa membuka kredensial.

Sumber: https://core.telegram.org/bots/api#setwebhook
Sumber: https://core.telegram.org/bots/api#getwebhookinfo
Sumber: https://core.telegram.org/bots/api#answercallbackquery
Sumber: https://developers.cloudflare.com/workers/observability/metrics-and-analytics/
