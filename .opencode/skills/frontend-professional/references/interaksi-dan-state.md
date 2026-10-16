# Interaksi, form dan state

## Kontrak sebelum implementasi

Definisikan trigger, input, awal, loading, hasil, kegagalan, retry, dan efek URL/focus. Gunakan referensi kontrak-state.md untuk alur kompleks. Jangan menambah state yang tidak berguna.

| Situasi | Perilaku |
| --- | --- |
| Loading awal | Konteks stabil, status bermakna, layout tidak melompat |
| Refetch | Pertahankan data valid, tandai sedang diperbarui |
| Dataset kosong | Jelaskan belum ada data dan tindakan pertama |
| Filter nol | Tampilkan filter aktif dan reset |
| Error | Pesan yang dapat ditindaklanjuti, retry, input tetap ada |
| Sukses | Konfirmasi hasil nyata dan langkah berikutnya |
| Partial/offline/stale | Jelaskan batas data dan aksi yang masih tersedia |
| Permission/session | Bedakan tidak berhak, belum login dan sesi habis |

## Kontrol dan navigasi

Link untuk berpindah, button untuk aksi. Hindari clickable div tanpa semantik/keyboard. Jangan menaruh button di dalam link atau form di dalam form. Dropdown, tabs, combobox dan dialog punya pola keyboard berbeda; gunakan primitive proyek atau WAI-ARIA APG.

Dialog perlu nama, focus masuk, trap yang benar jika modal, Escape bila sesuai, dan focus kembali ke pemicu. Menu mobile harus bisa ditutup, memiliki expanded state, dan tidak menahan fokus saat tersembunyi.

Link aktif/breadcrumb membantu orientasi. Route change tidak meninggalkan fokus pada elemen hilang. Copy memerlukan status sukses/gagal yang jujur; clipboard bisa gagal.

## Form

Gunakan label terhubung, type/autocomplete/inputmode sesuai data, petunjuk dan format. Placeholder bukan label. Error dekat field menggunakan aria-describedby/aria-invalid. Untuk form panjang, buat error summary berisi link field. Jangan hanya mengandalkan warna.

Pertahankan input saat error. Cegah submit ganda dan beri status loading pada aksi relevan. Validasi server tetap wajib. Optimistic update membutuhkan rollback, idempotensi, retry dan penanganan konflik.

Validasi native cocok untuk kasus sederhana. Jika memakai custom, jangan buat native/custom saling bertentangan. Pesan menyebut masalah dan cara memperbaiki.

## Destructive dan integrasi

Sebut objek serta akibat perubahan/penghapusan. Sediakan undo yang nyata atau konfirmasi sesuai dampak. Jangan meminta konfirmasi untuk klik biasa.

Labeli demo sebelum pengguna memasukkan data. Jangan mengumpulkan password, kartu atau data pribadi untuk simulasi. Ringkasan lokal boleh dipakai, tetapi jangan mengklaim email, booking, pembayaran atau database sudah diperbarui.
