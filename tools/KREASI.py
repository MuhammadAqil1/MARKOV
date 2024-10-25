import streamlit as st
import time

# Menentukan teks yang akan ditampilkan sebagai running text
text = "MARKOVV KERENNNN "
speed = 0.2  # Kecepatan perpindahan teks dalam detik

# Menampilkan judul di aplikasi Streamlit
st.title("Running Text")

# Loop untuk menggerakkan teks
while True:
    for i in range(len(text)):
        # Menampilkan teks yang diatur menjadi running text
        st.write(text[i:] + text[:i])
        
        # Delay untuk membuat efek pergerakan
        time.sleep(speed)
        
        # Mengosongkan tampilan agar teks bergerak
        st.empty()
