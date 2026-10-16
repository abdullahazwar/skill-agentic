# GitHub, CI/CD dan deployment

## Distribusi panduan

Repo paket skill hanya berisi Markdown. Jangan menambahkan script, workflow, config, kode contoh aplikasi, credential, identitas akun, atau data produksi. Mem-push panduan tidak memberi izin mengubah aplikasi Cloudflare.

Baca aturan repo, branch, remote dan perubahan pengguna. Stage file yang memang terkait. Tinjau diff sebelum commit, lalu verifikasi branch remote setelah push. Jangan force-push, menghapus branch atau mengikutkan pekerjaan lain tanpa scope.

## Aplikasi yang terpisah

Panduan ini menjelaskan proses jika pengguna kelak meminta implementasi/deploy di repo aplikasi. Baca perintah build dan test proyek terlebih dahulu. Jalankan pemeriksaan tipe/perilaku/runtime yang sesuai. Test unit tidak membuktikan seluruh binding dan routing platform.

Jangan menjalankan script repo tak tepercaya dengan akses credential produksi. Jangan menyalin file konfigurasi akun dari aplikasi ke repo skill.

## Deployment yang diminta

1. Tentukan target akun, aplikasi dan environment secara privat.
2. Periksa resource, secret, migrasi dan jalur pemulihan.
3. Uji perubahan lokal atau staging.
4. Terapkan migrasi kompatibel jika memang diperlukan dan diizinkan.
5. Publikasikan versi yang sudah diuji.
6. Periksa health, route, login dan alur utama sesuai scope.
7. Laporkan versi/commit serta hasil yang benar-benar terverifikasi tanpa membagikan data akun privat.

Jangan mengirim transaksi atau pesan produksi sebagai smoke test kecuali termasuk izin tugas.

## CI/CD sebagai rancangan

Jika pengguna hanya meminta panduan, jelaskan pilihan Workers Builds atau GitHub Actions secara tertulis. Jangan membuat atau mengaktifkan pipeline. Pada pekerjaan aplikasi yang diizinkan, pilih satu jalur utama agar deployment tidak saling menimpa.

Credential CI disimpan pada penyimpanan secret resmi, memiliki scope minimal, dan tidak disertakan dalam repo. Perubahan environment produksi dan akses fork perlu ditinjau sesuai kebijakan proyek.

## Rollback

Bedakan rollback kode dari pemulihan data. Rollback Worker tidak membatalkan perubahan D1, KV, R2, secret atau layanan luar. Pastikan versi lama masih cocok dengan skema. Gunakan perluasan skema, migrasi, lalu penghapusan terencana untuk perubahan besar.

Penghapusan kode/config pada commit baru tidak menghapus isi riwayat lama. Jangan mengklaim seluruh sejarah bersih jika tidak diperiksa.

Sumber: https://developers.cloudflare.com/workers/ci-cd/
Sumber: https://developers.cloudflare.com/workers/configuration/versions-and-deployments/rollbacks/
Sumber: https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions
