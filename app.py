import streamlit as st

# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------
st.set_page_config(
    page_title="Infused Pump – Arduino Uno",
    layout="wide",
    page_icon="💉",
)

# -------------------------------------------------------
# SIDEBAR MENU
# -------------------------------------------------------
menu = st.sidebar.selectbox(
    "📌 Pilih Halaman",
    [
        "Beranda",
        "Deskripsi Produk",
        "Proses Pembuatan",
        "Video Demonstrasi",
        "Biodata Tim",
    ]
)

# -------------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------------
page_style = r"""
<style>
body {
    background: linear-gradient(135deg, #e3f2fd, #e8eaf6);
    font-family: 'Segoe UI', sans-serif;
}

.card {
    background: #fff;
    padding: 20px;
    border-radius: 14px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

.title {
    color: #0d47a1;
    font-weight: bold;
}

</style>
"""
st.markdown(page_style, unsafe_allow_html=True)

# -------------------------------------------------------
# HALAMAN: BERANDA
# -------------------------------------------------------
if menu == "Beranda":
    st.markdown("<h1 class='title'>💉 Infused Pump Berbasis Arduino Uno</h1>", unsafe_allow_html=True)

    # ---- Gambar judul dari GitHub ----
    infuse_url = "https://raw.githubusercontent.com/USERNAME/REPO/main/infusepump.png"
    st.image(infuse_url, caption="Prototype Infused Pump", use_column_width=True)

    st.write("Selamat datang! Pilih menu di sebelah kiri untuk melihat informasi lengkap mengenai produk infused pump.")

    st.markdown(
        """
        <div class='card'>
        Sistem infused pump ini dibuat dengan tujuan menyediakan alat pemantauan infus otomatis 
        yang murah, sederhana, dan akurat, menggunakan Arduino Uno.
        </div>
        """,
        unsafe_allow_html=True,
    )

# -------------------------------------------------------
# HALAMAN: DESKRIPSI PRODUK
# -------------------------------------------------------
elif menu == "Deskripsi Produk":
    st.markdown("<h2 class='title'>1. Deskripsi Produk</h2>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class='card'>
        Infused pump berbasis Arduino Uno ini bekerja menggunakan metode <b>time-based control</b>.
        Pengguna memasukkan durasi melalui keypad 4×4, lalu pompa peristaltik akan mengalirkan cairan 
        secara otomatis dengan laju yang stabil.

        <br><br>
        <b>Keunggulan utama:</b>
        <ul>
            <li>⏱ Akurasi waktu: <b>100%</b></li>
            <li>💧 Deviasi volume: <b>0,2–0,4%</b></li>
            <li>🔔 Alarm real-time: <b>100% tepat waktu</b></li>
            <li>🚀 Dua mode aliran stabil: 8,3 mL/min & 2,2 mL/min</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -------------------------------------------------------
# HALAMAN: DOKUMENTASI PROSES
# -------------------------------------------------------
elif menu == "Proses Pembuatan Prototype":
    st.markdown("<h2 class='title'>2. Proses Pembuatan</h2>", unsafe_allow_html=True)

    # ---- Gambar alur dari GitHub ----
    alur_url = "https://raw.githubusercontent.com/USERNAME/REPO/main/alur.png"
    st.image(alur_url, caption="Diagram Alur Pembuatan Prototype", use_column_width=True)

    # ---- Penjelasan Tahapan ----
    st.markdown(
        """
        <div class='card'>
        <p><b>Tahapan pembuatan prototype infused pump meliputi proses berikut:</b></p>
        <ul>
            <li><b>Perancangan diagram blok</b> – menentukan alur kerja sistem mulai dari input keypad, pemrosesan Arduino, hingga output LCD, motor, dan buzzer.</li>
            <li><b>Pembuatan skematik rangkaian</b> – menyusun koneksi detail antar komponen seperti keypad, LCD I2C, motor driver L298N, pompa peristaltik, dan catu daya.</li>
            <li><b>Perakitan komponen</b> – merangkai seluruh modul pada casing akrilik agar ergonomis, stabil, dan aman digunakan.</li>
            <li><b>Pemrograman Arduino</b> – membuat logika timer, kontrol motor berbasis waktu, tampilan LCD real-time, serta alarm buzzer.</li>
            <li><b>Pengujian waktu, alarm, dan laju aliran</b> – mengevaluasi akurasi timer, kestabilan flow rate, dan respons alarm.</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -------------------------------------------------------
# HALAMAN: VIDEO DEMONSTRASI
# -------------------------------------------------------
elif menu == "Video Demonstrasi":
    st.markdown("<h2 class='title'>3. Video Demonstrasi</h2>", unsafe_allow_html=True)

    link = st.text_input("https://drive.google.com/drive/folders/16L5dx4bmIks9y16hYyNSFmjjDD5tTkvh?usp=sharing")

    if link:
        st.video(link)

# -------------------------------------------------------
# HALAMAN: BIODATA TIM
# -------------------------------------------------------
elif menu == "Biodata Tim":
    st.markdown("<h2 class='title'>4. Biodata Tim & Pembimbing</h2>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class='card'>
        <h4>👥 Anggota Tim</h4>
        <ul>
            <li><b>Dila Fadilatu Nisa</b> – Hardware & Sistem</li>
            <li><b>Angela Bertha Miady Torie</b> – Dokumentasi, Analisis, Website</li>
        </ul>

        <h4>🎓 Dosen Pembimbing</h4>
        <p>Isi nama dosen pembimbing di sini.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -------------------------------------------------------

# -------------------------------------------------------
# FOOTER
# -------------------------------------------------------
st.write("---")
st.markdown(
    "<p style='text-align:center; font-size:14px;'>Website ini dibuat untuk keperluan UAS Sistem Tertanam.</p>",
    unsafe_allow_html=True,
)
