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

### Tugas 1
AI tentu tidak selalu benar, beberapa kali kode yang disarankan AI justru mengalami error seperti lupa menutup `<div>` yang dibuka sehingga saya harus debug secara manual untuk memperbaiki error tersebut. Atau bahkan memaksakan penggunaan syntax `!important` yang membuat kode css yang saya miliki menjadi tidak best practice.

https://notebook.google.com/notebook/2ff52ba9-dd58-4a22-b8bf-5262db7b016e

### Tugas 2
Pada penggunaan AI kali ini, saya merasa jauh lebih kesulitan dengan AI yang saya gunakan. Beberapa kali permintaan referensi yang saya minta justru malah mengubah struktur paten kode yang sudah saya miliki sebelumnya. Sehingga, saya cukup sering mengubah manual referensi kode yang diberikan agar sesuai dengan yang saya butuhkan. Contohnya ketika saya meminta referensi test case karena saya masih cukup bingung dengan hal itu, AI justru memberikan struktur kode yang jauh berbeda dengan struktur kode yang saya miliki. Lalu ketika saya meminta referensi untuk mengubah warna background projek saya agar sesuai dengan background modul `experience` yang AI berikan, AI justru malah mengubah hal-hal yang tidak perlu sehingga saya harus melakukan perubahan manual yang benar-benar tidak merusak struktur kode yang saya miliki saat ini.

#### Additional Note for Individual Assignment 2: Saya masih bingung bagaimana cara mengakali deksripsi page agar memiliki font yang sesuai dengan class yang saya sudah buat di style.css, sehingga saya memutuskan untuk menggunakan syntax |safe pada bagian description skill mauapun experience yang saya punya, sehingga ketika saya menambah data untuk description, saya masih memasukkan syntax html untuk mendefinisikan class pada style.css apa yang ingin digunakan.

https://share.gemini.google/i9P0nHMV5RuJ

### Tugas 3
Pada penggunaan AI kali ini, saya cukup kesulitan ketika mengerjakan tutorial 3 karena hal yang saya lakukan merupakan hal baru yang saya tidak ketahui sebeumnya. Namun setelah selesai mengerjakan tutorial 3, saya sudah cukup paham dengan apa yang harus dilakukan sehingga ketika mengerjakan tugas 3 saya tidak merasakan kesulitan yang cukup signifikan, dikarenakan pada tugas kali ini tugasnya hanyalah refactor kode yang sudah saya punya sehingga saya lebih sering menggunakan AI sebagai panduan inovasi style yang ingin saya ubah dan saya tidak menemukan kesulitan pada saat pengerjaannya. Saya juga menggunakan AI untuk membantu saya menjawab pertanyaan reflektif yang saya tidak pahami sama sekali pada awalnya.

https://share.gemini.google/itof7uukcyBN

## Pertanyaan Reflektif
### Tugas 1

#### 1. Pada Tutorial dan Tugas 1, Anda diberi kebebasan untuk menentukan tampilan dari website portofolio Anda. Saat Anda merancang struktur HTML yang digunakan, apakah Anda menggunakan elemen semantik HTML5 seperti `<section>`, `<article>`, atau `<aside>`? Jika iya, bagaimana elemen tersebut membantu Anda dalam membuat static web? Jika tidak, mengapa tanpa elemen tersebut sudah memenuhi kebutuhan desain Anda?
Pada Tugas 1 kali ini, saya menggunakan elemen semantik HTML5 seperti `<header>`, `<section>`, `<nav>`, dan yang lainnya. Seperti yang dijelaskan pada tutorial 1, elemen-elemen semantik tersebut berguna sebagai aksebilitas untuk memaknai struktur kode sehingga orang yang bekerja sama dengan kita nanti tidak kesulitan untuk melakukan perubahan pada kode yang kita punya.

#### 2. Ketika Anda mengatur CSS Anda agar tetap responsive, tantangan tata letak apa yang Anda temukan? Bagaimana Anda mengevaluasi elemen mana yang harus diubah posisinya atau diprioritaskan ukurannya saat berpindah dari tampilan desktop ke mobile?
Saat saya sedang berusaha mengimplementasikan web saya agar responsive, saya sempat mengalami kebingungan karena bentuk header yang saya implementasikan hilang saat saya coba scroll. Setelah saya cermati kode saya ulang, ternyata saya tidak sadar belum menghapus syntax `position: fixed` yang belum terhapus di bagian bawah sehingga syntax `position: sticky` nya jadi tertimpa. Untuk masalah ketika berpindah dari tampilan desktop ke mobile saya tidak menemukan masalah apa-apa dan sejauh ini masih aman.

