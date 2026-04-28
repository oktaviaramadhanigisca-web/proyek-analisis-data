# Bike Sharing Analysis Dashboard ✨

## Deskripsi
Proyek ini merupakan dashboard interaktif hasil analisis data pada Bike Sharing Dataset. Dashboard ini memberikan informasi mengenai tren penyewaan sepeda berdasarkan kondisi cuaca, waktu, serta perbandingan antara pengguna Casual dan Registered.

## Struktur Direktori
- `dashboard/`: Berisi file dashboard utama (`dashboard.py`) dan dataset yang telah dibersihkan (`day.csv`).
- `data/`: Berisi dataset mentah original.
- `notebook.ipynb`: Dokumentasi lengkap proses Data Wrangling, EDA, hingga Visualisasi.
- `requirements.txt`: Daftar library Python yang dibutuhkan.
- `url.txt`: Tautan menuju dashboard yang telah dideploy (jika ada).

## Setup Environment - Shell/Terminal
Ikuti langkah-langkah berikut untuk menyiapkan lingkungan kerja di komputer Anda:

1. **Buat Virtual Environment:**
   ```powershell
   python -m venv v_env
   ```
2. **Aktifkan Virtual Environment:**  
   Windows (PowerShell): Jika muncul error `Scripts is disabled`, jalankan perintah ini terlebih dahulu:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
   ```
   Lalu aktifkan dengan:
   ```powershell
   .\v_env\Scripts\activate
   ```
3. **Install Library yang Dibutuhkan:**
   ```powershell
   pip install -r requirements.txt
   ```
## **Run Streamlit App**
```powershell
python -m streamlit run dashboard/dashboard.py
```



