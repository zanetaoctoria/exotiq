Nama : Rebecca Zaneta Octoria Hutajulu

NPM : 2306275065

Kelas : PBP-E

<details> <summary>Tugas 2</summary>

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

## 2. Bagan Alur Request dan Response Django

![Bagan](bagantugas2.png)


## 3. Fungsi Git dalam Pengembangan Perangkat Lunak

Git merupakan sistem kontrol yang berfungsi untuk melacak perubahan dalam kode utama selama pengembangan perangkat lunak.


## 4. Kenapa Django Cocok untuk Pemula?

- **Struktur Terorganisir**: Django mempunyai struktur yang terorganisir dan jelas, sehingga pemula bisa mudah memahami alur pengembangan aplikasi

- **Framework Lengkap**: Django menyediakan framework yang lengkap, sehingga pemula tidak harus membangun semuanya dari awal.

## 5. Alasan Model di Django Disebut ORM

Pada Django, model disebut sebagai **ORM (Object-Relational Mapping)** karena menyediakan lapisan abstraksi yang menghubungkan objek Python dengan tabel di database relasional. Ini memungkinkan pengguna berinteraksi dengan database menggunakan kode Python tanpa perlu menulis SQL secara manual.

---

</details> <details> <summary>Tugas 3</summary>

# TUGAS 3

## 1. Pentingnya Data Delivery

Data delivery diperlukan untuk memastikan bahwa data dapat dikirimkan, diterima, dan diakses pengguna dan sistem lain. Hal ini membantu pengguna cepat membuat keputusan berdasarkan data dan menjadikan platform mudah dan cepat untuk digunakan. Data delivery juga membantu menjaga informasi tetap sinkron, menjaga data tetap sama, dan mendukung aktivitas utama seperti menganalisis, memeriksa, dan membiarkan orang atau sistem berbicara satu sama lain.


## 2. JSON vs XML

- **JSON** lebih sederhana, ringan, dan mudah ditangani dibanding XML, dengan sintaks lebih ringkas, ukuran lebih kecil, dan lebih cepat dipahami web. JSON populer karena kompatibel dengan JavaScript, mendukung tipe data modern, dan mudah digunakan di layanan web seperti REST
- **XML** digunakan untuk kasus khusus yang butuh pemeriksaan detail.


## 3. Fungsi Method `is_valid()` pada Form Django

Method `is_valid()` digunakan untuk memeriksa apakah data yang dimasukkan ke dalam form valid. Method ini mengembalikan `True` jika data valid dan `False` jika tidak. Method ini sangat penting untuk mengecek apakah data yang dimasukkan akurat dan aman sebelum digunakan/disimpan

## 4. Pentingnya `csrf_token` di Form Django

`csrf_token` digunakan untuk mencegah serangan **Cross-Site Request Forgery (CSRF)**, di mana penyerang dapat memaksa pengguna untuk melakukan tindakan tanpa izin. Token ini memverifikasi bahwa permintaan form berasal dari sumber yang valid, menjaga keamanan aplikasi.

## 5. Implementasi Checklist Step-by-Step

- Saya memulai dengan membuat folder `templates` dan mengisinya dengan base template.
- Mengonfigurasi `templates` di `settings.py`.
- Menambahkan UUID di `models.py` untuk ID yang lebih aman.
- Melakukan migrasi dengan `makemigrations` dan `migrate`.
- Membuat file `forms.py` dan mendefinisikan `ItemsEntryForm`.
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
</details> <details> <summary>Tugas 4</summary>

# TUGAS 4  

## 1. Perbedaan antara HttpResponseRedirect() dan redirect()
- HttpResponseRedirect(): Merupakan respon HTTP standar yang mengarahkan pengguna ke URL tertentu
- redirect(): Fungsi shortcut Django yang lebih fleksibel, bisa mengarahkan ke URL, nama view, atau bahkan objek, dan Django akan otomatis memprosesnya ke URL yang sesuai.

