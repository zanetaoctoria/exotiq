Nama : Rebecca Zaneta Octoria Hutajulu
NPM : 2306275065
Kelas : PBP-E

TUGAS 2 

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step

- Buat direktori proyek bernama exotique dan install dependencies termasuk Django.

- Jalankan perintah django-admin startproject [nama_project] untuk membuat proyek baru.

- Jalankan python manage.py startapp main untuk membuat aplikasi bernama main

- Di dalam direktori main, buat file urls.py dan tambahkan URL yang diinginkan.

- Tambahkan model sesuai kebutuhan di models.py dan gunakan tipe data yang sesuai (seperti CharField atau IntegerField).

- Lakukan migrasi model dengan menjalankan python manage.py makemigrations dan python manage.py migrate.

- Buat fungsi di views.py yang mengembalikan template HTML yang menampilkan nama aplikasi serta nama dan kelas.

- Buat routing di urls.py aplikasi main untuk menghubungkan URL dengan fungsi di views.py.

- Deployment ke PWS 

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

<img src="bagantugas2.png">

3. Jelaskan fungsi git dalam pengembangan perangkat lunak!

- Git merupakan sistem kontrol yang berfungsi untuk melacak perubahan dalam kode utama selama pengembangan perangkat lunak.

4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

- Django mempunyai struktur yang terorganisir dan jelas, sehingga pemula bisa mudah memahami alur pengembangan aplikasi
- Django menyediakan framework yang lengkap, sehingga pemula tidak harus membangun semuanya dari awal.

5. Mengapa model pada Django disebut sebagai ORM?

- Pada Django, model disebut sebagai ORM karena menyediakan lapisan abstraksi yang menghubungkan objek Python dengan tabel di database relasional. Ini memungkinkan pengguna berinteraksi dengan database menggunakan kode Python tanpa perlu menulis SQL secara manual.


TUGAS 3

1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
- Data delivery diperlukan untuk memastikan bahwa data dapat dikirimkan, diterima, dan diakses pengguna dan sistem lain. Hal ini membantu pengguna cepat membuat keputusan berdasarkan data dan menjadikan platform mudah dan cepat untuk digunakan. Data delivery juga membantu menjaga informasi tetap sinkron, menjaga data tetap sama, dan mendukung aktivitas utama seperti menganalisis, memeriksa, dan membiarkan orang atau sistem berbicara satu sama lain.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
- JSON lebih sederhana, ringan, dan mudah ditangani dibanding XML, dengan sintaks lebih ringkas, ukuran lebih kecil, dan lebih cepat dipahami web. JSON populer karena kompatibel dengan JavaScript, mendukung tipe data modern, dan mudah digunakan di layanan web seperti REST sementara XML digunakan untuk kasus khusus yang butuh pemeriksaan detail.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
- Method `is_valid()` dalam formulir Django memeriksa apakah data yang dikirim valid. Jika informasi mengikuti instruksi yang diberikan, method ini memberikan `True`, dan jika ada kesalahan, memberikan `False`. Method ini sangat penting untuk mengecek apakah data yang dimasukkan akurat dan aman sebelum digunakan/disimpan.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

- Kita membutuhkan `csrf_token` di form Django untuk menghindari serangan **Cross-Site Request Forgery (CSRF)**, di mana penyerang bisa memaksa pengguna yang sudah login untuk melakukan tindakan tanpa izin `csrf_token` mencegah hal ini dengan memverifikasi apakah setiap permintaan form berasal dari sumber yang valid.


5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- Saya memulai dengan membuat folder templates, mengisi dengan base template untuk kerangka umum, dan mengonfigurasi templates di settings.py. Kemudian, saya menambahkan ID di models.py dengan mengimpor uuid untuk meningkatkan keamanan, lalu melakukan migrations.

- Saya membuat file forms.py dan mendefinisikan joshShopEntryForm sesuai dengan model dan fields di models.py. Di views.py, saya menambahkan fungsi create_item_entry untuk otomatis menambahkan data item ketika form disubmit, dan mengubah show_main agar menampilkan semua objek dari database di halaman utama.

- Setelah itu, saya membuat create_item_entry.html di folder templates yang memperluas base.html, dan mengubah main.html untuk menampilkan item baru yang diinput user. Path URL untuk create_item_entry ditambahkan di urls.py agar fungsinya bisa diakses.

- Saya juga menambahkan fungsi show_xml dan show_json di views.py untuk menampilkan data dalam format XML atau JSON, serta menambahkan show_xml_by_id dan show_json_by_id untuk filter data berdasarkan ID. Terakhir, saya memperbarui urls.py dengan path untuk fungsi-fungsi tersebut.






























