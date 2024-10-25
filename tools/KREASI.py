import streamlit as st
import time

# Judul aplikasi
st.title("Animasi Tulisan 'MARKOV' Bergerak")

# Menetapkan variabel untuk posisi teks
position = 0
direction = 1  # 1 untuk ke kanan, -1 untuk ke kiri
speed = 0.1  # Mengatur kecepatan pergerakan teks

# Membuat placeholder untuk menampilkan teks
text_placeholder = st.empty()

# Loop animasi untuk menggerakkan teks
while True:
    # Memperbarui posisi teks
    position += direction

    # Cek batas kanan dan kiri
    if position >= 50 or position <= 0:
        direction *= -1  # Ubah arah gerak

    # Menampilkan teks dengan posisi yang diperbarui
    text_placeholder.markdown(f"<h1 style='text-align: center; margin-left: {position}px;'>MARKOV</h1>", unsafe_allow_html=True)

    # Menunggu beberapa saat sebelum mengupdate posisi lagi
    time.sleep(speed)
