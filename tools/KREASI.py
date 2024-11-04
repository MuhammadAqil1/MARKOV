import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Judul aplikasi
st.title("Visualisasi Data Science Interaktif")

# Membuat data sampel
@st.cache_data
def generate_data():
    np.random.seed(42)
    dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='W')
    data = pd.DataFrame({
        'Tanggal': dates,
        'Penjualan': np.random.randint(100, 1000, size=len(dates)),
        'Pengunjung': np.random.randint(500, 5000, size=len(dates)),
        'Kategori': np.random.choice(['A', 'B', 'C'], size=len(dates))
    })
    return data

data = generate_data()

# Sidebar untuk pemilihan visualisasi
visualization = st.sidebar.selectbox(
    "Pilih Visualisasi",
    ["Tren Penjualan Sepanjang Tahun (Mingguan)", "Korelasi Penjualan vs Pengunjung (Harian)", "Distribusi Penjualan per Kategori (Boxplot)"]
)

# Visualisasi berdasarkan pilihan
if visualization == "Tren Penjualan Sepanjang Tahun (Mingguan)":
    st.subheader("Tren Penjualan Sepanjang Tahun")
    fig, ax = plt.subplots(figsize=(12, 6), dpi = 200)
    sns.lineplot(data=data, x='Tanggal', y='Penjualan', ax=ax)
    ax.set_xlabel("Tanggal")
    ax.set_ylabel("Penjualan")
    st.pyplot(fig)

elif visualization == "Korelasi Penjualan vs Pengunjung (Harian)":
    st.subheader("Korelasi antara Penjualan dan Jumlah Pengunjung")
    
    # Membuat data harian
    data_harian = generate_data().resample('D').interpolate()
    
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.scatterplot(data=data_harian, x='Pengunjung', y='Penjualan', hue='Kategori', ax=ax)
    ax.set_xlabel("Jumlah Pengunjung")
    ax.set_ylabel("Penjualan")
    st.pyplot(fig)

else:
    st.subheader("Distribusi Penjualan per Kategori")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=data, x='Kategori', y='Penjualan', ax=ax)
    ax.set_xlabel("Kategori")
    ax.set_ylabel("Penjualan")
    st.pyplot(fig)

# Menampilkan data mentah
if st.checkbox("Tampilkan Data Mentah"):
    st.write(data)

# Statistik deskriptif
if st.checkbox("Tampilkan Statistik Deskriptif"):
    st.write(data.describe())

# Tombol untuk mengunduh data
if st.button("Unduh Data CSV"):
    csv = data.to_csv(index=False)
    st.download_button(
        label="Klik untuk mengunduh",
        data=csv,
        file_name="data_penjualan.csv",
        mime="text/csv",
    )
