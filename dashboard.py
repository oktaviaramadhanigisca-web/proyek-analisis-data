import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page title
st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")

# 1. Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("day.csv")
    df['dteday'] = pd.to_datetime(df['dteday'])
    return df

day_df = load_data()

# Sidebar - Filter Tahun
st.sidebar.header("Filter Data")
year_option = st.sidebar.selectbox("Pilih Tahun:", [2011, 2012])
year_code = 0 if year_option == 2011 else 1

# Filter dataframe
main_df = day_df[day_df['yr'] == year_code]

# Header Utama
st.title("Bike Sharing Dashboard 🚲")
st.markdown(f"Menampilkan data penyewaan sepeda untuk tahun **{year_option}**")

# 2. Metric Cards (Ringkasan Angka)
col1, col2, col3 = st.columns(3)
with col1:
    total_rentals = main_df['cnt'].sum()
    st.metric("Total Penyewaan", value=f"{total_rentals:,}")
with col2:
    total_registered = main_df['registered'].sum()
    st.metric("Pengguna Terdaftar", value=f"{total_registered:,}")
with col3:
    total_casual = main_df['casual'].sum()
    st.metric("Pengguna Kasual", value=f"{total_casual:,}")

st.divider()

# 3. Visualisasi 1: Tren Bulanan
st.subheader("Tren Penyewaan Bulanan")
monthly_trend = main_df.groupby(main_df['dteday'].dt.strftime('%B'))[['casual', 'registered']].sum().reindex(
    ['January', 'February', 'March', 'April', 'May', 'June', 
     'July', 'August', 'September', 'October', 'November', 'December']
).reset_index()

fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(monthly_trend['dteday'], monthly_trend['casual'], marker='o', label='Casual', color='#72BCD4')
ax.plot(monthly_trend['dteday'], monthly_trend['registered'], marker='o', label='Registered', color='#D3DBE2')
ax.set_title(f"Tren Pengguna Casual vs Registered Tahun {year_option}", fontsize=15)
ax.legend()
plt.xticks(rotation=45)
st.pyplot(fig)

# 4. Visualisasi 2: Penyewaan Berdasarkan Cuaca
st.subheader("Pengaruh Cuaca Terhadap Penyewaan")
weather_rentals = main_df.groupby('weathersit')['cnt'].mean().reset_index()
weather_rentals['weathersit'] = weather_rentals['weathersit'].map({
    1: 'Cerah', 2: 'Mendung', 3: 'Hujan Ringan', 4: 'Hujan Lebat'
})

fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.barplot(data=weather_rentals, x='weathersit', y='cnt', palette='viridis', ax=ax2)
ax2.set_ylabel("Rata-rata Penyewaan")
ax2.set_xlabel("Kondisi Cuaca")
st.pyplot(fig2)

st.caption(f"Copyright © {year_option} - Bike Sharing Analysis")