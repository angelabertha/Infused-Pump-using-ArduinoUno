import streamlit as st

# --- Website Title ---
st.title("Infused Pump Berbasis Arduino Uno — Personal Product Website")

st.markdown("""
## 1. Deskripsi Produk / Prototipe
Sistem **Infused Pump berbasis Arduino Uno** adalah perangkat yang dirancang untuk mengatur dan memonitor aliran infus secara otomatis berdasarkan waktu. Sistem ini menggunakan *time-based control* sehingga motor pompa peristaltik bekerja sesuai durasi yang dimasukkan oleh pengguna melalui keypad 4×4. Perangkat dilengkapi LCD untuk menampilkan waktu, buzzer sebagai alarm, dan driver L298N untuk mengatur motor.

Fitur utama:
- Akurasi waktu 100% pada seluruh variasi pengujian.
- Deviasi volume sangat rendah (0,2–0,4%).
- Dua mode laju aliran stabil: **8,3 mL/min** dan **2,2 mL/min**.
- Alarm real-time pada menit terakhir dan waktu selesai.
- Desain sederhana, ekonomis, dan mudah digunakan.
""")

# --- Dokumentasi Proses Pembuatan ---
st.markdown("""
## 2. Dokumentasi Proses Pembuatan
**Tahap Pembuatan:**
1. **Perancangan Sistem:** Penyusunan diagram blok, skematik, serta alur kerja komponen.
2. **Perakitan Hardware:** Integrasi Arduino Uno, keypad 4×4, pompa peristaltik, driver L298N, LCD I2C, buzzer, serta catu daya.
3. **Pemrograman:** Implementasi kontrol berbasis waktu menggunakan Arduino IDE.
4. **Pengujian:** Pengukuran durasi, volume, stabilitas motor, dan respon alarm.
5. **Analisis Data:** Perhitungan error waktu, deviasi volume, dan konsistensi laju aliran.

Dokumentasi gambar dapat ditambahkan di sini (unggah foto prototipe jika diperlukan):
""")

uploaded_images = st.file_uploader("Upload dokumentasi gambar (opsional)", accept_multiple_files=True)
if uploaded_images:
    for img in uploaded_images:
        st.image(img)

# --- Video Demo ---
st.markdown("""
## 3. Video Demonstrasi Produk
Durasi yang diizinkan: **1–5 menit**.
Silakan masukkan link video demo (YouTube/Drive).
""")

video_link = st.text_input("Masukkan Link Video Demo:")
if video_link:
    st.video(video_link)

# --- Biodata Anggota Tim & Dosen Pembimbing ---
st.markdown("""
## 4. Biodata Anggota Tim & Dosen Pembimbing/Mitra
### Anggota Tim
- **Dila Fadilatu Nisa** — Peneliti dan Pengembang Hardware
- **Angela Bertha Miady Torie** — Dokumentasi, Analisis Data, dan Penyusunan Website

### Dosen Pembimbing/Mitra
- **(Isi Nama Dosen Pembimbing)**
""")

# --- Repository ---
st.markdown("""
## 5. Link Repository
Masukkan link repository GitHub jika tersedia.
""")
repo_link = st.text_input("Github Repository Link:")
if repo_link:
    st.markdown(f"🔗 **Repository:** {repo_link}")

# --- Footer ---
st.markdown("""
---
Website ini dibuat sebagai pemenuhan tugas UAS dan dapat diakses oleh dosen penguji melalui tautan yang diberikan.
""")
