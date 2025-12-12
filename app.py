import streamlit as st
from PIL import Image

# ============================
# PERSONAL PRODUCT WEBSITE – UAS
# ============================
# Dibuat sesuai instruksi pada screenshot:
# 1. Deskripsi Produk/Prototipe
# 2. Dokumentasi Proses Pembuatan
# 3. Video Demonstrasi Produk (1–5 menit)
# 4. Biodata Anggota Tim & Dosen Pembimbing/Mitra
# 5. Link Repository (jika ada)
# Website harus dapat diakses oleh dosen penguji
# ============================

st.set_page_config(page_title="Infused Pump – Personal Product Website", layout="wide")

st.title("💉 Infused Pump Berbasis Arduino Uno")
st.subheader("Personal Product Website – Ujian Akhir Semester")

# ============================
# 1. DESKRIPSI PRODUK
# ============================
st.header("1. Deskripsi Produk / Prototipe")
st.markdown("""
Sistem **Infused Pump berbasis Arduino Uno** dikembangkan sebagai solusi monitoring cairan infus menggunakan metode *time-based control*.  
Pengguna mengatur durasi infus menggunakan keypad 4×4, dan pompa peristaltik akan berjalan otomatis sesuai waktu yang diinput.

Fitur utama:
- Akurasi waktu 100% pada seluruh pengujian
- Deviasi volume rendah (0,2–0,4%)
- Laju aliran stabil 8,3 mL/min & 2,2 mL/min
- Alarm buzzer aktif real-time
- Tampilan LCD untuk monitoring
- Desain sederhana, ekonomis, mudah digunakan
""")

# ============================
# 2. DOKUMENTASI PROSES PEMBUATAN
# ============================
st.header("2. Dokumentasi Proses Pembuatan")
st.markdown("""
Berikut tahapan dalam pembuatan perangkat Infused Pump:

1. **Perancangan Diagram Blok Sistem** – Menentukan alur kerja komponen (Arduino, keypad, LCD, driver, motor, buzzer).  
2. **Perakitan Hardware** – Integrasi semua komponen pada casing akrilik.  
3. **Penyusunan Skematik Rangkaian** – Koneksi pin Arduino, driver L298N, LCD I2C, pompa, dan power supply.  
4. **Pemrograman Arduino** – Implementasi kontrol waktu dan alarm.  
5. **Pengujian Sistem** – Waktu operasi, respons alarm, output volume, stabilitas motor.

Unggah dokumentasi foto proses / alat di bawah ini:
""")

imgs = st.file_uploader("Upload dokumentasi (bisa lebih dari 1)", accept_multiple_files=True)
if imgs:
    for i in imgs:
        st.image(i, caption=i.name)

# ============================
# 3. VIDEO DEMONSTRASI
# ============================
st.header("3. Video Demonstrasi Produk (1–5 menit)")
video_link = st.text_input("Masukkan Link Video (YouTube / Google Drive):")
if video_link:
    st.video(video_link)

# ============================
# 4. BIODATA TIM
# ============================
st.header("4. Biodata Anggota Tim & Dosen Pembimbing")
st.markdown("""
### 👥 Anggota Tim
- **Dila Fadilatu Nisa** – Pengembangan Hardware & Sistem
- **Angela Bertha Miady Torie** – Dokumentasi, Analisis Data, Website

### 🎓 Dosen Pembimbing
- *(Isi nama dosen pembimbing di sini)*
""")

# ============================
# 5. REPOSITORY
# ============================
st.header("5. Link Repository (Jika Ada)")
repo = st.text_input("Masukkan link GitHub Repository:")
if repo:
    st.markdown(f"🔗 **Repository Anda:** {repo}")

# ============================
# FOOTER
# ============================
st.markdown("""
---
Website ini dibuat sebagai pemenuhan UAS dan dapat diakses oleh dosen penguji melalui tautan Streamlit yang diberikan.
"""
)
