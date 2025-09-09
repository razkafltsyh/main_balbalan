https://muhammad-razka41-mainbalbalan.pbp.cs.ui.ac.id/

- Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
  # Membuat Proyek Django
    1. Setup repositori proyek (lokal & GitHub)
    2. Buat dan aktifkan virtual environment
    3. instalasi dependencies
    4. Membuat proyek Django baru (django-admin startproject)
    5. Konfigurasi Environment Variables dan Proyek
    6. migrasi database dan jalankan server
    7. Aplikasi Django berhasil dibuat

  # Membuat Aplikasi main
    8. Membuat aplikasi main (python manage.py startapp main)
    9. Daftarkan aplikasi main ke INSTALLED_APPS di settings.py supaya dikenali oleh Django
    10. Menambahkan direktori template yang berisi file .html sebagai tampilan untuk pengguna

  # Membuat model product
    11. Membuat class Product pada models.py dengan field yang diperintahkan
    12. Membuat file migrasi (makemigrations)
    13. Mengaplikasikan file migrasi agar struktur database sesuai dengan model Product (migrate)

  # Konfigurasi View & Template
    15. Membuat fungsi show_main di views.py. Berfungsi untuk mengambil data dan menampilkannya ke template
    16. Menambahkan dictionary pada fungsi show_main berisi data diri
    17. Modifikasi file html pada direktori template agar dapat menampilkan data dari dictionary menggunakan sintaks Django {{ variable }}

  # Routing URL
    18. Membuat file urls.py di aplikasi main
    19. isi dengan path('', show_main, name='show_main') agar diarahkan ke fungsi show_main
    20. daftarkan urls.py punya aplikasi main ke dalam urls.py punya proyek Utama (path('', include('main.urls'))) supaya URL dari aplikasi main dapat dikenali dan diakses
 
  # Deploy
    21. Push ke GitHub dan deploy ke pws


- Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
  ![Bagan Req Django](https://github.com/user-attachments/assets/4dd2bb07-ebe8-4460-8dfd-ad8ee19f1c6b)


- Jelaskan peran settings.py dalam proyek Django!
  settings.py digunakan untuk mengonfigurasi seluruh proyek Django, semua pegaturan soal bagaimana proyek berjalan ada disini, mulai dari database, allowed host, installed apps, dll.


- Bagaimana cara kerja migrasi database di Django?
  Migrasi model pada Django diunakan untuk menyesuaikan struktur basis data dengan perubahan yang dibuat pada model di kode. Cara kerjanya dimulai dengan membuat file migrasi yang berisi perubahan model yang belum diaplikasikan ke database (makemigrations). Selanjutnya, Django akan mengaplikasikan perubahan dari file migrasi sehingga struktur database sesuai dengan model terbaru (migrate).


- Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
  Django dipilih karena open source, cepat dalam pengembangan, sudah menyediakan banyak fitur bawaan, aman, dan fleksibel digunakan untuk berbagai jenis aplikasi.


- Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
  Tutorial 1 sangat jelas dan mudah dipahami, asisten dosen sangat membantu.

