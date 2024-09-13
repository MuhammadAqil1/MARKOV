import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO


# JANGAN DIUBAH
@st.cache_data
def load_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = ImageOps.exif_transpose(img)
    return img


def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    for i, img in enumerate(images):
        # menampilkan gambar di tengah
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, use_column_width=True)

        if i < len(data_list):
            st.write(f"Nama: {data_list[i]['nama']}")
            st.write(f"Sebagai: {data_list[i]['sebagai']}")
            st.write(f"NIM: {data_list[i]['nim']}")
            st.write(f"Fun Fact: {data_list[i]['fun_fact']}")
            st.write(f"Motto Hidup: {data_list[i]['motto_hidup']}")


# JANGAN DIUBAH

st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='font-size: 5.5em;'>WEBSITE KATING</h1>
        <p style='font-size: 2em;'>CEO HMSD Adyatama ITERA 2024</p>
    </div>
    """,
    unsafe_allow_html=True,
)


url = "https://drive.google.com/uc?export=view&id=12cQ4T8NkVvVPVNX6zBQC4sviFcc4cDWx"
url1 = "https://drive.google.com/uc?export=view&id=12RBvQdMiqqqph-Q1QqLb0zvvIPnBjCYb"


def layout(url):
    col1, col2, col3 = st.columns([1, 2, 1])  # Menggunakan kolom dengan rasio 1:2:1
    with col1:
        st.write("")  # Menyisakan kolom kosong
    with col2:
        st.image(load_image(url), use_column_width="True", width=350)
    with col3:
        st.write("")  # Menyisakan kolom kosong


layout(url)
layout(url1)


def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=["Home", "About Us"],
        icons=["house-door", "hand-index"],
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "black", "font-size": "19px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#eee",
            },
            "nav-link-selected": {"background-color": "#3FBAD8"},
        },
    )
    return selected


menu = streamlit_menu()

if menu == "Home":

    def home_page():
        st.markdown(
            """<style>.centered-title {text-align: center;}</style>""",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<h1 class='centered-title'>Deskripsi Kelompok</h1>", unsafe_allow_html=True
        )
        st.markdown(
            """<div style="text-align: justify;">Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
                    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
                    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
                    uis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
                    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est 
                    laborum.</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)
        foto_kelompok = "https://drive.google.com/uc?export=view&id=1XzbVVIqowAq2KO5jnPON04-79KXA92nW"
        layout(foto_kelompok)
        st.markdown(
            """<div style="text-align: justify;">Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
                    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
                    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
                    uis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
                    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est 
                    laborum.</div>""",
            unsafe_allow_html=True,
        )
        st.write(""" """)

    home_page()

