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

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Gp3hQ8LYJg7z7AOF9kZGpkS_N77shnzx",#lutfi
            "https://drive.google.com/uc?export=view&id=1GZcOioJlC000XyfktJYUR2QJnDWhAuuM",#bintang
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
                "kesan" : "kakaknya baik",  
                "pesan" : "semoga lancar kuliahnya"
            },
            {
                "nama"  : "Annisa Cahyani Surya",
                "nim"   : "121450114",
                "umur"  : "21",
                "asal"  : "Tanggerang Selatan",
                "alamat": "Way Huwi",
                "hobbi" : "Membaca, Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan" : "kakaknya ramah",  
                "pesan" : "semoga kuliahnya lancar"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Gp3hQ8LYJg7z7AOF9kZGpkS_N77shnzx",#lutfi
            "https://drive.google.com/uc?export=view&id=1GZcOioJlC000XyfktJYUR2QJnDWhAuuM",#bintang
        ]
        data_list = [
                       {
                "nama"  : "Ericson Chandra Sihombing",
                "nim"   : "121450026",
                "umur"  : "21",
                "asal"  : "Bekasi",
                "alamat": "Khobam",
                "hobbi" : "Travelling",
                "sosmed": "@ericsonchandra99",
                "kesan" : "kakaknya baik",  
                "pesan" : "semoga lancar kuliahnya"
            },
            {
                "nama"  : "Elisabeth Claudia Simanjuntak",
                "nim"   : "122450123",
                "umur"  : "18",
                "asal"  : "Tanggerang",
                "alamat": " Kemiling",
                "hobbi" : " ",
                "sosmed": "@celisabethh_",
                "kesan" : "kakaknya ramah",  
                "pesan" : "semoga kuliahnya lancar"
            },
            {
                "nama"  : "Deyvan Loxefal",
                "nim"   : "121450148",
                "umur"  : "21",
                "asal"  : "Riau",
                "alamat": " Pulau Damar",
                "hobbi" : "Belajar",
                "sosmed": "@deyvanloo",
                "kesan" : "kakaknya ramah",  
                "pesan" : "semoga kuliahnya lancar"
            },
            {
                "nama"  : "Nisrina Nur Afifah",
                "nim"   : "122450033",
                "umur"  : "19",
                "asal"  : "Bekasi",
                "alamat": " Sukarame",
                "hobbi" : " ",
                "sosmed": "@afifahhnsrn",
                "kesan" : " ",  
                "pesan" : " "
            },
            {
                "nama"  : "M. Farhan Athaulloh",
                "nim"   : "121450117",
                "umur"  : "21",
                "asal"  : "Lampung",
                "alamat": "Kota Baru",
                "hobbi" : " ",
                "sosmed": "@mfarhan.ath",
                "kesan" : "kakaknya ramah",  
                "pesan" : " "
            },
            {
                "nama"  : "Kemas Veriandra Ramadhan",
                "nim"   : "122450016",
                "umur"  : "19",
                "asal"  : "Bekasi",
                "alamat": "Kojo ",
                "hobbi" : "Mainin ular Python digital",
                "sosmed": "@kemasverii",
                "kesan" : " ",  
                "pesan" : " "
            },
            {
                "nama"  : "Presilia",
                "nim"   : "122450081",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Kota Baru",
                "hobbi" : " ",
                "sosmed": "@presiliamg",
                "kesan" : " ",  
                "pesan" : " "
            },
            {
                "nama"  : "Rafa Aqilla Jungjunan",
                "nim"   : "122450142",
                "umur"  : "20",
                "asal"  : "Pekan Baru",
                "alamat": "Belwis",
                "hobbi" : " ",
                "sosmed": "@rafaaqilla",
                "kesan" : " ",  
                "pesan" : " "
            },
            {
                "nama"  : "Sahid Maulana",
                "nim"   : "122450109",
                "umur"  : "21",
                "asal"  : "Depok",
                "alamat": "Airan Raya",
                "hobbi" : " ",
                "sosmed": "@sahid_maulana",
                "kesan" : " ",  
                "pesan" : " "
            },
            {
                "nama"  : "Vanessa Olivia Rose",
                "nim"   : "121450108",
                "umur"  : "20",
                "asal"  : "Jakarta",
                "alamat": "Perum Korpri",
                "hobbi" : " ",
                "sosmed": "@roselivnes__ ",
                "kesan" : " ",  
                "pesan" : " "
            },
            {
                "nama"  : "Allya Nurul Islami Pasha",
                "nim"   : "122450033",
                "umur"  : "20",
                "asal"  : "Sumatera Barat",
                "alamat": "Gg. Perwira Belwis",
                "hobbi" : " ",
                "sosmed": "@allyaislami",
                "kesan" : " ",  
                "pesan" : " "
            },
            {
                "nama"  : "Eksanty Febriana Sukma Islamiaty",
                "nim"   : "122450001",
                "umur"  : "20",
                "asal"  : "Pringsewu",
                "alamat": "Natar",
                "hobbi" : " ",
                "sosmed": "@eksantyfebriana",
                "kesan" : " ",  
                "pesan" : " "
            },
            {
                "nama"  : "M. Deriansyah Okutra",
                "nim"   : "122450051",
                "umur"  : "19",
                "asal"  : "Kayu Agung",
                "alamat": "Kedaton",
                "hobbi" : " ",
                "sosmed": "@dransyah_",
                "kesan" : " ",  
                "pesan" : " "
            },
            {
                "nama"  : "Oktavia Nurwendah Puspita Sari",
                "nim"   : "122450041",
                "umur"  : "20",
                "asal"  : "Lampung Timur",
                "alamat": "Way Huwi",
                "hobbi" : " ",
                "sosmed": "@oktavianrwnda",
                "kesan" : " ",  
                "pesan" : " "
            },
            {
                "nama"  : "Gede Moena",
                "nim"   : "121450014",
                "umur"  : "21",
                "asal"  : "Bekasi",
                "alamat": "Korpri Raya",
                "hobbi" : " ",
                "sosmed": "@gedemoenaa",
                "kesan" : " ",  
                "pesan" : " "
            },
            {
                "nama"  : "Jaclin Alcavella",
                "nim"   : "122450015",
                "umur"  : "19",
                "asal"  : "Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi" : " ",
                "sosmed": "@jaclinaclcv_",
                "kesan" : " ",  
                "pesan" : " "
            },
            {
                "nama"  : "Rafly Prabu Darmawan",
                "nim"   : "122450140",
                "umur"  : "20",
                "asal"  : "Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi" : " ",
                "sosmed": "@raflyy_pd",
                "kesan" : " ",  
                "pesan" : " "
            },
            {
                "nama"  : "Syalaisha Andini Putriansyah",
                "nim"   : "122450111",
                "umur"  : "21",
                "asal"  : "Tangerang",
                "alamat": "KSukarame",
                "hobbi" : " ",
                "sosmed": "@syalaisha.i_",
                "kesan" : " ",  
                "pesan" : " "
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Gp3hQ8LYJg7z7AOF9kZGpkS_N77shnzx",#lutfi
            "https://drive.google.com/uc?export=view&id=1GZcOioJlC000XyfktJYUR2QJnDWhAuuM",#bintang
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
                "kesan" : "kakaknya baik",  
                "pesan" : "semoga lancar kuliahnya"
            },
            {
                "nama"  : "Annisa Cahyani Surya",
                "nim"   : "121450114",
                "umur"  : "21",
                "asal"  : "Tanggerang Selatan",
                "alamat": "Way Huwi",
                "hobbi" : "Membaca, Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan" : "kakaknya ramah",  
                "pesan" : "semoga kuliahnya lancar"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Gp3hQ8LYJg7z7AOF9kZGpkS_N77shnzx",#lutfi
            "https://drive.google.com/uc?export=view&id=1GZcOioJlC000XyfktJYUR2QJnDWhAuuM",#bintang
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
                "kesan" : "kakaknya baik",  
                "pesan" : "semoga lancar kuliahnya"
            },
            {
                "nama"  : "Annisa Cahyani Surya",
                "nim"   : "121450114",
                "umur"  : "21",
                "asal"  : "Tanggerang Selatan",
                "alamat": "Way Huwi",
                "hobbi" : "Membaca, Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan" : "kakaknya ramah",  
                "pesan" : "semoga kuliahnya lancar"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Gp3hQ8LYJg7z7AOF9kZGpkS_N77shnzx",#lutfi
            "https://drive.google.com/uc?export=view&id=1GZcOioJlC000XyfktJYUR2QJnDWhAuuM",#bintang
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
                "kesan" : "kakaknya baik",  
                "pesan" : "semoga lancar kuliahnya"
            },
            {
                "nama"  : "Catherine Firdhasari Maulina Sinaga",
                "nim"   : "121450071",
                "umur"  : "20",
                "asal"  : "Sumatera Utara",
                "alamat": "Airan",
                "hobbi" : "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan" : "kakaknya ramah",  
                "pesan" : "semoga kuliahnya lancar"
            },
            {
                "nama"  : "M.Akbar Resdika",
                "nim"   : "121450066",
                "umur"  : "20",
                "asal"  : "Lampung Barat (Way Tenun)",
                "alamat": "Labuhan Dalam (Untung)",
                "hobbi" : "Suka kucing tapi gak suka ngurusnya",
                "sosmed": "@akbar_restika",
                "kesan" : "Selalu komunikatif dan informatif dalam menjelaskan perannya. Penjelasannya yang jelas membantu saya memahami tugas dan tanggung jawab yang ada di badan ini",  
                "pesan" : "Teruslah semangat dalam menjalankan tugas dan perannya, semoga terus informatif dan komunikatif selalu dalam memberikan penjelasan"
            },
            {
                "nama"  : "Renta Siahaan",
                "nim"   : "122450070",
                "umur"  : "21",
                "asal"  : "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi" : "Membaca dan Memancing",
                "sosmed": "@renita.shn",
                "kesan" : "Selalu komunikatif dan informatif dalam menjelaskan perannya. Penjelasannya yang jelas membantu saya memahami tugas dan tanggung jawab yang ada di badan ini",  
                "pesan" : "Teruslah semangat dalam menjalankan tugas dan perannya, semoga terus informatif dan komunikatif selalu dalam memberikan penjelasan"
            },
            {
                "nama"  : "Salwa Farhanatussaidah",
                "nim"   : "122450055",
                "umur"  : "20",
                "asal"  : "Pesawaran",
                "alamat": "Airan",
                "hobbi" : "Nonton",
                "sosmed": "@slwfhn_694",
                "kesan" : "Selalu komunikatif dan informatif dalam menjelaskan perannya. Penjelasannya yang jelas membantu saya memahami tugas dan tanggung jawab yang ada di badan ini",  
                "pesan" : "Teruslah semangat dalam menjalankan tugas dan perannya, semoga terus informatif dan komunikatif selalu dalam memberikan penjelasan"
            },
            {
                "nama"  : "Rendra Eka Prayoga",
                "nim"   : "122450112",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Belwis",
                "hobbi" : "Mancing Ikan Mas",
                "sosmed": "@rendraepr",
                "kesan" : "Selalu komunikatif dan informatif dalam menjelaskan perannya. Penjelasannya yang jelas membantu saya memahami tugas dan tanggung jawab yang ada di badan ini",  
                "pesan" : "Teruslah semangat dalam menjalankan tugas dan perannya, semoga terus informatif dan komunikatif selalu dalam memberikan penjelasan"
            },
            {
                "nama"  : "Yosia Retare Banurea",
                "nim"   : "121450149",
                "umur"  : "20",
                "asal"  : "Dairi, Sumatera Utara",
                "alamat": "Perum Griya Indah",
                "hobbi" : "Tidur",
                "sosmed": "@yosiabanurea",
                "kesan" : "baik dan asik diajak ngobrol",  
                "pesan" : "semoga harapan baik selalu ada untuk kakak "
            },
            {
                "nama"  : " Ari Sigit",
                "nim"   : "121450069",
                "umur"  : "23",
                "asal"  : "Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobbi" : "Futsal",
                "sosmed": "@ari_sigit17",
                "kesan" : "ramah diajak ngobrol",  
                "pesan" : "Semoga bisa mencapai semua impian dan cita-citanya"
            },
            {
                "nama"  : "Josua Panggabean",
                "nim"   : "122450061",
                "umur"  : "21",
                "asal"  : "Pematang Siantar",
                "alamat": "Gerbang Barat",
                "hobbi" : "Menonton",
                "sosmed": "@josuapanggabean_",
                "kesan" : "Baik dan Murah Senyum",  
                "pesan" : "Jangan lupa untuk jaga kesehatan dan semangat"
            },
            {
                "nama"  : "Azizah Kusumah Putri",
                "nim"   : "122450068",
                "umur"  : "21",
                "asal"  : "Lampung Selatan",
                "alamat": "Natar",
                "hobbi" : "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan" : "ramah banget",  
                "pesan" : "sukses terus kak"
            },
            {
                "nama"  : "Meira Listyaningrum",
                "nim"   : "122450011",
                "umur"  : "20",
                "asal"  : "Pesawaran",
                "alamat": "Airan",
                "hobbi" : "Membaca",
                "sosmed": "@meirasty_",
                "kesan" : "baik banget",  
                "pesan" : "Jaga kesehatan selalu"
            },
            {
                "nama"  : "Rendi Alexander Hutagalung",
                "nim"   : "122450057",
                "umur"  : "20",
                "asal"  : "Tangerang",
                "alamat": "Kost Benawang",
                "hobbi" : "Menyanyi",
                "sosmed": "@rexander",
                "kesan" : "seru banget",  
                "pesan" : "Tetap semangat menjalani kuliah"
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
            "https://drive.google.com/uc?export=view&id=1Gp3hQ8LYJg7z7AOF9kZGpkS_N77shnzx",#lutfi
            "https://drive.google.com/uc?export=view&id=1GZcOioJlC000XyfktJYUR2QJnDWhAuuM",#bintang
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
                "kesan" : "kakaknya baik",  
                "pesan" : "semoga lancar kuliahnya"
            },
            {
                "nama"  : "Annisa Cahyani Surya",
                "nim"   : "121450114",
                "umur"  : "21",
                "asal"  : "Tanggerang Selatan",
                "alamat": "Way Huwi",
                "hobbi" : "Membaca, Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan" : "kakaknya ramah",  
                "pesan" : "semoga kuliahnya lancar"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()
# Tambahkan menu lainnya sesuai kebutuhan

# Tambahkan menu lainnya sesuai kebutuhan
