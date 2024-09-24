Here’s your cleaned-up README:

---

# TUGAS 2

## 1. Implementasi Checklist Step-by-Step:

- **Buat Direktori Proyek**  
  Buat direktori proyek bernama `exotique` dan install dependencies termasuk Django.

- **Buat Proyek Django**  
  Jalankan perintah `django-admin startproject [nama_project]` untuk membuat proyek baru.

- **Buat Aplikasi**  
  Jalankan `python manage.py startapp main` untuk membuat aplikasi bernama `main`.

- **Konfigurasi Routing**  
  Di dalam direktori `main`, buat file `urls.py` dan tambahkan URL yang diinginkan.

- **Tambahkan Model**  
  Tambahkan model sesuai kebutuhan di `models.py` dan gunakan tipe data yang sesuai (seperti `CharField` atau `IntegerField`).

- **Migrasi Model**  
  Jalankan perintah `python manage.py makemigrations` dan `python manage.py migrate` untuk membuat dan menerapkan migrasi model.

- **Fungsi di `views.py`**  
  Buat fungsi di `views.py` yang mengembalikan template HTML yang menampilkan nama aplikasi serta nama dan kelas.

- **Hubungkan URL ke Views**  
  Buat routing di `urls.py` aplikasi `main` untuk menghubungkan URL dengan fungsi di `views.py`.

- **Deployment ke PWS**  
  Lakukan deployment ke PWS untuk membuat aplikasi dapat diakses secara online.

## 2. Bagan Alur Request dan Response Django

![Bagan](bagantugas2.png)

Pada bagan ini:
- **urls.py**: Menghubungkan URL yang diminta klien ke views yang sesuai.
- **views.py**: Menangani logika bisnis dan mengambil data dari model atau mengembalikan template.
- **models.py**: Berfungsi sebagai lapisan ORM yang menghubungkan objek Python ke database.
- **HTML Template**: Berkas yang menampilkan data dan hasil yang dikirimkan views.

## 3. Fungsi Git dalam Pengembangan Perangkat Lunak

Git adalah sistem kontrol versi yang melacak perubahan pada kode selama pengembangan perangkat lunak. Ini memungkinkan kolaborasi antar pengembang, memudahkan rollback ke versi sebelumnya, dan membantu menjaga integritas proyek.

## 4. Kenapa Django Cocok untuk Pemula?

- **Struktur Terorganisir**: Django memiliki struktur yang jelas sehingga memudahkan pemula memahami alur pengembangan aplikasi.
- **Framework Lengkap**: Django menyediakan banyak fitur bawaan sehingga pemula tidak perlu membangun semuanya dari nol.

## 5. Alasan Model di Django Disebut ORM

Model di Django disebut **ORM (Object-Relational Mapping)** karena memberikan lapisan abstraksi antara objek Python dan database relasional, memungkinkan interaksi dengan database tanpa menulis SQL secara langsung.

---

# TUGAS 3

## 1. Pentingnya Data Delivery

Data delivery sangat penting untuk memastikan data dapat dikirimkan, diterima, dan diakses dengan mudah oleh pengguna dan sistem lain. Ini memungkinkan pengguna membuat keputusan berdasarkan data dengan cepat, menjaga sinkronisasi informasi, serta mendukung aktivitas seperti analisis dan komunikasi antar sistem.

## 2. JSON vs XML

- **JSON** lebih sederhana, ringan, dan mudah dihandle dibandingkan XML. Sintaksnya ringkas, ukurannya lebih kecil, dan mudah dipahami oleh browser modern.
- **JSON** lebih populer karena kompatibilitasnya dengan JavaScript, dukungannya terhadap tipe data modern, dan kemudahan penggunaannya di layanan web seperti REST.
- **XML** digunakan pada kasus khusus yang membutuhkan pemeriksaan detail atau penanganan data lebih kompleks.

## 3. Fungsi Method `is_valid()` pada Form Django

Method `is_valid()` digunakan untuk memeriksa apakah data yang dimasukkan ke dalam form valid. Method ini mengembalikan `True` jika data valid dan `False` jika tidak. Ini penting untuk memastikan data yang dikirimkan aman sebelum diproses lebih lanjut.

## 4. Pentingnya `csrf_token` di Form Django

`csrf_token` digunakan untuk mencegah serangan **Cross-Site Request Forgery (CSRF)**, di mana penyerang dapat memaksa pengguna untuk melakukan tindakan tanpa izin. Token ini memverifikasi bahwa permintaan form berasal dari sumber yang valid, menjaga keamanan aplikasi.

## 5. Implementasi Checklist Step-by-Step

- Membuat folder `templates` dan mengisinya dengan base template.
- Mengonfigurasi `templates` di `settings.py`.
- Menambahkan UUID di `models.py` untuk ID yang lebih aman.
- Melakukan migrasi dengan `makemigrations` dan `migrate`.
- Membuat file `forms.py` dan mendefinisikan `JoshShopEntryForm`.
- Menambahkan fungsi `create_item_entry` di `views.py` untuk menambahkan item secara otomatis ketika form disubmit.
- Mengubah fungsi `show_main` untuk menampilkan semua objek dari database di halaman utama.
- Membuat template `create_item_entry.html` dan menghubungkan URL di `urls.py`.
- Menambahkan fungsi `show_xml`, `show_json`, `show_xml_by_id`, dan `show_json_by_id` di `views.py`.
- Memperbarui `urls.py` dengan path untuk fungsi tersebut.

## 6. Screenshots
- XML Data  
  ![XML](xml.jpg)
- JSON Data  
  ![JSON](json.jpg)
- XML by ID  
  ![XML by ID](xmlid.jpg)
- JSON by ID  
  ![JSON by ID](jsonid.jpg)

---

Let me know if you'd like to add or change anything!