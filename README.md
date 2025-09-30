https://muhammad-razka41-mainbalbalan.pbp.cs.ui.ac.id/

# TUGAS 2

### **1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

#### **Membuat Proyek Django**
1.  Setup repositori proyek (lokal & GitHub)
2.  Buat dan aktifkan virtual environment
3.  Instalasi dependencies
4.  Membuat proyek Django baru (`django-admin startproject`)
5.  Konfigurasi Environment Variables dan Proyek
6.  Migrasi database dan jalankan server
7.  Aplikasi Django berhasil dibuat

#### **Membuat Aplikasi main**
8.  Membuat aplikasi `main` (`python manage.py startapp main`)
9.  Daftarkan aplikasi `main` ke `INSTALLED_APPS` di `settings.py` supaya dikenali oleh Django
10. Menambahkan direktori `template` yang berisi file `.html` sebagai tampilan untuk pengguna

#### **Membuat model product**
11. Membuat class `Product` pada `models.py` dengan field yang diperintahkan
12. Membuat file migrasi (`makemigrations`)
13. Mengaplikasikan file migrasi agar struktur database sesuai dengan model Product (`migrate`)

#### **Konfigurasi View & Template**
15. Membuat fungsi `show_main` di `views.py`. Berfungsi untuk mengambil data dan menampilkannya ke template
16. Menambahkan dictionary pada fungsi `show_main` berisi data diri
17. Modifikasi file html pada direktori template untuk menampilkan data dari dictionary menggunakan sintaks Django `{{ variable }}`

#### **Routing URL**
18. Membuat file `urls.py` di aplikasi `main`
19. Isi dengan `path('', show_main, name='show_main')` agar diarahkan ke fungsi show_main
20. Daftarkan `urls.py` punya aplikasi `main` ke dalam `urls.py` punya proyek utama `path('', include('main.urls'))` supaya URL dari aplikasi main dapat dikenali dan diakses

#### **Deploy**
21. Push ke GitHub dan deploy ke PWS

---

### **2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django.**

![Bagan Req Django](https://github.com/user-attachments/assets/4dd2bb07-ebe8-4460-8dfd-ad8ee19f1c6b)

---

### **3. Jelaskan peran settings.py dalam proyek Django!**

`settings.py` digunakan untuk mengonfigurasi seluruh proyek Django, semua pengaturan soal bagaimana proyek berjalan ada di sini, mulai dari database, `ALLOWED_HOSTS`, `INSTALLED_APPS`, dll.

---

### **4. Bagaimana cara kerja migrasi database di Django?**

Migrasi model pada Django digunakan untuk menyesuaikan struktur basis data dengan perubahan yang dibuat pada model di kode. Cara kerjanya dimulai dengan membuat file migrasi (`makemigrations`) yang berisi perubahan model yang belum diaplikasikan ke database. Selanjutnya, Django akan mengaplikasikan perubahan dari file migrasi (`migrate`) sehingga struktur database sesuai dengan model terbaru.

---

### **5. Mengapa framework Django dijadikan permulaan pembelajaran?**

Django dipilih karena:
- Open source
- Cepat dalam pengembangan
- Sudah menyediakan banyak fitur bawaan
- Aman
- Fleksibel digunakan untuk berbagai jenis aplikasi

---

### **6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?**

Tutorial 1 sangat jelas dan mudah dipahami, asisten dosen sangat membantu.

---
---

# TUGAS 3

### **1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**

Data delivery diperlukan dalam pengimplementasian platform agar server, aplikasi, dan user dapat bertukar data secara terstruktur dan aman, sehingga komunikasi antar komponen berjalan lancar.

---

### **2. Mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**

Menurut saya, salah satu alasan mengapa JSON lebih baik dibandingkan XML adalah karena penulisannya lebih sederhana, ringkas, dan mudah dibaca. Hal ini membuat JSON menghasilkan ukuran data yang lebih kecil sehingga lebih efisien untuk penyimpanan. Selain itu, JSON juga terintegrasi langsung dengan JavaScript sehingga sangat cocok digunakan pada aplikasi web modern.

---

### **3. Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?.**

Method `is_valid()` pada form Django berfungsi untuk memeriksa apakah data yang dimasukkan user sudah sesuai dengan aturan validasi yang telah didefinisikan. Jika semua data valid, method ini akan mengembalikan True, jika ada kesalahan, method ini akan mengembalikan False. Method ini dibutuhkan karena data harus dipastikan benar dan sesuai sebelum diproses lebih lanjut atau disimpan ke database.

---

### **4. Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**

`csrf_token` dibutuhkan untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF). Token ini dibuat otomatis oleh Django dan diverifikasi saat form di-submit, sehingga hanya permintaan yang sah dari aplikasi kita yang akan diterima.

