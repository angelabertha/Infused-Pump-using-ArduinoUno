<think>
Pertama, pengguna ingin memperbaiki website Streamlit mereka. Kode asli sudah ada, dan saya perlu menambahkan konten sesuai permintaan.


## Addressing User Request  
- The user wants to enhance their Streamlit website with new content based on existing code.  
- The main request is to add text about a "pember" on the homepage.  
- Need to integrate this addition smoothly without altering the original functionality.
</think>```python
import streamlit as st

# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------
st.set_page_config(
    page_title="INFUSED PUMP BERBASIS ARDUINO UNO",
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

/* Table Styling */
.table-container {
    overflow-x: auto;
    margin-bottom: 20px;
}

table {
    width: 100%;
    border-collapse: collapse;
    background: #ffffff;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

th, td {
    padding: 12px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}

th {
    background-color: #f2f2f2;
    color: #0d47a1;
    font-weight: bold;
}

tr:hover {
    background-color: #f9f9f9;
}

/* Code Block Styling */
.code-block {
    background: #f4f4f4;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 15px;
    font-family: 'Courier New', monospace;
    font-size: 14px;
    overflow-x: auto;
    margin-bottom: 20px;
}
</style>
"""
st.markdown(page_style, unsafe_allow_html=True)

# -------------------------------------------------------
# BERANDA
# -------------------------------------------------------
if menu == "Beranda":

    st.markdown("<h1 class='title'>INFUSED PUMP BERBASIS ARDUINO UNO</h1>", unsafe_allow_html=True)

    # --- FIX GAMBAR: Panggil langsung file lokal ---
    st.image("infusepump.png", caption="Infuse Pump", use_column_width=True)

    st.markdown(
        """
        <div class='card'>
        <p>Pemberian cairan infus merupakan salah satu tindakan medis yang membutuhkan ketelitian tinggi, khususnya dalam pengaturan laju aliran dan waktu pemberian cairan. Kesalahan dalam pengaturan laju infus dapat berdampak pada ketidakseimbangan cairan tubuh pasien dan berpotensi menimbulkan risiko kesehatan. Oleh karena itu, diperlukan suatu sistem yang mampu mengatur dan memantau proses pemberian infus secara akurat, konsisten, dan mudah dioperasikan. Proyek ini bertujuan untuk merancang dan mengimplementasikan sistem infus pump otomatis berbasis mikrokontroler Arduino yang dilengkapi dengan keypad sebagai media input, LCD sebagai tampilan informasi, serta motor DC dengan driver L298N sebagai aktuator penggerak aliran cairan, sehingga diharapkan dapat membantu meningkatkan ketepatan dan keandalan pengaturan laju infus.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class='card'>
        Selamat datang! 
        Gunakan menu di sebelah kiri untuk melihat deskripsi produk,
        perakitan & pengujian, video demonstrasi, dan biodata tim kami!
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

    st.markdown("<h3 class='title'>Sistem Kerja</h3>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class='card'>
        Sistem infus pump otomatis ini dirancang untuk mengatur laju dan durasi pengaliran cairan infus secara terkontrol menggunakan mikrokontroler Arduino. Sistem bekerja dengan menerima masukan berupa volume cairan (dalam mL) dan waktu pemberian infus (dalam menit) melalui keypad 4×4, kemudian mengendalikan motor DC menggunakan driver L298N untuk mengalirkan cairan sesuai parameter yang telah ditentukan.<br><br>
        Pada tahap awal, sistem diinisialisasi melalui fungsi setup(). Pada bagian ini, LCD I2C 16×2 diaktifkan sebagai media tampilan, pin-pin motor driver L298N diatur sebagai keluaran, serta buzzer disiapkan sebagai alarm. Arah putaran motor ditentukan dengan memberikan logika HIGH dan LOW pada pin IN1 dan IN2 sehingga motor berputar satu arah untuk mendorong mekanisme infus. Setelah inisialisasi selesai, sistem langsung masuk ke menu input parameter. Pengguna memasukkan volume cairan infus dalam satuan mililiter melalui keypad. Angka yang ditekan akan ditampilkan secara langsung pada baris kedua LCD sebagai umpan balik visual. Tombol # digunakan untuk mengonfirmasi input, sedangkan tombol * berfungsi untuk menghapus angka yang telah dimasukkan. Setelah volume ditentukan, sistem meminta input waktu infus dalam satuan menit dengan mekanisme input yang sama.<br><br>
        Setelah volume dan waktu dimasukkan, mikrokontroler menghitung laju aliran cairan dalam satuan mL per menit. Nilai laju aliran ini kemudian dikonversi menjadi sinyal PWM (Pulse Width Modulation) yang sesuai menggunakan fungsi map(). PWM ini digunakan untuk mengatur kecepatan motor DC, sehingga semakin besar laju infus yang diinginkan, semakin tinggi nilai PWM yang diberikan ke pin ENA pada driver L298N. Ketika proses infus dimulai, sistem mencatat waktu awal menggunakan fungsi millis() sebagai acuan penghitungan durasi kerja. Motor DC kemudian dijalankan secara kontinu dengan kecepatan yang telah ditentukan. Selama sistem berjalan, LCD menampilkan sisa waktu infus dalam satuan detik serta estimasi laju aliran cairan dalam mL per menit, sehingga pengguna dapat memantau proses infus secara real-time. Sistem juga dilengkapi dengan fitur peringatan menggunakan buzzer. Ketika sisa waktu infus kurang dari atau sama dengan 60 detik, buzzer akan aktif sebagai tanda bahwa proses infus akan segera selesai. Jika sisa waktu masih lebih dari 60 detik, buzzer akan dimatikan secara otomatis. Fitur ini bertujuan untuk meningkatkan keselamatan dan kewaspadaan pengguna.<br><br>
        Selain itu, sistem menyediakan kontrol manual untuk kondisi darurat. Tombol C pada keypad berfungsi sebagai tombol STOP untuk menghentikan proses infus secara langsung, sedangkan tombol D digunakan sebagai tombol RESET untuk mengulang sistem ke kondisi awal. Ketika salah satu tombol ini ditekan, motor akan dihentikan, buzzer dimatikan, dan sistem kembali ke menu input. Proses infus akan berhenti secara otomatis ketika waktu yang telah ditentukan habis. Pada kondisi ini, motor DC dimatikan sepenuhnya, LCD menampilkan pesan bahwa infus telah selesai, dan sistem menunggu beberapa detik sebelum kembali ke menu awal. Dengan mekanisme ini, sistem mampu bekerja secara otomatis, terkontrol, dan memberikan notifikasi yang jelas kepada pengguna selama proses infus berlangsung.
        </div>
        """,
        unsafe_allow_html=True,
    )


# -------------------------------------------------------
# PERAKITAN & PENGUJIAN
# -------------------------------------------------------
elif menu == "Perakitan & Pengujian":

    st.markdown("<h2 class='title'>2. Perakitan & Pengujian</h2>", unsafe_allow_html=True)

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

    st.markdown("<h3 class='title'>Hardware & Software</h3>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class='card'>
        <b>Hardware:</b><br>
        Berikut adalah daftar komponen yang digunakan dalam perakitan sistem infus pump.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Tabel Hardware
    hardware_data = {
        "No": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        "Nama Barang": ["Arduino Uno", "Peristaltic Pump", "Motor Driver (L298N)", "LCD 16×2", "Keypad 4×4", "Sensor Berat", "Buzzer", "Selang kecil", "Power Supply 12V", "Kabel Jumper", "Resistor", "Kotak Akrilik (Box)", "Lem", "Timah", "Breadboard"],
        "Jumlah": [1, 1, 1, 1, 1, 1, 1, "1 meter", 1, "1 set", "1 set", 1, 1, 1, 1]
    }
    st.markdown("<div class='table-container'>", unsafe_allow_html=True)
    st.table(hardware_data)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class='card'>
        <b>Software:</b><br>
        Sistem ini menggunakan Arduino IDE untuk pemrograman. Berikut adalah kode program yang dapat Anda salin dan gunakan.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Kode Arduino
    arduino_code = """
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
byte rowPins[ROWS] = {4, 5, 6, 7};      // Hubungkan ke baris keypad
byte colPins[COLS] = {8, 9, 10, 11};    // Hubungkan ke kolom keypad
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

    // Tampilkan sisa waktu dan laju cairan
    lcd.setCursor(0, 0);
    lcd.print("Sisa: ");
    lcd.print(remainingTime);
    lcd.print(" s   ");

    float flowRate = map(pwmSpeed, 28, 230, 220, 860) / 100.0; // mL/menit
    lcd.setCursor(0, 1);
    lcd.print("Laju: ");
    lcd.print(flowRate, 1);
    lcd.print(" ml/mnt ");

    // Debug Serial Monitor
    Serial.print("PWM: ");
    Serial.print(pwmSpeed);
    Serial.print(" | Sisa: ");
    Serial.print(remainingTime);
    Serial.print(" s | Laju: ");
    Serial.print(flowRate);
    Serial.println(" ml/mnt");

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

  // Hitung mL per menit dan konversi ke PWM
  int target_mL_per_min = targetVolume / targetTime;
  pwmSpeed = map(target_mL_per_min * 10, 22, 86, 28, 230); // Skala 10x untuk presisi
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
    st.code(arduino_code, language='cpp')

    st.markdown("<h3 class='title'>Hasil Pengujian</h3>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class='card'>
        Berikut adalah hasil pengujian sistem infus pump dengan variasi input volume dan waktu.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Tabel Hasil Pengujian
    pengujian_data = {
        "No": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "Input Volume (mL)": [500, 250, 125, 50
