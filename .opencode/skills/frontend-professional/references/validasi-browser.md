# Validasi di browser

## Pilih cek berdasarkan perubahan

Baca perintah proyek lalu jalankan format/lint/typecheck/build dan test yang relevan. Jangan mengulang seluruh suite tanpa alasan setelah semua cek terkait lulus. Test memeriksa perilaku, batas data dan regresi, bukan menyalin implementasi.

Gunakan browser/Playwright tersedia. Jika tidak ada, lakukan cek yang mungkin dan catat batasnya. Jangan mengaku telah melihat screenshot atau menguji interaksi jika belum.

## Matriks minimum

| Area | Periksa |
| --- | --- |
| Desktop | Hierarki, alignment, lebar, fokus, data realistis |
| Mobile | Sekitar 360px, navigasi, wrapping, target, form, scroll region |
| Medium | Sekitar 768px dan sisi breakpoint yang berubah |
| Reflow | Konten relevan 320 CSS px dan zoom/pembesaran teks |
| Keyboard | Tab/Shift+Tab, submit, menu/dialog, focus return |
| State | Empty, hasil filter nol, loading, error, sukses, stale sesuai fitur |
| Data | Angka panjang, nol, nama panjang, missing image, locale |
| Motion | Reduced motion dan konten tetap terlihat |
| Teknis | Console error, request gagal, link rusak, overflow |

Viewport bukan bukti tes perangkat fisik. Catat browser dan batas simulasi jika relevan.

## Alur yang bermanfaat

Portofolio: buka karya, pahami konteks, kembali dan temukan kontak. Bisnis: temukan layanan, baca detail, coba form invalid/valid sesuai integrasi. Dashboard: filter, cocokkan total, no-results, reset, ekspor jika ada. Toko: pilih varian, qty, periksa stok/total dan gagal checkout.

Pakai query role/name/label. Playwright punya auto-waiting assertions; hindari sleep acak. Jangan hanya mengambil screenshot tanpa memicu kontrol. Testing Library memprioritaskan query yang mendekati cara pengguna mencari elemen.

## Review visual

Ambil screenshot setelah halaman stabil. Lihat desktop/mobile, viewport awal, tengah, footer, dan state penting. Perbaiki type, spacing, urutan, density, contrast sesuai brief.

Periksa kontrol bawah fold, konten tidak ideal dan URL langsung. Jangan menghapus focus ring atau memotong teks penting demi screenshot.

## Bukti

Catat perintah, hasil, alur browser dan temuan tersisa. Bedakan kegagalan lingkungan dengan produk. Jangan menulis lulus a11y/performance atau production-ready tanpa cakupan bukti.

Sumber: [Playwright assertions](https://playwright.dev/docs/test-assertions), [Testing Library queries](https://testing-library.com/docs/queries/about/).
