# Memasang skill di OpenCode

## Isi

- Instalasi pada repo skill-agentic
- Instalasi global atau proyek aplikasi
- Memulai agent
- Memverifikasi pemuatan
- Memperbarui paket

## Repo skill-agentic

Repo distribusi: https://github.com/abdullahazwar/skill-agentic

Struktur yang dipakai:

    AGENTS.md
    .opencode/agents/cloudflare-terminal.md
    .opencode/commands/cf-audit.md
    .opencode/commands/cf-implement.md
    .opencode/commands/cf-deploy.md
    .opencode/skills/cloudflare-opencode-terminal/SKILL.md

Folder di bawah skill berisi references, scripts dan assets. Perintah shell dijalankan dari terminal biasa. Prompt seperti /cf-audit dijalankan di dalam TUI OpenCode.

## Clone dan periksa

    git clone https://github.com/abdullahazwar/skill-agentic.git
    cd skill-agentic
    opencode --version
    opencode --help
    python3 --version
    node --version

Periksa asal binary jika ada beberapa instalasi:

    command -v opencode

Pada PowerShell, gunakan Get-Command opencode. Contoh Bash di panduan dapat dijalankan di Linux, macOS atau WSL. Jangan mencampurkan sintaks ekspor env Bash dengan PowerShell.

## Pasang secara global

Jalankan dari root repo skill-agentic:

    python3 .opencode/skills/cloudflare-opencode-terminal/scripts/install_opencode.py --global --with-agent --with-commands

Default global ialah ~/.config/opencode. Jika instalasi menggunakan lokasi khusus atau XDG_CONFIG_HOME, berikan lokasinya secara eksplisit:

    python3 .opencode/skills/cloudflare-opencode-terminal/scripts/install_opencode.py --global --config-dir /lokasi/config/opencode --with-agent --with-commands

Installer tidak mengubah opencode.json, AGENTS.md atau provider. Jika ada file berbeda dengan nama sama, installer berhenti sebelum menulis. Cadangkan versi lama dan pindahkan keluar direktori discovery sebelum memperbarui. Jangan mengaktifkan dua skill berbeda dengan nama sama.

## Pasang pada satu aplikasi

    python3 .opencode/skills/cloudflare-opencode-terminal/scripts/install_opencode.py --project /lokasi/proyek-cloudflare --with-agent --with-commands

Hasilnya berada dalam .opencode milik proyek tujuan. Jalankan OpenCode dari proyek aplikasi, bukan dari repo skill-agentic jika tugasnya memperbaiki aplikasi lain.

Untuk memeriksa rencana instalasi tanpa menulis:

    python3 .opencode/skills/cloudflare-opencode-terminal/scripts/install_opencode.py --project /lokasi/proyek-cloudflare --with-agent --with-commands --dry-run

## Memulai agent

    cd /lokasi/proyek-cloudflare
    opencode --agent cloudflare-terminal

Masukkan prompt:

    Muat skill cloudflare-opencode-terminal. Audit proyek ini dan laporkan temuan dengan bukti. Jangan mengubah akun Cloudflare.

Untuk implementasi:

    Muat skill cloudflare-opencode-terminal. Perbaiki bug yang dijelaskan, jalankan test dan dry-run. Pertahankan data dan Worker yang sudah ada.

Untuk CLI non-interaktif jika help lokal mendukung:

    opencode run --agent cloudflare-terminal "Muat skill cloudflare-opencode-terminal. Periksa proyek ini tanpa deploy."

Jangan menganggap shell memahami simbol $skill sebagai pemanggilan skill. Pakai nama skill dalam prompt. Jangan menambahkan model tertentu jika provider/model yang dipakai belum terverifikasi.

## Memverifikasi pemuatan

Periksa agent melalui opencode agent list jika subcommand tersedia. Lihat opencode debug --help sebelum memakai diagnostik skill. Jika debug skill tersedia, gunakan untuk memeriksa name dan lokasi. Keberadaan file tidak membuktikan model telah memuat skill dalam sesi. Minta agent memuat skill dan menyebutkan referensi yang dipakai.

Skill juga dapat dipakai lewat agent Build bawaan tanpa custom agent. Restart sesi setelah pemasangan bila discovery belum berubah.

## Template Worker

Salin assets/worker-starter dari base directory skill ke folder aplikasi baru. Jangan deploy folder paket skill. Setelah memilih nama Worker dan tanggal kompatibilitas:

    npm ci
    npm run types
    npm run check
    npm test
    npm run build
    npm run dev

Starter memakai Node 24 untuk test TypeScript native dan menyertakan lockfile. Deployment nyata dilakukan hanya setelah diminta, dengan akun dan target yang telah diverifikasi.

Sumber: https://opencode.ai/docs/skills/
Sumber: https://opencode.ai/docs/cli/
