# 🚀 WEB RAPID FIRE — High-Speed L7 Flooder

> **Layer 7 Stress Tester** — 100% Nyata, Tanpa Root, Tanpa Simulasi.
> Dirancang untuk menguji kecepatan dan ketahanan *Application Layer* (HTTP/HTTPS) pada website/server milikmu sendiri.

![Python](https://img.shields.io/badge/python-3.8%2B-brightgreen)
![Platform](https://img.shields.io/badge/platform-linux%20%7C%20termux-green)
![License](https://img.shields.io/badge/license-MIT-green)

---

## ⚠️ DISCLAIMER

> **Tool ini HANYA untuk pengujian beban (stress testing) pada website yang KAMU MILIKI SENDIRI.**
> Menjalankan tool ini terhadap website orang lain tanpa izin adalah **TINDAKAN ILEGAL**. Penulis tidak bertanggung jawab atas penyalahgunaan.

---

## 🚀 Fitur & Vektor

1. **HTTP GET Rapid Fire** — Spam request GET ke server.
2. **HTTP POST Rapid Fire** — Spam request POST dengan *body* besar.
3. **HTTP/2 Rapid Reset** — Eksploitasi celah protokol HTTP/2.
4. **TLS Handshake Exhaust** — Beban enkripsi SSL.
5. **OVERDRIVE MODE** — Gabungan GET Flood dan HTTP/2 secara bersamaan.

---

## 🛠️ CARA INSTALASI (Termux / Android)

**1. Update & Install Dependensi**
```bash
pkg update && pkg upgrade -y
pkg install python git -y

2. Clone Repositori & Masuk ke Folder

```bash
git clone https://github.com/tirekx849-crypto/web-rapid-fire.git
cd web-rapid-fire
```

3. Jalankan Tool

```bash
python web_rapid_fire.py
```

---

📖 CARA PENGGUNAAN

1. Pilih nomor vektor (1-5). Disarankan pilih [5] OVERDRIVE.
2. Masukkan URL target. (Contoh: http://target-website-lu.com).
3. Masukkan durasi serangan dalam detik (Contoh: 60).
4. Masukkan jumlah thread (Maksimal 200).
5. Tekan Enter, dan tool akan menembak tanpa jeda.

Cara Cek Efek:
Buka website target di browser lain saat serangan berlangsung. Jika halaman berputar lama atau muncul "Error 503/504", berarti server kewalahan.

---

```

5. Klik **Commit changes...** (Lakukan perubahan).

---

### LANGKAH 4: Cara Orang Lain (atau Lu) Clone di Termux

Sekarang lu atau orang lain bisa nge-*clone* tanpa error, karena nama repo dan link di README udah **sinkron**.

Buka Termux, ketik ini persis seperti ini:
```bash
git clone https://github.com/tirekx849-crypto/web-rapid-fire.git
cd web-rapid-fire
python web_rapid_fire.py
```
