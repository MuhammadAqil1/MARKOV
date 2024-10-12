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
            "https://drive.google.com/uc?export=view&id=1mFyCD4XyjbGMcAWPs93sEvRM95IH3Wrh", #Bang Kharisma
            "https://drive.google.com/uc?export=view&id=1q2-oFxsQb2C4hhmjpF1SWUAsK_RMP1FG", #Bang Pandra
            "https://drive.google.com/uc?export=view&id=15Pyj65fZk_tixlXrfK7fnD2yvU13xQst", #kak meliza
            "https://drive.google.com/uc?export=view&id=1NaGMZu1QfB5LpHC0iKL8TSks14BJmeHJ", #kak putri
            "https://drive.google.com/uc?export=view&id=1v5MKlnnaAzB8UB6nozXRe5TWfgjkXMFw", #kak hartiti
            "https://drive.google.com/uc?export=view&id=1ZlQVIQQ07KSUnLW8Q2n-Nm4Becbag6vY", #kak nadila


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
                "kesan" : "Sanggat berwibawa sekali dan memperlihatkan jiwa kepemimpinan yang kuat",  
                "pesan" : "Semoga semakin berkembang lagi dan lebih baik lagi di kehidupan organisasi maupun kehidupan pribadi"
            },
            {
                "nama"  : "Pandra Insani Putra Azwan",
                "nim"   : "121450137",
                "umur"  : "21",
                "asal"  : "Bukit Kemuning, Lampung Utara",
                "alamat": "Bawen 2",
                "hobbi" : "Bermain gitar dan menyanyi",
                "sosmed": "@pandrainsni27",
                "kesan" : "Sanggat ceria sekali dan humoris dan banyak ceritanya",  
                "pesan" : "Semoga kedepannya lebih maju lagi dan semangat menjalani hari dan kuliahnya"
            },
            {
                "nama"  : "Meliza Wulandari",
                "nim"   : "121450065",
                "umur"  : "20",
                "asal"  : "Pagar Alam, Sumatera Selatan",
                "alamat": "Kotabaru",
                "hobbi" : "Nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan" : "Kakak pendiam tetapi sanggat ceria dan merespon setiap cerita yang kami sampaikan ",  
                "pesan" : "Semoga semakin ceria dan semanggat terus"
            },
            {
                "nama"  : "Putri Maulida Chairani",
                "nim"   : "121450050",
                "umur"  : "21",
                "asal"  : "Payakumbuh, Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi" : "Dengerin bang pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan" : "Kakak lebih banyak diam tetapi mengikuti alur cerita yang kami sampaikan dan mendengarkan dengan baik",  
                "pesan" : "Semoga kedepannya lebih ceria lagi dan tetap menjalani hari dengan hati bahagia"
            },
            {
                "nama"  : "Hartiti Fadilah",
                "nim"   : "121450031",
                "umur"  : "21",
                "asal"  : "Palembang",
                "alamat": "Pemda",
                "hobbi" : "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan" : "Kakak ceria sekali walaupun agak terlihat jutek namun ternyata nular tertawanya",  
                "pesan" : "Semoga tetap menjadi diri sendiri dan bahagia terus"
            },
            {
                "nama"  : "Nadilla Andara Putri",
                "nim"   : "121450003",
                "umur"  : "21",
                "asal"  : "Metro",
                "alamat": "KotaBaru",
                "hobbi" : "Membaca",
                "sosmed": "@ndillaandr26",
                "kesan" : "Ternyata kita satu kota tapi beda tempat, kakaknya juga memberikan informasi dengan baik dan cakap",  
                "pesan" : "Semoga selalu sehat dan semangat menjalani kuliahnya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1sBQzX-V3RmLTOHzbIe1RuqK5bZsYKCNN",
            "https://drive.google.com/uc?export=view&id=1-WudblXJAT3lhDi2rr4wf305DYX7LEmK",
            "https://drive.google.com/uc?export=view&id=1yjXLjN0jUwGgqe-nY6i1XRjvj6R3Hyj3",
            "https://drive.google.com/uc?export=view&id=14oUGJl9x_YzpjmsxkjRT2NSCvJ1yi2wF",
            "https://drive.google.com/uc?export=view&id=1WFgX0N42ZNFKw9rg9_b8JbwLIXbEGUcN",
            "https://drive.google.com/uc?export=view&id=1Yc_tOSxcUKbk2lKYaA3sNI4b8Qy-Ob8z",
            "https://drive.google.com/uc?export=view&id=1WFgX0N42ZNFKw9rg9_b8JbwLIXbEGUcN",
            "https://drive.google.com/uc?export=view&id=1TLaCfP3PJlp_xWekGsdowmzy9PMj2bam",
            "https://drive.google.com/uc?export=view&id=1SsbuhirfvLG948n5u4S5S2kCPHTBi_lk",
            "https://drive.google.com/uc?export=view&id=1Oy7t7LDHTaO6t0peA5nBWaLhYW5jP_nO",
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
                "kesan" : "VIbe kakaknya ceria sekali dan sanggat mengayomi kami sebagai mahasiswa yang masih awam",  
                "pesan" : "Tetap teruskan hal-hal baik yang kakak punya karena ga vibe kakak ga semua orang punya"
            },
            {
                "nama"  : "Annisa Cahyani Surya",
                "nim"   : "121450114",
                "umur"  : "21",
                "asal"  : "Tanggerang Selatan",
                "alamat": "Way Huwi",
                "hobbi" : "Membaca, Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan" : "Memberikan materi dan penjelasan baik",  
                "pesan" : "Tetap semanggat dan terus menjadi orang yang baik"
            },
            {
                "nama"  : "Wulan Sabina",
                "nim"   : "121450150",
                "umur"  : "21",
                "asal"  : "Medan",
                "alamat": "Raden Saleh",
                "hobbi" : "Nonton Drakor",
                "sosmed": "@wlnsbn0",
                "kesan" : "Tidak banyak bicara ketimbang yang lain tapi sanggat memberikan materi dengan jelas",  
                "pesan" : "Tetap bahagia dan jangan lupa tetap tersenyum"
            },
            {
                "nama"  : "Annisa Dini Amaliya",
                "nim"   : "121450081",
                "umur"  : "21",
                "asal"  : "Tanggerang",
                "alamat": "Jati Agung",
                "hobbi" : "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan" : "Kakak memang terlihat sanggat suka bertemu orang banyak jadi vibe kebahagiaan itu menular kepada kami",  
                "pesan" : "Terus bahagia dan tularkan kebahagian itu bersama kami"
            },
            {
                "nama"  : "Anisa Fitriyani",
                "nim"   : "121450150",
                "umur"  : "21",
                "asal"  : "Medan",
                "alamat": "Raden Saleh",
                "hobbi" : "Nonton Drakor",
                "sosmed": "@wlnsbn0",
                "kesan" : "Kakaknya baik dan memberikan banyak pelajaran kepada kami",  
                "pesan" : "Terus semanggat dan tetap sehat selalu"
            },
            {
                "nama"  : "Mirzan Yusuf Rabbani",
                "nim"   : "122450118",
                "umur"  : "20",
                "asal"  : "Jakarta",
                "alamat": "Korpri",
                "hobbi" : "Main Kucing",
                "sosmed": "@myrrinn",
                "kesan" : "Memang tidak banyak bicara namun memberikan kesan baik terhadap kami",  
                "pesan" :"Semoga bahagia dan semanggat menjalani hari kuliahnya"
            },
            {
                "nama"  : "Dhea Amelia Putri",
                "nim"   : "122450004",
                "umur"  : "20",
                "asal"  : "Sukabumi, Jawa Barat",
                "alamat": "Natar",
                "hobbi" : "Suka Ikut Tes SKD",
                "sosmed": "@dhea_wedding",
                "kesan" : "Kakaknya baik dan penuh keceriaan",  
                "pesan" : "Semoga tetap kuat sampai akhir"
            },
            {
                "nama"  : "Muhammad Fahrul Aditya",
                "nim"   : "121450156",
                "umur"  : "22",
                "asal"  : "Surakarta, Jawa Tengah",
                "alamat": "Pahoman",
                "hobbi" : "Melukis, badminton, hiking, ngopi, dengerin music, nonton film dan ngoding",
                "sosmed": "@fhrul.pdf",
                "kesan" : "Tidak banyak bicara namun mendengarkan kami dengan seksama dan mengikuti alurnya ",  
                "pesan" : "Semoga hoby nya berkembang lebih banyak lagi"
            },
            {
                "nama"  : "Berlianda Enda Putri",
                "nim"   : "122450065",
                "umur"  : "21",
                "asal"  : "Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi" : "Main Game",
                "sosmed": "@berlyyanda",
                "kesan" : "Sanggat mengikuti apa yang kita bicarakan dengan baik",  
                "pesan" : "Tetap semanggat dan jangan lupa tetap berdoa"
            },
            {
                "nama"  : "Jeremia Susanto",
                "nim"   : "122450022",
                "umur"  : "20",
                "asal"  : " Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi" : "Marah-marah",
                "sosmed": "@jeremia_s_",
                "kesan" : "Baik dan mampu mengikuti pembicaraan kita",  
                "pesan" : "Semoga tetap menjadi orang baik dan tetap semanggat"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

# Tambahkan menu lainnya sesuai kebutuhan