## 2. Jelaskan cara kerja penghubungan model Product dengan User!
Untuk menghubungkan model Product dengan User di Django, kita bisa menggunakan ForeignKey. Di models.py, tambahkan field `user = models.ForeignKey(User, on_delete=models.CASCADE)` pada class Product, yang menunjukkan bahwa setiap produk terkait dengan satu instance User. Dengan begitu, saat produk dibuat, kita bisa mengidentifikasi pengguna yang membuatnya dan mengelola produk tersebut melalui hubungan ini. Relasi ini mempermudah akses ke data yang terkait, seperti menampilkan produk yang dimiliki oleh seorang pengguna tertentu atau menentukan pengguna mana yang memiliki akses ke suatu produk.

## 3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
- Authentication : proses memverifikasi identitas user, biasanya dengan memeriksa kecocokan antara username dan password. 
- Authorization : proses menentukan hak akses user setelah berhasil diautentikasi, yaitu apa saja yang boleh dan tidak boleh dilakukan dalam aplikasi. 
Ketika pengguna login, sistem akan memvalidasi kredensial mereka melalui proses authentication. Django menyediakan kedua konsep ini melalui sistem autentikasi bawaan yang mendukung mekanisme login, logout, dan manajemen sesi untuk authentication. Untuk authorization, Django menggunakan sistem izin (permissions), grup pengguna, serta decorator seperti @login_required untuk mengatur akses ke berbagai bagian aplikasi berdasarkan hak yang diberikan kepada pengguna.

## 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat pengguna yang sudah login melalui sistem sesi yang menggunakan cookies. Setelah login, Django membuat sesi unik dan menyimpan ID sesi dalam cookie di browser. Setiap kali pengguna mengakses server, cookie ini dikirim kembali untuk mengidentifikasi pengguna yang sudah login. Selain autentikasi, cookies juga digunakan untuk menyimpan preferensi, melacak aktivitas, dan mengelola konten. Namun, cookies bisa rentan terhadap serangan seperti XSS, sehingga penting untuk menggunakannya dengan aman menggunakan atribut seperti HttpOnly dan Secure serta menghindari menyimpan informasi sensitif.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step 
- Saya membuat halaman **register.html** dan **login.html** di `templates` (main) untuk menampilkan form registrasi dan login.
- Implementasikan form registrasi dengan mengimpor **UserCreationForm** dan **messages** di `views.py` untuk menampilkan pesan keberhasilan saat user dibuat.
- Buat fungsi **register** di `views.py` untuk merender halaman registrasi (`register.html`).
- Buat fungsi login dengan mengimpor **authenticate** dan **login**, serta buat fungsi **login_user** untuk merender halaman login (`login.html`).
- Tambahkan fungsi **logout_user** di `views.py`, menggunakan **logout**, untuk mengarahkan user kembali ke halaman login setelah logout, menambahkan tombol **logout** di `main.html` yang memanggil fungsi **logout_user** untuk logout user.
- Menggunakan **@login_required** pada fungsi **show_main** agar user harus login sebelum mengakses halaman utama.
- Konfigurasi semua fungsi di **urls.py** dengan menambahkannya ke dalam **urlpatterns** untuk mengaktifkan fungsi-fungsi tersebut.
- Mengatur **cookie** saat fungsi **login_user** dijalankan dan hapus cookie saat user logout untuk melacak kapan user terakhir login.
- Tampilkan informasi login terakhir di halaman **show_main** dan render di **main.html**.
- Menghubungkan model **Product** dengan **User** di `models.py` menggunakan **ForeignKey**, dengan mengimpor model **User**.
- Modifikasi fungsi **create_item_entry** di `views.py` untuk mengaitkan item dengan user yang login sebelum menyimpannya ke database.
- Memfilter produk yang ditampilkan di **show_main** berdasarkan user yang sedang login.
- Mengimpor **os**, dan sesuaikan variabel **DEBUG** di `settings.py` 

</details> <details> <summary>Tugas 5</summary>

# TUGAS 5

Berikut adalah format README yang telah dirapikan untuk tugas Anda:

---

# TUGAS 5

## 1. Urutan Prioritas Pengambilan CSS Selector

Urutan prioritas pengambilan CSS selector ditentukan oleh **specificity (spesifisitas)** sebagai berikut:

