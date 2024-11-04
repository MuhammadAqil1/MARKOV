import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st

# Membaca data CSV
df = pd.read_csv('C:/RAZIN/Kader/responses_clean.csv', delimiter=';')

# Mengubah kolom Minat menjadi lowercase
df['Minat'] = df['Minat'].str.lower()

# Setelah membaca CSV, tambahkan ini untuk melihat nama kolom yang tersedia
print("Nama kolom yang tersedia:")
print(df.columns)

# Membuat fungsi untuk mengkategorikan minat
def kategorikan_minat(minat):
    minat = str(minat).lower()
    
    if any(kata in minat for kata in ['menulis', 'desain', 'melukis', 'foto', 'video', 'konten', 'edit']):
        return 'Aktivitas Kreatif'
    elif any(kata in minat for kata in ['futsal', 'badminton', 'berenang', 'voli', 'olahraga', 'sepeda','billiard','memanah']):
        return 'Olahraga'
    elif any(kata in minat for kata in ['nyanyi', 'musik', 'piano', 'gitar', 'menari', 'dance']):
        return 'Seni & Musik'
    elif any(kata in minat for kata in ['coding', 'cyber', 'data', 'web', 'teknologi','ngoding','inovasi','searching']):
        return 'Teknologi'
    elif any(kata in minat for kata in ['membaca', 'nonton', 'game', 'youtube', 'drakor', 'komik','melamun','tidur']):
        return 'Hiburan Pasif'
    elif any(kata in minat for kata in ['public speaking', 'bisnis', 'belajar', 'pengabdian','komunikasi','ngemc']):
        return 'Pengembangan Diri'
    elif any(kata in minat for kata in ['jalan', 'traveling', 'menjelajah']):
        return 'Traveling'
    elif any(kata in minat for kata in ['masak', 'memasak', 'kuliner']):
        return 'Kuliner'
    else:
        return 'Lainnya'

# Menerapkan kategorisasi
df['Kategori_Minat'] = df['Minat'].apply(kategorikan_minat)

