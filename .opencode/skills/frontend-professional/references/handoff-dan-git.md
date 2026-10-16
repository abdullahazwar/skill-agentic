# Handoff, git dan publikasi

1. Baca status/diff. Pertahankan perubahan pengguna dan file di luar scope. Jangan reset/force push untuk merapikan riwayat.
2. Tinjau file commit: fixture, screenshot, lockfile dan environment. Jangan commit credential, PII, auth store atau data produksi.
3. Ringkas perubahan menurut perilaku pengguna dan alasan desain. Sebut tes nyata dan batas backend/demo.
4. Commit/push/deploy hanya jika diminta atau sudah masuk scope. Audit saja berarti tanpa edit, instalasi atau menjalankan script tak tepercaya.
5. Periksa target remote, branch dan hasil publikasi. Push paket skill bukan deployment aplikasi.

Untuk PR, tulis masalah, perilaku hasil, validasi dan risiko material. Jangan mengklaim semua route diuji jika hanya satu. Hindari laporan yang hanya mengulang urutan perintah.

Untuk aplikasi baru, dokumentasikan cara menjalankan pada tempat yang sudah dipakai repo. Detail implementasi hanya muncul di alur produk bila membantu pengguna. Jika integrasi belum ada, jelaskan kontraknya kepada developer dan statusnya kepada pengguna.
