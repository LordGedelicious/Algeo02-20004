# Compressify - Algeo02-20004
Tugas Besar 2 IF 2123 Aljabar Linier dan Geometri

Aplikasi Nilai Eigen dan Vektor Eigen dalam Kompresi Gambar

## Daftar Isi
* [Informasi Umum](#informasi-umum)
* [Anggota Kelompok](#anggota-kelompok)
* [Teknologi yang Digunakan](#teknologi-yang-digunakan)
* [Fitur](#fitur)
* [Setup](#setup)
* [Penggunaan](#penggunaan)
* [Cara](#room-for-improvement)

## Informasi Umum
Pada Tugas Besar 2 IF 2123 Aljabar Linier dan Geometri kali ini kita diminta untuk membuat sebuah program kompresi gambar dengan memanfaatkan Singular Value Decomposition (SVD) yang berjalan di suatu web lokal sederhana. 

Algoritma yang digunakan untuk mencari nilai dan vektor eigen untuk membentuk matriks SVD adalah QR Algorithm yang melibatkan pengiterasian Dekomposisi QR dengan A<sub>k+1</sub> = R<sub>k</sub>Q<sub>k</sub> sehingga matriks A berkonvergensi menjadi matriks diagonal yang memegang nilai-nilai eigen, dan matriks U = Q<sub>1</sub> * Q<sub>2</sub> * ... * Q<sub>k</sub> yang memegang vektor eigen dari matriks A<sub>0</sub>.

## Anggota Kelompok
### The penCITRAan Team
| Nama                           | NIM      |
| ------------------------------ | -------- |
| Gede Prasidha Bhawarnawa       | 13520004 |
| Muhammad Helmi Hibatullah      | 13520014 |
| Ahmad Alfani Handoyo           | 13520023 |

## Teknologi yang Digunakan
* <b>numpy v.1.21.4</b>: untuk melakukan operasi-operasi pada matriks, array, dan operasi matematika lainnya
* <b>Pillow v.8.4.0</b>: untuk segala pemrosesan gambar termasuk mengkonversinya menjadi matriks dan sebaliknya dan mengetahui mode warna yang digunakan
* <b>Flask v.2.0.2</b>: untuk menghubungkan program Python pada backend dengan frontend website dan request dari keduanya
* <b>Bootstrap v5.1.3</b>: untuk membangun web yang elegan dan dengan cepat.

## Fitur
Beberapa fitur yang dapat diakses oleh user saat menggunakan website/program:
* User dapat memberi masukan tingkat kompresi gambar (0-100%)
* User dapat melihat hasil persentase data akhir yang dipakai dan runtime program
* User dapat mengunduh hasil kompresi gambar
* Mendukung gambar dengan format yang <b>didukung sepenuhnya</b> oleh <a href="http://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#fully-supported-formats">library PILLOW</a>
* Mendukung gambar dengan mode warna L, LA, P, PA, RGB, RGBA, dan CMYK

## Setup
Python 3 digunakan untuk menjalankan frontend dan backend dari program, sehingga pastikan Python telah terinstall pada komputer. Bila belum, unduh terlebih dahulu Python 3 <a href="http://www.python.org/downloads/">di sini.</a>

Pastikan Python dan PIP sudah ditambahkan ke PATH, bila belum lihat stackoverflow <a href="http://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-so-it-finds-my-modules-packages>ini</a> dan <a href="http://stackoverflow.com/questions/23708898/pip-is-not-recognized-as-an-internal-or-external-command">ini</a>.

Dengan PIP, install library Flask, numpy, dan Pillow yang dibutuhkan untuk menjalankan program:
```
pip install Flask
pip install numpy
pip install Pillow
```

## Penggunaan
Untuk menjalankan program, jalankan file <b><i>app.py</i></b>
Dapat juga menjalankan program dengan membuka terminal ke folder `/src` dan jalankan
```
python app.py
```
Pada terminal Python akan ada munculan sebagai berikut:
```
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 727-607-683
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
Untuk mengakses website, akses link yang terdapat pada baris terbawah (yang pada kasus ini adalah `http://127.0.0.1:5000/`) pada web browser pilihan Anda. Selamat! Sekarang Anda dapat menjalankan website kompresi gambar.
![home](https://user-images.githubusercontent.com/70305222/141699530-c626ad59-63c6-48c7-a2ce-337e08b0efce.png)