elif menu == "About Us":

    def about_page():
        st.markdown(
            """<style>.centered-title {text-align: center;}</style>""",
            unsafe_allow_html=True,
        )
        st.markdown("<h1 class='centered-title'>About Us</h1>", unsafe_allow_html=True)
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Zve71iFzR4TZgREJabirqaylyd_2iXzM",
            "https://drive.google.com/uc?export=view&id=1lszi7rS9Z_hfy5j6BqnYVlE795zUUYqW",
            "https://drive.google.com/uc?export=view&id=1iaZL1_TxVsiY8vkk2uUH7eLjeBmzHS4l",
            "https://drive.google.com/uc?export=view&id=1r-a4D2WwIxHyR3J3oT9idn0zgswTLPB3",
            "https://drive.google.com/uc?export=view&id=1d31GuEALSjNsYtk_KoE-r0oxCSJtU89C",
            "https://drive.google.com/uc?export=view&id=1IJYNoMdPhx1SUtDT17ac0BdE7nyh4-qj",
            "https://drive.google.com/uc?export=view&id=1YKOvVq2xMwBwjuRLb8I-OU-yGC-dFxoE",
            "https://drive.google.com/uc?export=view&id=19UH_AssOYVxbLe9Cs0BMDYVqVol4Y0Z5",
            "https://drive.google.com/uc?export=view&id=1-2Zf9AK6Fl2W_qoTEIDuLi7N9sYhg-IZ",
            "https://drive.google.com/uc?export=view&id=1lYpd13339cFupk3Fbasj3LFBW3mk47_a",
            "https://drive.google.com/uc?export=view&id=1XCvG1XK9FFCLtCDTiZ44FpfhZC6mveW3",
            "https://drive.google.com/uc?export=view&id=1XKjAYneQg5Kd5J30TIuGlyKX0DIid81X",
        ]
        data_list = [
                {
                "nama": "Aditya Taufiqurrohman",
                "sebagai": "Pak Lurah",
                "nim": "123450032",
                "fun_fact": "kalau tidur gabisa tidur bareng",
                "motto_hidup": "harus tetap sholat",
            },
            {
                "nama": "Hanna Gresia Sinaga",
                "sebagai": "Bu Lurah",
                "nim": "123450038",
                "fun_fact": "kalau tidur harus mati lampu",
                "motto_hidup": "harus tetap greja",
            },
            {
                "nama": "Muhammad Aqil Ramadhan",
                "sebagai": "Anggota",
                "nim": "123450066",
                "fun_fact": "kalau tidur ganteng banget",
                "motto_hidup": "jangan menilai seseorang dari penampilannya",
            },
            {
                "nama": "khoirul muttoharoh",
                "sebagai": "Anggota",
                "nim": "123450021",
                "fun_fact": "kalau tidur ga bisa gelap",
                "motto_hidup": "kita bisa karena terbiasa",
            },
            {
                "nama": "Azzahra Putri Kamilah",
                "sebagai": "Anggota",
                "nim": "123450013",
                "fun_fact": "Makan harus ada cabe",
                "motto_hidup": "jangan pernah takut gagal",
            },
            {
                "nama": "Muhammad Naufal Ramadhan",
                "sebagai": "Anggota",
                "nim": "123450113",
                "fun_fact": "Tidur harus gelap",
                "motto_hidup": "Pasti ada jalannya",
            },
            {
                "nama": "Salsabila Putri Maharani",
                "sebagai": "Anggota",
                "nim": "123450070",
                "fun_fact": "ga syuka kuaci",
                "motto_hidup": "hidup adalah takdir",
            },
            {
                "nama": "Razin Hafid Hamdi",
                "sebagai": "Anggota",
                "nim": "123450096",
                "fun_fact": "lebih suka bubur di aduk",
                "motto_hidup": "dima bumi dipijak di situ langik di junjuang",
            },
            {
                "nama": "Natasya Lutfyah Ramadhan",
                "sebagai": "Anggota",
                "nim": "123450031",
                "fun_fact": "Ga suka bubur dan makanan berbau kecap",
                "motto_hidup": "Lakukan yang terbaik, sisanya biar Tuhan yang mengatur",
            },
            {
                "nama": "Nabyla Sharfina",
                "sebagai": "Anggota",
                "nim": "123450008",
                "fun_fact": "Kalau ujian belajarnya harus h-1",
                "motto_hidup": "Selesaikan apa yang sudah kamu mulai",
            },
            {
                "nama": "Devi Rahayu",
                "sebagai": "Anggota",
                "nim": "123450010",
                "fun_fact": "Lebih suka makan yang berkuah dan kalo tidur gak bisa di tempat yang gelap",
                "motto_hidup": "Jangan takut gagal, takutlah untuk tidak mencoba",
            },
            {
                "nama": "Sarah Wasti",
                "sebagai": "Anggota",
                "nim": "123450057",
                "fun_fact": "Ga suka perbawangan",
                "motto_hidup": "Kalau orang lain bisa, kenapa harus aku",
            }
        ]
        display_images_with_data(gambar_urls, data_list)

    about_page()
