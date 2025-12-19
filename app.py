import streamlit as st
import pandas as pd
from PIL import Image

# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------
st.set_page_config(
    page_title="Infused Pump Otomatis | Arduino Uno",
    layout="wide",
)

# -------------------------------------------------------
# MODERN STARTUP STYLE CSS
# -------------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    body {
        background: linear-gradient(135deg, #e6dcff, #cbece0, #f9f9ff);
        background-size: 400% 400%;
        animation: gradientShift 12s ease infinite;
    }
    @keyframes gradientShift {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    .fade-in {
        animation: fadeIn 1s ease-in-out;
    }
    @keyframes fadeIn {
        0% {opacity: 0; transform: translateY(10px);} 
        100% {opacity: 1; transform: translateY(0);} 
    }

    .card {
        background: #ffffffdd;
        padding: 25px;
        border-radius: 16px;
        backdrop-filter: blur(10px);
        box-shadow: 0 6px 16px rgba(0,0,0,0.1);
        margin-bottom: 25px;
    }

    .title {
        color: #4f3aa7;
        font-weight: 700;
    }

    .subtitle {
        font-size: 18px;
        color: #444;
    }

    .hero {
        border-radius: 22px;
        overflow: hidden;
        margin-bottom: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True,
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

# -------------------------------------------------------
# BERANDA (HERO SECTION)
# -------------------------------------------------------
if menu == "Beranda":
    st.markdown("<h1 class='title fade-in'>Infused Pump Otomatis</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p class='subtitle fade-in'>Sistem infus otomatis berbasis Arduino dengan kontrol waktu presisi dan alarm real‑time.</p>",
        unsafe_allow_html=True,
    )

    st.markdown("<div class='hero fade-in'>", unsafe_allow_html=True)
    st.image("infusepump.png", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class='card fade-in'>
        <p>
        Pemberian cairan infus merupakan tindakan medis yang membutuhkan ketelitian tinggi, terutama dalam pengaturan 
        laju aliran dan waktu pemberian cairan. Kesalahan kecil dapat mengakibatkan ketidakseimbangan cairan tubuh dan 
        risiko kesehatan serius. <br><br>
        Untuk itu, dikembangkanlah <b>infused pump otomatis</b> berbasis Arduino yang mampu mengatur volume dan durasi
        infus secara akurat, stabil, dan mudah digunakan.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -------------------------------------------------------
# DESKRIPSI PRODUK
# -------------------------------------------------------
elif menu == "Deskripsi Produk":
    st.markdown("<h2 class='title fade-in'>Deskripsi Produk</h2>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class='card fade-in'>
        Infused pump berbasis Arduino Uno bekerja menggunakan pendekatan <b>time‑based control</b>.
        Pengguna memasukkan volume dan waktu, kemudian sistem menghitung laju infus dan mengendalikan motor DC melalui
        driver L298N agar cairan mengalir sesuai nilai yang ditentukan.
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<h3 class='title fade-in'>Sistem Kerja (Selengkapnya)</h3>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class='card fade-in'>
        Sistem menerima input volume (mL) dan waktu (menit) melalui keypad 4×4. Arduino menghitung laju infus, 
        mengubahnya ke PWM, dan mengendalikan motor DC. LCD 16×2 menampilkan sisa waktu dan laju aliran setiap detik.
        <br><br>
        Tombol <b>C</b> berfungsi sebagai STOP, sedangkan tombol <b>D</b> untuk RESET. Ketika waktu tersisa ≤ 60 detik, 
        buzzer akan aktif sebagai alarm peringatan. Setelah waktu habis, motor berhenti otomatis dan sistem kembali ke menu awal.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Arduino Code Block
    st.markdown("<h3 class='title fade-in'>Kode Program Arduino</h3>", unsafe_allow_html=True)

    arduino_code = r"""
#include <Keypad.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// LCD I2C
LiquidCrystal_I2C lcd(0x27, 16, 2);

// Motor Driver L298N
const int in1 = 12;
const int in2 = 13;
const int ena = 3; // PWM pin

// Buzzer
const int buzzerPin = A3;

// Keypad setup
const byte ROWS = 4;
const byte COLS = 4;
char keys[ROWS][COLS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},  // C = STOP
  {'*','0','#','D'}   // D = RESET
};
byte rowPins[ROWS] = {4, 5, 6, 7};
byte colPins[COLS] = {8, 9, 10, 11};
Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

// Variabel utama
int targetVolume = 0;
int targetTime = 0; // dalam menit
int pwmSpeed = 130;

unsigned long startTime;
bool running = false;
bool buzzerOn = false;

void setup() {
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();

  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(ena, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
  digitalWrite(buzzerPin, LOW);

  // Arah motor (maju)
  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);

  inputMenu();
}

void loop() {
  if (running) {
    char key = keypad.getKey();
    if (key == 'C') {
      stopSystem("STOP ditekan!");
      return;
    } else if (key == 'D') {
      stopSystem("RESET ditekan!");
      return;
    }

    unsigned long elapsed = (millis() - startTime) / 1000;
    int remainingTime = (targetTime * 60) - elapsed;

    if (remainingTime <= 60 && !buzzerOn && remainingTime > 0) {
      digitalWrite(buzzerPin, HIGH);
      buzzerOn = true;
    }

    if (remainingTime > 60) {
      digitalWrite(buzzerPin, LOW);
      buzzerOn = false;
    }

    analogWrite(ena, pwmSpeed); // Jalankan motor

    // Tampilkan sisa waktu
    lcd.setCursor(0, 0);
    lcd.print("Sisa: ");
    lcd.print(remainingTime);
    lcd.print(" s   ");

    float flowRate = map(pwmSpeed, 28, 230, 220, 860) / 100.0; // mL/menit
    lcd.setCursor(0, 1);
    lcd.print("Laju: ");
    lcd.print(flowRate, 1);
    lcd.print(" ml/mnt ");

    if (remainingTime <= 0) {
      stopSystem("Infus selesai!");
    }

    delay(1000);
  }
}

void inputMenu() {
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Volume (ml):");
  targetVolume = inputNumber();

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Waktu (mnt):");
  targetTime = inputNumber();

  int target_mL_per_min = targetVolume / targetTime;
  pwmSpeed = map(target_mL_per_min * 10, 22, 86, 28, 230);
  if (pwmSpeed < 28) pwmSpeed = 28;
  if (pwmSpeed > 230) pwmSpeed = 230;

  Serial.print("Target: ");
  Serial.print(target_mL_per_min);
  Serial.print(" mL/mnt | PWM: ");
  Serial.println(pwmSpeed);

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Mulai...");
  delay(1000);

  digitalWrite(buzzerPin, LOW);
  buzzerOn = false;
  startTime = millis();
  running = true;
}

int inputNumber() {
  String input = "";
  while (true) {
    char key = keypad.getKey();
    if (key) {
      if (key >= '0' && key <= '9') {
        input += key;
        lcd.setCursor(0, 1);
        lcd.print(input + "   ");
      } else if (key == '#') {
        if (input.length() > 0)
          return input.toInt();
      } else if (key == '*') {
        input = "";
        lcd.setCursor(0, 1);
        lcd.print("                ");
      }
    }
  }
}

void stopSystem(String message) {
  analogWrite(ena, 0);
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print(message);
  Serial.println(message);
  digitalWrite(buzzerPin, LOW);
  delay(3000);
  running = false;
  inputMenu();
}
"""


# -------------------------------------------------------
# PERAKITAN & PENGUJIAN
# -------------------------------------------------------
elif menu == "Perakitan & Pengujian":
    st.markdown("<h2 class='title fade-in'>Perakitan & Pengujian</h2>", unsafe_allow_html=True)

    # Hardware Table
    st.markdown("<h3 class='title fade-in'>Daftar Hardware</h3>", unsafe_allow_html=True)
    hardware_data = {
        'No': list(range(1,16)),
        'Nama Barang': ['Arduino Uno','Peristaltic Pump','Motor Driver (L298N)','LCD 16×2','Keypad 4×4','Sensor Berat','Buzzer','Selang kecil (1 meter)','Power Supply 12V','Kabel Jumper','Resistor','Kotak Akrilik','Lem','Timah','Breadboard'],
        'Jumlah': [1,1,1,1,1,1,1,'1 meter',1,'1 set','1 set',1,1,1,1]
    }
    st.dataframe(pd.DataFrame(hardware_data), use_container_width=True)

    # Software
    st.markdown("<h3 class='title fade-in'>Software yang Digunakan</h3>", unsafe_allow_html=True)
    st.markdown("<div class='card fade-in'><b>Arduino IDE</b> — digunakan untuk pemrograman mikrokontroler.</div>", unsafe_allow_html=True)

    # Hasil Pengujian
    st.markdown("<h3 class='title fade-in'>Hasil Pengujian</h3>", unsafe_allow_html=True)
    uji_data = {
        'No': list(range(1,11)),
        'Input Volume (mL)': [500,250,125,50,25,300,150,75,37.5,18.75],
        'Input Waktu (menit)': [60,30,15,6,3,136,68,34,17,8.5],
        'Output Volume (mL)': [498,248,124.5,49.8,24.9,299.2,149.6,74.8,37.4,18.7],
        'Output Waktu (menit)': [60,30,15,6,3,136,68,34,17,8.5],
        'Laju Aliran (mL/menit)': [8.3,8.3,8.3,8.3,8.3,2.2,2.2,2.2,2.2,2.2]
    }
    st.dataframe(pd.DataFrame(uji_data), use_container_width=True)

    # Analisis
    st.markdown("<h3 class='title fade-in'>Analisis Hasil Pengujian</h3>", unsafe_allow_html=True)
    st.markdown(
        "<div class='card fade-in'>Sistem menunjukkan performa stabil dengan dua laju utama: <b>8.3 mL/menit</b> dan <b>2.2 mL/menit</b>. Selisih volume kecil (&lt;1 mL) menandakan error mekanis minimal. Kontrol PWM efektif menjaga laju tetap konstan pada berbagai kondisi pengujian.</div>",
        unsafe_allow_html=True,
    )