1. **Inline styles** (di atribut `style` HTML) memiliki prioritas tertinggi.
2. **ID selector** (`#id`) memiliki prioritas lebih tinggi dibanding lainnya.
3. **Class, attribute, dan pseudo-class selectors** (`.class`, `[attr]`, `:hover`, dll.) berada di bawah ID selector.
4. **Element dan pseudo-element selectors** (`div`, `h1`, `::before`, dll.) memiliki prioritas paling rendah.
5. Jika spesifisitas sama, urutan deklarasi (posisi di CSS) menentukan prioritas, di mana yang terakhir ditulis akan diprioritaskan.

## 2. Pentingnya Responsive Design dalam Pengembangan Aplikasi Web

**Responsive design** penting karena memastikan tampilan dan fungsi aplikasi web dapat diakses dengan baik di semua perangkat (desktop, tablet, ponsel). Hal ini memungkinkan pengguna menikmati konten secara optimal tanpa harus memperbesar (zoom-in) atau mengecilkan (zoom-out) tampilan secara berlebihan.

**Contoh aplikasi yang sudah menerapkan responsive design**:
- Spotify
- WhatsApp
- Line

**Contoh aplikasi yang belum menerapkan responsive design**:
- SIAK-NG

## 3. Perbedaan Antara Margin, Border, dan Padding

- **Margin**: Ruang kosong di luar elemen, mengatur jarak antara elemen satu dengan yang lain. 
 
- **Border**: Garis yang mengelilingi elemen, berada di antara margin dan padding.

- **Padding**: Ruang di dalam elemen, mengatur jarak antara konten elemen dan tepi elemen (border).


## 4. Konsep Flexbox dan Grid Layout

- **Flexbox (Flexible Box Layout)**:
  Flexbox dirancang untuk tata letak satu dimensi, baik secara horizontal maupun vertikal. Elemen di dalam **flex container** dapat diatur agar beradaptasi secara otomatis dengan ukuran kontainer, membuatnya ideal untuk tata letak dinamis seperti navbar atau card yang dapat diselaraskan, dipusatkan, atau dibagi ruangnya dengan mudah.

- **Grid Layout**:
  Grid Layout digunakan untuk tata letak dua dimensi, di mana elemen dapat diatur dalam baris dan kolom. Grid memungkinkan kontrol yang lebih presisi atas posisi elemen di dalam grid, membuatnya cocok untuk desain yang lebih kompleks, seperti dashboard atau layout halaman utama.

Kegunaan utama **Flexbox**  untuk tata letak yang fleksibel dan satu dimensi, sedangkan **Grid Layout** lebih cocok untuk tata letak dua dimensi yang lebih kompleks dan terstruktur.

## 5. Implementasi Checklist secara Step-by-Step

1. Menambahkan fungsi baru di **views.py** yaitu **edit_item** dan **delete_item**, yang masing-masing berfungsi untuk mengedit dan menghapus data produk yang sudah ada.
   
2. Mengintegrasikan path di **urls.py** pada app **main** untuk menghubungkan fungsi edit dan delete tersebut.

3. Membuat folder **static** untuk menyimpan file CSS dan gambar-gambar yang akan digunakan dalam aplikasi.

4. Melakukan perubahan pada **settings.py** agar dapat menggunakan **static files** yang sudah dibuat.

5. Mengubah **base.html** untuk menggunakan **Tailwind CSS**.

6. Membuat **navbar.html** yang digunakan di **main.html**, serta **navbar2.html** yang digunakan di **edit_item.html** dan **create_item_entry.html**. Selanjutnya, saya menyesuaikan tampilan HTML agar sesuai dengan kebutuhan.

7. Melakukan benchmarking terhadap website **Dolce & Gabbana** untuk mengedit bagian **main.html**.

8. Membuat **product_list.html** untuk menampilkan daftar produk yang sudah ditambahkan oleh pengguna, serta menambahkan tombol **edit** dan **delete** pada setiap produk.

9. Mengedit **login.html** dan **register.html** agar sesuai dengan preferensi tampilan yang diinginkan.

10. Mendesain keseluruhan aplikasi menggunakan **Tailwind CSS** dan mengedit **global.css** untuk mendefinisikan desain yang konsisten di seluruh aplikasi.
