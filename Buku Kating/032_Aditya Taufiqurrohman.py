import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image, ImageOps
from io import BytesIO

st.markdown("""<style>.centered-title {text-align: center;}</style>""",unsafe_allow_html=True)
st.markdown("<h1 class='centered-title'>BUKU KATING</h1>", unsafe_allow_html=True)

# bagian sini jangan diubah
def streamlit_menu():
    selected = option_menu(
        menu_title=None,
        options=[
            "Kesekjenan",
            "Baleg",
            "Senator",
            "Departemen PSDA",
            "Departemen MIKFES",
            "Departemen MEDKRAF",
            "Departemen Eksternal",
            "Departemen Internal",
            "Departemen SSD",
        ],
        icons=[
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
            "people-fill",
        ],
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

@st.cache_data
def load_image(url):
    response = requests.get(url)
    if response.status_code != 200:
        st.error(
            f"Failed to fetch image from {url}, status code: {response.status_code}"
        )
        return None
    try:
        img = Image.open(BytesIO(response.content))
        img = ImageOps.exif_transpose(img)
        img = img.resize((300, 400))
        return img
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None
    
@st.cache_data
def display_images_with_data(gambar_urls, data_list):
    images = []
    for i, url in enumerate(gambar_urls):
        with st.spinner(f"Memuat gambar {i + 1} dari {len(gambar_urls)}"):
            img = load_image(url)
            if img is not None:
                images.append(img)

    for i, img in enumerate(images):
        # Menggunakan Streamlit untuk menampilkan gambar di tengah kolom
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, use_column_width=True)

        if i < len(data_list):
            st.write(f"Nama: {data_list[i]['nama']}")
            st.write(f"NIM: {data_list[i]['nim']}")
            st.write(f"Umur: {data_list[i]['umur']}")
            st.write(f"Asal: {data_list[i]['asal']}")
            st.write(f"Alamat: {data_list[i]['alamat']}")
            st.write(f"Hobbi: {data_list[i]['hobbi']}")
            st.write(f"Sosial Media: {data_list[i]['sosmed']}")
            st.write(f"Kesan: {data_list[i]['kesan']}")
            st.write(f"Pesan: {data_list[i]['pesan']}")
            st.write("  ")
    st.write("Semua gambar telah dimuat!")
menu = streamlit_menu()

