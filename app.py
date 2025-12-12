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
# CUSTOM PAGE STYLE
# -------------------------------------------------------
page_style = r"""
<style>
body {
    background: linear-gradient(135deg, #e3f2fd, #e8eaf6);
    font-family: 'Segoe UI', sans-serif;
}

.block-container {
    padding-top: 1rem;
}

h1, h2, h3 {
    color: #0d47a1;
}

.card {
    background: #fff;
    padding: 20px;
    border-radius: 14px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

.section-title {
    background: #1976d2;
    padding: 10px 18px;
    color: white;
    border-radius: 8px;
    font-size: 20px;
    margin-top: 20px;
}

</style>
"""
st.markdown(page_style, unsafe_allow_html=True)

# -------------------------------------------------------
# HEADER
# -------------------------------------------------------
st.markdown("<h1 style='text-align:center;'>💉 INFUSED PUMP – Arduino Uno</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color:#1e88e5;'>Sistem Alarm Pemantauan Waktu Infus Real-Time</h3>", unsafe_allow_html=True)
st.write("---")

# -------------------------------------------------------
# SECTION 1 — DESKRIPSI PRODUK
# -------------------------------------------------------
st.markdown("<div class='section-title'>1. Deskripsi Produk</div>", unsafe_allow_html=True)
st.markdown("""
<div class='card'>
Infused pump berbasis Arduino Uno ini dirancang sebagai solusi otomatis untuk memantau aliran cairan infus. 
Sistem bekerja menggunakan **time-based control**, di mana pengguna memasukkan durasi melalui keypad 4×4 dan motor 
peristaltik akan mengatur aliran cairan sesuai waktu yang ditentukan.

Sistem ini memadukan beberapa komponen utama:
- Arduino Uno  
- Motor DC + Driver L298N  
- Keypad 4×4  
- LCD I2C  
- Buzzer alarm  

Hasil pengujian menunjukkan:
- ⏱ Akurasi waktu: **100%**  
- 💧 Deviasi volume: **0,2–0,4%**  
- 🔔 Alarm: **100% tepat waktu**  
- 🚀 Dua mode aliran stabil: **8,3 mL/min** dan **2,2 mL/min**
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# SECTION 2 — Dokumentasi Proses Pembuatan
# -------------------------------------------------------
st.markdown("<div class='section-title'>2. Dokumentasi Proses Pembuatan</div>", unsafe_allow_html=True)

st.markdown("""
<div class='card'>
Tahapan pembuatan alat meliputi:
- Perancangan diagram blok sistem  
- Penyusunan skematik rangkaian  
- Perakitan komponen pada casing akrilik  
- Pemrograman Arduino  
- Pengujian waktu, alarm, dan stabilitas aliran  

Unggah dokumentasi (foto prototipe atau proses):
</div>
""", unsafe_allow_html=True)

img_files = st.file_uploader("Upload dokumentasi (boleh lebih dari 1 gambar)", accept_multiple_files=True)
if img_files:
    for f in img_files:
        st.image(f, caption=f.name)

# -------------------------------------------------------
# SECTION 3 — VIDEO DEMONSTRASI
# -------------------------------------------------------
st.markdown("<div class='section-title'>3. Video Demonstrasi Produk (1–5 menit)</div>", unsafe_allow_html=True)

video_url = st.text_input("Masukkan URL video (YouTube / Google Drive):")

if video_url:
    st.video(video_url)

# -------------------------------------------------------
# SECTION 4 — BIODATA TIM
# -------------------------------------------------------
st.markdown("<div class='section-title'>4. Biodata Anggota Tim & Dosen Pembimbing</div>", unsafe_allow_html=True)

st.markdown("""
<div class='card'>
<h4>👥 Anggota Tim</h4>
<ul>
<li><b>Dila Fadilatu Nisa</b> – Hardware & Sistem</li>
<li><b>Angela Bertha Miady Torie</b> – Dokumentasi, Analisis, Website</li>
</ul>

<h4>🎓 Dosen Pembimbing</h4>
<p>Masukkan nama dosen pembimbing di sini.</p>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# SECTION 5 — LINK REPOSITORY
# -------------------------------------------------------
st.markdown("<div class='section-title'>5. Link Repository</div>", unsafe_allow_html=True)

repo = st.text_input("Masukkan link repository GitHub (jika ada):")

if repo:
    st.markdown(f"<div class='card'>🔗 <b>Repository:</b> {repo}</div>", unsafe_allow_html=True)

# -------------------------------------------------------
# FOOTER
# -------------------------------------------------------
st.markdown("""
<hr>
<p style='text-align:center; color:#333; font-size:14px;'>
Website ini dibuat untuk keperluan UAS dan berisi publikasi produk Infused Pump berbasis Arduino Uno.
</p>
""", unsafe_allow_html=True)