#### 3. Website yang Anda buat saat ini adalah static web murni. Batasan apa yang Anda rasakan saat mencoba menyajikan informasi pada portofolio Anda secara optimal? Berdasarkan batasan tersebut, fungsionalitas dinamis apa yang paling ingin Anda persiapkan dan tambahkan pada iterasi proyek selanjutnya?
Dalam pembuatan web ini, saya sering kali melakukan kesalahan kecil konyol seperti typo saat mengisi nama tab pada skills section milik saya, lalu pemikiran saya yang berubah-ubah tentang tulisan apa yang cocok untuk ditaruh di bio ataupun skills. Dan tiap saya memikirkan sesuatu yang lebih baik, saya harus mengupdatenya secara manual di html dimana itu cukup melelahkan karena dilakukan berulang kali. Untuk mengatasi masalah tersebut, saya tertarik untuk menambahkan Content Management System (CMS).

### Tugas 2

#### 1. Jelaskan alur yang terjadi ketika pengguna membuka halaman portofolio baru, mulai dari permintaan yang diterima proyek hingga data ditampilkan pada browser. Dalam jawabanmu, jelaskan peran urls.py proyek, urls.py aplikasi, view, model, dan template.
- Browser: Pengguna mengetikkan URL di browser (misalnya localhost:8000/) dan mengirimkan HTTP Request ke server Django.
- urls.py proyek : Bertindak sebagai gerbang utama dimana file ini akan mengecek URL dasar yang diminta dan meneruskannya ke urls.py milik aplikasi yang tepat (misalnya aplikasi main).
- urls.py aplikasi: Menerima URL dari proyek dan mencocokkan pola rute yang lebih spesifik (misalnya name="show_experience"). Jika cocok, URL ini akan memanggil fungsi View yang terkait.
- View: Bertindak sebagai otak. Fungsi di dalam view akan memproses request tersebut. Jika halaman membutuhkan data portofolio, view akan meminta data tersebut ke Model.
- Model: Bertindak sebagai jembatan komunikasi dengan database. Model mengambil data yang diminta oleh View (misalnya mengambil seluruh data Experience atau Skill). Setelah dapat, Model mengembalikannya ke View.
- Template: View mengumpulkan data dari Model ke dalam sebuah dictionary (biasa disebut context), lalu mengirimkannya ke Template. Template bertugas menggabungkan kerangka UI (HTML/CSS) dengan data dinamis dari context tersebut (menggunakan tag seperti {% for %}).
- Kembali ke Browser: Template yang sudah berisi data lengkap dirender menjadi halaman HTML utuh, lalu View mengirimkannya kembali ke browser pengguna sebagai HTTP Response untuk ditampilkan.

#### 2. Mengapa data untuk bagian portofolio baru sebaiknya disimpan pada model dan tidak ditulis langsung di dalam template? Jelaskan dampaknya terhadap kemudahan pemeliharaan dan pengembangan aplikasi.
Dengan menyimpan data pada model, tentu hal tersebut akan memudahkan kita ketika ingin memodifikasi ataupun menambah data yang ingin dimasukkan ke dalam portofolio kita. Jika ditulis langsung dalam template, itu akan menyulitkan kita sebagai pengembang aplikasi karena harus mengubah lagi struktur kode di dalamnya, namun jika data nya disimpan di model, kita dapat dengan mudah langsung mengeksekusi apa yang kita butuhkan.

