# Blog Rangkuman Perkuliahan

Proyek Django minimalis untuk menampilkan blog berisi rangkuman materi perkuliahan, dengan tema visual arsitektur perangkat lunak.

## Menjalankan

```powershell
pip install -r requirements.txt
python manage.py runserver
```

Halaman awal tersedia di `http://127.0.0.1:8000/`.

## Mengisi Materi

Konten artikel berada di `blog/content.py`. Tambahkan atau ubah item di `POSTS` untuk memperbarui materi blog.

## Deploy ke Railway

Project ini sudah disiapkan untuk Railway dengan `railway.json`, `Procfile`, Gunicorn, dan WhiteNoise.

Variabel environment yang disarankan di Railway:

```text
SECRET_KEY=isi-dengan-secret-yang-kuat
DEBUG=False
```

Railway akan menjalankan `python manage.py collectstatic --noinput` saat build dan menjalankan aplikasi dengan Gunicorn.
