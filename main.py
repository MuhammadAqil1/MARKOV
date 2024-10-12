import streamlit as st

# session state agar ketika pindah page tidak berubah data yang tersedia

st.session_state.pindah = True

Homepage = st.Page("Halaman Utama/halaman_utama.py",
    title=" Profil Kelompok",
    default=True)

Mahasiswa1 = st.Page(
    "Buku Kating/008_Nabyla Sharfina.py",
    title="008 - Nabyla Sharfina",
    icon=":material/person:",
)
Mahasiswa2 = st.Page(
    "Buku Kating/010_Devi Rahayu.py",
    title="010 - Devi Rahayu",
    icon=":material/person:",
)
Mahasiswa3 = st.Page(
    "Buku Kating/013_Azzahra Putri Kamilah.py",
    title="013-Azzahra Putri Kamilah",
    icon=":material/person:",
)
Mahasiswa4 = st.Page(
    "Buku Kating/021_ Khoirul Muttoharoh.py",
    title="021-Khoirul Muttoharoh",
    icon=":material/person:",
)
Mahasiswa5 = st.Page(
    "Buku Kating/031_Natasya Lutfyah Ramadhan.py",
    title="031-Natasya Lutfyah Ramadhan",
    icon=":material/person:",
)
Mahasiswa6 = st.Page(
    "Buku Kating/032_Aditya Taufiqurrohman.py",
    title="032-Aditya Taufiqurrohman",
    icon=":material/person:",
)
Mahasiswa7 = st.Page(
    "Buku Kating/038_Hanna Gresia Sinaga.py",
    title="038-Hanna Gresia Sinaga",
    icon=":material/person:",
)
Mahasiswa8 = st.Page(
    "Buku Kating/057_ Sarah Wasti.py",
    title="057-Sarah Wasti",
    icon=":material/person:",
)
Mahasiswa9 = st.Page(
    "Buku Kating/066_Muhammad Aqil Ramadhan.py",
    title="066-Muhammad Aqil Ramadhan",
    icon=":material/person:",
)
Mahasiswa10 = st.Page(
    "Buku Kating/070_Salsabila Putri Maharani.py",
    title="070-Salsabila Putri Maharani",
    icon=":material/person:",
)
Mahasiswa11 = st.Page(
    "Buku Kating/096_Razin Hafid Hamdi.py",
    title="096-Razin Hafid Hamdi",
    icon=":material/person:",
)
Mahasiswa12 = st.Page(
    "Buku Kating/113_Muhammad Naufal Ramadhan.py",
    title="113-Muhammad Naufal Ramadhan",
    icon=":material/person:",
)

#Perlu diperhatikan perubahannya
KREASI = st.Page("tools/KREASI.py", title="KREASI", icon=":material/search:")
KREASII = st.Page("tools/KREASII.py", title="KREASII", icon=":material/search:")

#Perlu diperhatikan perubahannya
if st.session_state.pindah:
    pg = st.navigation(
        {
            "Halaman Utama": [Homepage],
            "Buku Kating": [Mahasiswa1, Mahasiswa2, Mahasiswa3, Mahasiswa4, Mahasiswa5, Mahasiswa6,Mahasiswa7, Mahasiswa8, Mahasiswa9, Mahasiswa10, Mahasiswa11, Mahasiswa12],
            "Try Me !!": [KREASI, KREASII],
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :(") 
pg.run()
 
