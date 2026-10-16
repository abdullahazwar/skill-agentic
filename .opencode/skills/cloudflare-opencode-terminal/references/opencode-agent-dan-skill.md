# Skill, agent, rules dan command OpenCode

## Fungsi tiap komponen

| Komponen | Tugas |
| --- | --- |
| SKILL.md | Instruksi tugas yang dimuat saat relevan |
| references | Detail yang dibaca sesuai kebutuhan |
| scripts | Operasi lokal yang dapat diulang |
| assets | Template yang disalin ke aplikasi |
| Agent Markdown | Primary agent khusus terminal |
| AGENTS.md | Aturan repo yang masuk konteks proyek |
| commands | Prompt singkat seperti /cf-audit |
| opencode.json/jsonc | Provider, model, izin dan konfigurasi OpenCode |

OpenCode membaca skill dari .opencode/skills pada proyek atau ~/.config/opencode/skills secara global menurut dokumentasi yang diperiksa. Direktori compatibility lain dapat berlaku, tetapi pilih satu lokasi agar tidak ada nama ganda.

## Discovery dan base directory

Nama folder harus cocok dengan frontmatter name. Gunakan huruf kecil, angka dan satu tanda hubung antar kata. SKILL.md memakai huruf besar.

Frontmatter paket ini hanya memakai name dan description agar portabel. Tidak ada anggapan bahwa /cloudflare-opencode-terminal otomatis menjadi slash command. Custom commands dipasang terpisah.

Setelah tool skill memuat isi utama, supporting files belum otomatis dibaca. Gunakan base directory yang disediakan tool untuk membuka satu referensi yang diperlukan. Untuk skill global, membaca support file dapat memerlukan permission external_directory sesuai policy pengguna.

## Primary agent

Agent cloudflare-terminal memakai mode primary. Agent tidak menetapkan model sehingga mengikuti pilihan model pengguna. Agent tidak menambahkan izin bash global atau menimpa permission produksi.

Mulai dengan opencode --agent cloudflare-terminal jika CLI lokal mendukung. Dalam TUI, pilih primary agent melalui mekanisme pemilihan versi yang dipakai.

Jangan memanggil subagent otomatis untuk setiap tugas. Delegasikan hanya jika pengguna meminta atau aturan proyek secara jelas membutuhkannya. Tetapkan peran read-only bila hanya meminta review.

## Rules repo

AGENTS.md di root skill-agentic mengarahkan penggunaan paket. Jangan menyalin rules distribusi sebagai aturan universal pada semua proyek.

Untuk proyek aplikasi, gabungkan aturan yang relevan ke AGENTS.md yang sudah ada. Hindari /init pada proyek lama jika belum ditinjau karena perintah itu dapat mengubah rules.

## Slash command yang disertakan

| Command | Hasil yang diminta |
| --- | --- |
| /cf-audit | Diagnosis dengan bukti, tanpa mutasi |
| /cf-implement | Implementasi kebutuhan dalam argumen dan test |
| /cf-deploy | Deployment target yang disebutkan |

Argumen command ialah instruksi pengguna, bukan teks yang boleh dieksekusi sebagai shell mentah. Template tidak memakai substitusi shell otomatis yang mengeksekusi perintah saat command dibuka.

Contoh di TUI:

    /cf-audit bot terus memanggil AI saat tidak ada update
    /cf-implement pertahankan scroll katalog setelah edit stok
    /cf-deploy deploy Worker yang ada pada environment staging

Perintah deploy mewarisi batas instruksi dan permission aktif. Jangan menganggap kata deploy memberi izin menghapus database, mengubah billing atau mengirim pesan produksi.

Sumber: https://opencode.ai/docs/skills/
Sumber: https://opencode.ai/docs/agents/
Sumber: https://opencode.ai/docs/rules/
Sumber: https://opencode.ai/docs/commands/
