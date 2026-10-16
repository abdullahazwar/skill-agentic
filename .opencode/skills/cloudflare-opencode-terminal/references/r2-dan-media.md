# R2 dan media

## Penyimpanan

Simpan file biner di R2, bukan sebagai base64 pada KV atau satu baris D1. Simpan object key, pemilik, ukuran, MIME, checksum, status dan relasi menu pada D1.

Gunakan object key acak dengan prefix tenant, misalnya users/123/menu/uuid.webp. Jangan memakai nama upload sebagai path yang dipercaya.

## Upload melalui Worker

1. Verifikasi sesi dan kepemilikan menu.
2. Batasi ukuran dari header dan jumlah byte aktual stream. Header Content-Length saja tidak cukup.
3. Allowlist format dan validasi isi/signature. Jangan menerima SVG/HTML aktif tanpa sanitasi yang sesuai.
4. Simpan file ke R2 dengan httpMetadata yang benar.
5. Update relasi metadata D1.
6. Jika update D1 gagal, jadwalkan cleanup object baru.
7. Jika mengganti foto, hapus foto lama setelah relasi baru berhasil disimpan.

Contoh operasi binding, dengan validatedStream dan validatedMime hasil pemeriksaan:

    await env.FILES.put(objectKey, validatedStream, {
      httpMetadata: { contentType: validatedMime }
    });
    const object = await env.FILES.get(objectKey);

Jangan mem-buffer file besar tanpa batas. Gunakan mekanisme multipart untuk file besar bila diperlukan dan periksa batas terkini.

## Akses

| Kebutuhan | Cara |
| --- | --- |
| Foto katalog publik | Domain publik/cache dengan kebijakan yang jelas |
| Dokumen privat | Worker memverifikasi pemilik lalu stream body |
| Upload langsung client | URL presigned berumur pendek dan CORS terbatas |
| Lingkungan uji | Bucket terpisah |

Presigned URL R2 memakai endpoint S3 API yang didukung. Jangan menganggap URL itu berlaku pada custom domain publik. URL bertanda tangan dapat dipakai siapa pun yang memilikinya hingga habis.

Saat menyajikan object, teruskan metadata, ETag dan ukuran yang sesuai. Tangani object tidak ada dengan 404. Jangan menaruh respons privat pada cache bersama.

Untuk foto menu yang diperbarui, gunakan key/version baru agar cache lama tidak membuat gambar tampak tidak berubah. Lazy-load gambar katalog dan tentukan dimensi agar layout tidak meloncat.

## Operasi

    npx wrangler r2 bucket create aplikasi-files
    npx wrangler r2 object put aplikasi-files/contoh.txt --file ./contoh.txt --remote
    npx wrangler r2 object get aplikasi-files/contoh.txt --remote

Periksa help sebelum pemakaian dan target lokal/remote. Jangan mengunggah data nyata ke bucket contoh.

Konfigurasikan lifecycle hanya sesuai retensi. Backup metadata D1 tidak mencadangkan bytes R2. Periksa biaya storage, class operasi, lifecycle dan produk transformasi gambar secara terpisah. Jangan menjanjikan semua fitur media gratis.

Sumber: https://developers.cloudflare.com/r2/api/workers/workers-api-reference/
Sumber: https://developers.cloudflare.com/r2/api/s3/presigned-urls/
Sumber: https://developers.cloudflare.com/r2/buckets/cors/
Sumber: https://developers.cloudflare.com/r2/buckets/object-lifecycles/
