Nama : Kaysan Navid Musyaffa

NPM : 2506625470

Kelas : PBP B

## Panduan Jalankan Aplikasi Secara Lokal

#### 1. Clone Repositori Buka terminal/command prompt, lalu klon repositori GitHub kamu ke komputer lokal:
``` 
git clone https://github.com/nalkq/[nama-repo-kamu].git
cd [nama-repo-kamu]
``` 

#### 2. Buat dan Aktifkan Virtual Environment Gunakan virtual environment agar pustaka (library) proyek ini terisolasi dengan rapi dan tidak bentrok dengan proyek lain:

Windows:
```
python -m venv env
env\Scripts\activate
```

macOS / Linux:
```
python3 -m venv env
source env/bin/activate
```

#### 3. Install Django Karena proyek ini menggunakan Django untuk mengelola halaman dan berkas statis, instal Django di dalam virtual environment-mu:
```
pip install django
```

#### 4. Jalankan Server Lokal Gunakan perintah bawaan Django untuk menyalakan server pengembangan lokal:
```
python manage.py runserver
```

Setelah server menyala, buka browser dan akses alamat http://127.0.0.1:8000/ 


## AI Disclosure
Tentu projek yang saya kerjakan ini memiliki andil AI di dalamnya, AI membantu saya mengeksplor apa saja yang bisa dilakukan css dan memberikan saya berbagai macam pilihan style yang dapat saya implementasikan ke projek yang saya kerjakan ini. AI juga membantu saya dalam memahami tata cara conventional commits yang baik dan benar agar sesuai dengan standar profesional.

https://notebook.google.com/notebook/2ff52ba9-dd58-4a22-b8bf-5262db7b016e

### Tugas 1

#### 1. Pada Tutorial dan Tugas 1, Anda diberi kebebasan untuk menentukan tampilan dari website portofolio Anda. Saat Anda merancang struktur HTML yang digunakan, apakah Anda menggunakan elemen semantik HTML5 seperti `<section>`, `<article>`, atau `<aside>`? Jika iya, bagaimana elemen tersebut membantu Anda dalam membuat static web? Jika tidak, mengapa tanpa elemen tersebut sudah memenuhi kebutuhan desain Anda?
Pada Tugas 1 kali ini, saya menggunakan elemen semantik HTML5 seperti `<header>`, `<section>`, `<nav>`, dan yang lainnya. Seperti yang dijelaskan pada tutorial 1, elemen-elemen semantik tersebut berguna sebagai aksebilitas untuk memaknai struktur kode sehingga orang yang bekerja sama dengan kita nanti tidak kesulitan untuk melakukan perubahan pada kode yang kita punya.

#### 2. Ketika Anda mengatur CSS Anda agar tetap responsive, tantangan tata letak apa yang Anda temukan? Bagaimana Anda mengevaluasi elemen mana yang harus diubah posisinya atau diprioritaskan ukurannya saat berpindah dari tampilan desktop ke mobile?
Saat saya sedang berusaha mengimplementasikan web saya agar responsive, saya sempat mengalami kebingungan karena bentuk header yang saya implementasikan hilang saat saya coba scroll. Setelah saya cermati kode saya ulang, ternyata saya tidak sadar belum menghapus syntax `position: fixed` yang belum terhapus di bagian bawah sehingga syntax `position: sticky` nya jadi tertimpa. Untuk masalah ketika berpindah dari tampilan desktop ke mobile saya tidak menemukan masalah apa-apa dan sejauh ini masih aman.

#### 3. Website yang Anda buat saat ini adalah static web murni. Batasan apa yang Anda rasakan saat mencoba menyajikan informasi pada portofolio Anda secara optimal? Berdasarkan batasan tersebut, fungsionalitas dinamis apa yang paling ingin Anda persiapkan dan tambahkan pada iterasi proyek selanjutnya?
Dalam pembuatan web ini, saya sering kali melakukan kesalahan kecil konyol seperti typo saat mengisi nama tab pada skills section milik saya, lalu pemikiran saya yang berubah-ubah tentang tulisan apa yang cocok untuk ditaruh di bio ataupun skills. Dan tiap saya memikirkan sesuatu yang lebih baik, saya harus mengupdatenya secara manual di html dimana itu cukup melelahkan karena dilakukan berulang kali. Untuk mengatasi masalah tersebut, saya tertarik untuk menambahkan Content Management System (CMS).