# Message Blaster X 🚀

![Message Blaster X](https://via.placeholder.com/800x400.png?text=Message+Blaster+X)  
*Blast your messages with style!*

Selamat datang di **Message Blaster X**, sebuah aplikasi Python berbasis GUI yang dirancang untuk mensimulasikan pengiriman pesan berulang dengan antarmuka yang *eye-catching* dan futuristik. Dibangun dengan \`tkinter\`, proyek ini menawarkan desain modern dengan gradasi latar belakang, efek hover, dan progress bar yang dinamis—semuanya untuk pengalaman visual yang memukau!

> **Catatan**: Ini adalah simulasi untuk tujuan edukasi. Fitur pengiriman pesan nyata membutuhkan integrasi API eksternal (misalnya Twilio) dan kepatuhan terhadap hukum setempat.

---

## ✨ Fitur Utama

- **Antarmuka Modern**: Gradasi latar belakang yang halus dengan tema gelap dan aksen merah-neon.
- **Input Intuitif**: Kolom untuk nomor telepon, pesan, jumlah pengiriman, dan delay—dilengkapi emoji keren (📞💬🔢⏱).
- **Tombol Dinamis**: Tombol "Blast Off!" dengan efek hover yang berubah warna dari merah tua ke merah cerah.
- **Progress Bar**: Visualisasi proses dengan progress bar berwarna merah yang elegan.
- **Status Real-Time**: Pesan status dalam warna cyan (#00ffcc) untuk umpan balik langsung.
- **Simulasi Aman**: Output hanya ke konsol, tanpa risiko hukum atau gangguan.

---

## 🛠️ Cara Instalasi

### Prasyarat
- Python 3.x terinstal (disarankan menggunakan Anaconda atau lingkungan virtual).
- Modul \`tkinter\` (biasanya sudah ada di instalasi Python standar).

### Langkah-Langkah
1. **Clone Repository**  
   \`\`\`bash
   git clone https://github.com/username/message-blaster-x.git
   cd message-blaster-x
   \`\`\`
2. **Jalankan Aplikasi**  
   Pastikan Anda berada di direktori proyek, lalu jalankan:
   \`\`\`bash
   python main.py
   \`\`\`
3. **Eksplorasi!**  
   Masukkan nomor telepon, pesan, jumlah pengiriman, dan delay, lalu tekan "Blast Off!" untuk melihat simulasi di konsol.

---

## 🎨 Desain Visual

- **Gradasi Latar**: Transisi halus dari biru tua (#0f0f1a) ke biru terang untuk kesan futuristik.
- **Warna Aksen**: Merah (#ff4444) untuk tombol dan progress bar, cyan (#00ffcc) untuk status.
- **Font**: Menggunakan "Arial" dengan ukuran variatif untuk hierarki yang jelas.
- **Efek Hover**: Tombol berubah warna saat disentuh kursor, menambah interaktivitas.

---

## 📝 Cara Penggunaan

1. **Masukkan Data**:
   - **Nomor Telepon**: Target simulasi (hanya untuk tampilan).
   - **Pesan**: Teks yang akan "dikirim".
   - **Jumlah**: Berapa kali pesan akan diulang.
   - **Delay**: Jeda antar pengiriman dalam detik.
2. **Tekan "Blast Off!"**:
   - Progress bar akan berjalan, dan status akan diperbarui. Cek konsol untuk output simulasi.
3. **Hasil**:
   - Popup sukses akan muncul setelah simulasi selesai.

---

## ⚙️ Kode Struktur

- **main.py**: File utama yang berisi logika GUI dan simulasi.
- **Dependensi**: Hanya \`tkinter\` dan \`ttk\` (tanpa library tambahan).

### Contoh Kode
\`\`\`python
# Fungsi simulasi pengiriman
def send_spam():
    phone_number = entry_number.get()
    message = entry_message.get()
    count = int(entry_count.get())
    delay = float(entry_delay.get())
    for i in range(count):
        print(f"Pesan ke-{i+1} ke {phone_number}: {message}")
        time.sleep(delay)
\`\`\`

---

## 🚧 Batasan & Pengembangan

- **Saat Ini**: Hanya simulasi (output ke konsol).
- **Potensi**: Integrasi dengan API seperti Twilio untuk pengiriman nyata (harus mematuhi regulasi).
- **Ide Masa Depan**:
  - Animasi tambahan (misalnya efek partikel).
  - Tema warna yang dapat diganti.
  - Dukungan multi-target.

---

## ⚠️ Peringatan

Proyek ini dibuat untuk tujuan edukasi. Menggunakan alat ini untuk spam atau mengganggu orang lain dapat melanggar hukum dan etika. Gunakan dengan bijak!

---

## 🤝 Kontribusi

Ingin berkontribusi? Fork repo ini, buat perubahan, dan ajukan pull request. Ide desain, fitur baru, atau perbaikan bug sangat diterima!

---

## 📬 Kontak

Punya pertanyaan? Hubungi saya di:

- **Email**: email@example.com
- **GitHub**: username

---

Message Blaster X - Blast pesanmu dengan gaya, tapi tetap bertanggung jawab!

⭐ Beri bintang di GitHub jika Anda menyukainya!