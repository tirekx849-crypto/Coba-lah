# 🚀 WEB RAPID FIRE — High-Speed L7 Flooder

> **Layer 7 Stress Tester** — 100% Nyata, Tanpa Root, Tanpa Simulasi.
> Dirancang untuk menguji kecepatan dan ketahanan *Application Layer* (HTTP/HTTPS) pada website/server milikmu sendiri dengan metode *Raw Socket Zero-Delay*.

![Python](https://img.shields.io/badge/python-3.8%2B-brightgreen)
![Platform](https://img.shields.io/badge/platform-linux%20%7C%20termux-green)
![Speed](https://img.shields.io/badge/speed-extreme-red)
![License](https://img.shields.io/badge/license-MIT-green)

---

## ⚠️ DISCLAIMER — BACA SEBELUM PAKAI

> **Tool ini HANYA untuk pengujian beban (stress testing) pada website yang KAMU MILIKI SENDIRI atau di mana kamu memiliki izin tertulis.**
> 
> Menjalankan tool ini terhadap jaringan, server, atau website milik orang lain tanpa izin adalah **TINDAKAN ILEGAL** dan melanggar hukum siber (UU ITE). 
> **Penulis tidak bertanggung jawab atas penyalahgunaan yang dilakukan oleh pengguna.**

---

## 🚀 Fitur & Vektor Serangan (High-Speed)

Berbeda dari versi sebelumnya, script ini membuang semua jeda (`sleep`) dan menggunakan *Raw Socket Non-Blocking* untuk mengirim request secepat mungkin.

1. **HTTP GET Rapid Fire** — Spam request GET ke server dengan parameter unik tanpa henti.
2. **HTTP POST Rapid Fire** — Spam request POST dengan *body* besar untuk membebani *worker* server.
3. **HTTP/2 Rapid Reset** — Mengirim *frame* HTTP/2 secara langsung untuk mengeksploitasi celah protokol yang membuat CPU server *spike*.
4. **TLS Handshake Exhaust** — Menembak koneksi SSL/TLS terus-menerus hingga server kehabisan *buffer* enkripsi.
5. **OVERDRIVE MODE** — Menggabungkan HTTP GET Flood dan HTTP/2 Rapid Reset secara bersamaan. Jaminan server *timeout* (Error 503/504) jika target adalah VPS standar.

---

## 🛠️ CARA INSTALASI LENGKAP

### Opsi A: Pengguna Termux (Android)

**1. Update & Install Dependensi Sistem**
```bash
pkg update && pkg upgrade -y
pkg install python git -y


2. Clone Repositori & Masuk ke Folder

```bash
git clone https://github.com/tirekx849-crypto/web_rapid_fire.git
cd web_rapid_fire
```

3. Jalankan Tool

```bash
python web_rapid_fire.py
```

---

Opsi B: Pengguna Kali Linux / Ubuntu / VPS

1. Update Repositori Sistem

```bash
sudo apt update && sudo apt upgrade -y
```

2. Install Python & Git

```bash
sudo apt install python3 git -y
```

3. Clone Repositori & Masuk ke Folder

```bash
git clone https://github.com/tirekx849-crypto/web_rapid_fire.git
cd web_rapid_fire
```

4. Jalankan Tool

```bash
python3 web_rapid_fire.py
```

---

📖 CARA PENGGUNAAN

1. Saat script berjalan, layar akan menampilkan menu berwarna hijau neon.
2. Pilih nomor vektor (1-5). Disarankan pilih [5] OVERDRIVE untuk hasil maksimal.
3. Masukkan URL target. (Contoh: http://target-website-lu.com).
4. Masukkan durasi serangan dalam detik (Contoh: 60).
5. Masukkan jumlah thread. Maksimal 200 (jika lebih, script akan otomatis menurunkannya agar Termux tidak force close).
6. Tekan Enter, dan tool akan menembak secara brutal tanpa jeda.

Cara Cek Efek:
Buka website target di browser HP/PC lain saat serangan berlangsung. Jika halaman berputar lama, timeout, atau muncul "Error 503/504 Service Unavailable", berarti serangan berhasil dan server kewalahan.

---

🛑 BATASAN FISIKA (PENTING)

· Tool ini TIDAK menggunakan spoofing IP (karena butuh root). Serangan datang dari IP asli perangkatmu.
· Jika website target dilindungi oleh Cloudflare/Akamai dengan mode Under Attack, IP kamu akan di-block dalam hitungan detik (muncul halaman Checking your browser...).
· Jika target menggunakan hosting standar/VPS murah, vektor nomor 3 dan 5 dijamin membuat server mereka down atau restart.
· Tool ini hanya menyerang web (Layer 7). Tidak bisa digunakan untuk mematikan WiFi orang lain (Layer 2).

```
