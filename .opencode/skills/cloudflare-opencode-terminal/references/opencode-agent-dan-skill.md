# Skill dan aturan proyek OpenCode

## Peran dokumen

SKILL.md memuat alur inti; references berisi detail yang dibaca sesuai kebutuhan. AGENTS.md memuat aturan repo dan harus dihormati dalam lingkup direktori yang berlaku.

Paket ini menyediakan instruksi skill saja. Tidak ada primary agent khusus, slash command, script, installer atau config akun yang ikut dipasang. Gunakan agent/model yang sudah dipilih pengguna.

## Discovery

Nama folder cocok dengan metadata name. Pertahankan SKILL.md dengan penulisan huruf yang tepat. OpenCode memuat skill sesuai lokasi discovery dan permission versi yang digunakan.

Setelah skill dimuat, supporting files tidak otomatis sudah dibaca. Gunakan base directory aktual yang diberikan tool untuk membuka referensi. Skill global mungkin membutuhkan izin membaca direktori luar sesuai kebijakan pengguna.

Nama skill bukan otomatis sebuah slash command. Jangan mengiklankan command yang tidak tersedia.

## Aturan proyek

Baca AGENTS.md aplikasi sebelum bekerja. AGENTS.md repo distribusi mengatur paket panduan dan bukan aturan deployment universal bagi aplikasi lain. Jangan menyalin atau menimpa aturan pengguna tanpa kebutuhan.

Hormati model, provider dan permission yang sudah ada. Delegasi hanya bila pengguna meminta atau aturan proyek membutuhkannya. Skill tidak meningkatkan izin sistem atau akun.

Sumber: https://opencode.ai/docs/skills/
Sumber: https://opencode.ai/docs/rules/
Sumber: https://opencode.ai/docs/agents/
