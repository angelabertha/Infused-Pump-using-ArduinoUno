import streamlit as st

# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------
st.set_page_config(
    page_title="Infused Pump berbasis Arduino Uno",
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

/* Card Styling */
.card {
    background: #ffffff !important;
    padding: 20px;
    border-radius: 14px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

.card, .card * {
    color: #0d0d0d !important;
}

.title {
    color: #0d47a1;
    font-weight: bold;
}
</style>
"""
st.markdown(page_style, unsafe_allow_html=True)

# -------------------------------------------------------
# BERANDA
# -------------------------------------------------------
if menu == "Beranda":

    st.markdown("<h1 class='title'>💉 Infused Pump Berbasis Arduino Uno</h1>", unsafe_allow_html=True)

    # --- FIX GAMBAR: Panggil langsung file lokal ---
    st.image("infusepump.png", caption="Infuse Pump", use_column_width=True)

    st.markdown(
        """
        <div class='card'>
        Selamat datang! Gunakan menu di sebelah kiri untuk melihat deskripsi produk,
        proses pembuatan, video demonstrasi, dan biodata tim kami!
        </div>
        """,
        unsafe_allow_html=True,
    )


# -------------------------------------------------------
# DESKRIPSI PRODUK
# -------------------------------------------------------
elif menu == "Deskripsi Produk":

    st.markdown("<h2 class='title'>1. Deskripsi Produk</h2>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class='card'>
        Infused pump berbasis Arduino Uno bekerja menggunakan metode <b>time-based control</b>.
        Pengguna memasukkan durasi melalui keypad 4×4, lalu pompa peristaltik akan mengalirkan
        cairan infus secara otomatis.
        <br><br>
        <b>Keunggulan:</b>
        <ul>
            <li>⏱ Akurasi waktu 100%</li>
            <li>💧 Deviasi volume 0,2–0,4%</li>
            <li>🔔 Alarm tepat waktu 100%</li>
            <li>🚀 Laju aliran stabil: 8,3 mL/min & 2,2 mL/min</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )


# -------------------------------------------------------
# PROSES PEMBUATAN
# -------------------------------------------------------
elif menu == "Proses Pembuatan":

    st.markdown("<h2 class='title'>2. Proses Pembuatan</h2>", unsafe_allow_html=True)

    # --- FIX GAMBAR ALUR: gunakan raw GitHub (ganti USERNAME/REPO) ---
    alur_url = "https://raw.githubusercontent.com/angelabertha/Infused-Pump-using-ArduinoUno/main/alur.png"
    st.image(alur_url, caption="Diagram Alur Pembuatan", use_column_width=True)

    st.markdown(
        """
        <div class='card'>
        <b>Tahapan pembuatan:</b>
        <ul>
            <li>Perancangan diagram blok – menentukan alur kerja sistem dari input keypad hingga output.</li>
            <li>Penyusunan skematik rangkaian – koneksi modul keypad, LCD I2C, motor driver L298N, pompa, dan catu daya.</li>
            <li>Perakitan hardware – merangkai seluruh modul pada casing akrilik agar ergonomis dan stabil.</li>
            <li>Pemrograman Arduino – logika timer, kontrol motor, LCD real-time display, dan alarm buzzer.</li>
            <li>Pengujian performa – mengevaluasi akurasi timer, kestabilan flow rate, dan respons alarm.</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )


# -------------------------------------------------------
# VIDEO DEMO
# -------------------------------------------------------
elif menu == "Video Demonstrasi":

    st.markdown("<h2 class='title'>3. Video Demonstrasi</h2>", unsafe_allow_html=True)

    link = st.text_input("Tempelkan link video Google Drive:")

    if link:
        st.video(link)


# -------------------------------------------------------
# BIODATA TIM
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
        <p>I Gde Eka Dirgayussa, M.Si.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# -------------------------------------------------------
# FOOTER
# -------------------------------------------------------
st.write("---")
st.markdown(
    "<p style='text-align:center; font-size:14px;'>Website ini dirancang untuk keperluan UAS Sistem Tertanam.</p>",
    unsafe_allow_html=True,
)
