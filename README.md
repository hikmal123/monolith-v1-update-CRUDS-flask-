# c003-monolith
Course 003 Monolith

Aplikasi ini adalah sebuah web monolitik berbasis Flask (Python) yang mengimplementasikan operasi CRUD (Create, Read, Update, Delete) untuk manajemen data mobil menggunakan database SQLite dan Peewee ORM.

## Struktur dan Deskripsi File/Direktori

- **`cars.py`**: File utama aplikasi Flask. Berisi definisi model database (`TBCars`), konfigurasi Peewee ORM, dan seluruh *routing/endpoint* untuk operasi CRUD (tambah, tampilkan, ubah, hapus, dan cari mobil).
- **`carsweb.db`**: File database SQLite yang menyimpan data mobil.
- **`static/`**: Direktori yang berisi file-file statis seperti CSS (`style.css`), JavaScript, dan *fonts* untuk keperluan tata letak dan desain (*styling*) halaman web.
- **`templates/`**: Direktori yang memuat file-file HTML (Jinja2 *templates*) sebagai antarmuka pengguna:
  - `index.html`: Halaman utama aplikasi (beranda).
  - `createcar.html`: Halaman formulir untuk menambahkan data mobil baru.
  - `readcar.html`: Halaman tabel untuk menampilkan daftar seluruh data mobil.
  - `updatecar.html`: Halaman formulir untuk mengubah data mobil yang sudah ada.
  - `deletecar.html`: Halaman untuk menghapus data mobil.
  - `searchcar.html`: Halaman untuk melakukan pencarian spesifik data mobil berdasarkan nama.
  - `header.html` & `footer.html`: Komponen *header* dan *footer* (bagian atas dan bawah halaman) yang digunakan ulang di berbagai halaman.
- **`venv/`**: Direktori *virtual environment* Python yang berisi dependensi/library (*packages*) yang dibutuhkan oleh aplikasi (seperti Flask dan Peewee).
- **`.gitignore`**: File konfigurasi Git untuk mengabaikan file/direktori tertentu (seperti `venv` dan `__pycache__`) agar tidak masuk ke *repository*.
- **`LICENSE`**: File yang memuat informasi lisensi proyek.
- **`README.md`**: File dokumentasi proyek (file ini) yang berisi penjelasan singkat dan struktur direktori.