Jika tidak ada token, penyerang bisa memaksa browser pengguna yang sedang login untuk mengirim request palsu ke aplikasi kita. Ini bisa dimanfaatkan untuk tindakan berbahaya seperti mengubah data atau melakukan transaksi atas nama korban tanpa sepengetahuan mereka.

---

### **5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

1.  Membuat `base.html` sebagai template dasar dan mengonfigurasi `settings.py`.
2.  Membuat `forms.py` yang berisi `ProductForm` untuk input data produk.
3.  Menambahkan fungsi `add_product` dan `show_product` di `views.py`.
4.  Mengubah `main.html` agar menampilkan daftar produk dengan tombol "Add" dan "Detail".
5.  Membuat file `add_product.html` untuk halaman tambah produk dan `product_details.html` untuk halaman detail produk.
6.  Menambahkan fungsi `show_xml`, `show_json`, `show_xml_by_id`, dan `show_json_by_id` di `views.py`.
7.  Mengatur routing di `urls.py` untuk semua fungsi view yang telah dibuat.
8.  Push ke GitHub dan deploy ke PWS.

---

### **6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?**

Tutorial 2 sangat jelas dan mudah dipahami, asisten dosen sangat membantu.

---

### **7. Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.**

<img width="1790" height="960" alt="Screenshot 2025-09-14 140052" src="https://github.com/user-attachments/assets/a49bacf7-f77d-4b48-91de-dff554a2f389" />
<img width="1791" height="962" alt="Screenshot 2025-09-14 140115" src="https://github.com/user-attachments/assets/6df751a9-8def-421e-9f85-c9058907533c" />
<img width="1790" height="965" alt="Screenshot 2025-09-14 140234" src="https://github.com/user-attachments/assets/c1d0500d-d4cf-4861-9e35-6091be5eeb00" />
<img width="1790" height="959" alt="Screenshot 2025-09-14 140304" src="https://github.com/user-attachments/assets/abcbbe42-4f5b-4d20-8f67-d97c7f5c5fdd" />

---
---

# TUGAS 4

### **1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.**

Django AuthenticationForm adalah sebuah form bawaan dari Django yang digunakan untuk menangani proses login pengguna. Form ini secara otomatis akan memvalidasi username dan password yang dimasukkan oleh pengguna.

---

### **2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?**

Autentikasi adalah proses verifikasi identitas pengguna yang semisalnya ingin mengakses suatu aplikasi menggunakan username dan password yang sudah terdaftar. Django memiliki sistem autentikasi bawaan, yaitu django.contrib.auth yang menyediakan model User untuk mengelola data pengguna, serta form bawaan seperti UserCreationForm dan AuthenticationForm.

Otorisasi adalah proses menentukan izin atau akses yang dimiliki pengguna setelah berhasil diautentikasi. Django memiliki mekanisme otorisasi dengan sistem permission dan groups untuuk mengatur akses apa saja yang dimiliki pengguna terhadap data atau fitur tertentu. Selain itu, Django juga menyediakan dekorator seperti @login_required untuk membatasi akses ke halaman tertentu hanya untuk pengguna yang sudah login.

---

### **3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?**

Cookies menyimpan sedikit data langsung di browser pengguna. Kelebihannya, tidak membebani server. Namun, kekurangannya adalah kurang aman karena data disimpan langsung di perangkat pengguna serta memiliki kapasitas yang terbatas.

Sementara itu, session menyimpan data di sisi server. Agar server bisa tahu data milik user yang mana, browser hanya menyimpan sebuah kode unik (biasanya dinamakan sessionid) di dalam cookie. Keunggulannya, lebih aman untuk menyimpan data sensitif dan dapat menampung informasi dalam jumlah lebih besar. Kekurangannya, setiap sesi aktif akan memakan memori pada server.

---

### **4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?**

Secara umum, penggunaan cookies tidak bisa langsung dianggap aman. Keamanannya bergantung pada bagaimana pengembang mengatur dan menggunakannya. Karena cookies disimpan dalam bentuk teks biasa di browser pengguna, informasi di dalamnya rentan terhadap berbagai risiko jika tidak dilindungi dengan benar. Untuk menangani berbagai risiko tersebut, Django menyediakan mekanisme keamanan bawaan untuk cookies, antara lain:
- SESSION_COOKIE_HTTPONLY = mencegah JavaScript mengakses cookie (melindungi dari XSS).
- SESSION_COOKIE_SECURE = cookie hanya dikirim lewat HTTPS, bukan HTTP biasa.
- SESSION_EXPIRE_AT_BROWSER_CLOSE = session akan habis begitu browser ditutup.
- CSRF protection = Django otomatis menambahkan token CSRF untuk mencegah serangan Cross-Site Request Forgery.

