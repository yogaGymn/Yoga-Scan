# Yoga-Scan

Tools ini adalah alat untuk melakukan pemindaian (scanning) terhadap beberapa jenis kerentanan (vulnerabilities) umum pada aplikasi web, Berikut adalah jenis-jenis kerentanan yang dapat dideteksi oleh alat ini :
1. SQL Injection (SQLi)
Deskripsi: SQL Injection adalah teknik serangan di mana penyerang dapat menyisipkan atau menginjeksikan kode SQL berbahaya ke dalam kueri yang dieksekusi oleh basis data. Ini dapat memungkinkan penyerang untuk mengakses, memodifikasi, atau menghancurkan data dalam basis data.
2. Cross-Site Scripting (XSS)
Deskripsi: XSS adalah kerentanan yang memungkinkan penyerang untuk menyisipkan skrip berbahaya ke dalam halaman web yang dilihat oleh pengguna lain. Skrip ini dapat mencuri cookie pengguna, mengubah tampilan halaman, atau melakukan tindakan berbahaya lainnya.
3. Directory Traversal
Deskripsi: Directory Traversal adalah teknik serangan di mana penyerang dapat mengakses file atau direktori yang berada di luar direktori root web. Ini memungkinkan penyerang untuk membaca file sensitif seperti password atau konfigurasi.

Install From Linux :
sudo apt update
sudo apt install git
git clone https://github.com/yogaGymn/Yoga-Scan.git
cd Yoga-Scan
pip install -r requirements.txt
python scanner.py 
