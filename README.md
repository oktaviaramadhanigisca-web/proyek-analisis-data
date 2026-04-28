# Bike Sharing Analysis Dashboard ✨

## Deskripsi
Proyek ini bertujuan untuk menganalisis data pada Bike Sharing Dataset. Dashboard ini memberikan informasi mengenai tren penyewaan sepeda berdasarkan kondisi cuaca dan waktu.

## Struktur Direktori
- `dashboard/`: Berisi file dashboard utama dan data yang telah dibersihkan.
- `data/`: Berisi dataset mentah (day.csv & hour.csv).
- `notebook.ipynb`: Dokumentasi lengkap proses Data Wrangling, EDA, hingga Visualisasi.
- `requirements.txt`: Daftar library Python yang dibutuhkan.
- `url.txt`: Tautan menuju dashboard yang telah dideploy.

## Setup Environment - Shell/Terminal
1. Pastikan Anda memiliki Python terinstal.
2. Buka terminal (di VS Code atau terminal lainnya).
3. Jalankan perintah berikut:
```bash
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt

## Run Streamlit App
streamlit run dashboard


