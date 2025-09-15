# TUGAS 1

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

# TUGAS 2

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