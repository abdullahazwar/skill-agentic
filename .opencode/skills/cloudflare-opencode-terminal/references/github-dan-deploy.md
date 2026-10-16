# GitHub, CI/CD dan deployment

## Isi

- Target repo dan perlindungan kode
- Validasi
- Deploy manual dan otomatis
- Rollback
- Distribusi skill

## Target repo

Temukan identitas akun dan repo lewat integrasi yang aktif. Jika pengguna memberi nama repo baru, pertahankan nama persis. Jangan mengganti target dengan repo lain hanya karena aksesnya tersedia.

Untuk repo baru dengan audience tidak ditentukan, preferensikan privat. Jangan mempublikasikan data, token atau kode pribadi tanpa instruksi. Jika alat tidak bisa membuat repo, selesaikan commit lokal lalu jelaskan kemampuan yang kurang. Gunakan kemampuan resmi yang tersedia dan hormati aturan fallback lingkungan.

Baca AGENTS.md dan status branch. Jangan force-push, menghapus branch atau mengikutkan perubahan pengguna yang tidak berkaitan. Stage file spesifik. Periksa diff staged sebelum commit.

    git status --short --branch
    git diff
    git add path-yang-diubah
    git diff --cached --stat
    git diff --cached
    git commit -m "Perbaiki alur yang diminta"
    git push origin nama-branch

Nama branch dan remote harus berasal dari repo nyata. Gunakan identitas git yang sah dari lingkungan, bukan identitas orang lain.

## Validasi

Urutan proyek npm dengan lockfile:

    npm ci
    npm run types
    npm run check
    npm test
    npm run build

Sesuaikan script dengan proyek. Build starter ialah dry-run Wrangler. Typecheck tidak menggantikan pengujian bisnis. Test Node tidak menggantikan integrasi binding/runtime.

Jangan menjalankan script package yang belum ditinjau dari repo tidak tepercaya dengan akses secret produksi.

## Deploy manual

1. Verifikasi akun, Worker dan environment.
2. Pastikan resource, migrasi dan secret siap.
3. Jalankan migrasi backward-compatible jika perubahan memerlukannya.
4. Deploy state sumber yang telah diuji.
5. Catat version/deployment ID dan commit.
6. Uji health, login, API, webhook dan alur utama.

Deploy berhasil secara API belum membuktikan aplikasi berfungsi. Jangan mengirim transaksi nyata sebagai smoke test tanpa izin yang mencakupnya.

## Deploy otomatis

Pilih satu sistem utama: Workers Builds atau GitHub Actions. Hindari dua pipeline menerbitkan Worker yang sama secara bersamaan.

Untuk Workers Builds, periksa repo/branch, root directory, install/build/deploy command, secret dan keterkaitan Worker.

Untuk Actions, gunakan asset deploy-worker.yml.example pada repo aplikasi. File example tidak aktif sebelum disalin ke .github/workflows dengan ekstensi yml. Template memakai workflow_dispatch sehingga push skill tidak memicu deploy aplikasi.

Simpan CLOUDFLARE_API_TOKEN dan CLOUDFLARE_ACCOUNT_ID pada GitHub Actions secrets sesuai kebutuhan. Batasi izin token. Gunakan environment GitHub untuk produksi jika memerlukan aturan deployment.

Gunakan permissions: contents: read dan concurrency agar deploy tidak saling menimpa. Jangan mengirim secret ke workflow PR dari fork. Pin action ke versi/commit yang ditinjau sesuai kebijakan repo.

Migrations perlu langkah tersendiri yang eksplisit. Pipeline tidak boleh otomatis memulihkan backup database atau menghapus resource.

## Rollback

    npx wrangler deployments list
    npx wrangler versions list
    npx wrangler rollback <VERSION-ID>

Periksa sintaks help dan target environment. Gunakan ID yang benar dari hasil alat. Rollback kode tidak membatalkan perubahan D1, R2, KV, secret atau layanan luar. Pastikan kode lama kompatibel dengan skema baru.

Untuk perubahan schema berisiko, gunakan expand, migrate, contract. Penundaan penghapusan kolom memberi jalur rollback yang lebih aman.

## Distribusi skill

Repo skill memuat folder cloudflare-opencode-terminal dengan SKILL.md, agents, references, scripts dan assets. Jangan menyimpan node_modules, state Wrangler, data backup atau secret.

Validasi skill, test script dan template. Setelah commit dan push, periksa SHA branch remote dan satu berkas utama. Laporkan link repo dan commit nyata. Jangan memberi link sandbox ke berkas skill sebagai pengganti penyimpanan yang diminta.

Sumber: https://developers.cloudflare.com/workers/ci-cd/
Sumber: https://developers.cloudflare.com/workers/ci-cd/external-cicd/github-actions/
Sumber: https://developers.cloudflare.com/workers/configuration/versions-and-deployments/rollbacks/
Sumber: https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions
