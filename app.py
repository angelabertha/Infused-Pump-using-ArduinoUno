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
        "Dokumentasi Proses",
        "Video Demonstrasi",
        "Biodata Tim",
        "Repository",
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
elif menu == "Dokumentasi Proses":
    st.markdown("<h2 class='title'>2. Dokumentasi Proses Pembuatan</h2>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class='card'>
        Tahapan pembuatan alat meliputi:
        <ul>
            <li>Perancangan diagram blok</li>
            <li>Pembuatan skematik rangkaian</li>
            <li>Perakitan komponen</li>
            <li>Pemrograman Arduino</li>
            <li>Pengujian waktu, alarm, dan laju aliran</li>
        </ul>
        Unggah foto dokumentasi di bawah:
        </div>
        """,
        unsafe_allow_html=True,
    )

    imgs = st.file_uploader("Upload dokumentasi (boleh lebih dari 1)", accept_multiple_files=True)
    if imgs:
        for img in imgs:
            st.image(img, caption=img.name)

# -------------------------------------------------------
# HALAMAN: VIDEO DEMONSTRASI
# -------------------------------------------------------
elif menu == "Video Demonstrasi":
    st.markdown("<h2 class='title'>3. Video Demonstrasi</h2>", unsafe_allow_html=True)

    link = st.text_input("Masukkan link video (YouTube / Google Drive):")

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
# HALAMAN: REPOSITORY
# -------------------------------------------------------
elif menu == "Repository":
    st.markdown("<h2 class='title'>5. Repository</h2>", unsafe_allow_html=True)

    repo = st.text_input("Masukkan link repository GitHub:")

    if repo:
        st.markdown(f"<div class='card'>🔗 <b>Repository:</b> {repo}</div>", unsafe_allow_html=True)

# -------------------------------------------------------
# FOOTER
# -------------------------------------------------------
st.write("---")
st.markdown(
    "<p style='text-align:center; font-size:14px;'>Website ini dibuat untuk keperluan UAS Sistem Tertanam.</p>",
    unsafe_allow_html=True,
)
