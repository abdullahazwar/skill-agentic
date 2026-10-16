# Terminal dan autentikasi

## Isi

- Preflight
- Shell dan output
- Cloudflare
- GitHub
- Dokumen dan MCP

## Preflight

Jalankan di root aplikasi:

    pwd
    git status --short --branch
    git remote -v
    rg --files -g AGENTS.md -g package.json -g '*lock*' -g 'wrangler*'
    opencode --version
    opencode --help
    node --version
    npm --version

Redaksi remote yang memuat kredensial sebelum menyalin output. Jangan mencetak seluruh env. Periksa status tool tanpa memperlihatkan nilai key.

Gunakan helper terminal_preflight.py dengan path skill yang dilaporkan OpenCode. Flag --probe hanya menjalankan version/help binary yang ditemukan dengan timeout. Helper tidak login, install atau deploy.

## Shell

Quote path dan simpan heredoc sebagai literal. Jangan membuat perintah dengan menggabungkan input bebas. Gunakan argumen array pada Python subprocess tanpa shell=True.

Gunakan set -e pada script Bash berurutan jika perintah berikutnya bergantung pada keberhasilan sebelumnya. Hindari separator dekoratif. Baca output dan exit code sebelum melanjutkan.

Simpan process server development pada session yang dapat dihentikan. Jangan meninggalkan wrangler dev, tail atau opencode serve berjalan setelah pengujian selesai.

Jangan memakai nama variabel HOME, home atau CODEX_HOME untuk path sementara. Gunakan nama khusus tugas. Jangan menaruh secret pada flag, URL atau file yang ikut git.

## Cloudflare

    npx wrangler --version
    npx wrangler whoami
    npx wrangler login

Whoami memeriksa identitas. Login hanya diperlukan jika belum terautentikasi untuk operasi yang diminta. Gunakan akun yang dipilih pengguna. Mode tanpa browser atau CI memakai API token dengan scope sesuai melalui mekanisme env/secret CI yang aman.

Gunakan Wrangler lokal dari dependency proyek. Jika belum ada, tinjau package lalu tambahkan versi yang sesuai. Jangan menginstal ulang setiap sesi. Periksa schema pada node_modules/wrangler/config-schema.json untuk binding dan opsi.

    npx wrangler types
    npx wrangler deploy --dry-run

Perintah itu tidak menerbitkan aplikasi, tetapi plugin/toolchain dapat melakukan aktivitas jaringan pendukung. Pastikan sumber proyek dipercaya.

## GitHub

    gh --version
    gh auth status
    git status --short --branch

Jika gh tersedia dan terautentikasi, gunakan gh untuk informasi repo/PR dan git untuk source. Jangan menjalankan gh auth token atau mencetak credential helper.

Jika remote belum ada, cari repo yang dimaksud dari hasil resmi. Jangan push ke repo lain karena namanya mirip. Commit tidak sama dengan push. Sesudah push, periksa branch dan SHA remote.

Jika tidak terautentikasi, siapkan seluruh patch/test/commit yang dapat dilakukan, lalu gunakan alur login resmi. Jangan meminta token ditempel ke prompt.

## Dokumen dan MCP

MCP opsional. Skill tetap bekerja dengan terminal dan dokumentasi resmi. Jika menggunakan MCP Cloudflare, temukan endpoint dari daftar server resmi dan gunakan autentikasi yang tersedia. Jangan menanam token pada config repo.

MCP dokumentasi dan MCP pengelola akun memiliki kemampuan berbeda. Jangan menganggap endpoint docs dapat deploy. Jika tool MCP dan Wrangler sama-sama cukup, pilih jalur paling langsung dan hindari membuat resource dua kali.

Sumber: https://developers.cloudflare.com/workers/wrangler/commands/
Sumber: https://opencode.ai/docs/cli/
Sumber: https://opencode.ai/docs/mcp-servers/
Sumber: https://docs.github.com/en/github-cli/github-cli/quickstart
