import streamlit as st
from PIL import Image
import pandas as pd

# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------
st.set_page_config(
    page_title="INFUSED PUMP BERBASIS ARDUINO UNO",
    layout="wide",
)

# -------------------------------------------------------
# DARK / LIGHT MODE SWITCH
# -------------------------------------------------------
if 'theme' not in st.session_state:
    st.session_state.theme = 'light'

mode = st.sidebar.radio("🌗 Tema Website", ["Light", "Dark"])
st.session_state.theme = 'dark' if mode == "Dark" else 'light'

theme_css = {
    'light': """
        body { background: linear-gradient(135deg, #e3f2fd, #e8eaf6); color: #000; }
        .card { background:#fff; }
        .title { color:#0d47a1; }
    """,
    'dark': """
        body { background: #0f1214; color: #e2e2e2; }
        .card { background:#1f1f1f; color:#e2e2e2 !important; }
        .title { color:#64b5f6; }
    """,
}

# -------------------------------------------------------
# ANIMATION CSS
# -------------------------------------------------------
animation_css = """
<style>
.fade-in {
    animation: fadeIn 1s ease-in-out;
}
@keyframes fadeIn {
    0% {opacity: 0; transform: translateY(10px);}
    100% {opacity: 1; transform: translateY(0);}
}
.card { padding:20px; border-radius:14px; box-shadow:0 4px 10px rgba(0,0,0,0.1); margin-bottom:20px; }
.title { font-weight:bold; }
table th {background-color:#bbdefb !important;}
</style>
"""

st.markdown(f"<style>{theme_css[st.session_state.theme]}</style>", unsafe_allow_html=True)
st.markdown(animation_css, unsafe_allow_html=True)

# -------------------------------------------------------
# SIDEBAR LOGO
# -------------------------------------------------------
st.sidebar.image("logo.png", width=150)

menu = st.sidebar.selectbox(
    "📌 Pilih Halaman",
    ["Beranda", "Deskripsi Produk", "Perakitan & Pengujian", "Video Demonstrasi", "Biodata Tim"]
)

# -------------------------------------------------------
# BERANDA
# -------------------------------------------------------
if menu == "Beranda":

    st.markdown("<h1 class='title fade-in'>INFUSED PUMP BERBASIS ARDUINO UNO</h1>", unsafe_allow_html=True)
    st.image("infusepump.png", caption="Infuse Pump", use_column_width=True)

    st.markdown("""
    <div class='card fade-in'>
    <p style='font-size:17px;'>
    Pemberian cairan infus merupakan tindakan medis penting yang membutuhkan ketelitian tinggi, terutama dalam pengaturan laju aliran dan durasi pemberian cairan. Kesalahan kecil dalam pengaturan infus dapat berdampak pada ketidakseimbangan cairan tubuh dan risiko kesehatan bagi pasien.
    <br><br>
    Sistem infused pump otomatis ini dirancang untuk memberikan solusi yang akurat, konsisten, dan mudah dioperasikan.
    </p></div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------
# DESKRIPSI PRODUK
# -------------------------------------------------------
elif menu == "Deskripsi Produk":
    st.markdown("<h2 class='title fade-in'>1. Deskripsi Produk</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class='card fade-in'>
    Infused pump berbasis Arduino Uno bekerja menggunakan metode <b>time-based control</b>.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h3 class='title fade-in'>Sistem Kerja:</h3>", unsafe_allow_html=True)

    st.markdown("""
    <div class='card fade-in'>Sistem menerima input volume dan waktu melalui keypad, menghitung laju aliran, mengatur motor lewat PWM, menampilkan sisa waktu di LCD, dan mengaktifkan alarm saat sisa waktu ≤ 60 detik.</div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------
# PERAKITAN & PENGUJIAN
# -------------------------------------------------------
elif menu == "Perakitan & Pengujian":
    st.markdown("<h2 class='title fade-in'>3. Perakitan & Pengujian</h2>", unsafe_allow_html=True)

    hardware_data = {
        "Nama Barang": ["Arduino Uno","Peristaltic Pump","Motor Driver (L298N)","LCD 16×2","Keypad 4×4","Sensor Berat","Buzzer","Selang kecil (1 m)","Power Supply 12V","Kabel Jumper","Resistor","Kotak Akrilik","Lem","Timah","Breadboard"],
        "Jumlah": [1,1,1,1,1,1,1,"1 meter",1,"1 set","1 set",1,1,1,1]
    }
    st.dataframe(pd.DataFrame(hardware_data), use_container_width=True)

    test_data = {
        "Input Volume": [500,250,125,50,25,300,150,75,37.5,18.75],
        "Input Waktu": [60,30,15,6,3,136,68,34,17,8.5],
        "Output Volume": [498,248,124.5,49.8,24.9,299.2,149.6,74.8,37.4,18.7],
        "Output Waktu": [60,30,15,6,3,136,68,34,17,8.5],
        "Laju": [8.3,8.3,8.3,8.3,8.3,2.2,2.2,2.2,2.2,2.2]
    }
    st.dataframe(pd.DataFrame(test_data), use_container_width=True)

# -------------------------------------------------------
# VIDEO DEMO
# -------------------------------------------------------
elif menu == "Video Demonstrasi":
    st.markdown("<h2 class='title fade-in'>4. Video Demonstrasi</h2>", unsafe_allow_html=True)
    link = st.text_input("Masukkan link video:")
    if link:
        st.video(link)

# -------------------------------------------------------
# BIODATA TIM
# -------------------------------------------------------
elif menu == "Biodata Tim":
    st.markdown("<h2 class='title fade-in'>5. Biodata Tim & Pembimbing</h2>", unsafe_allow_html=True)
    st.markdown("<div class='card fade-in'><b>Dila Fadilatu Nisa</b><br><b>Angela Bertha Miady Torie</b></div>", unsafe_allow_html=True)

# -------------------------------------------------------
# FOOTER
# -------------------------------------------------------
st.write("---")
st.markdown("<p style='text-align:center;'>Website ini dirancang untuk memenuhi MK Perancangan Sistem Biomedis II</p>", unsafe_allow_html=True)
