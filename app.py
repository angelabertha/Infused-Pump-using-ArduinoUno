import streamlit as st
from PIL import Image
import base64

# ============================
#  PERSONAL PRODUCT WEBSITE – INFUSED PUMP
#  Web Display Style (Modern, Colored, Clean)
# ============================

st.set_page_config(
    page_title="Infused Pump – Product Showcase",
    layout="wide",
    page_icon="💉",
)

# ====== Custom CSS Styling ======
page_bg = f"""
<style>
body {
    background: linear-gradient(135deg, #e3f2fd, #e8eaf6);
    font-family: 'Segoe UI', sans-serif;
}

.block-container {
    padding-top: 2rem;
}

h1, h2, h3, h4 {
    color: #0d47a1;
}

.product-card {
    background-color: #ffffff;
    border-radius: 15px;
    padding: 25px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    margin-bottom: 25px;
}

.section-header {
    background-color: #1976d2;
    padding: 12px 20px;
    border-radius: 10px;
    color: white;
    font-size: 22px;
    font-weight: bold;
    margin-top: 40px;
}

.highlight-box {
    background-color: #e3f2fd;
    padding: 15px;
    border-left: 6px solid #1e88e5;
    border-radius: 8px;
    font-size: 17px;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ========== HEADER ==========
st.markdown("<h1 style='text-align:center;'>💉 Infused Pump Berbasis Arduino Uno</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color:#1e88e5;'>Automatic Time-Based Infusion Monitoring System</h3>", unsafe_allow_html=True)

# ============================
# 1. DESKRIPSI PRODUK (Showcase Style)
# ============================
st.markdown('<div class="section-header">1. Deskripsi Produk</div>', unsafe_allow_html=True)

st.markdown(
    """
<div class='product-card'>
    <p style='font-size:18px;'>
        Infused Pump berbasis Arduino Uno ini adalah sistem **otomatisasi infus** yang bekerja menggunakan metode
        <b>time-based control</b>. Pengguna hanya memasukkan durasi melalui keypad 4×4, dan pompa peristaltik akan
        mengalirkan cairan infus secara otomatis dengan laju yang stabil.
        <br><br>
        Sistem ini dirancang sebagai solusi <b>murah, sederhana, dan akurat</b> untuk fasilitas kesehatan dengan keterbatasan sumber daya,
        namun tetap mengutamakan keamanan pasien.
    </p>
    
    <div class='highlight-box'>
        <b>Fitur Utama:</b>
        <ul>
            <li>🎯 Akurasi waktu 100% pada semua pengujian</li>
            <li>💧 Deviasi volume hanya 0,2–0,4%</li>
            <li>🚀 Laju aliran stabil: 8,3 mL/min & 2,2 mL/min</li>
            <li>🔔 Alarm aktif tepat waktu (100% respons)</li>
            <li>🖥️ LCD I2C menunjukkan status real-time</li>
            <li>⚙️ Motor + L298N untuk aktuasi pompa peristaltik</li>
        </ul>
    </div>
</div>
    """,
    unsafe_allow_html=True,
)

# ============================
# 2. DOKUMENTASI PROSES PEMBUATAN
# ============================
st.markdown('<div class="section-header">2. Dokumentasi Proses Pembuatan</div>', unsafe_allow_html=True)

st.markdown(
    """
<div class='product-card'>
    <p style='font-size:17px;'>
    Proses pembangunan perangkat mengikuti alur berikut:
    </p>
    <ul style='font-size:17px;'>
        <li><b>Perancangan diagram blok</b> integrasi Arduino–driver–LCD–keypad–pompa</li>
        <li><b>Penyusunan skematik rangkaian</b> untuk koneksi pin dan power supply</li>
        <li><b>Perakitan perangkat keras</b> di casing akrilik</li>
        <li><b>Pemrograman Arduino</b> untuk timer & alarm</li>
        <li><b>Pengujian performa</b>: waktu, volume, alarm, stabilitas motor</li>
    </ul>
    <br>
    <i>Unggah foto proses atau prototipe di bawah ini:</i>
</div>
""",
    unsafe_allow_html=True,
)

imgs = st.file_uploader("Upload dokumentasi (bisa lebih dari 1)", accept_multiple_files=True)
if imgs:
    for i in imgs:
        st.image(i, caption=i.name)

# ============================
# 3. VIDEO DEMONSTRASI PRODUK
# ============================
st.markdown('<div class="section-header">3. Video Demonstrasi Produk (1–5 menit)</div>', unsafe_allow_html=True)
video = st.text_input("Masukkan link video (YouTube / Drive):")
if video:
    st.video(video)

# ============================
# 4. BIODATA TIM
# ============================
st.markdown('<div class="section-header">4. Biodata Tim & Dosen Pembimbing</div>', unsafe_allow_html=True)

st.markdown(
    """
<div class='product-card'>
    <h4>👥 Anggota Tim</h4>
    <ul style='font-size:17px;'>
        <li><b>Dila Fadilatu Nisa</b> – Hardware & Sistem</li>
        <li><b>Angela Bertha Miady Torie</b> – Dokumentasi, Analisis, Website</li>
    </ul>
    <br>
    <h4>🎓 Dosen Pembimbing</h4>
    <p>Masukkan nama dosen pembimbing di sini.</p>
</div>
""",
    unsafe_allow_html=True,
)

# ============================
# 5. LINK REPOSITORY
# ============================
st.markdown('<div class="section-header">5. Link Repository (Jika Ada)</div>', unsafe_allow_html=True)
repo = st.text_input("Masukkan link GitHub repository:")
if repo:
    st.markdown(f"🔗 <b>Repository Anda:</b> {repo}", unsafe_allow_html=True)

# ============================
# FOOTER
# ============================
st.markdown("""
<hr>
<p style='text-align:center; color:#555;'>Website ini dibuat untuk keperluan UAS dan menampilkan produk Infused Pump berbasis Arduino sesuai makalah penelitian.</p>
""", unsafe_allow_html=True)
