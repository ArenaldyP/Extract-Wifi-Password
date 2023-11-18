# Extract-Wifi-Password-Windows (Windows Wifi Extractor) 😎😎
## Gambaran Umum
Skrip Python ini digunakan untuk mengekstrak kata sandi WiFi yang disimpan pada mesin Windows dengan menggunakan perintah "netsh". Memberikan cara yang nyaman untuk mendapatkan profil WiFi, termasuk SSID, sandi enkripsi, dan kata sandi.

## Fitur
### Mengekstrak dan menampilkan SSID, sandi enkripsi, dan kata sandi WiFi dari profil yang disimpan di Windows.
### Struktur data namedtuple yang terorganisir dengan baik untuk integrasi yang mudah ke dalam proyek-proyek lain.
### Pilihan pencetakan verbose secara real-time untuk detail profil.

## Penggunaan
### 1. Ekstraksi Kata Sandi WiFi di Windows:
* Jalankan skrip di mesin Windows.
* Mengambil profil WiFi yang disimpan menggunakan perintah "netsh".
* Menampilkan SSID, sandi enkripsi, dan kata sandi (jika tersedia).
### python windows_wifi_extractor.py


# Extract-Wifi-Password-Linux (Windows Wifi Extractor) 😎😎
## Gambaran Umum:
Skrip Python ini mengekstrak kata sandi WiFi yang disimpan pada mesin Linux dengan memeriksa konfigurasi dalam direktori '/etc/NetworkManager/system-connections/'. Menawarkan tampilan komprehensif tentang profil WiFi, termasuk SSID, algoritma otentikasi, manajemen kunci, dan kunci bersama (PSK).

## Fitur
* Mengekstrak dan menampilkan SSID, algoritma otentikasi, detail manajemen kunci, dan PSK dari profil yang disimpan di Linux.
* Menggunakan struktur data namedtuple untuk organisasi yang jelas dan adaptabilitas.
* Pilihan pencetakan verbose secara real-time untuk detail profil.

## Penggunaan:
### 1. Ekstraksi Kata Sandi WiFi di Linux:
* Jalankan skrip di mesin Linux.
* Mengekstrak profil WiFi dari direktori '/etc/NetworkManager/system-connections/'.
* Menampilkan SSID, algoritma otentikasi, manajemen kunci, dan PSK.
### sudo python3 linux_wifi_extractor.py

## Catatan 
### Pastikan izin yang tepat untuk mengakses file konfigurasi jaringan di Linux (/etc/NetworkManager/system-connections/).
### Untuk Windows, jalankan skrip dengan hak administratif untuk ekstraksi profil yang akurat.

Selamat mengintegrasikan skrip ini ke dalam proyek Anda atau gunakan standalone untuk mempermudah pengambilan kata sandi WiFi pada sistem Windows dan Linux. Kontribusi dan perbaikan dipersilakan!👍👌







