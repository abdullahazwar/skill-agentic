# Jadwal dan pekerjaan background

## Isi

- Memilih pemicu
- Zona waktu
- Cron yang hemat
- Claim dan retry
- Antrean dan workflow

## Memilih pemicu

| Kebutuhan | Mekanisme |
| --- | --- |
| HTTP atau webhook | fetch |
| Tugas berkala global | scheduled dan Cron Triggers |
| Waktu berikutnya per entity | Durable Object alarm |
| Kerja async dengan retry | Queues |
| Proses panjang bertahap | Workflows |
| Telemetri singkat setelah respons | ctx.waitUntil dalam batas runtime |

Cron selalu memicu jadwal yang terpasang meskipun tabel kosong. DO alarm hanya dipasang saat ada pekerjaan berikutnya dan harus dijadwalkan ulang secara sengaja. Mengganti cron dengan DO mengubah biaya/semantik, jadi ukur dan verifikasi paket.

## Zona waktu

Cron Cloudflare menggunakan UTC. Simpan waktu sebagai timestamp UTC dan zona IANA, misalnya Asia/Jakarta. Pukul 21.00 WIB sama dengan 14.00 UTC. Jangan menerapkan offset WIB ke semua pengguna.

    {
      "triggers": {
        "crons": ["0 14 * * *"]
      }
    }

Contoh itu untuk validasi malam setiap hari, bukan pengingat jam bebas. Pengingat menit tertentu membutuhkan scheduler yang sesuai. Jangan menurunkan frekuensi cron hingga melewati toleransi keterlambatan yang diminta.

Untuk jadwal kuliah mingguan, simpan hari, waktu mulai/selesai, dosen dan zona. Validasi kehadiran dosen pada occurrence besok, bukan mematikan seluruh matkul selamanya. Hubungkan tugas kelompok lewat course_id, dengan konfirmasi jika nama matkul ambigu.

## Cron yang hemat

1. Query pekerjaan due dari indeks berdasarkan status dan waktu.
2. Batasi batch.
3. Bila kosong, return tanpa AI, scan user, update KV atau self-fetch.
4. Claim pekerjaan secara atomik dengan lease/token.
5. Kerjakan hanya pekerjaan yang berhasil diklaim.
6. Catat hasil dan waktu berikutnya.

    SELECT id FROM reminder_jobs
    WHERE status = 'pending' AND next_attempt_at <= ?
    ORDER BY next_attempt_at
    LIMIT 50;

Angka 50 ialah ukuran batch contoh, bukan batas platform. Pantau backlog dan sesuaikan.

## Claim dan retry

Lakukan conditional UPDATE untuk status pending atau lease kedaluwarsa. Periksa perubahan baris. Simpan claim token dan pastikan hanya pemegang token dapat menyelesaikan job.

Status dapat berupa pending, processing, sent, failed, cancelled. Simpan attempts, next_attempt_at dan lease_until. Buat indeks untuk due query dan recovery lease. Jangan melakukan read-then-write KV untuk claim.

Gunakan exponential backoff dengan jitter dan jumlah percobaan terbatas. Hormati retry_after provider. Pisahkan error permanen, seperti chat diblokir, dari gangguan sementara.

Pengiriman eksternal dapat sukses sebelum penanda sent tersimpan. Pada celah crash ini, retry dapat menggandakan pesan. Jangan menjanjikan exactly-once tanpa dukungan idempotensi end-to-end. Tetapkan kompromi duplikat versus kehilangan secara eksplisit.

## Antrean dan workflow

Untuk Queues, producer hanya mengakui penerimaan setelah enqueue berhasil. Consumer idempoten, memiliki batas retry dan jalur dead-letter. Jangan menelan error sehingga pesan gagal dianggap sukses.

Untuk Workflows, buat step yang dapat diulang dengan aman. Jangan mengulang side effect saat replay. Simpan referensi file besar di R2, bukan seluruh bytes dalam state langkah. Berikan status proses yang ringkas kepada pengguna.

Untuk DO, ikuti pola class resmi dan migrasi new_sqlite_classes yang berlaku. Pakai class extends DurableObject. Uji alarm ganda, recovery dan object eviction. WebSocket hibernation berguna pada koneksi realtime yang lama idle.

## Uji jadwal

    npx wrangler dev --test-scheduled
    curl "http://localhost:8787/__scheduled"

Uji kosong, due, not-yet-due, cron tumpang tindih, lease habis, provider timeout dan pembatalan. Jangan memicu pengingat produksi untuk sekadar test.

Sumber: https://developers.cloudflare.com/workers/configuration/cron-triggers/
Sumber: https://developers.cloudflare.com/durable-objects/api/alarms/
Sumber: https://developers.cloudflare.com/queues/best-practices/
Sumber: https://developers.cloudflare.com/workflows/build/rules-of-workflows/
Sumber: https://developers.cloudflare.com/workers/runtime-apis/context/
