# Domain, DNS dan TLS

## Bedakan identitas

| Identitas | Fungsi |
| --- | --- |
| Account ID | Akun pemilik resource |
| Zone ID | Zona domain tertentu |
| Worker name | Nama deployment |
| Subdomain workers.dev akun | Bagian akun pada hostname Worker |
| Custom Domain | Worker sebagai origin pada hostname khusus |
| Worker Route | Worker di depan origin menurut pola route |

Mengubah subdomain akun bukan mengubah Account ID. Format URL Worker ialah nama-worker.subdomain-akun.workers.dev. Verifikasi hostname dari dashboard/deployment.

## Sesudah mengganti subdomain akun

1. Catat URL lama dan URL baru semua Worker yang terdampak.
2. Periksa workers_dev aktif, nama Worker dan deployment.
3. Uji DNS hostname baru dan koneksi HTTPS.
4. Perbarui webhook Telegram, callback OAuth, allowed origins, URL frontend, link dan monitor.
5. Uji API serta alur aplikasi.
6. Hapus referensi lama setelah perpindahan berhasil.

Layanan luar tidak otomatis mengetahui URL baru. Jangan menganggap URL lama redirect. Token provider umumnya tidak berubah karena domain berubah, tetapi allowlist URL provider dapat perlu diperbarui.

## Custom domain

Gunakan domain yang berada pada akun/zona yang benar. Pilih Custom Domain jika Worker menjadi origin. Pilih Route jika Worker memproses request menuju origin yang sudah ada. Periksa konflik DNS/route sebelum menambah record.

Tentukan custom domain pada proyek aplikasi hanya jika perubahan domain memang diminta. Jangan menerbitkan hostname akun pengguna pada repo panduan.

Jangan menambahkan wildcard luas jika cukup satu hostname. Untuk produksi, pilih domain stabil sehingga perpindahan subdomain workers.dev tidak memaksa pembaruan seluruh integrasi.

## Diagnosis berurutan

| Gejala | Periksa |
| --- | --- |
| NXDOMAIN | Ejaan, nameserver, record dan aktivasi |
| Koneksi timeout sebelum HTTP | DNS, firewall, routing jaringan, ISP, layanan |
| Sertifikat salah | Hostname, provisioning, cakupan sertifikat |
| Redirect loop | Aturan redirect dan mode TLS origin |
| 404 | Route, assets, path API dan deployment |
| 403 | Access, WAF, bot rule, otorisasi |
| 5xx | Exception Worker, origin, quota, provider |
| Hanya API gagal | CORS, URL API, token/sesi dan binding |

Bandingkan domain custom dengan URL workers.dev bila memang diaktifkan. Jika tidak ada log invocation pada waktu tes, jangan langsung menyimpulkan bug kode. Periksa lapisan jaringan lebih dahulu.

## TLS dan cache

Untuk origin milik sendiri, gunakan TLS end-to-end dan Full (strict) jika sertifikat origin memenuhi syarat. Hindari Flexible sebagai tambalan redirect loop. Untuk Worker murni tanpa origin, fokus pada route dan sertifikat hostname.

Jangan matikan verifikasi sertifikat atau memakai curl -k sebagai perbaikan. Purge cache tidak menyelesaikan DNS salah atau webhook yang masih menunjuk alamat lama.

Sumber: https://developers.cloudflare.com/workers/configuration/routing/workers-dev/
Sumber: https://developers.cloudflare.com/workers/configuration/routing/custom-domains/
Sumber: https://developers.cloudflare.com/workers/configuration/routing/routes/
Sumber: https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full-strict/
Sumber: https://developers.cloudflare.com/dns/troubleshooting/
