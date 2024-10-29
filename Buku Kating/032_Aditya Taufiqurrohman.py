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
                "kesan" : "--",  
                "pesan" :"--"
            },
            {
                "nama"  : "Pandra Insani Putra Azwan",
                "nim"   : "121450137",
                "umur"  : "21",
                "asal"  : "Bukit Kemuning, Lampung Utara",
                "alamat": "Bawen 2",
                "hobbi" : "Bermain gitar dan menyanyi",
                "sosmed": "@pandrainsni27",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Meliza Wulandari",
                "nim"   : "121450065",
                "umur"  : "20",
                "asal"  : "Pagar Alam, Sumatera Selatan",
                "alamat": "Kotabaru",
                "hobbi" : "Nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Putri Maulida Chairani",
                "nim"   : "121450050",
                "umur"  : "21",
                "asal"  : "Payakumbuh, Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi" : "Dengerin bang pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Hartiti Fadilah",
                "nim"   : "121450031",
                "umur"  : "21",
                "asal"  : "Palembang",
                "alamat": "Pemda",
                "hobbi" : "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Nadilla Andara Putri",
                "nim"   : "121450003",
                "umur"  : "21",
                "asal"  : "Metro",
                "alamat": "KotaBaru",
                "hobbi" : "Membaca",
                "sosmed": "@ndillaandr26",
                "kesan" : "--",  
                "pesan" : "--"
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

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Ej4ehUAodDUbxec9wBKHIJHhRL6YNlun",#lutfi
            "https://drive.google.com/uc?export=view&id=1EuTVdC5HAoIZlDR3Z-W69OkW2r8X5bwE",#bintang
        ]
        data_list = [
             {
                "nama"  : "Anissa Luthfi Alifia",
                "nim"   : "121450093",
                "umur"  : "22",
                "asal"  : "Lampung Tengah",
                "alamat": "Kost Putri Rahayu",
                "hobbi" : "Mendengarkan bang Bintang dengerin lagu",
                "sosmed": "@anissaluthfi_",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Rian Bintang Wijaya",
                "nim"   : "122450094",
                "umur"  : "20",
                "asal"  : "Palembang, Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi" : "Mendengar Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan" : "--",  
                "pesan" : "--"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=17kdJhs0bLcFO_zKcGFpN6FgmVbV9eDHP",#lutfi
            "https://drive.google.com/uc?export=view&id=1967V3pVY_CKGvSSmViASFj8yPb8Izc8X",#bintang
            "https://drive.google.com/uc?export=view&id=1CQ5cjlw9g1eNSSMs23NNs9zLd5RFoLJ_",#lutfi
            "https://drive.google.com/uc?export=view&id=1n6OWLz-g3wEvghPQf2r1pBuhHiupyY5G",#bintang
            "https://drive.google.com/uc?export=view&id=1NJRfoOnS6x9kNKZfqwCCfhpIjQ3mPCB4",#lutfi
            "https://drive.google.com/uc?export=view&id=1NwVkGd0dFKaqzTC5vlngiUv_fm7R_0Ij",#bintang
            "https://drive.google.com/uc?export=view&id=1SLrvPgh32VTDfTGv0a1ep2L02GHO6eaC",#lutfi
            "https://drive.google.com/uc?export=view&id=1r2-hd00ieM7cGXHySr_T_kNESjZM4U_n",#bintang
            "https://drive.google.com/uc?export=view&id=1HXWMoecrvbGw0WryTTyjIQdo8w73UNh4",#lutfi
            "https://drive.google.com/uc?export=view&id=1LT_au-QkY57A0P7uIl1UGSJ6b9SlEiHv",#bintang
            "https://drive.google.com/uc?export=view&id=1pgx6-nQlptKFh1O0w_H8iQ7JQDwPXUs8",#lutfi
            "https://drive.google.com/uc?export=view&id=1fAyy_u6yUqODRmxn_0EuU7m8tNFJOnBv",#bintang
            "https://drive.google.com/uc?export=view&id=156kL0yOCQPfkQGvB_Kke8kawKPlrRQhd",#lutfi
            "https://drive.google.com/uc?export=view&id=17GbtBSmX5P0EnYlM_RwSx3j-neKjlw1O",#bintang
            "https://drive.google.com/uc?export=view&id=1B825apMA1gz9aXSh_sE-qFnVJlCKcPvm",#lutfi
            "https://drive.google.com/uc?export=view&id=1kSRzYHLsHRCBgGMX8HcZeDoYzc_l6OV6",#bintang
            "https://drive.google.com/uc?export=view&id=1ocBcV5S_aMWSBTR7zgNeRptxlo0Qvrda",#lutfi
            "https://drive.google.com/uc?export=view&id=1RLfU3bFmPfi2TY-x4_MDDXlk3cUrMRRw",#bintang
            "https://drive.google.com/uc?export=view&id=1Tr6tLF-_KnpdXMXotf4hCDpalzmfIieP",#lutfi
            "https://drive.google.com/uc?export=view&id=1sfVTvq-BX1m5VwbhNc55v6Jsk3a-GB5P",#bintang
            "https://drive.google.com/uc?export=view&id=18Hu6kNnQLzXqiyDl0yugP_Lg1TYdhstp",#lutfi
            "https://drive.google.com/uc?export=view&id=1KqqoiTxo5swvfqIYuKEPc_Go8p-Dt1FB",#bintang
        ]
        data_list = [
            {
                "nama"  : "Ericson Chandra Sihombing",
                "nim"   : "121450026",
                "umur"  : "21",
                "asal"  : "Bekasi",
                "alamat": "Kobam",
                "hobbi" : "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Elisabeth Claudia Simanjuntak",
                "nim"   : "122450123",
                "umur"  : "18",
                "asal"  : "Pekanbaru",
                "alamat": "Sukarame",
                "hobbi" : "Memancing keributan",
                "sosmed": "@celisabethh_",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Nisrina Nur Afifah",
                "nim"   : "122450052",
                "umur"  : "19",
                "asal"  : "Bekasi",
                "alamat": "Sukarame",
                "hobbi" : "Nabok orang",
                "sosmed": "@afifahhnsrn",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Allya Nurul Islami Pasha",
                "nim"   : "122450033",
                "umur"  : "20",
                "asal"  : "Sumatera Barat",
                "alamat": "Gang Perwira, Belwis",
                "hobbi" : "Nonton Dracin",
                "sosmed": "@allyaislami_",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Farahanum Afifah Ardiansyah",
                "nim"   : "122450056",
                "umur"  : "20",
                "asal"  : "Padang, Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi" : "Tidur",
                "sosmed": "@farahanumafifahh",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Ferdy Kevin Naibaho",
                "nim"   : "122450107",
                "umur"  : "19",
                "asal"  : "Medan, Sumatera Utara",
                "alamat": "Jalan Senopati Raya 18",
                "hobbi" : "Dengerin Rocky Gerung",
                "sosmed": "@ferdy_kevin",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "M. Deriansyah Okutra",
                "nim"   : "122450101",
                "umur"  : "19",
                "asal"  : "Kayu Agung",
                "alamat": "Jalan Pagar Alam",
                "hobbi" : "Bercerita horror",
                "sosmed": "@dransyh_",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Oktavia Nurwenda Puspita Sari",
                "nim"   : "122450041",
                "umur"  : "20",
                "asal"  : "Lampung Timur",
                "alamat": "Way Hui",
                "hobbi" : "Memasak",
                "sosmed": "@_oktavianrwnda_",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Deyvan Loxefal",
                "nim"   : "121450148",
                "umur"  : "21",
                "asal"  : "Riau",
                "alamat": "Pulau Damar",
                "hobbi" : "Belajar",
                "sosmed": "@depanloo",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Ibnu Farhan Al-Ghifari",
                "nim"   : "121450121",
                "umur"  : "21",
                "asal"  : "Jambi",
                "alamat": "Pulau Damar, Kobam",
                "hobbi" : "Bermain Game Online",
                "sosmed": "@al_ghifari032",
                "kesan" : "--",  
                "pesan" : "--"
            },
             {
                "nama"  : "Johannes Krisjon Silitonga",
                "nim"   : "122450043",
                "umur"  : "19",
                "asal"  : "Tanggerang",
                "alamat": "Jalan Lapas",
                "hobbi" : "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Kemas Veriandra Ramadhan",
                "nim"   : "122450016",
                "umur"  : "19",
                "asal"  : "Bekasi",
                "alamat": "Golf Asri",
                "hobbi" : "Bermain ular python digital",
                "sosmed": "@kemasverii",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Leonard Andreas Napitupulu",
                "nim"   : "121450153",
                "umur"  : "21",
                "asal"  : "Sumatera Utara",
                "alamat": "Kobam",
                "hobbi" : "Belajar",
                "sosmed": "@lnrd.__",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Presilia",
                "nim"   : "122450081",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Kota Baru",
                "hobbi" : "Tidur",
                "sosmed": "@presiliamg",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Rafa Aqilla Jungjunan",
                "nim"   : "122450148",
                "umur"  : "20",
                "asal"  : "Riau",
                "alamat": "Belwis",
                "hobbi" : "Membaca webtoon",
                "sosmed": "@rafaaqilla",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Sahid Maulana",
                "nim"   : "122450109",
                "umur"  : "21",
                "asal"  : "Depok, Jawa Barat",
                "alamat": "Airan Raya",
                "hobbi" : "Bermain Game",
                "sosmed": "@sahid_maul19",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Vanessa Olivia Rose",
                "nim"   : "121450068",
                "umur"  : "20",
                "asal"  : "Jakarta",
                "alamat": "Perumahan Korpri",
                "hobbi" : "Belajar",
                "sosmed": "@roselivnes__",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "M. Farhan Athaulloh",
                "nim"   : "121450117",
                "umur"  : "21",
                "asal"  : "Bandar Lampung",
                "alamat": "Kota Baru",
                "hobbi" : "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Gede Moena",
                "nim"   : "121450014",
                "umur"  : "21",
                "asal"  : "Bekasi",
                "alamat": "Korpri Raya",
                "hobbi" : "Belajar dan main game",
                "sosmed": "@gedemoenaa",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Jaclin Alcavella",
                "nim"   : "122450015",
                "umur"  : "19",
                "asal"  : "Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi" : "Berenang",
                "sosmed": "@jaclinalcv_",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Rafly Prabu Darmawan",
                "nim"   : "122450140",
                "umur"  : "20",
                "asal"  : "Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi" : "Main Game",
                "sosmed": "@raflyy_pd2684",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Syalaisha Andini Putriansyah",
                "nim"   : "122450111",
                "umur"  : "21",
                "asal"  : "Tanggerang",
                "alamat": "Sukarame",
                "hobbi" : "Membaca",
                "sosmed": "@syalaisha.i__",
                "kesan" : "--",  
                "pesan" : "--"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1dS6ITlLNUdIkNR0jyLqvC0gER3q99IO5",#lutfi
            "https://drive.google.com/uc?export=view&id=1UAOS4XlUsf7OtL7J9BiH1ZYe3fMI1GIh",#bintang
            "https://drive.google.com/uc?export=view&id=1ncOxEz2D9FHN-6D_2aUKX5JejUpccrEj",#lutfi
            "https://drive.google.com/uc?export=view&id=1FE7p0E-P7PAZIykO7gspvwvumgT093zz",#bintang
            "https://drive.google.com/uc?export=view&id=1kknKQBQBx4aUe_LTNbUE5bV646LXKCyh",#lutfi
            "https://drive.google.com/uc?export=view&id=1sz8ubbvwUAAXQPJEQpyj2xhiLhkoZg1u",#bintang
            "https://drive.google.com/uc?export=view&id=1froreiE2yG90QYIut12LmUzpASv9woGX",#lutfi
            "https://drive.google.com/uc?export=view&id=1KTzsL7fdhaMDKKkoXxeL4QIqEEympmQj",#bintang
            "https://drive.google.com/uc?export=view&id=1eIlWPak1lFokVq2J7BY0SlPsVae-pdk2",#lutfi
            "https://drive.google.com/uc?export=view&id=18l-YF1YdmUhWkk_OaXZvVQNJfF86eSau",#bintang
            "https://drive.google.com/uc?export=view&id=17pp7ZsvnHDRRFvZfknOiR8UQeT05zv4e",#lutfi
            "https://drive.google.com/uc?export=view&id=1mv6ZzO77botwKvSY3Z8xLPdsarP_6Des",#bintang
            "https://drive.google.com/uc?export=view&id=1b_NYTa7khMQS3MIcE7HRzmllVLYWmZ-J",#lutfi
        ]
        data_list = [
            {
                "nama"  : "Rafi Fadhlillah",
                "nim"   : "121450143",
                "umur"  : "21",
                "asal"  : "Lubuk Linggau",
                "alamat": "Jalan Nangka 4",
                "hobbi" : "Olahraga",
                "sosmed": "@rafadhilillahh13",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Annisa Novantika",
                "nim"   : "121450005",
                "umur"  : "21",
                "asal"  : "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi" : "Memasak",
                "sosmed": "@anovavona",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Ahmad Sahidin Akbar",
                "nim"   : "122450044",
                "umur"  : "20",
                "asal"  : "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi" : "Olahraga",
                "sosmed": "@sahid22__",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Fadhil Fitra Wijaya",
                "nim"   : "122450082",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Teluk Betung",
                "hobbi" : "Main game",
                "sosmed": "@fadhilfwee",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Syalaisha Andina Putriansyah",
                "nim"   : "122450121",
                "umur"  : "21",
                "asal"  : "Tangerang",
                "alamat": "Gang Yudhistira",
                "hobbi" : "Baca jurnal",
                "sosmed": "@dkselsd_31",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Dinda Nababan",
                "nim"   : "122450120",
                "umur"  : "20",
                "asal"  : "Medan, Sumatera Utara",
                "alamat": "Jalan Lapas",
                "hobbi" : "Belajar",
                "sosmed": "@dindanababan_",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Marleta Cornelia Leander",
                "nim"   : "122450092",
                "umur"  : "20",
                "asal"  : "Depok, Jawa Barat",
                "alamat": "Gang Nangka 3",
                "hobbi" : "Review Jurnal",
                "sosmed": "@marletacornelia",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Rut Junita Sari Siburian",
                "nim"   : "122450103",
                "umur"  : "20",
                "asal"  : "Batam, Kepulauan Riau",
                "alamat": "Gang Nangka 3",
                "hobbi" : "Review Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Syadza Puspadari Azhar",
                "nim"   : "122450072",
                "umur"  : "20",
                "asal"  : "Palembang",
                "alamat": "Belwis",
                "hobbi" : "Resume SG",
                "sosmed": "@puspadrr",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Eggi satria",
                "nim"   : "122450032",
                "umur"  : "20",
                "asal"  : "Sukabumi",
                "alamat": "Korpri",
                "hobbi" : "Ngoding WISATA",
                "sosmed": "@egistr",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Febiya Jomy Pratiwi",
                "nim"   : "122450074",
                "umur"  : "20",
                "asal"  : "Tulang Bawang",
                "alamat": "Jalan Kelengkeng Raya",
                "hobbi" : "Review jurnal",
                "sosmed": "@pratiwifebiya",
                "kesan" : "--",  
                "pesan" : "--"
            },
             {
                "nama"  : "Happy Syahrul Ramadhan",
                "nim"   : "122450013",
                "umur"  : "20",
                "asal"  : "Lampung Timur",
                "alamat": "Karang Anyar",
                "hobbi" : "Main game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Randa Andriana Putra",
                "nim"   : "122450083",
                "umur"  : "21",
                "asal"  : "Banten",
                "alamat": "Sukarame",
                "hobbi" : "Tidur dan berkembang",
                "sosmed": "@randaandriana_",
                "kesan" : "--",  
                "pesan" : "--"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1MKtctC3jixEbWoZnQTz-jc-uGFwRSMBh",#lutfi
            "https://drive.google.com/uc?export=view&id=1MMn9N0SQRYEA0o0bxj5en3rvzljgdOoE",#bintang
            "https://drive.google.com/uc?export=view&id=1rb1cTKH6UQ-Rc7SdWt0HH9QMo6TH6FpP",#lutfi
            "https://drive.google.com/uc?export=view&id=1NRJfFwtA38TlIWMjeuKv-F7G8GeBRI7s",#lutfi
            "https://drive.google.com/uc?export=view&id=1O2A6WP_bERCmf6dodkVxg9qruCB-WEbV",#bintang
            "https://drive.google.com/uc?export=view&id=1Nyuikt8VXNBN1x2oWIcAEHcDSMtf8D2E",#lutfi
            "https://drive.google.com/uc?export=view&id=1OAfRzRBrh3BX92fZgEGiq98dtKGLz6pS",#bintang
            "https://drive.google.com/uc?export=view&id=1Nm06scA2E9_PszDgt1kZBiN5UMQu5Tsm",#lutfi
            "https://drive.google.com/uc?export=view&id=1OD6lOVAkoJ9P553avWTNSccXcxvkpJo2",#bintang
            "https://drive.google.com/uc?export=view&id=1NjZdUk7wAMSNAzeBTyXlls4-HAHfZQUO",#lutfi
            "https://drive.google.com/uc?export=view&id=1P1SEW2wq70o_AW5gZFAaD28tZDfnH6Fq",#bintang
            "https://drive.google.com/uc?export=view&id=1P1qO4feaE2zNzAlC0X23UxFW4wkLWVLt",#lutfi
            "https://drive.google.com/uc?export=view&id=1MPE0yiCej3huEZ4AJvOObUOKainbVodK",#bintang
            "https://drive.google.com/uc?export=view&id=1Oq0Qi25AzmbSVJ1Sf97W_PdxMdEn9PEW",#lutfi
            "https://drive.google.com/uc?export=view&id=1PAJF2J0-IN1bYSNm2S4BbdvxgmSuR_cO",#bintang
            "https://drive.google.com/uc?export=view&id=1NAOT44m_h1RS1Kd_q1rJvgSwdT6BUYtv",#lutfi
            "https://drive.google.com/uc?export=view&id=1M9dFrcpcFLXyAqLuWdkCWygepFzEGnbf",#bintang
            "https://drive.google.com/uc?export=view&id=1N1a4yly9b2ooboBdJqOlzrhEbxRtzmpA",#lutfi
            "https://drive.google.com/uc?export=view&id=1Miin5UmcTBbpTNk6IIvjIDQ2SC65cZHV",#bintang
            "https://drive.google.com/uc?export=view&id=1MqrXvKpBpqLaL2fUQb-oU5txn_S-OKXv",#bintang
        ]
        data_list = [
            {
                "nama"  : "Yogy Sae Tama",
                "nim": "121450041",
                "umur": "21 Tahun",
                "asal": "Tangerang",
                "alamat": "Jatimulyo",
                "hobbi": "Bangun pagi",
                "sosmed": "@yogyyyyyy",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan" : "--",  
                "pesan" : "--k"
            },
            {
                "nama"  : "Nazwa Nabilla",
                "nim": "121450122",
                "umur": "21 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Way kandis",
                "hobbi": "Belajar",
                "sosmed": "@nazwanbilla",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21 Tahun",
                "asal": "Batam, Kepulauan Riau",
                "alamat": "Belwis",
                "hobbi": "Main game",
                "sosmed": "@bastiansilaban_",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20 Tahun",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Dengerin musik",
                "sosmed": "@deaa.rsn",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Esteria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "19 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Belwis",
                "hobbi": "Main golf bareng kadiv",
                "sosmed": "@esteriars",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Natasya Ega Lina",
                "nim": "122450024",
                "umur": "19 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Belwis",
                "hobbi": "Jadi humas",
                "sosmed": "@nateee__15",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Novelia Adinda",
                "nim": "122450104",
                "umur": "21 Tahun",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Main sepak takraw",
                "sosmed": "@jasminednva",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20 Tahun",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Jogging",
                "sosmed": "@tobiassiagian",
                "kesan" : "--",  
                "pesan" : "--"
            },
             {
                "nama"  : "Yohana Manik",
                "nim": "122450126",
                "umur": "19 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi": "Main Bowling",
                "sosmed": "@yo_annamnk",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21 Tahun",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobbi": "Bikin portofolio",
                "sosmed": "@rzkdrnnn",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20 Tahun",
                "asal": "Bandung",
                "alamat": "Way Huwi",
                "hobbi": "Bertani",
                "sosmed": "@rafiramadhanmaulana",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20 Tahun",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobbi": "Tepuk Semangat",
                "sosmed": "@u_yippy",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20 Tahun",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Q Time",
                "sosmed": "@chlfawww",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21 Tahun",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton youtube, main game",
                "sosmed": "@alfaritziirvan",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Izza Lutfia",
                "nim": "122450090",
                "umur": "20 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Main Rubik",
                "sosmed": "@izzalutfia",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@alyaavanevi",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20 Tahun",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "telat",
                "sosmed": "@rayths_",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Tria Yunanni",
                "nim": "122450062",
                "umur": "20 Tahun",
                "asal": "Way Kanan",
                "alamat": "Sukarame",
                "hobbi": "Baca Buku",
                "sosmed": "@tria_y062",
                "kesan" : "--",  
                "pesan" : "--"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=",#Dimas
            "https://drive.google.com/uc?export=view&id=1vuhYo8mx7zCMgT4e7c-IoB8fFf3s7mxH",#bintang
            "https://drive.google.com/uc?export=view&id=1nGl3QdYjD5Fl13MSVFbNDa_kZcTHofRq",#lutfi
            "https://drive.google.com/uc?export=view&id=1DyNjoMh-VxYFuBdwGQpF_IRaFCEeEa8t",#bintang
            "https://drive.google.com/uc?export=view&id=1NdEXHI_foLP0vUA0Wxiw9Z_Qsyr_eodV",#lutfi
            "https://drive.google.com/uc?export=view&id=1WrM6QbEP3jEJxDur2xGxHfol7nyN2-pt",#lutfi
            "https://drive.google.com/uc?export=view&id=1egkMTpCDKebUSXZSP0YM--YKwsPrOaAQ",#bintang
            "https://drive.google.com/uc?export=view&id=185h7ert59BDruNz2kGdTV4LH-11wOvVG",#yosia
            "https://drive.google.com/uc?export=view&id=1oTQ8hctE2ny4oqJU0GjA9cVsLjjgevU_",#bintang
            "https://drive.google.com/uc?export=view&id=1hpiqO8ucKASOv8_ujlYds5RiH39UU5uv",#lutfi
            "https://drive.google.com/uc?export=view&id=1XpdXlXX1MOCWwyj-OQmOVMLBRNoTZLbL",#azizah
            "https://drive.google.com/uc?export=view&id=1n7cpuPFvL_SImLm3Iq_7iH_VoANmj2bK",#meira
            "https://drive.google.com/uc?export=view&id=1dtMAeI8_iYJCWGjuD5A1c2Cu3OFVej5O",#bintang
        ]
        data_list = [
            {
                "nama"  : "Dimas Rizky Ramadhani",
                "nim"   : "121450027",
                "umur"  : "20",
                "asal"  : "Tanggerang Selatan",
                "alamat": "Way Kandis (Kobam)",
                "hobbi" : "Memancing keributan",
                "sosmed": "@dimzrky_",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Catherine Firdhasari Maulina Sinaga",
                "nim"   : "121450071",
                "umur"  : "20",
                "asal"  : "Sumatera Utara",
                "alamat": "Airan",
                "hobbi" : "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "M.Akbar Resdika",
                "nim"   : "121450066",
                "umur"  : "20",
                "asal"  : "Lampung Barat (Way Tenun)",
                "alamat": "Labuhan Dalam (Untung)",
                "hobbi" : "Suka kucing tapi gak suka ngurusnya",
                "sosmed": "@akbar_restika",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Rani Puspita Sari",
                "nim"   : "122450030",
                "umur"  : "20",
                "asal"  : "KOta Metro",
                "alamat": "Rajabasa",
                "hobbi" : "Dengar musik",
                "sosmed": "@ranniu",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Renta Siahaan",
                "nim"   : "122450070",
                "umur"  : "21",
                "asal"  : "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi" : "Membaca dan Memancing",
                "sosmed": "@renita.shn",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Salwa Farhanatussaidah",
                "nim"   : "122450055",
                "umur"  : "20",
                "asal"  : "Pesawaran",
                "alamat": "Airan",
                "hobbi" : "Nonton",
                "sosmed": "@slwfhn_694",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Rendra Eka Prayoga",
                "nim"   : "122450112",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Belwis",
                "hobbi" : "Mancing Ikan Mas",
                "sosmed": "@rendraepr",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Yosia Retare Banurea",
                "nim"   : "121450149",
                "umur"  : "20",
                "asal"  : "Dairi, Sumatera Utara",
                "alamat": "Perum Griya Indah",
                "hobbi" : "Tidur",
                "sosmed": "@yosiabanurea",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : " Ari Sigit",
                "nim"   : "121450069",
                "umur"  : "23",
                "asal"  : "Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobbi" : "Futsal",
                "sosmed": "@ari_sigit17",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Josua Panggabean",
                "nim"   : "122450061",
                "umur"  : "21",
                "asal"  : "Pematang Siantar",
                "alamat": "Gerbang Barat",
                "hobbi" : "Menonton",
                "sosmed": "@josuapanggabean_",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Azizah Kusumah Putri",
                "nim"   : "122450068",
                "umur"  : "21",
                "asal"  : "Lampung Selatan",
                "alamat": "Natar",
                "hobbi" : "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Meira Listyaningrum",
                "nim"   : "122450011",
                "umur"  : "20",
                "asal"  : "Pesawaran",
                "alamat": "Airan",
                "hobbi" : "Membaca",
                "sosmed": "@meirasty_",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Rendi Alexander Hutagalung",
                "nim"   : "122450057",
                "umur"  : "20",
                "asal"  : "Tangerang",
                "alamat": "Kost Benawang",
                "hobbi" : "Menyanyi",
                "sosmed": "@rexander",
                "kesan" : "--",  
                "pesan" : "--"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=16M7mgyemT-sq1342aQTHHZks9YBo9fyR",#Andrian
            "https://drive.google.com/uc?export=view&id=15wF7gbUI2bLwmtFgWsqIuSRdevECZmQv",#Adisty
            "https://drive.google.com/uc?export=view&id=15wFJRrElcZMHuk8LSi-pD-CKFIMR3O8S",#NABILA
            "https://drive.google.com/uc?export=view&id=15xffZAK1VATRCfNlGUCZXfldvMym1Gwm",#Danang
            "https://drive.google.com/uc?export=view&id=15njS9GXw3wli0xLdugjeHDFfdB87YH-s",#farel
            "https://drive.google.com/uc?export=view&id=16-7x13vWiBlUaHPs808-HzLQvB1k6K0R",#Nabilah
            "https://drive.google.com/uc?export=view&id=15teyLrsKdLTmNgoq_lJNaDWUZ4Fazm8Z",#Elia
            "https://drive.google.com/uc?export=view&id=15v2PzPwdCTeQdEbe2jnyxu79nAY3fQtq",#Dhafin
            "https://drive.google.com/uc?export=view&id=15vu3x39CzBg4LTzm2FFMyFQ6-xix32Dp",#Alvia 
        ]
        data_list = [
            {
                "nama"  : "Andrian Agustinus Lumbangaol",
                "nim"   : "121450090",
                "umur"  : "21",
                "asal"  : "Sidikalang",
                "alamat": "Dekat Penjara",
                "hobbi" : "Lagi nyari",
                "sosmed": "@andriangaol",
                "kesan" : "--",  
                "pesan" : "--"

            },
            {
                "nama"  : "Adisty Syawaida Arianto",
                "nim"   : "121450136",
                "umur"  : "22",
                "asal"  : "Metro",
                "alamat": "Sukarame ",
                "hobbi" : "Nonton Film",
                "sosmed": "@adistysa_",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Nabila Azhari",
                "nim"   : "121450029",
                "umur"  : "21",
                "asal"  : "Simalungun",
                "alamat": "Airan ",
                "hobbi" : "Menghitung Uang",
                "sosmed": "@zhjung",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Danang Hilal Kurniawan",
                "nim"   : "122450085",
                "umur"  : "21",
                "asal"  : "Bandar Lampung",
                "alamat": "Airan",
                "hobbi" : "Belajar",
                "sosmed": "@dananghk_",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "farel Julio Akbar",
                "nim"   : "122450110",
                "umur"  : "20",
                "asal"  : "Bogor",
                "alamat": "Lapas",
                "hobbi" : "Kayang",
                "sosmed": "@farel_julio",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Nabilah Andika Fitriati",
                "nim"   : "121450139",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi" : "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Elia Meylani Simanjuntak",
                "nim"   : "122450026",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Korpri",
                "hobbi" : "Main Alat Musik",
                "sosmed": "@meylanielia",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Dhafin Razaqa Luthfi",
                "nim"   : "122450133",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi" : "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Alvia Asrinda Br.Gintng",
                "nim"   : "122450077",
                "umur"  : "20",
                "asal"  : "Binjai",
                "alamat": "Korpri",
                "hobbi" : "Nonton Winda",
                "sosmed": "@aliviagntinig",
                "kesan" : "--",  
                "pesan" : "--"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

elif menu == "Departemen MEDKRAF":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1xCAc4a2_MZ4WMaHogBGKh883_g0tU4c-",#lutfi
            "https://drive.google.com/uc?export=view&id=1NvsSBULzZGjepk3qQX4adf1QKKaC5c7l",#bintang
            "https://drive.google.com/uc?export=view&id=15G5JsFTE7ltflvhPRgbQD3IpmAN8oK7Z",#lutfi
            "https://drive.google.com/uc?export=view&id=1_unr2cpDQZ7clJr28IgsBjymuP8Yg4t1",#bintang
            "https://drive.google.com/uc?export=view&id=1vu7sBrdHUx3S8FsG-kNeWZC_EsNSN8k_",#lutfi
            "https://drive.google.com/uc?export=view&id=17d5RfUhmFucVA0OjJfl5XU3qYInm5XFX",#bintang
            "https://drive.google.com/uc?export=view&id=1e7r0ZrqM1SM5i3OzSGQUd-jVOgwa2Jso",#lutfi
            "https://drive.google.com/uc?export=view&id=1ApZzc4DEQMFafGPuo57KM_7px0Qfqm1q",#bintang
            "https://drive.google.com/uc?export=view&id=1HT-fg3Ic2o18x6A5B7_cFRuNID43vdwQ",#lutfi
            "https://drive.google.com/uc?export=view&id=1NQKCsM7SaK09YQFKuIEiSV12JTRtlcVm",#bintang
            "https://drive.google.com/uc?export=view&id=1TZXk2gB1IhWjY8eeiDtwuVwaokZzevy0",#lutfi
            "https://drive.google.com/uc?export=view&id=1gmtggIPZ266BDNiuj1_8LwfMHRrx0fBP",#bintang
            "https://drive.google.com/uc?export=view&id=1SHUWOwtU0DeUyFeXuza9OJdPA_yPPI2K",#bintang
            "https://drive.google.com/uc?export=view&id=1yWT8enIzGFDpGEZe61wXHDokFbDV1CGM",#lutfi
            "https://drive.google.com/uc?export=view&id=14uFiS6DxekPq8Jn_sunNcXckzyVUGB6Y",#bintang
            "https://drive.google.com/uc?export=view&id=1vKFKHuUNXTxLyaJvPglSfqKJTt1cryib",#lutfi
            "https://drive.google.com/uc?export=view&id=1iGaf7fVB8kEruP299akuiCzlVX5gPDoH",#bintang
        ]
        data_list = [
            {
                "nama"  : "Wahyudiyanto",
                "nim"   : "121450040",
                "umur"  : "22",
                "asal"  : "Makassar ",
                "alamat": "Sukarame",
                "hobbi" : "Menonton Film",
                "sosmed": "@",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Elok Fiola",
                "nim"   : "122450051",
                "umur"  : "19",
                "asal"  : "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi" : "Editing",
                "sosmed": "@elokfiola",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Arsyiah Azahra",
                "nim"   : "121450035",
                "umur"  : "21",
                "asal"  : "Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi" : "Nugas",
                "sosmed": "@arsyiah.__",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Cintya Bella",
                "nim"   : "122450066",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Teluk",
                "hobbi" : "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Najla Juwairia",
                "nim"   : "122450037",
                "umur"  : "19",
                "asal"  : "Sumatera Utara",
                "alamat": "Airan",
                "hobbi" : "Menulis, Membaca, Fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Rahma Neliyana",
                "nim"   : "122450036",
                "umur"  : "20",
                "asal"  : "Lampung",
                "alamat": "Sukarame",
                "hobbi" : "Baca Coding",
                "sosmed": "@rahmanellyana",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Try Yani Rizki Nur Rohmah",
                "nim"   : "122450020",
                "umur"  : "20",
                "asal"  : "Lampung Barat",
                "alamat": "Korpri",
                "hobbi" : "Bernyanyi dan Menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Muhammad Kaisar Firdaus",
                "nim"   : "121450135",
                "umur"  : "21",
                "asal"  : "Pesawaran",
                "alamat": "Pulau Damar",
                "hobbi" : "Lagi nyari",
                "sosmed": "@dino_lapet",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Dwi Ratna Anggraeni",
                "nim"   : "122450008",
                "umur"  : "20",
                "asal"  : "Jambi",
                "alamat": "Jalan Durian 5 Pemda",
                "hobbi" : "Membaca",
                "sosmed": "@dwiratnn_",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Gymnastiar Al Khoarizmy",
                "nim"   : "122450096",
                "umur"  : "20",
                "asal"  : "Serang",
                "alamat": "Lapangan Golf UIN",
                "hobbi" : "Baca komik",
                "sosmed": "@jimnn.as",
                "kesan" : "--",  
                "pesan" : "--"
            },
             {
                "nama"  : "Nasywa Nur Afifah",
                "nim"   : "122450125",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Jalan Durian 1 Pemda",
                "hobbi" : "Nonton drakor",
                "sosmed": "@nsywanaf",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Priska Silvia Ferantiana",
                "nim"   : "122450053",
                "umur"  : "19",
                "asal"  : "Palembang",
                "alamat": "Jalan Nangka 2",
                "hobbi" : "Baca novel yang bikin nangis",
                "sosmed": "@prskslv",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Muhammad Arsal Ranjana Utama",
                "nim"   : "121450111",
                "umur"  : "21",
                "asal"  : "Depok",
                "alamat": "Jalan Nangka 4",
                "hobbi" : "Ngoding",
                "sosmed": "@arsal.utama",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Abit Ahmad Oktarian",
                "nim"   : "122450042",
                "umur"  : "19",
                "asal"  : "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi" : "Ngoding, Gaming",
                "sosmed": "@abitahmad",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Akmal Faiz Abdillah",
                "nim"   : "122450114",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi" : "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Hermawan Manurung",
                "nim"   : "122450069",
                "umur"  : "20",
                "asal"  : "Bogor",
                "alamat": "Dekat jalan tol, Wisma Hana Hani",
                "hobbi" : "Bengong dan membaca buku",
                "sosmed": "@hermawan.mnrng",
                "kesan" : "--",  
                "pesan" : "--"
            },
            {
                "nama"  : "Khusnun Nisa",
                "nim"   : "122450078",
                "umur"  : "20",
                "asal"  : "Lampung Selatan",
                "alamat": "Belwis",
                "hobbi" : "Mengerjakan tugas",
                "sosmed": "@khusnun_nisa335",
                "kesan" : "--",  
                "pesan" : "--"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()
# Tambahkan menu lainnya sesuai kebutuhan

# Tambahkan menu lainnya sesuai kebutuhan
