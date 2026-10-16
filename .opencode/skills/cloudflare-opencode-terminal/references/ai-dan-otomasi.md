# AI dan otomasi

## Workers AI

Tambahkan binding AI hanya jika inference diperlukan. Pilih model dari katalog saat implementasi. Jangan menjanjikan model lama masih tersedia atau kuota tetap sama.

Generate tipe setelah perubahan. Ikuti input/output model yang dipilih. Jangan menganggap seluruh model menerima parameter chat yang sama. Workers AI memakai layanan remote, sehingga pengujian binding dapat memakai kuota nyata.

Simpan nama model sebagai konfigurasi non-secret yang jelas. Simpan key provider eksternal sebagai secret per provider. Bedakan model klasifikasi cepat, penalaran, embedding, ASR dan gambar.

## AI dalam bot keuangan

Gunakan parser deterministik untuk nominal umum dan AI untuk teks ambigu. Minta output terstruktur dengan tipe transaksi, amount, wallet, category dan confidence. Validasi semua field di backend.

Nilai "200 rb" harus menjadi 200000 Rupiah. Bedakan "tf ke teman" sebagai keluar dari "pindah BCA ke DANA" sebagai transfer antar wallet. Jangan membiarkan model langsung menjalankan SQL atau mengubah saldo.

Untuk kategori produk, gunakan daftar yang diizinkan. Alias seperti nasgor dapat dipetakan ke makanan, boba ke minuman. Pertahankan flow manual yang sudah berfungsi. Jika ambigu, minta konfirmasi.

## Batas dan kegagalan

Tetapkan timeout, batas input/output, batas retry dan budget user. Retry hanya error sementara. Jangan berganti model tanpa batas saat semua provider kehabisan kuota.

Bedakan quota/rate limit, kredensial, model tidak ada, format output salah, input terlalu panjang dan penolakan model. Simpan error code tersanitasi. Jangan mengubah semua error menjadi INTERNAL_ERROR.

Untuk output panjang, stream bila provider mendukung. Jika parsing JSON memerlukan hasil lengkap, batasi ukurannya. Validasi schema dan tampilkan field yang perlu dikoreksi.

## AI Gateway dan RAG

AI Gateway dapat membantu routing, logging, cache dan pengendalian provider sesuai fitur terkini. Periksa apakah prompt/respons disimpan dan siapa yang dapat mengaksesnya. Jangan cache jawaban finansial user dengan key bersama.

RAG memerlukan dokumen, chunking, embedding, Vectorize index dan metadata. Dimensi index harus sama dengan model embedding. Filter tenant pada upsert dan query. Hapus vektor saat dokumen sumber dihapus atau akses dicabut.

Gunakan ID stabil dan versi embedding. Perubahan model dapat memerlukan re-embedding dan index baru. Pisahkan hasil retrieval dari instruksi tepercaya. Teks dokumen/email tidak boleh memberi izin memakai alat atau membocorkan secret.

## PDF dan proses panjang

Pisahkan tahap isi, perapihan, sitasi dan render. Gunakan job ID, state durable dan progress yang jujur. Simpan file hasil di R2. Kirim attachment setelah file lolos pemeriksaan.

Batasi quality review dan revisi. Bila batas habis, beri alasan konkret dan opsi melanjutkan draf yang tersedia. Jangan mengulang tahap yang sudah valid tanpa alasan.

Untuk Browser Rendering, verifikasi dukungan PDF, batas sesi dan biaya terkini. Untuk generator lain, periksa font, halaman, margin, tabel dan tautan. Jangan memakai screenshot sebagai pengganti PDF teks bila pengguna meminta dokumen yang dapat dicari.

Sumber: https://developers.cloudflare.com/workers-ai/models/
Sumber: https://developers.cloudflare.com/workers-ai/configuration/bindings/
Sumber: https://developers.cloudflare.com/ai-gateway/
Sumber: https://developers.cloudflare.com/vectorize/get-started/embeddings/
Sumber: https://developers.cloudflare.com/browser-rendering/
