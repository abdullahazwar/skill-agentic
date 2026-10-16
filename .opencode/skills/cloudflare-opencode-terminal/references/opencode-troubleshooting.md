# Troubleshooting OpenCode

| Gejala | Pemeriksaan dan tindakan |
| --- | --- |
| Skill tidak terlihat | Nama folder/frontmatter, SKILL.md uppercase, lokasi discovery, skill permission, nama duplikat |
| Agent tidak muncul | File .opencode/agents atau config global, frontmatter, restart sesi |
| Agent tidak membaca referensi | Muat skill dulu, gunakan base directory aktual, periksa external_directory |
| Unknown flag | Baca --help subcommand pada binary yang benar |
| Unexpected positional argument | CLI lokal tidak menerima argumen tambahan itu |
| Model tidak tersedia | Periksa opencode models dan provider/model persis |
| Provider 401/403 | Autentikasi provider, endpoint, scope, tanpa membuka key |
| 9Router gagal | Periksa base URL/protokol/provider yang sebenarnya, lalu format model dan API kompatibilitas |
| Wrangler tidak ditemukan | Dependency proyek dan Node/PATH, bukan OpenCode model |
| Bash ditolak | Permission aktif dan agent override, jangan mengubah policy untuk melewatinya |
| Config invalid | JSONC, schema versi, field salah atau campuran format v1/dev |
| Package starter tidak ikut git | Periksa .opencode/.gitignore. Pola basename dapat mengabaikan package.json dan lockfile di dalam assets skill |
| Headless berhenti | Prompt permission, login, provider, timeout atau batas iterasi |
| Output secret muncul | Hentikan penyebaran, redaksi dan rotasi secret yang benar-benar terpapar |
| uv_interface_addresses | Batas OS/runtime saat dev server, bedakan dari bug source |

## Kasus models 9Router

Jangan mengasumsikan setiap binary menerima opencode models 9router. Mulai dengan:

    opencode --version
    opencode models --help
    opencode models

Jika help mendukung filter positional provider, pakai provider ID yang tercantum. Jika tidak, gunakan daftar tanpa argumen atau filter output secara lokal. Jangan mengganti command acak berulang.

Nama provider OpenCode, model upstream dan model alias router dapat berbeda. Jangan menebak endpoint 9Router atau menimpa konfigurasi yang sudah dipakai. Gunakan nilai dari service/config yang ditunjuk pengguna.

## Tools dan varian versi

Dokumentasi utama yang diperiksa memakai permission, agent dan tool skill berbasis name. Halaman dev/v2 dapat berbeda. Periksa schema versi terpasang sebelum menulis config.

Jangan memakai flag --standalone, --server, --refresh atau --auto kecuali help binary lokal mendukung dan efeknya sesuai tujuan. Flag yang membuat persetujuan otomatis bukan solusi untuk command salah.

## Jaringan dan provider lokal

OpenCode, router, Ollama dan Cloudflare ialah layanan berbeda. Model lokal dapat menjawab tanpa biaya API provider, tetapi tetap memerlukan RAM, konteks dan tool yang memadai. Ketersediaan tools/model harus diuji.

Tidak semua model kompatibel dengan tool calling yang diperlukan agent. Uji tugas kecil: membaca satu file, menjalankan version command, dan merangkum hasil. Jangan menguji kredensial produksi pada model/provider yang belum dipercaya.

## Verifikasi pemuatan tanpa model

Jika CLI menyediakan debug skill dan agent list, gunakan untuk memeriksa konfigurasi tanpa menjalankan tugas berbayar. Itu membuktikan discovery, bukan kualitas penalaran atau keberhasilan deploy.

Jika CLI belum ada, validasi file, installer dan YAML/JSON secara lokal. Nyatakan bahwa integrasi runtime belum diuji. Jangan membuat simulasi yang diklaim sebagai output OpenCode nyata.

## File starter terabaikan oleh git

Pada pengujian OpenCode 1.19.3, CLI membuat .opencode/.gitignore dengan pola package.json, package-lock.json dan .gitignore tanpa awalan /. Pola itu juga cocok dengan file template di bawah skill.

Periksa sebelum commit:

    git check-ignore -v .opencode/skills/cloudflare-opencode-terminal/assets/worker-starter/package.json
    git ls-files .opencode/skills/cloudflare-opencode-terminal/assets/worker-starter

Untuk repo distribusi ini, pola dibatasi ke root .opencode memakai awalan /. Contoh tersedia pada assets/opencode/gitignore.example. Pada proyek lain, tinjau aturan lama terlebih dahulu dan jangan mengganti seluruh .gitignore pengguna. Jangan memakai force-add massal karena file rahasia mungkin sengaja diabaikan.

Sumber: https://opencode.ai/docs/cli/
Sumber: https://opencode.ai/docs/skills/
Sumber: https://opencode.ai/docs/troubleshooting/
