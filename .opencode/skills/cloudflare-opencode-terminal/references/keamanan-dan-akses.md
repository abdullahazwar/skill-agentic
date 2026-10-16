# Keamanan dan akses

## Isi

- Identitas dan secret
- Keamanan aplikasi
- Turnstile, WAF dan Access
- Tunnel
- API administrasi

## Identitas dan secret

Gunakan API token dengan izin minimal dan scope akun/zona yang diperlukan. Jangan memakai Global API Key untuk contoh umum. Binding aplikasi tidak memerlukan API token Cloudflare di setiap request.

Jangan menyimpan password admin dalam HTML/JS. Jangan membandingkan password dengan nilai plaintext dari client. Pilih penyedia identitas atau Access bila sesuai. Untuk password aplikasi, gunakan algoritme hash password yang sesuai runtime dan verifikasi parameter terkini.

Gunakan sesi server dengan cookie Secure, HttpOnly, SameSite yang sesuai. Rotasi sesi setelah login dan sediakan logout. Hindari menyimpan bearer token sensitif pada storage browser tanpa mempertimbangkan XSS.

Jangan mencetak nilai env, Authorization, cookie, token Telegram, body keuangan atau isi prompt privat ke log. Saat secret bocor, rotasi/revoke dan tinjau riwayat git. Menghapus satu baris dari commit baru tidak menghilangkan secret pada commit lama.

## Keamanan aplikasi

| Permukaan | Kendali |
| --- | --- |
| SQL | Prepared statement dan allowlist identifier |
| Data multi-user | Ownership di setiap operasi server |
| HTML | Escape output, hindari innerHTML input bebas |
| Form cookie-auth | Proteksi CSRF dan pemeriksaan origin |
| API lintas origin | CORS allowlist, Vary: Origin |
| Upload | Ukuran, MIME, signature, kepemilikan |
| Fetch URL input | Allowlist host/protokol dan kontrol redirect/SSRF |
| Login dan OTP | Rate limit, kedaluwarsa, batas percobaan |
| Error | Kode umum, request ID, tanpa stack |
| Token | Web Crypto dan perbandingan aman yang didukung runtime |

CORS bukan autentikasi. Tanpa CORS pun client non-browser dapat mengirim HTTP. Jangan memasangkan wildcard origin dengan credentialed requests.

## Turnstile

Letakkan sitekey publik pada frontend dan secret pada backend. Kirim token ke server. Server memanggil Siteverify dan memeriksa success serta hostname/action yang diharapkan.

Token Turnstile sekali pakai dan memiliki masa berlaku terbatas. Pada hasil timeout-or-duplicate, minta token baru. Jangan menerima token hanya karena widget menampilkan sukses. Jangan memaksa challenge browser pada webhook mesin seperti Telegram.

## Access dan WAF

Access cocok untuk panel staf. Periksa JWT assertion dengan issuer, audience dan JWKS yang benar jika backend menerima akses langsung. Keberadaan header saja bukan bukti.

Tutup jalur bypass, termasuk hostname alternatif atau workers.dev yang tetap publik. Jangan memasang Access pada endpoint webhook publik tanpa memastikan provider dapat mengautentikasi.

WAF/rate limiting membantu menyaring traffic. Periksa event keamanan sebelum melonggarkan rule. Batasi pengecualian pada route/jenis request yang benar, bukan mematikan seluruh proteksi.

## Tunnel

Tunnel menghubungkan layanan lokal ke Cloudflare tanpa membuka port masuk publik secara langsung. Layanan dan komputer asal harus berjalan. Untuk pengembangan sementara, gunakan mekanisme tunnel resmi. Untuk layanan tetap, gunakan konfigurasi, service manager dan Access yang sesuai.

Jangan mengekspos panel lokal atau database ke internet hanya untuk mempermudah debug. Quick tunnel pengembangan bukan pengganti deployment Worker.

## API administrasi

Gunakan connector atau Wrangler jika cukup. Jika memerlukan REST, ambil endpoint/schema resmi, verifikasi akun/ID, lalu lakukan operasi terkecil.

Untuk daftar resource, tangani pagination. Untuk 429, patuhi retry dan backoff. Retry write hanya jika idempoten atau dilindungi idempotency key. Jangan mengulangi create secara buta setelah timeout karena resource mungkin sudah dibuat.

Pisahkan kredensial CI dari aplikasi. Simpan secret pada penyimpanan resmi. Jangan meminta pengguna menempel token jika tersedia alur pengisian aman.

Sumber: https://developers.cloudflare.com/fundamentals/api/get-started/create-token/
Sumber: https://developers.cloudflare.com/turnstile/get-started/server-side-validation/
Sumber: https://developers.cloudflare.com/cloudflare-one/access-controls/
Sumber: https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/
Sumber: https://developers.cloudflare.com/waf/