#### 3. Apa perbedaan fungsi makemigrations dan migrate pada Django? Berikan contoh perubahan model yang mengharuskanmu menjalankan kedua perintah tersebut.
`makemigrations` bertugas untuk mendeteksi perubahan pada `models.py` dan membuat file draft dari perubahan tersebut, sedangkan `migrate` bertugas mengeksekusi file draft tersebut sebagai patokan untuk mengubah struktur tabel di dalam database. Contoh perubahan model berdasarkan yang terjadi pada projek saya adalah ketika saya ingin mengubah nama class `Skill` saya menjadi `Skills` dan ketika saya ingin menambah variabel `code_snippet`, kesimpulannya adalah `makemigrations` dan `migrate` wajib dilakukan ketika kita mengubah apapun walau sedikit di bagian model agar perubahan tersebut diterapkan ke database.

### Tugas 3

#### 1. Jelaskan mengapa kita menggunakan ModelForm pada Django alih-alih membuat form HTML secara manual. Selain itu, jelaskan pula mengapa kita diwajibkan menambahkan {% csrf_token %} pada form tersebut!
- Prinsip DRY (Don't Repeat Yourself): Jika kita menggunakan form HTML manual, kita harus menulis ulang atribut field (seperti tipe data, panjang maksimal, keharusan isi) yang sebenarnya sudah didefinisikan di `models.py`. Dengan `ModelForm`, Django secara otomatis membuat form berdasarkan model yang sudah ada.
- Validasi Otomatis: `ModelForm` secara otomatis memvalidasi data berdasarkan konstrain yang ada di model. Jika data tidak valid, Django akan mengembalikan pesan error tanpa harus kita program secara manual.
- Kemudahan Menyimpan Data: Dengan `ModelForm`, menyimpan data ke database sangat ringkas. kita cukup memanggil `form.save()` di views, dan Django akan mengurus pembuatan objek baru di database.

CSRF merupakan singkatan dari Cross-Site Request Forgery. Ini adalah celah keamanan di mana situs berbahaya mencoba mengirimkan request (biasanya POST) dengan memanfaatkan kredensial/sesi pengguna yang sedang login di situs aslimu. Tag {% csrf_token %} akan men-generate token unik dan rahasia ke dalam form HTML. Saat form di-submit, Django akan mencocokkan token ini. Jika tidak ada atau tidak cocok, Django akan menolak request tersebut demi keamanan.


#### 2. Pada Tutorial 03, kita membahas format data JSON dan XML. Mengapa JSON lebih disukai dalam pengembangan aplikasi web modern dibandingkan XML?
Karena JSON lebih rapi dan lebih enak dibaca. Misal untuk menulis nama saja, jika menggunakan XML maka kita harus menulis syntax `<nama>Kaysan</nama>`, sedangkan jika menggunakan JSON, kita hanya perlu menulis syntax `"nama": "Kaysan"`. Syntax JSON disini jauh lebih mudah untuk dimengerti dibanding XML. Selain itu, formatnya yang sederhana dapat berpengaruh pada ukuran datanya yang jadi lebih kecil dan loading website yang menjadi lebih cepat.

#### 3. Jelaskan alur yang terjadi saat kamu menggunakan fungsi view untuk mengembalikan data portofoliomu dalam bentuk JSON. Mengapa kita perlu melakukan proses serialization pada model Django sebelum datanya dikembalikan?
Alur yang terjadi saat view mengembalikan data JSON:
1. Menerima Request: Fungsi view menerima request HTTP dari klien (browser).
2. Mengambil Data: View menggunakan Django ORM untuk mengambil data dari database (contoh: pengalaman = Experience.objects.all()). Hasil dari proses ini adalah `QuerySet`, yaitu kumpulan objek Python/Django.
3. Proses Serialization: `QuerySet` yang berisi objek Python tersebut dimasukkan ke dalam fungsi serializer Django (contoh: serializers.serialize('json', pengalaman)).
4. Mengirim Response: Data yang sudah diubah menjadi string berformat JSON tadi dimasukkan ke dalam `HttpResponse` dengan tipe konten application/json, lalu dikirim kembali ke klien.

Simpelnya, data yang diambil dari database melalui Django ORM berbentuk objek Python yang kompleks. Sedangkan, Web browser atau aplikasi klien tidak mengerti apa itu "objek Python". Oleh karena itu, kita butuh Serialization, yaitu proses menerjemahkan objek Python yang kompleks tersebut menjadi format teks standar dan universal (seperti JSON). Dengan begitu, datanya bisa dikirim melalui protokol HTTP dan dipahami serta diolah oleh berbagai macam klien