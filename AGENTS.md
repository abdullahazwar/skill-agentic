# Aturan repo skill-agentic

Repo ini membagikan instruksi Cloudflare untuk AI agent OpenCode di terminal. Repo ini bukan aplikasi Cloudflare yang perlu dideploy.

## Mulai

Muat skill cloudflare-opencode-terminal pada .opencode/skills/cloudflare-opencode-terminal/SKILL.md. Baca supporting files sesuai kebutuhan. Primary agent tersedia pada .opencode/agents/cloudflare-terminal.md.

Untuk pemakaian langsung di repo ini:

    opencode --agent cloudflare-terminal

Untuk memasang pada proyek aplikasi atau global, baca .opencode/skills/cloudflare-opencode-terminal/references/mulai-dan-instalasi.md. Installer tidak menimpa file berbeda dan tidak mengganti konfigurasi provider.

## Struktur

- .opencode/skills/cloudflare-opencode-terminal: skill, referensi, script dan template.
- .opencode/agents: primary agent yang dapat dipilih.
- .opencode/commands: cf-audit, cf-implement dan cf-deploy.
- assets/opencode di dalam skill: sumber template agent/command untuk installer.

Jika mengubah agent atau command, selaraskan template di assets/opencode dan salinan aktif pada .opencode. Jangan menyalin seluruh skill ke system prompt.

## Validasi

Jalankan dari root repo:

    python3 .opencode/skills/cloudflare-opencode-terminal/scripts/validate_skill.py
    python3 .opencode/skills/cloudflare-opencode-terminal/scripts/test_opencode.py
    python3 .opencode/skills/cloudflare-opencode-terminal/scripts/test_tools.py

Template Worker memiliki test terpisah. Setelah npm ci pada folder starter, jalankan npm run types, npm run check, npm test dan npm run build. Build ialah dry-run, bukan publikasi.

## Prinsip

Gunakan bahasa Indonesia sederhana. Hormati permission dan AGENTS.md proyek aplikasi. Periksa versi CLI, akun, Worker, environment, binding dan branch sebelum operasi remote.

Pertahankan data pengguna dan perubahan lokal. Jangan menanam token, password, ID akun pengguna nyata, auth.json, .env asli atau backup produksi di repo.

Gunakan dokumentasi resmi terkini untuk field konfigurasi, API, batas, model dan harga. Jangan mencampur schema dokumentasi OpenCode dev/v2 dengan konfigurasi utama tanpa verifikasi.

Instruksi deploy aplikasi harus menyebut target aplikasi. Jangan menjalankan wrangler deploy dari repo paket skill. Commit dan push repo ini hanya memublikasikan instruksi.