# BAGIAN SINI YANG HANYA BOLEH DIUABAH
if menu == "Kesekjenan":
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1zULOhNEvwHSdj8cwoLA2JHQYKh6vLlPD", #Bang Kharisma
            "https://drive.google.com/uc?export=view&id=13TPY1H_DmtkOR6sJneSpSzqFj7A4cUD5", #Bang Pandra
            "https://drive.google.com/uc?export=view&id=14vRpc3DuTEspBCEHlmfeOMmLFsbpHf2J",# kak meliza
            "https://drive.google.com/uc?export=view&id=1qw6pPQKNVXQc6y8qGf5SOGyogkqP6MTf",#kak putri
            "https://drive.google.com/uc?export=view&id=1RIINjtasBDo_wRFcQPqpgd0t67UQUX3j",#kak hartiti
            "https://drive.google.com/uc?export=view&id=18QHImvi6T7sTERUW-BpzylLaoZ-P9Lcd",#kak nadila


        ]
        data_list = [
            {
                "nama"  : "Kharisma Gumilang",
                "nim"   : "121450142",
                "umur"  : "21",
                "asal"  :"Palembang",
                "alamat": "Kandis",
                "hobbi" : "Mendengerkan musik",
                "sosmed": "@gumilangkharisma",
                "kesan" : "Asik dan berkarisma",  
                "pesan" :"semangat terus bang"
            },
            {
                "nama"  : "Pandra Insani Putra Azwan",
                "nim"   : "121450137",
                "umur"  : "21",
                "asal"  : "Bukit Kemuning, Lampung Utara",
                "alamat": "Bawen 2",
                "hobbi" : "Bermain gitar dan menyanyi",
                "sosmed": "@pandrainsni27",
                "kesan" : "asik sama kayak bang gumilang",  
                "pesan" : "semngat terus bang"
            },
            {
                "nama"  : "Meliza Wulandari",
                "nim"   : "121450065",
                "umur"  : "20",
                "asal"  : "Pagar Alam, Sumatera Selatan",
                "alamat": "Kotabaru",
                "hobbi" : "Nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan" : "baik",  
                "pesan" : "semangat kak"
            },
            {
                "nama"  : "Putri Maulida Chairani",
                "nim"   : "121450050",
                "umur"  : "21",
                "asal"  : "Payakumbuh, Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi" : "Dengerin bang pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan" : "baik",  
                "pesan" : "semangat kak"
            },
            {
                "nama"  : "Hartiti Fadilah",
                "nim"   : "121450031",
                "umur"  : "21",
                "asal"  : "Palembang",
                "alamat": "Pemda",
                "hobbi" : "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan" : "baik",  
                "pesan" : "semangat kak"
            },
            {
                "nama"  : "Nadilla Andara Putri",
                "nim"   : "121450003",
                "umur"  : "21",
                "asal"  : "Metro",
                "alamat": "KotaBaru",
                "hobbi" : "Membaca",
                "sosmed": "@ndillaandr26",
                "kesan" : "semagat",  
                "pesan" : "baik"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1aaRfIBYMSd9MK9hKAnrVCIbCgLaML6wZ",#kak tri
            "https://drive.google.com/uc?export=view&id=1DiLXGB2CUxWzMOPCd5YntKYk5xU7uryh", # kak cahyani
            "https://drive.google.com/uc?export=view&id=1TytKk1itvXSnUYa5CaWamoAf8MsYWZcY", # kak wulan
            "https://drive.google.com/uc?export=view&id=1lF7Xj0uCdRDZdoS1-u2_9Svb9tWrQjtD", # kak dini
            "https://drive.google.com/uc?export=view&id=1vdo2tDYc3i2T_HPtIExRAV1R8bqDAv4k", # kak fitriani
            "https://drive.google.com/uc?export=view&id=1kHJQT3mdBDM1pqbpMGrmasx6jR4oLYpy", # bang mirzan
            "https://drive.google.com/uc?export=view&id=1ysktoOsp0f9kDDDRPooqXGwA_PhmnRuJ", # kak dhea
            "https://drive.google.com/uc?export=view&id=1z1jsrYO4V9l_zOe-SjN0r5imW9ntskN6", # bang fahrul
            "https://drive.google.com/uc?export=view&id=1nqBAaksg_0b1vG3GlRJdhYquAOzeU_Gz", # kak berlin
            "https://drive.google.com/uc?export=view&id=1fOQ9sNx28dTXwjuQdSilf0kfVb5k2_d0", # bang jeremia
        ]
        data_list = [
            {
                "nama"  : "Tri Murniya Ningsih",
                "nim"   : "121450038",
                "umur"  : "21",
                "asal"  : "Bogor",
                "alamat": "Raden Saleh",
                "hobbi" : "Kalo ke coffe shop pesen red velvet bukan kopi",
                "sosmed": "@trimurniyaa",
                "kesan" : "baik asik banget pokok nya semua kakak dan abang di BALEG!!!",  
                "pesan" : "SEMANGAT TERUSS KAKAK ABANG!!!"
            },
            {
                "nama"  : "Annisa Cahyani Surya",
                "nim"   : "121450114",
                "umur"  : "21",
                "asal"  : "Tanggerang Selatan",
                "alamat": "Way Huwi",
                "hobbi" : "Membaca, Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan" : "baik asik banget pokok nya semua kakak dan abang di BALEG!!!",  
                "pesan" : "SEMANGAT TERUSS KAKAK ABANG!!!"
            },
            {
                "nama"  : "Wulan Sabina",
                "nim"   : "121450150",
                "umur"  : "21",
                "asal"  : "Medan",
                "alamat": "Raden Saleh",
                "hobbi" : "Nonton Drakor",
                "sosmed": "@wlnsbn0",
                "kesan" : "baik asik banget pokok nya semua kakak dan abang di BALEG!!!",  
                "pesan" : "SEMANGAT TERUSS KAKAK ABANG!!!"
            },
            {
                "nama"  : "Annisa Dini Amaliya",
                "nim"   : "121450081",
                "umur"  : "21",
                "asal"  : "Tanggerang",
                "alamat": "Jati Agung",
                "hobbi" : "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan" : "baik asik banget pokok nya semua kakak dan abang di BALEG!!!",  
                "pesan" : "SEMANGAT TERUSS KAKAK ABANG!!!"
            },
            {
                "nama"  : "Anisa Fitriyani",
                "nim"   : "121450150",
                "umur"  : "21",
                "asal"  : "Medan",
                "alamat": "Raden Saleh",
                "hobbi" : "Nonton Drakor",
                "sosmed": "@wlnsbn0",
                "kesan" : "baik asik banget pokok nya semua kakak dan abang di BALEG!!!",  
                "pesan" : "SEMANGAT TERUSS KAKAK ABANG!!!"
            },
            {
                "nama"  : "Mirzan Yusuf Rabbani",
                "nim"   : "122450118",
                "umur"  : "20",
                "asal"  : "Jakarta",
                "alamat": "Korpri",
                "hobbi" : "Main Kucing",
                "sosmed": "@myrrinn",
                "kesan" : "baik asik banget pokok nya semua kakak dan abang di BALEG!!!",  
                "pesan" : "SEMANGAT TERUSS KAKAK ABANG!!!"
            },
            {
                "nama"  : "Dhea Amelia Putri",
                "nim"   : "122450004",
                "umur"  : "20",
                "asal"  : "Sukabumi, Jawa Barat",
                "alamat": "Natar",
                "hobbi" : "Suka Ikut Tes SKD",
                "sosmed": "@dhea_wedding",
                "kesan" : "baik asik banget pokok nya semua kakak dan abang di BALEG!!!",  
                "pesan" : "SEMANGAT TERUSS KAKAK ABANG!!!"
            },
            {
                "nama"  : "Muhammad Fahrul Aditya",
                "nim"   : "121450156",
                "umur"  : "22",
                "asal"  : "Surakarta, Jawa Tengah",
                "alamat": "Pahoman",
                "hobbi" : "Melukis, badminton, hiking, ngopi, dengerin music, nonton film dan ngoding",
                "sosmed": "@fhrul.pdf",
                "kesan" : "baik asik banget pokok nya semua kakak dan abang di BALEG!!!",  
                "pesan" : "SEMANGAT TERUSS KAKAK ABANG!!!"
            },
            {
                "nama"  : "Berlianda Enda Putri",
                "nim"   : "122450065",
                "umur"  : "21",
                "asal"  : "Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi" : "Main Game",
                "sosmed": "@berlyyanda",
                "kesan" : "baik asik banget pokok nya semua kakak dan abang di BALEG!!!",  
                "pesan" : "SEMANGAT TERUSS KAKAK ABANG!!!"
            },
            {
                "nama"  : "Jeremia Susanto",
                "nim"   : "122450022",
                "umur"  : "20",
                "asal"  : " Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi" : "Marah-marah",
                "sosmed": "@jeremia_s_",
                "kesan" : "baik asik banget pokok nya semua kakak dan abang di BALEG!!!",  
                "pesan" : "SEMANGAT TERUSS KAKAK ABANG!!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

# Tambahkan menu lainnya sesuai kebutuhan