---

### **5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)**

1. Membuat form register
2. Membuat fungsi login
3. Membuat fungsi logout
4. Menambahkan ketiga fungsi diatas ke dalam `views.py`, menghubungkan urlnya, dan membuat template html nya
5. Menambahkan field `User` pada model `Product` untuk menghubungkan satu produk dengan satu user
6. Menyesuaikan fungsi `add_product` agar setiap produk baru yang dibuat otomatis terhubung dengan pengguna yang sedang login.
7. Modifikasi fungsi show main supaya informasi "name" yg ditampilkan adalah nama pengguna yg sedang log in `(request.user.username)`
8. Mengambil informasi last_login dari cookies `(response.set_cookie('last_login', str(datetime.datetime.now())))` dan menampilkan sesi terakhir login pada halaman utama
9.  Push ke GitHub dan deploy ke PWS.

---
---

# TUGAS 5

### **1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!**

1. Inline Styles: Atribut style yang ditulis langsung pada elemen HTML. Ini adalah prioritas tertinggi.

    - Contoh: `<p style="color: red;">Merah.</p>`

2. ID Selectors: Selector yang menggunakan ID unik suatu elemen (#id).

    - Contoh: `#header { background-color: blue; }`

3. Class Selectors, Attribute Selectors, dan Pseudo-classes: Selector yang menggunakan `.class`, atribut seperti `[type="text"]`, dan pseudo-class seperti `:hover`.

    - Contoh: `.menu-item { color: green; }`

4. Type Selectors dan Pseudo-elements: Selector yang menargetkan nama tag HTML (p, div, h1) dan pseudo-elemen seperti `::before` atau `::after`.

    - Contoh: `p { font-size: 16px; }`

5. Universal Selector (*): Selector ini memiliki spesifisitas paling rendah.

----

### **2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!**

Responsive design adalah pendekatan dalam desain web yang membuat tampilan situs web dapat beradaptasi dengan berbagai ukuran layar perangkat, mulai dari desktop, tablet, hingga ponsel. Ini penting karena:

- Ada banyak jenis perangkat, satu UI saja belum tentu cocok di semua perangkat.
- Memberikan pengalaman yang nyaman bagi pengguna di semua perangkat.
- Google memprioritaskan situs yang mobile-friendly dalam hasil pencariannya. (SEO)
- Mengelola satu situs web yang responsif lebih mudah daripada harus mengelola versi terpisah pisah.

Sebagian besar situs generasi sekarang sudah menerapkan responsive design, seperti tokopedia, traveloka dll. Mungkin yang belum menerapkan responsive design itu situs situs generasi lama yang biasanya hanya dibangun khusus untuk desktop.

----

### **3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!**

- Margin: Ruang di luar border, berfungsi untuk memberikan jarak antara satu elemen dengan elemen lain di sekitarnya.

- Border: Garis di sekitar padding dan konten, bisa diatur ketebalan, gaya (misalnya, solid, dashed), dan warnanya.

- Padding: Ruang di dalam border, antara border dan konten, berfungsi untuk memberikan ruang untuk konten di dalam elemen.

Contoh:
`.box {
  margin: 20px;

  border: 2px solid black;

  padding: 15px;

  margin-top: 10px;
  border-left: 5px dotted green;
  padding-bottom: 25px;
}`

---

### **4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!**

- Flexbox: Model layout satu dimensi, hanya mengatur elemen dalam satu baris atau satu kolom saja. Cocok digunakan untuk mengatur tata letak komponen komponen kecil dalam sebuah aplikasi, seperti menyelaraskan item item pada navbar atau card.

- Grid Layout: Model layout dua dimensi, memungkinkan pengaturan elemen dalam baris dan kolom secara bersamaan. Cocok digunakan untuk mengatur tata letak keseluruhan web, seperti tata letak header, sidebar, dll.

### **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!**

1. Mengintegrasikan Tailwind CSS ke dalam `base.html` dan menambahkan direktori `static/css/global.css` untuk styling custom.
2. Konfigurasi static di `settings.py` (STATIC_URL, STATIC_ROOT) dan tambahkan middleware `WhiteNoise`.
3. Membuat fungsi `edit_product` dan `delete_product` di `views.py` kemudian mengatur URL path nya
4. Membuat template html untuk `edit_product`
5. Membuat template `card_product.html` untuk menampilkan setiap produk di halaman utama dan menambahkan tombol untuk edit dan delete product di dalam card nya.
6. Membuat navigation bar yang responsif
7. Mengatur styling di `global.css` dan menerapkan styling ke semua halaman utama (main.html, login.html, register.html, dll).
8. Push ke GitHub dan deploy ke PWS.