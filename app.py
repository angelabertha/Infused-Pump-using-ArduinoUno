import streamlit as st
import pandas as pd

# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------
st.set_page_config(
    page_title="INFUSED PUMP BERBASIS ARDUINO UNO",
    page_icon="💉",
    layout="wide",
)

# -------------------------------------------------------
# SIDEBAR MENU
# -------------------------------------------------------
menu = st.sidebar.selectbox(
    "📌 Pilih Halaman",
    [
        "Beranda",
        "Deskripsi Produk",
        "Perakitan & Pengujian",
        "Video Demonstrasi",
        "Biodata Tim",
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 Proyek MK Perancangan Sistem Biomedis II")

# -------------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------------
page_style = r"""
<style>
body {
    background: linear-gradient(135deg, #e3f2fd, #e8eaf6);
    font-family: 'Segoe UI', sans-serif;
}

.title {
    color: #0d47a1;
    font-weight: 700;
}

.subtitle {
    color: #1565c0;
    font-weight: 600;
}

.card {
    background: #ffffff !important;
    padding: 22px;
    border-radius: 16px;
    box-shadow: 0 6px 14px rgba(0,0,0,0.12);
    margin-bottom: 20px;
}

.card * {
    color: #0d0d0d !important;
}

.badge {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 20px;
    background: #e3f2fd;
    color: #0d47a1;
    font-size: 13px;
    margin-right: 6px;
}

code {
    background-color: #f4f6f8;
    padding: 6px 10px;
    border-radius: 8px;
}
</style>
"""
st.markdown(page_style, unsafe_allow_html=True)

# -------------------------------------------------------
# BERANDA
# -------------------------------------------------------
if menu == "Beranda":

    st.markdown("<h1 class='title'>INFUSED PUMP BERBASIS ARDUINO UNO</h1>", unsafe_allow_html=True)
    st.markdown("<span class='badge'>Biomedical Engineering</span><span class='badge'>Arduino</span><span class='badge'>Infusion Control</span>", unsafe_allow_html=True)

    col1, col2 = st.columns([1.1, 1])

    with col1:
        st.image("infusepump.png", caption="Prototype Infuse Pump Otomatis", use_column_width=True)

    with col2:
        st.markdown(
            """
            <div class='card'>
            <b>Latar Belakang</b><br><br>
            Pemberian cairan infus merupakan salah satu tindakan medis yang membutuhkan ketelitian tinggi,
            khususnya dalam pengaturan laju aliran dan waktu pemberian cairan. Kesalahan dalam pengaturan
            laju infus dapat berdampak pada ketidakseimbangan cairan tubuh pasien dan berpotensi menimbulkan
            risiko kesehatan.
            <br><br>
            Oleh karena itu, diperlukan suatu sistem yang mampu mengatur dan memantau proses pemberian infus
            secara akurat, konsisten, dan mudah dioperasikan.
            <br><br>
            Proyek ini bertujuan untuk merancang dan mengimplementasikan sistem <b>infuse pump otomatis berbasis
            mikrokontroler Arduino Uno</b> yang dilengkapi dengan keypad sebagai media input, LCD sebagai
            tampilan informasi, serta motor DC dengan driver L298N sebagai aktuator penggerak aliran cairan,
            sehingga diharapkan dapat meningkatkan ketepatan dan keandalan pengaturan laju infus.
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
        Pengguna memasukkan durasi dan volume melalui keypad 4×4, kemudian pompa peristaltik akan
        mengalirkan cairan infus secara otomatis sesuai parameter yang ditentukan.
        <br><br>
        <b>Keunggulan Sistem:</b>
        <ul>
            <li>⏱ Akurasi waktu 100%</li>
            <li>💧 Deviasi volume rendah (±0,2–0,4%)</li>
            <li>🔔 Alarm tepat waktu 100%</li>
            <li>🚀 Laju aliran stabil: 8,3 mL/menit & 2,2 mL/menit</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<h3 class='subtitle'>Sistem Kerja</h3>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class='card'>
        Sistem infus pump otomatis ini dirancang untuk mengatur laju dan durasi pengaliran cairan infus
        secara terkontrol menggunakan mikrokontroler Arduino. Sistem menerima masukan berupa volume cairan
        (mL) dan waktu pemberian infus (menit) melalui keypad 4×4, kemudian mengendalikan motor DC menggunakan
        driver L298N.
        <br><br>
        Pada tahap inisialisasi (<i>setup()</i>), LCD I2C 16×2 diaktifkan sebagai media tampilan, pin motor
        driver disiapkan sebagai output, dan buzzer dikonfigurasi sebagai alarm. Arah putaran motor diatur
        satu arah untuk mendorong mekanisme infus.
        <br><br>
        Setelah pengguna memasukkan volume dan waktu, sistem menghitung laju aliran (mL/menit) dan
        mengonversinya menjadi sinyal PWM menggunakan fungsi <i>map()</i>. PWM ini mengatur kecepatan motor DC
        sehingga debit aliran sesuai parameter.
        <br><br>
        Selama proses infus, LCD menampilkan sisa waktu dan laju aliran secara real-time. Buzzer akan aktif
        saat sisa waktu ≤ 60 detik sebagai peringatan. Tombol <b>C</b> berfungsi sebagai STOP darurat dan
        tombol <b>D</b> sebagai RESET sistem. Setelah waktu habis, motor berhenti otomatis dan sistem kembali
        ke menu awal.
        </div>
        """,
        unsafe_allow_html=True,
    )

# -------------------------------------------------------
# PERAKITAN & PENGUJIAN
# -------------------------------------------------------
elif menu == "Perakitan & Pengujian":

    st.markdown("<h2 class='title'>2. Perakitan & Pengujian</h2>", unsafe_allow_html=True)

    alur_url = "https://raw.githubusercontent.com/angelabertha/Infused-Pump-using-ArduinoUno/main/alur.png"
    st.image(alur_url, caption="Diagram Alur Sistem", use_column_width=True)

    st.markdown("<h3 class='subtitle'>Hardware</h3>", unsafe_allow_html=True)

    hardware_data = {
        "No": list(range(1, 16)),
        "Nama Barang": [
            "Arduino Uno", "Peristaltic Pump", "Motor Driver (L298N)", "LCD 16×2",
            "Keypad 4×4", "Sensor Berat", "Buzzer", "Selang kecil",
            "Power Supply 12V", "Kabel Jumper", "Resistor", "Kotak Akrilik",
            "Lem", "Timah", "Breadboard"
        ],
        "Jumlah": [
            "1", "1", "1", "1", "1", "1", "1", "1 meter",
            "1", "1 set", "1 set", "1", "1", "1", "1"
        ]
    }

    df_hardware = pd.DataFrame(hardware_data)
    st.dataframe(df_hardware, use_container_width=True)

    st.markdown("<h3 class='subtitle'>Software</h3>", unsafe_allow_html=True)
    st.markdown("<div class='card'>Arduino IDE</div>", unsafe_allow_html=True)

    st.markdown("<h3 class='subtitle'>Program Arduino</h3>", unsafe_allow_html=True)
    st.code(open("pasted.txt").read(), language="cpp")

    st.markdown("<h3 class='subtitle'>Hasil Pengujian</h3>", unsafe_allow_html=True)

    pengujian_data = {
        "No": list(range(1, 11)),
        "Input Volume (mL)": [500, 250, 125, 50, 25, 300, 150, 75, 37.5, 18.75],
        "Input Waktu (menit)": [60, 30, 15, 6, 3, 136, 68, 34, 17, 8.5],
        "Output Volume (mL)": [498, 248, 124.5, 49.8, 24.9, 299.2, 149.6, 74.8, 37.4, 18.7],
        "Output Waktu (menit)": [60, 30, 15, 6, 3, 136, 68, 34, 17, 8.5],
        "Laju Aliran (mL/menit)": [8.3, 8.3, 8.3, 8.3, 8.3, 2.2, 2.2, 2.2, 2.2, 2.2]
    }

    df_test = pd.DataFrame(pengujian_data)
    st.dataframe(df_test, use_container_width=True)

    st.markdown(
        """
        <div class='card'>
        Berdasarkan hasil pengujian, sistem infus pump otomatis menunjukkan kinerja yang stabil dan
        konsisten. Sistem mampu mempertahankan dua mode laju aliran (±8,3 mL/menit dan ±2,2 mL/menit)
        meskipun input volume dan waktu divariasikan. Selisih volume input dan output relatif kecil
        (< 1 mL) dan masih berada dalam batas toleransi prototipe.
        <br><br>
        Hal ini membuktikan bahwa metode pengendalian motor DC berbasis PWM bekerja secara efektif dan
        sistem memiliki potensi sebagai alat bantu pengaturan laju infus yang terkontrol.
        </div>
        """,
        unsafe_allow_html=True,
    )

# -------------------------------------------------------
# VIDEO DEMONSTRASI
# -------------------------------------------------------
elif menu == "Video Demonstrasi":

    st.markdown("<h2 class='title'>3. Video Demonstrasi</h2>", unsafe_allow_html=True)

    video_link = "https://drive.google.com/file/d/1LfszewNma00GHxid5a17z2UtKCeK_boo/view?usp=sharing"

    st.markdown(
        f"""
        <div class='card'>
        <a href="{video_link}" target="_blank" style="text-decoration:none; font-weight:600;">
        ▶ Klik untuk menonton video demonstrasi alat
        </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

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
    "<p style='text-align:center; font-size:14px;'>Website ini dirancang untuk memenuhi MK Perancangan Sistem Biomedis II</p>",
    unsafe_allow_html=True,
)