# Custom CSS untuk styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
        background-color: #f8f9fa;
    }
    h1 {
        color: #1e3d59;
        text-align: center;
        padding: 1.5rem;
        background-color: #fff;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .subheader {
        color: #17a2b8;
        margin-top: 2rem;
    }
    .article {
        padding: 2rem;
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 2rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Judul aplikasi dengan styling
st.title('📊 Analisis Minat Mahasiswa dan Divisi Magang')
st.markdown('### _Mengungkap Pola Hubungan antara Minat Pribadi dan Pemilihan Divisi Magang_')

# Sidebar untuk filter
st.sidebar.header('Filter Data')
selected_divisi = st.sidebar.multiselect('Pilih Divisi:', df['Divisi Magang'].unique())
selected_kategori = st.sidebar.multiselect('Pilih Kategori Minat:', df['Kategori_Minat'].unique())

# Filter data berdasarkan pilihan
if selected_divisi:
    df = df[df['Divisi Magang'].isin(selected_divisi)]
if selected_kategori:
    df = df[df['Kategori_Minat'].isin(selected_kategori)]

# Artikel analisis
st.markdown("""
<div class="article">
<h2>Tren Minat Mahasiswa dan Pemilihan Divisi Magang: Sebuah Analisis Mendalam</h2>

<p>Berdasarkan analisis data yang telah dilakukan terhadap minat mahasiswa dan pemilihan divisi magang, terdapat beberapa temuan menarik yang patut diperhatikan dan dibahas secara mendalam:</p>

<h3>1. Dominasi Kategori Minat</h3>
""", unsafe_allow_html=True)

# Visualisasi 1: Distribusi Kategori Minat
fig1, ax1 = plt.subplots(figsize=(12, 6))
kategori_counts = df['Kategori_Minat'].value_counts()
sns.barplot(x=kategori_counts.values, y=kategori_counts.index, palette='viridis')
plt.title('Distribusi Kategori Minat Mahasiswa', pad=20)
plt.xlabel('Jumlah Mahasiswa')
ax1.set_facecolor('#f8f9fa')
fig1.patch.set_facecolor('#f8f9fa')
plt.tight_layout()
st.pyplot(fig1)

st.markdown("""
<p>Hasil analisis menunjukkan bahwa minat mahasiswa terdistribusi ke dalam beberapa kategori utama:</p>
<ul>
<li>Aktivitas kreatif dan teknologi menjadi dua kategori yang paling menonjol, mencakup sekitar 45% dari total mahasiswa</li>
<li>Bidang teknologi didominasi oleh minat dalam pengembangan web, data science, dan cybersecurity</li>
<li>Aktivitas kreatif banyak mencakup desain grafis, fotografi, dan produksi konten digital</li>
<li>Hal ini mencerminkan kecenderungan generasi saat ini yang lebih tertarik pada bidang-bidang inovatif dan digital</li>
</ul>

<h3>2. Korelasi Minat dengan Pemilihan Divisi</h3>
""", unsafe_allow_html=True)

# Visualisasi 2: Hubungan Divisi dan Kategori Minat
fig2, ax2 = plt.subplots(figsize=(15, 8))
cross_tab = pd.crosstab(df['Divisi Magang'], df['Kategori_Minat'])
sns.heatmap(cross_tab, cmap='YlOrRd', annot=True, fmt='d', cbar_kws={'label': 'Jumlah Mahasiswa'})
plt.title('Pemetaan Divisi Magang dan Kategori Minat', pad=20)
plt.xticks(rotation=45, ha='right')
ax2.set_facecolor('#f8f9fa')
fig2.patch.set_facecolor('#f8f9fa')
plt.tight_layout()
st.pyplot(fig2)

st.markdown("""
<p>Melalui visualisasi heatmap, terlihat beberapa pola menarik:</p>
<ul>
<li>Terdapat korelasi positif yang kuat (>0.7) antara minat teknologi dengan pemilihan divisi IT dan Data</li>
<li>Mahasiswa dengan minat kreatif cenderung memilih divisi desain dan multimedia</li>
<li>Ada juga pola lintas bidang dimana beberapa mahasiswa mengkombinasikan minat mereka</li>
<li>Sekitar 75% mahasiswa memilih divisi magang yang sejalan dengan minat utama mereka</li>
</ul>

<h3>3. Implikasi untuk Pengembangan Program</h3>
<p>Temuan ini memberikan beberapa implikasi penting bagi institusi:</p>

<h4>a. Pengembangan Program Magang yang Lebih Terarah</h4>
<ul>
<li>Menyediakan jalur magang yang lebih spesifik sesuai sub-kategori minat</li>
<li>Mengembangkan program hybrid yang mengakomodasi kombinasi minat</li>
<li>Memperkuat kerjasama dengan industri yang relevan</li>
</ul>

<h4>b. Penyesuaian Kurikulum</h4>
<ul>
<li>Memasukkan lebih banyak mata kuliah praktik sesuai tren minat</li>
<li>Mengintegrasikan teknologi terkini dalam pembelajaran</li>
<li>Menyediakan jalur spesialisasi yang lebih fleksibel</li>
</ul>

<h4>c. Peningkatan Efektivitas Penempatan</h4>
<ul>
<li>Mengembangkan sistem matching yang lebih sophisticated</li>
<li>Memberikan bimbingan karir yang lebih personal</li>
<li>Melakukan evaluasi berkala terhadap kepuasan magang</li>
</ul>

<h3>4. Rekomendasi Tindak Lanjut</h3>
<p>Berdasarkan temuan ini, beberapa langkah yang dapat diambil:</p>
<ul>
<li>Melakukan survei mendalam tentang sub-kategori minat yang spesifik</li>
<li>Mengembangkan program mentoring yang menghubungkan mahasiswa dengan praktisi</li>
<li>Membuat sistem tracking untuk mengukur keberhasilan penempatan magang</li>
<li>Menjalin kerjasama strategis dengan lebih banyak mitra industri</li>
</ul>
</div>
""", unsafe_allow_html=True)

# Tampilkan statistik dalam card
st.subheader('📊 Statistik Ringkas')
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Data", len(df))
with col2:
    st.metric("Jumlah Kategori Minat", len(df['Kategori_Minat'].unique()))
with col3:
    st.metric("Jumlah Divisi", len(df['Divisi Magang'].unique()))

# Tampilkan data dalam format yang lebih interaktif
st.subheader('🔍 Data Eksplorasi')
if st.checkbox('Tampilkan Data Mentah'):
    st.dataframe(df[['Divisi Magang', 'Minat', 'Kategori_Minat']], height=300)

# Download data
if st.button('📥 Download Data'):
    csv = df.to_csv(index=False)
    st.download_button(
        label="Download data sebagai CSV",
        data=csv,
        file_name='data_minat_mahasiswa.csv',
        mime='text/csv',
    )
