# 💰 Simulasi Tabungan Liburan

## 📌 Deskripsi
**Simulasi Tabungan Liburan** merupakan program sederhana berbasis Python yang dibuat untuk mensimulasikan kegiatan menabung selama beberapa hari dengan tujuan mengumpulkan uang untuk kebutuhan liburan.

Program ini memungkinkan pengguna menentukan berapa lama waktu menabung dan jumlah uang yang ingin ditabung pada setiap sesi. Selama proses berlangsung, terdapat beberapa kondisi khusus yang memengaruhi aktivitas menabung, seperti melewatkan hari tertentu dan menghentikan sesi menabung.

Program ini dibuat sebagai latihan dasar pemrograman Python, khususnya dalam memahami penggunaan perulangan dan percabangan.

## 🎯 Tujuan Pembuatan
- Memahami penggunaan perulangan `for`.
- Memahami penggunaan percabangan `if`, `elif`, dan `else`.
- Mempelajari penggunaan `break` untuk menghentikan perulangan.
- Mempelajari penggunaan `continue` untuk melewati iterasi tertentu.
- Memahami penggunaan `for-else`.
- Mengimplementasikan operasi penjumlahan untuk menghitung total tabungan.

## ⚙️ Fitur Program
1. **Input Durasi Menabung**  
   Pengguna dapat menentukan jumlah hari untuk melakukan kegiatan menabung.

2. **Input Nominal Tabungan**  
   Pengguna dapat menentukan jumlah uang yang akan ditabung pada setiap sesi.

3. **Simulasi Menabung Harian**  
   Program menjalankan proses menabung menggunakan perulangan berdasarkan jumlah hari yang telah ditentukan.

4. **Melewati Hari Tertentu (`continue`)**  
   Pada hari ke-3, aktivitas menabung dilewati karena diasumsikan uang digunakan untuk membeli bensin.

5. **Menghentikan Sesi Menabung (`break`)**  
   Pada sesi ke-3, perulangan sesi dihentikan sehingga pengguna hanya melakukan dua sesi menabung setiap harinya.

6. **Menghitung Total Tabungan**  
   Program menjumlahkan seluruh uang yang berhasil ditabung selama simulasi berlangsung.

7. **Menampilkan Status Tabungan**  
   Hasil akhir dikategorikan berdasarkan jumlah uang yang terkumpul:
   - Rp200.000 atau lebih: Bisa digunakan untuk liburan ke luar kota.
   - Rp50.000 sampai kurang dari Rp200.000: Bisa digunakan untuk jalan-jalan di dalam kota.
   - Kurang dari Rp50.000: Tabungan masih terbatas untuk jajan di sekitar rumah.

## 🧠 Konsep Pemrograman yang Digunakan
| Konsep | Fungsi |
|---|---|
| `input()` | Menerima masukan dari pengguna. |
| `int()` | Mengubah input menjadi tipe data integer. |
| `for` | Melakukan perulangan berdasarkan jumlah hari dan sesi. |
| `if` | Memeriksa kondisi tertentu. |
| `elif` | Memeriksa kondisi alternatif. |
| `else` | Menjalankan perintah ketika kondisi sebelumnya tidak terpenuhi. |
| `continue` | Melewati proses pada hari ke-3. |
| `break` | Menghentikan perulangan sesi ketika mencapai sesi ke-3. |
| `for-else` | Menjalankan pesan ketika perulangan hari selesai secara normal. |
| `+=` | Menambahkan nominal uang ke total tabungan. |

## 💻 Teknologi
- **Bahasa Pemrograman:** Python
- **Konsep:** Fundamental Programming
- **Editor:** Visual Studio Code / Python IDE lainnya

## ▶️ Cara Menjalankan Program

1. Pastikan Python sudah terinstal pada komputer.
2. Clone repository ini:

   ```bash
   git clone https://github.com/USERNAME/simulasi-tabungan-liburan.git
   ```

3. Masuk ke direktori repository:

   ```bash
   cd simulasi-tabungan-liburan
   ```

4. Jalankan program:

   ```bash
   python main.py
   ```

## 📷 Contoh Tampilan Program

```text
===== Simulasi Tabungan Liburan =====
Berapa hari anda menabung?: 5
Berapa uang yang ingin anda tabung per sesinya?: 25000

===== Mulai menabung =====

[ Hari ke- 1 ]
Sesi ke- 1 Anda menabung sebanyak 25000
Sesi ke- 2 Anda menabung sebanyak 25000
Anda terlalu banyak menabung dihari ini

[ Hari ke- 2 ]
Sesi ke- 1 Anda menabung sebanyak 25000
Sesi ke- 2 Anda menabung sebanyak 25000
Anda terlalu banyak menabung dihari ini

[ Hari ke- 3 ]
Hari ke 3 di skip dulu buat bensin

[ Hari ke- 4 ]
Sesi ke- 1 Anda menabung sebanyak 25000
Sesi ke- 2 Anda menabung sebanyak 25000
Anda terlalu banyak menabung dihari ini

[ Hari ke- 5 ]
Sesi ke- 1 Anda menabung sebanyak 25000
Sesi ke- 2 Anda menabung sebanyak 25000
Anda terlalu banyak menabung dihari ini

===== Hasil tabungan =====
Uang anda Rp 200000 -Keren! bisa dipakai liburan keluar kota.
```

## 📚 Catatan Pembelajaran
Project ini merupakan salah satu latihan untuk memahami alur perulangan bersarang (*nested loop*) serta bagaimana `break` dan `continue` memengaruhi jalannya sebuah program.

Melalui project ini, diharapkan pemahaman mengenai dasar-dasar logika pemrograman Python dapat semakin berkembang.

---

**Author:** Irga Mochamad Rafly  
**Program Studi:** Informatika  
**Fakultas:** Teknik  
**Universitas:** Universitas Siliwangi (UNSIL)
