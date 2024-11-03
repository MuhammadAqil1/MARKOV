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
            "https://drive.google.com/uc?export=view&id=1YXRTbajbrY9VLIagPNexpAkLA4Dw6B0S",##Kahim
            "https://drive.google.com/uc?export=view&id=1YLYRSnr9Q0Sx0Jt4cbUvbwCLoD_dn5nS",##Sekjen
            "https://drive.google.com/uc?export=view&id=1YXdeSTr53EvGZF7O9tLeRkGP9jVGspaW",##Sekretaris kak meliza
            "https://drive.google.com/uc?export=view&id=1Yto5G_-TbJhuYoa34IQxFvseDnwccuVp",##Sekretaris kak putri 
            "https://drive.google.com/uc?export=view&id=1YPaDA1_BC-mkwsG5qGGtcdn-fAKOEWfD",##Bendahara kak hartiti
            "https://drive.google.com/uc?export=view&id=1YU-BEVfEKVYifOXPvN75it_jzLWQ-42N",##Bendahara kak nadilla
        ]
        data_list = [
            {
                "nama": "Kharisma Gumilang",
                "nim": "121450142",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Kandis",
                "hobbi": "Denger musik",
                "sosmed": "@gumilangkharisma",
                "kesan": "abang sangat inspiratif, karena berhasil membagi waktu antara kuliah dan aktivitas di organisasi dengan sangat baik.",  
                "pesan":"Semoga sukses dalam TA dan segala rencana yang kakak impikan! Teruslah berjuang dan jangan ragu untuk mengejar cita-cita!"
            },
            {
                "nama": "Pandra Insani Putra Azwan",
                "nim": "121450137",
                "umur": "21",
                "asal":"Bukitr Kemuning, Lampung Utara",
                "alamat": "Bawen 2",
                "hobbi": "Bermain gitar dan menyanyi",
                "sosmed": "@pandrainsni27",
                "kesan": "Kakaknya asik, bisa jadi teman diskusi yang seru dan inspiratif.",  
                "pesan":"Tetap semangat, bang! Semoga semua usaha dan kerja kerasnya membuahkan hasil. Jangan lupa untuk selalu enjoy di setiap momen!"
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam, Sumatera Selatan",
                "alamat": "Kota baru",
                "hobbi": "Nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "Kakak keren banget!",  
                "pesan":"Teruskan kerja kerasnya, Kak! Semoga semua cita-cita dan rencana Kakak bisa tercapai. Jangan lupa untuk selalu istirahat, ya!"
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh, Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin bang pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kakak keren banget, kakak punya kemampuan manajemen waktu yang luar biasa, bikin kita semua iri!",  
                "pesan":"Jangan pernah ragu untuk melangkah, Kak! Semoga semua impian bisa terwujud dan sukses di setiap langkah!"
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "Kakak punya kemampuan manajemen waktu yang luar biasa, bikin kita semua iri!",  
                "pesan":"Semoga Kakak selalu bahagia dan sukses di segala hal, ya! Tetap jadi diri sendiri!"
            },
            {
                "nama": "Nadilla Andara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kota Baru",
                "hobbi": "Membaca",
                "sosmed": "@ndillaandr26",
                "kesan": "Kakak sangat humble, kakak punya kemampuan manajemen waktu yang luar biasa, bikin kita semua iri!",  
                "pesan":"Semoga Kakak selalu bahagia dan sukses di segala hal, ya! Tetap jadi diri sendiri!!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ekzuBmLpF4lYssumHeUoftkqABwQi4X0",#kak tri
            "https://drive.google.com/uc?export=view&id=1eJSNMpeappvDO-TXOetEjNq9U9THt5tb",#kak annisa cahya
            "https://drive.google.com/uc?export=view&id=1eRSdDdrJHc2IlQPJygUG3hEWPaQzMkPV",#kak wulan sabina
            "https://drive.google.com/uc?export=view&id=1edAgkaJOuOoKSv02NCFd4JKstrpg5cdO",# kak anisa dini
            "https://drive.google.com/uc?export=view&id=1eZwkK80AwJKOa9JtdWYBkBLjoFwAabWT",#anisa Fitriyani
            "https://drive.google.com/uc?export=view&id=1eP0IICGKitqbmAsIq3sr2lZvGgmVllGl",#Mirzan
            "https://drive.google.com/uc?export=view&id=1eltleTi5yS2R4NkfzqcCQHENOnF36kmO",# dhea
            "https://drive.google.com/uc?export=view&id=1efYncfXLImIDgQ-1ISrzagbhOo2DVu7a",# fahrul
            "https://drive.google.com/uc?export=view&id=1emg-cM6aWSMhYtXnEhl2bzErLgONcXE3",# berliana
            "https://drive.google.com/uc?export=view&id=1e_z6GmbIEc_iKfDlA7HgM9q2qc27eBXM",#bang jere
 
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
                "kesan" : "Kakak keren banget, asyik, juga humble! Selalu bisa bikin suasana jadi lebih asyik di kampus.",  
                "pesan" : "Keep it up, Kak! Semoga selalu jadi inspirasi buat kita semua. Jangan lupa untuk tetap senyum ya!"
            },
            {
                "nama"  : "Annisa Cahyani Surya",
                "nim"   : "121450114",
                "umur"  : "21",
                "asal"  : "Tanggerang Selatan",
                "alamat": "Way Huwi",
                "hobbi" : "Membaca, Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan" : "Kakak asyik dan keren",  
                "pesan" : "Semangat terus, Kak! Semoga bisa terus menginspirasi dan capai semua yang diimpikan!"
            },
            {
                "nama"  : "Wulan Sabina",
                "nim"   : "121450150",
                "umur"  : "21",
                "asal"  : "Medan",
                "alamat": "Raden Saleh",
                "hobbi" : "Nonton Drakor",
                "sosmed": "@wlnsbn0",
                "kesan" : "Kakak asyik dan keren",  
                "pesan" : "Semangat terus, Kak! Semoga bisa terus menginspirasi dan capai semua yang diimpikan!"
            },
            {
                "nama"  : "Annisa Dini Amalia",
                "nim"   : "121450081",
                "umur"  : "21",
                "asal"  : "Tanggerang",
                "alamat": "Jati Agung",
                "hobbi" : "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan" : "Kakak asyik dan keren",  
                "pesan" : "Semoga Kakak selalu dikelilingi orang-orang baik dan penuh cinta! Sukses, ya!"
            },
            {
               "nama"  : "Anisa Fitriyani",
                "nim"   : "122450019",
                "umur"  : "20",
                "asal"  : "Batam",
                "alamat": "Kalianda",
                "hobbi" : "Membaca Al-Waqiah setiap maghrib",
                "sosmed": "@ansftynn_",
                "kesan" : "Kakak asyik dan keren",  
                "pesan" : "Semoga Kakak selalu dikelilingi orang-orang baik dan penuh cinta! Sukses, ya!"
            },
            {
                "nama"  : "Mirzan Yusuf Rabbani",
                "nim"   : "122450118",
                "umur"  : "20",
                "asal"  : "Jakarta",
                "alamat": "Korpri",
                "hobbi" : "Main Kucing",
                "sosmed": "@myrrinn",
                "kesan" : "Abang keren banget",  
                "pesan" :"Semoga Kakak selalu dikelilingi orang-orang baik dan penuh cinta! Sukses, ya!"
            },
            {
                "nama"  : "Dhea Amelia Putri",
                "nim"   : "122450004",
                "umur"  : "20",
                "asal"  : "Sukabumi, Jawa Barat",
                "alamat": "Natar",
                "hobbi" : "Suka Ikut Tes SKD",
                "sosmed": "@dhea_wedding",
                "kesan" : "Kakak asyik dan keren banget",  
                "pesan" : "Semoga Kakak selalu dikelilingi orang-orang baik dan penuh cinta! Sukses, ya!"
            },
            {
                "nama"  : "Muhammad Fahrul Aditya",
                "nim"   : "121450156",
                "umur"  : "22",
                "asal"  : "Surakarta, Jawa Tengah",
                "alamat": "Pahoman",
                "hobbi" : "Melukis, badminton, hiking, ngopi, dengerin music, nonton film dan ngoding",
                "sosmed": "@fhrul.pdf",
                "kesan" : "Abang itu seru, bisa bikin kita ketawa di tengah tekanan kuliah!",  
                "pesan" : "Semoga senyummu selalu ada, Kak! Terus bawa kebahagiaan ke dalam hidup kami!"
            },
            {
                "nama"  : "Berlianda Enda Putri",
                "nim"   : "122450065",
                "umur"  : "21",
                "asal"  : "Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi" : "Main Game",
                "sosmed": "@berlyyanda",
                "kesan" : "Kakak asyik dan keren",  
                "pesan" : "Semangat terus, ya, Kak! Semoga perjalanan ke depan penuh dengan kebahagiaan!"
            },
            {
                "nama"  : "Jeremia Susanto",
                "nim"   : "122450022",
                "umur"  : "20",
                "asal"  : " Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi" : "Marah-marah",
                "sosmed": "@jeremia_s_",
                "kesan" : "Abangnya asik dan keren juga",  
                "pesan" : "Semoga semua impian abang bisa tercapai! dan bahagia selalu"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1e8NYvFt_CVk70S64KRv9lPGPTCm2hAIb",#lutfi
            "https://drive.google.com/uc?export=view&id=1eAUf48pD_DSPRQHv1KIjejOi_XHFKZWT",#bintang
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
                "kesan" : "Kakak selalu memberikan penjelasan yang jelas dan mudah dipahami. Motivasi dari kakak juga sangat membangkitkan semangat kami untuk menyelesaikan tugas!",  
                "pesan" : "Semoga semua aktivitas kakak, baik di kampus maupun di luar, selalu berjalan lancar. Tetap semangat ya, Kak!"
            },
            {
                "nama"  : "Rian Bintang Wijaya",
                "nim"   : "122450094",
                "umur"  : "20",
                "asal"  : "Palembang, Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi" : "Mendengar Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan" : "Kakak selalu memberikan penjelasan yang jelas dan mudah dipahami. Motivasi dari kakak juga sangat membangkitkan semangat kami untuk menyelesaikan tugas!",  
                "pesan" : "Semoga semua aktivitas kakak, baik di kampus maupun di luar, selalu berjalan lancar. Tetap semangat ya, Kak!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
             "https://drive.google.com/uc?export=view&id=1QsnHsFDw6cNZWO25E6g5CzN1fazqC3CK", #bang erickson dn
            "https://drive.google.com/uc?export=view&id=1QnK0iYO-pIOggjwxq7qpcIRfy-YQQVBA", #kak abeth dn
            "https://drive.google.com/uc?export=view&id=1QgEH_XM877ZG5woIc1yA-yl7ka1onOos", #kak afifah dn
            "https://drive.google.com/uc?export=view&id=1R2Oll7sxtpyNsApQ1AkRZgjTeTII1FBe", #kak allya dn
            "https://drive.google.com/uc?export=view&id=1QhIiVs5hNT6EmGjYyM5CDp-LvQTsWB9r", #kak hanum dn
            "https://drive.google.com/uc?export=view&id=1QsEjxtz4M9xZmlxDCnsHifrL_Yz3pjtf", #bang ferdy dn
            "https://drive.google.com/uc?export=view&id=1R7NjVx3LyPloPfW0hEsGHu2qhitPRgbU", #bang deri dn
            "https://drive.google.com/uc?export=view&id=1QzGEwC35YX9Mra9JcWN0OL2BGGYuIHHG", #kak oktavia dn
            "https://drive.google.com/uc?export=view&id=1Q6dWOCHc6faVLAij0B1NTXQRHkDMmVtn", #bang deyvan dn
            "https://drive.google.com/uc?export=view&id=1QGJ6ZvnfZbQDAKGJRXJ4M4cYxCoxGB0I", #bang ibnu dn
            "https://drive.google.com/uc?export=view&id=1QYukAPdo_1_YkTnZD_-2_B7zbGJKI-Mt", #bang jo dn
            "https://drive.google.com/uc?export=view&id=1Qdq_CnfPtqPbJU66zqGzS-XwcIlZdWsU", #bang kemas dn
            "https://drive.google.com/uc?export=view&id=1QUtFmgAqlvQyXE66rzsNLMo84C4vhI4u", #bang leonard dn
            "https://drive.google.com/uc?export=view&id=1R0553fMgcopI94NsrNc-3_TZVWxNBw4v", #kak presilia dn
            "https://drive.google.com/uc?export=view&id=1QSDmFqYWLC8FtbpGrRff-Ngiu3zgHCqw", #kak rafa dn
            "https://drive.google.com/uc?export=view&id=1Qf_GumaM-Pm70t5nnDLPkly7wUYHlyRo", #bang sahid dn
            "https://drive.google.com/uc?export=view&id=1Qds8DrC2q45WGi7kUyMZ0EuhRVLH5rhj", #kak vanes dn
            "https://drive.google.com/uc?export=view&id=1RwrsLq1PUz7KfsxJMMeKcSIkZZVs5Vu4", #bang ateng dn
            "https://drive.google.com/uc?export=view&id=1RT1GYFu-LWG4ReyEqxEic2kCuSmJNpng", #bang gede dn
            "https://drive.google.com/uc?export=view&id=1R7PnEV91lDjFfpiv-9zDeb14V4bzC7LF", #kak jaclin dn
            "https://drive.google.com/uc?export=view&id=1RT1GYFu-LWG4ReyEqxEic2kCuSmJNpng", #bang rafly dn
            "https://drive.google.com/uc?export=view&id=1RQQewSzCw8ETGX2VHCHqrLfpnlAOO_ni", #kak dini dn

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
                "kesan" : "Abang keren banget dan baik juga",  
                "pesan" : "Semoga sehat selalu dan dilancarkan kuliahnya sampai akhir serta lulus tepat waktu",
            },
            {
                "nama"  : "Elisabeth Claudia Simanjuntak",
                "nim"   : "122450123",
                "umur"  : "18",
                "asal"  : "Pekanbaru",
                "alamat": "Sukarame",
                "hobbi" : "Memancing keributan",
                "sosmed": "@celisabethh_",
                "kesan" : "kakak keren banget dan baik juga",  
                "pesan" : "Semoga sehat selalu dan dilancarkan kuliahnya sampai akhir serta lulus tepat waktu",
            },
            {
                "nama"  : "Nisrina Nur Afifah",
                "nim"   : "122450052",
                "umur"  : "19",
                "asal"  : "Bekasi",
                "alamat": "Sukarame",
                "hobbi" : "Nabok orang",
                "sosmed": "@afifahhnsrn",
                "kesan" : "kakak keren banget dan baik juga",  
                "pesan" : "Semoga sehat selalu dan dilancarkan kuliahnya sampai akhir serta lulus tepat waktu",
            },
            {
                "nama"  : "Allya Nurul Islami Pasha",
                "nim"   : "122450033",
                "umur"  : "20",
                "asal"  : "Sumatera Barat",
                "alamat": "Gang Perwira, Belwis",
                "hobbi" : "Nonton Dracin",
                "sosmed": "@allyaislami_",
                "kesan" : "kakak keren banget dan baik juga",  
                "pesan" : "Semoga sehat selalu dan dilancarkan kuliahnya sampai akhir serta lulus tepat waktu",
            },
            {
                "nama"  : "Farahanum Afifah Ardiansyah",
                "nim"   : "122450056",
                "umur"  : "20",
                "asal"  : "Padang, Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi" : "Tidur",
                "sosmed": "@farahanumafifahh",
                "kesan" : "kakak keren banget dan baik juga",  
                "pesan" : "Semoga sehat selalu dan dilancarkan kuliahnya sampai akhir serta lulus tepat waktu",
            },
            {
                "nama"  : "Ferdy Kevin Naibaho",
                "nim"   : "122450107",
                "umur"  : "19",
                "asal"  : "Medan, Sumatera Utara",
                "alamat": "Jalan Senopati Raya 18",
                "hobbi" : "Dengerin Rocky Gerung",
                "sosmed": "@ferdy_kevin",
                "kesan" : "Sangat menginspirasi dalam kehidupan ",  
                "pesan" : "Tetap semangat kak dalam menjalani dunia perkuliahan"
            },
            {
                "nama"  : "M. Deriansyah Okutra",
                "nim"   : "122450101",
                "umur"  : "19",
                "asal"  : "Kayu Agung",
                "alamat": "Jalan Pagar Alam",
                "hobbi" : "Bercerita horror",
                "sosmed": "@dransyh_",
                "kesan" : "Abang keren banget dan baik juga",  
                "pesan" : "Semoga sehat selalu dan dilancarkan kuliahnya sampai akhir serta lulus tepat waktu",
            },
            {
                "nama"  : "Oktavia Nurwenda Puspita Sari",
                "nim"   : "122450041",
                "umur"  : "20",
                "asal"  : "Lampung Timur",
                "alamat": "Way Hui",
                "hobbi" : "Memasak",
                "sosmed": "@_oktavianrwnda_",
                "kesan" : "kakak keren banget dan baik juga",  
                "pesan" : "Semoga sehat selalu dan dilancarkan kuliahnya sampai akhir serta lulus tepat waktu",
            },
            {
                "nama"  : "Deyvan Loxefal",
                "nim"   : "121450148",
                "umur"  : "21",
                "asal"  : "Riau",
                "alamat": "Pulau Damar",
                "hobbi" : "Belajar",
                "sosmed": "@depanloo",
                "kesan" : "Abang keren banget dan baik juga",  
                "pesan" : "Semoga sehat selalu dan dilancarkan kuliahnya sampai akhir serta lulus tepat waktu",
            },
            {
                "nama"  : "Ibnu Farhan Al-Ghifari",
                "nim"   : "121450121",
                "umur"  : "21",
                "asal"  : "Jambi",
                "alamat": "Pulau Damar, Kobam",
                "hobbi" : "Bermain Game Online",
                "sosmed": "@al_ghifari032",
                "kesan" : "Abanng keren banget dan baik juga",  
                "pesan" : "Semoga sehat selalu dan dilancarkan kuliahnya sampai akhir serta lulus tepat waktu",
            },
             {
                "nama"  : "Johannes Krisjon Silitonga",
                "nim"   : "122450043",
                "umur"  : "19",
                "asal"  : "Tanggerang",
                "alamat": "Jalan Lapas",
                "hobbi" : "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan" : "Abang keren banget dan baik juga",  
                "pesan" : "Semoga sehat selalu dan dilancarkan kuliahnya sampai akhir serta lulus tepat waktu",
            },
            {
                "nama"  : "Kemas Veriandra Ramadhan",
                "nim"   : "122450016",
                "umur"  : "19",
                "asal"  : "Bekasi",
                "alamat": "Golf Asri",
                "hobbi" : "Bermain ular python digital",
                "sosmed": "@kemasverii",
                "kesan" : "Abang keren banget dan baik juga",  
                "pesan" : "Semoga sehat selalu dan dilancarkan kuliahnya sampai akhir serta lulus tepat waktu",
            },
            {
                "nama"  : "Leonard Andreas Napitupulu",
                "nim"   : "121450153",
                "umur"  : "21",
                "asal"  : "Sumatera Utara",
                "alamat": "Kobam",
                "hobbi" : "Belajar",
                "sosmed": "@lnrd.__",
                "kesan" : "kakak keren banget dan baik juga",  
                "pesan" : "Semoga sehat selalu dan dilancarkan kuliahnya sampai akhir serta lulus tepat waktu",
            },
            {
                "nama"  : "Presilia",
                "nim"   : "122450081",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Kota Baru",
                "hobbi" : "Tidur",
                "sosmed": "@presiliamg",
                "kesan" : "kakak keren banget dan baik juga",  
                "pesan" : "Semoga sehat selalu dan dilancarkan kuliahnya sampai akhir serta lulus tepat waktu",
            },
            {
                "nama"  : "Rafa Aqilla Jungjunan",
                "nim"   : "122450148",
                "umur"  : "20",
                "asal"  : "Riau",
                "alamat": "Belwis",
                "hobbi" : "Membaca webtoon",
                "sosmed": "@rafaaqilla",
                "kesan" : "kakak keren banget dan baik juga",  
                "pesan" : "Semoga sehat selalu dan dilancarkan kuliahnya sampai akhir serta lulus tepat waktu",
            },
            {
                "nama"  : "Sahid Maulana",
                "nim"   : "122450109",
                "umur"  : "21",
                "asal"  : "Depok, Jawa Barat",
                "alamat": "Airan Raya",
                "hobbi" : "Bermain Game",
                "sosmed": "@sahid_maul19",
                "kesan" : "kakak keren banget dan baik juga",  
                "pesan" : "Semoga sehat selalu dan dilancarkan kuliahnya sampai akhir serta lulus tepat waktu",
            },
            {
                "nama"  : "Vanessa Olivia Rose",
                "nim"   : "121450068",
                "umur"  : "20",
                "asal"  : "Jakarta",
                "alamat": "Perumahan Korpri",
                "hobbi" : "Belajar",
                "sosmed": "@roselivnes__",
                "kesan" : "kakak keren banget dan baik juga",  
                "pesan" : "Semoga sehat selalu dan dilancarkan kuliahnya sampai akhir serta lulus tepat waktu",            
            },
            {
                "nama"  : "M. Farhan Athaulloh",
                "nim"   : "121450117",
                "umur"  : "21",
                "asal"  : "Bandar Lampung",
                "alamat": "Kota Baru",
                "hobbi" : "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan" : "kakak keren banget dan baik juga",  
                "pesan" : "Semoga sehat selalu dan dilancarkan kuliahnya sampai akhir serta lulus tepat waktu",
            },
            {
                "nama"  : "Gede Moena",
                "nim"   : "121450014",
                "umur"  : "21",
                "asal"  : "Bekasi",
                "alamat": "Korpri Raya",
                "hobbi" : "Belajar dan main game",
                "sosmed": "@gedemoenaa",
                "kesan" : "kakak keren banget dan baik juga",  
                "pesan" : "Semoga sehat selalu dan dilancarkan kuliahnya sampai akhir serta lulus tepat waktu",
            },
            {
                "nama"  : "Jaclin Alcavella",
                "nim"   : "122450015",
                "umur"  : "19",
                "asal"  : "Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi" : "Berenang",
                "sosmed": "@jaclinalcv_",
                "kesan" : "kakak keren banget dan baik juga",  
                "pesan" : "Semoga sehat selalu dan dilancarkan kuliahnya sampai akhir serta lulus tepat waktu",
            },
            {
                "nama"  : "Rafly Prabu Darmawan",
                "nim"   : "122450140",
                "umur"  : "20",
                "asal"  : "Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi" : "Main Game",
                "sosmed": "@raflyy_pd2684",
                "kesan" : "kakak keren banget dan baik juga",  
                "pesan" : "Semoga sehat selalu dan dilancarkan kuliahnya sampai akhir serta lulus tepat waktu",
            },
            {
                "nama"  : "Syalaisha Andini Putriansyah",
                "nim"   : "122450111",
                "umur"  : "21",
                "asal"  : "Tanggerang",
                "alamat": "Sukarame",
                "hobbi" : "Membaca",
                "sosmed": "@syalaisha.i__",
                "kesan" : "kakak keren banget dan baik juga",  
                "pesan" : "Semoga sehat selalu dan dilancarkan kuliahnya sampai akhir serta lulus tepat waktu",
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1T0ACsYpIK1ZEFf3hKfoNAd9hbYNpTguX", #bang rafi dn
            "https://drive.google.com/uc?export=view&id=1SrJDJRKCQwM_hhZBXhTcL-92bl9aMtgB", #bang ahmad dn
            "https://drive.google.com/uc?export=view&id=1Skt1RWiaGf1cw6pka7H-GxKMxqechI2b", #bang fadhil dn
            "https://drive.google.com/uc?export=view&id=1Shn5lY1fw1YkjWx_9Qfv0d7FGNM1DnbS", #kak dina dn
            "https://drive.google.com/uc?export=view&id=1SQm34QqbcBtffZu27iZmRfXjWfO9dCwR", #kak dinda dn
            "https://drive.google.com/uc?export=view&id=1SdfeKJh0sJFVotyRPQgEBp7gmRaO59Bv", #kak marleta dn
            "https://drive.google.com/uc?export=view&id=1SEo5w7N5-Q8Oay8hmO9HriSTwZkakYkr", #kak rut junita dn
            "https://drive.google.com/uc?export=view&id=1SKYwnYh0VBl2ybyA5LYox7qyhxh7_Pde", #kak syadza dn
            "https://drive.google.com/uc?export=view&id=1SxaxcarR1ZLcDbrrokXiRSlP8YUBF4i2", #bang eggi dn
            "https://drive.google.com/uc?export=view&id=1SNSZwthOSjMhnhVD8ZVQJwTg9EIfthtl", #kak febiya dn
            "https://drive.google.com/uc?export=view&id=1Sx7cHHwBWXASnaKQf_MSSXGp89Ykj9jd", #kak happy syahrul dn
            "https://drive.google.com/uc?export=view&id=1Smh7tjV9xdNOMfgst0i0rK1zNIVoGG6t", #bang randa dn
        ]
        data_list = [
            {
                "nama"  : "Rafi Fadhlillah",
                "nim"   : "121450143",
                "umur"  : "21",
                "asal"  : "Lubuk Linggau",
                "alamat": "Jalan Nangka 4",
                "hobbi" : "Olahraga",
                "sosmed": "@rafadhilillah",
                "kesan" : "Banyak manfaat yang didapat",  
                "pesan" : "Sukses selalu untuk semua yang terlibat dan semoga dilancarkan kuliahnya serta lulus tepat waktu plus langsung dapet kerja yang diinginkan "
            },
            {
                "nama"  : "Ahmad Sahidin Akbar",
                "nim"   : "122450044",
                "umur"  : "20",
                "asal"  : "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi" : "Olahraga",
                "sosmed": "@sahid22__",
                "kesan" : "Banyak manfaat yang didapat",  
                "pesan" : "Sukses selalu untuk semua yang terlibat dan semoga dilancarkan kuliahnya serta lulus tepat waktu plus langsung dapet kerja yang diinginkan "
            },
            {
                "nama"  : "Fadhil Fitra Wijaya",
                "nim"   : "122450082",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Teluk Betung",
                "hobbi" : "Main game",
                "sosmed": "@fadhilfwee",
                "kesan" : "Banyak manfaat yang didapat",  
                "pesan" : "Sukses selalu untuk semua yang terlibat dan semoga dilancarkan kuliahnya serta lulus tepat waktu plus langsung dapet kerja yang diinginkan "
            },
            {
                "nama"  : "Syalaisha Andina Putriansyah",
                "nim"   : "122450121",
                "umur"  : "21",
                "asal"  : "Tangerang",
                "alamat": "Gang Yudhistira",
                "hobbi" : "Baca jurnal",
                "sosmed": "@dkselsd_31",
                "kesan" : "Banyak manfaat yang didapat",  
                "pesan" : "Sukses selalu untuk semua yang terlibat dan semoga dilancarkan kuliahnya serta lulus tepat waktu plus langsung dapet kerja yang diinginkan "
            },
            {
                "nama"  : "Dinda Nababan",
                "nim"   : "122450120",
                "umur"  : "20",
                "asal"  : "Medan, Sumatera Utara",
                "alamat": "Jalan Lapas",
                "hobbi" : "Belajar",
                "sosmed": "@dindanababan_",
                "kesan" : "Banyak manfaat yang didapat",  
                "pesan" : "Sukses selalu untuk semua yang terlibat dan semoga dilancarkan kuliahnya serta lulus tepat waktu plus langsung dapet kerja yang diinginkan ",
            },
            {
                "nama"  : "Marleta Cornelia Leander",
                "nim"   : "122450092",
                "umur"  : "20",
                "asal"  : "Depok, Jawa Barat",
                "alamat": "Gang Nangka 3",
                "hobbi" : "Review Jurnal",
                "sosmed": "@marletacornelia",
                "kesan" : "Banyak manfaat yang didapat",  
                "pesan" : "Sukses selalu untuk semua yang terlibat dan semoga dilancarkan kuliahnya serta lulus tepat waktu plus langsung dapet kerja yang diinginkan ",
            },
            {
                "nama"  : "Rut Junita Sari Siburian",
                "nim"   : "122450103",
                "umur"  : "20",
                "asal"  : "Batam, Kepulauan Riau",
                "alamat": "Gang Nangka 3",
                "hobbi" : "Review Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan" : "Banyak manfaat yang didapat",  
                "pesan" : "Sukses selalu untuk semua yang terlibat dan semoga dilancarkan kuliahnya serta lulus tepat waktu plus langsung dapet kerja yang diinginkan ",       
            },
            {
                "nama"  : "Syadza Puspadari Azhar",
                "nim"   : "122450072",
                "umur"  : "20",
                "asal"  : "Palembang",
                "alamat": "Belwis",
                "hobbi" : "Resume SG",
                "sosmed": "@puspadrr",
                "kesan" : "Banyak manfaat yang didapat",  
                "pesan" : "Sukses selalu untuk semua yang terlibat dan semoga dilancarkan kuliahnya serta lulus tepat waktu plus langsung dapet kerja yang diinginkan ",
            },
            {
                "nama"  : "Eggi satria",
                "nim"   : "122450032",
                "umur"  : "20",
                "asal"  : "Sukabumi",
                "alamat": "Korpri",
                "hobbi" : "Ngoding WISATA",
                "sosmed": "@egistr",
                "kesan" : "Banyak manfaat yang didapat",  
                "pesan" : "Sukses selalu untuk semua yang terlibat dan semoga dilancarkan kuliahnya serta lulus tepat waktu plus langsung dapet kerja yang diinginkan ",
            },
            {
                "nama"  : "Febiya Jomy Pratiwi",
                "nim"   : "122450074",
                "umur"  : "20",
                "asal"  : "Tulang Bawang",
                "alamat": "Jalan Kelengkeng Raya",
                "hobbi" : "Review jurnal",
                "sosmed": "@pratiwifebiya",
                "kesan" : "Sangat baik dan sangat mengasyikkan",  
                "pesan" : "Semangat kak dalam menjalani hari-harinya, semoga urusannya dalam dunia perkuliahan dapat diselesaikan dengan mudah"
            },
             {
                "nama"  : "Happy Syahrul Ramadhan",
                "nim"   : "122450013",
                "umur"  : "20",
                "asal"  : "Lampung Timur",
                "alamat": "Karang Anyar",
                "hobbi" : "Main game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan" : "Sangat informatif dalam menjelaskan sesuatu dan menjadi sosok yang memberikan banyak masukan serta motivasi melalui pengalaman yang telah dilakukan",  
                "pesan" : "Tetap semangat kak dalam menjalani hari-harinya, semoga diperlancar dalam menyelesaikan tugas dan tanggung jawab yang sedang di emban"
            },
            {
                "nama"  : "Randa Andriana Putra",
                "nim"   : "122450083",
                "umur"  : "21",
                "asal"  : "Banten",
                "alamat": "Sukarame",
                "hobbi" : "Tidur dan berkembang",
                "sosmed": "@randaandriana_",
                "kesan" : "Sangat informatif dalam menjelaskan sesuatu dan banyak memberikan motivasi",  
                "pesan" : "Semoga kegiatannya di dalam maupun di luar perkuliahan tetap lancar dan tetap semangat kak"
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen MEDKRAF":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1QLR9zDy_VHzjRivXX01kUd4U7WF-y0cR", #bang wahyu dn
            "https://drive.google.com/uc?export=view&id=1kEmaVSgSw_5o7D0WDJlSPEtsWXtDouOc", #kak elok dn
            "https://drive.google.com/uc?export=view&id=1lTzl0IUbiMU2RhKY3szhmZP1jFwshsfJ", #kak arsyiah dn
            "https://drive.google.com/uc?export=view&id=13tmkskkmumDnLEEXcjpmQdoOc_dKyErc", #kak cintya dn
            "https://drive.google.com/uc?export=view&id=1XGUrNTRkwzoeDHZTAqINvjMxJjCz9Jlj", #kak najla dn
            "https://drive.google.com/uc?export=view&id=1cIbyW1j8H4fWrxdWS6i9GF0GbrmKFU56", #kak rahma dn
            "https://drive.google.com/uc?export=view&id=14iiCFz9NDVFXxcrFMX-ABBeBU_3595no", #kak try yani dn
            "https://drive.google.com/uc?export=view&id=1HaiTQcYQTGsqzuHvNgpFu9TCQAUFPRZQ", #bang kaisar dn
            "https://drive.google.com/uc?export=view&id=1U2DNjNg7PWVO2kZd60_6RpHAHKmVPnNW", #kak dwi dn
            "https://drive.google.com/uc?export=view&id=14GC7YsIbL5M9emabAQRtv6Yj_zL5uAWZ", #bang gym dn
            "https://drive.google.com/uc?export=view&id=13TwS35Qq0BiiKg1HdGpXrfBrXVJn0-Eg", #kak nasywa dn
            "https://drive.google.com/uc?export=view&id=17lsOQVr-Y3ZC9t5bz4ceZf4QOJq9detW", #kak priska dn
            "https://drive.google.com/uc?export=view&id=1UEZlFFu37H5G1lUlsfm7DPF7u7kWQaT6", #bang arsal dn
            "https://drive.google.com/uc?export=view&id=1idQBrMpSOq5Waosk2UpAF83nyKcAKkUj", #bang abit dn
            "https://drive.google.com/uc?export=view&id=1T_q-akzDsfMNeFKG8eMNScZv2a8dh1gE", #bang akmal dn
            "https://drive.google.com/uc?export=view&id=1TSiD3W6SnFzmr_ryIbHrDANysZ52dCnk", #bang hermawan dn
            "https://drive.google.com/uc?export=view&id=1TpnwlkcyuSJmSM2C2scSCGqbdxzrPnhj", #kak nisa dn
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
                "kesan" : "Menambah pengetahuan dan jaringan pertemanan",  
                "pesan" : "Terima kasih atas semua ilmu yang sudah dibagikan. Semoga kakak makin berprestasi!"
            },
            {
                "nama"  : "Elok Fiola",
                "nim"   : "122450051",
                "umur"  : "19",
                "asal"  : "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi" : "Editing",
                "sosmed": "@elokfiola",
                "kesan" : "Menambah pengetahuan dan jaringan pertemanan",  
                "pesan" : "Terima kasih atas semua ilmu yang sudah dibagikan. Semoga kakak makin berprestasi!"
            },
            {
                "nama"  : "Arsyiah Azahra",
                "nim"   : "121450035",
                "umur"  : "21",
                "asal"  : "Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi" : "Nugas",
                "sosmed": "@arsyiah.__",
                "kesan" : "Menambah pengetahuan dan jaringan pertemanan",  
                "pesan" : "Terima kasih atas semua ilmu yang sudah dibagikan. Semoga kakak makin berprestasi!"
            },
            {
                "nama"  : "Cintya Bella",
                "nim"   : "122450066",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Teluk",
                "hobbi" : "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan" : "Menambah pengetahuan dan jaringan pertemanan",  
                "pesan" : "Terima kasih atas semua ilmu yang sudah dibagikan. Semoga kakak makin berprestasi!"
            },
            {
                "nama"  : "Najla Juwairia",
                "nim"   : "122450037",
                "umur"  : "19",
                "asal"  : "Sumatera Utara",
                "alamat": "Airan",
                "hobbi" : "Menulis, Membaca, Fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan" : "Menambah pengetahuan dan jaringan pertemanan",  
                "pesan" : "Terima kasih atas semua ilmu yang sudah dibagikan. Semoga kakak makin berprestasi!"
            },
            {
                "nama"  : "Rahma Neliyana",
                "nim"   : "122450036",
                "umur"  : "20",
                "asal"  : "Lampung",
                "alamat": "Sukarame",
                "hobbi" : "Baca Coding",
                "sosmed": "@rahmanellyana",
                "kesan" : "kakak baik dan keren juga menambah pengetahuan dan jaringan pertemanan",  
                "pesan" : "Terima kasih atas semua ilmu yang sudah dibagikan. Semoga kakak makin berprestasi!"
            },
            {
                "nama"  : "Try Yani Rizki Nur Rohmah",
                "nim"   : "122450020",
                "umur"  : "20",
                "asal"  : "Lampung Barat",
                "alamat": "Korpri",
                "hobbi" : "Bernyanyi dan Menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan" : "kakak baik dan keren juga menambah pengetahuan dan jaringan pertemanan",  
                "pesan" : "Terima kasih atas semua ilmu yang sudah dibagikan. Semoga kakak makin berprestasi!"
            },
            {
                "nama"  : "Muhammad Kaisar Firdaus",
                "nim"   : "121450135",
                "umur"  : "21",
                "asal"  : "Pesawaran",
                "alamat": "Pulau Damar",
                "hobbi" : "Lagi nyari",
                "sosmed": "@dino_lapet",
                "kesan" : "kakak baik dan keren juga menambah pengetahuan dan jaringan pertemanan",  
                "pesan" : "Terima kasih atas semua ilmu yang sudah dibagikan. Semoga kakak makin berprestasi!"
            },
            {
                "nama"  : "Dwi Ratna Anggraeni",
                "nim"   : "122450008",
                "umur"  : "20",
                "asal"  : "Jambi",
                "alamat": "Jalan Durian 5 Pemda",
                "hobbi" : "Membaca",
                "sosmed": "@dwiratnn_",
                "kesan" : "kakak baik dan keren juga menambah pengetahuan dan jaringan pertemanan",  
                "pesan" : "Terima kasih atas semua ilmu yang sudah dibagikan. Semoga kakak makin berprestasi!"
            },
            {
                "nama"  : "Gymnastiar Al Khoarizmy",
                "nim"   : "122450096",
                "umur"  : "20",
                "asal"  : "Serang",
                "alamat": "Lapangan Golf UIN",
                "hobbi" : "Baca komik",
                "sosmed": "@jimnn.as",
                "kesan" : "abang baik dan keren juga menambah pengetahuan dan jaringan pertemanan",  
                "pesan" : "Terima kasih atas semua ilmu yang sudah dibagikan. Semoga kakak makin berprestasi!"
            },
             {
                "nama"  : "Nasywa Nur Afifah",
                "nim"   : "122450125",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Jalan Durian 1 Pemda",
                "hobbi" : "Nonton drakor",
                "sosmed": "@nsywanaf",
                "kesan" : "kakak baik dan keren juga menambah pengetahuan dan jaringan pertemanan",  
                "pesan" : "Terima kasih atas semua ilmu yang sudah dibagikan. Semoga kakak makin berprestasi!"
            },
            {
                "nama"  : "Priska Silvia Ferantiana",
                "nim"   : "122450053",
                "umur"  : "19",
                "asal"  : "Palembang",
                "alamat": "Jalan Nangka 2",
                "hobbi" : "Baca novel yang bikin nangis",
                "sosmed": "@prskslv",
                "kesan" : "kakak baik dan keren juga menambah pengetahuan dan jaringan pertemanan",  
                "pesan" : "Terima kasih atas semua ilmu yang sudah dibagikan. Semoga kakak makin berprestasi!"
            },
            {
                "nama"  : "Muhammad Arsal Ranjana Utama",
                "nim"   : "121450111",
                "umur"  : "21",
                "asal"  : "Depok",
                "alamat": "Jalan Nangka 4",
                "hobbi" : "Ngoding",
                "sosmed": "@arsal.utama",
                "kesan" : "kakak baik dan keren juga menambah pengetahuan dan jaringan pertemanan",  
                "pesan" : "Terima kasih atas semua ilmu yang sudah dibagikan. Semoga kakak makin berprestasi!"
            },
            {
                "nama"  : "Abit Ahmad Oktarian",
                "nim"   : "122450042",
                "umur"  : "19",
                "asal"  : "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi" : "Ngoding, Gaming",
                "sosmed": "@abitahmad",
                "kesan" : "kakak baik dan keren juga menambah pengetahuan dan jaringan pertemanan",  
                "pesan" : "Terima kasih atas semua ilmu yang sudah dibagikan. Semoga kakak makin berprestasi!"
            },
            {
                "nama"  : "Akmal Faiz Abdillah",
                "nim"   : "122450114",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi" : "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan" : "kakak baik dan keren juga menambah pengetahuan dan jaringan pertemanan",  
                "pesan" : "Terima kasih atas semua ilmu yang sudah dibagikan. Semoga kakak makin berprestasi!"
            },
            {
                "nama"  : "Hermawan Manurung",
                "nim"   : "122450069",
                "umur"  : "20",
                "asal"  : "Bogor",
                "alamat": "Dekat jalan tol, Wisma Hana Hani",
                "hobbi" : "Bengong dan membaca buku",
                "sosmed": "@hermawan.mnrng",
                "kesan" : "kakak baik dan keren juga menambah pengetahuan dan jaringan pertemanan",  
                "pesan" : "Terima kasih atas semua ilmu yang sudah dibagikan. Semoga kakak makin berprestasi!"
            },
            {
                "nama"  : "Khusnun Nisa",
                "nim"   : "122450078",
                "umur"  : "20",
                "asal"  : "Lampung Selatan",
                "alamat": "Belwis",
                "hobbi" : "Mengerjakan tugas",
                "sosmed": "@khusnun_nisa335",
                "kesan" : "kakak baik dan keren juga menambah pengetahuan dan jaringan pertemanan",  
                "pesan" : "Terima kasih atas semua ilmu yang sudah dibagikan. Semoga kakak makin berprestasi!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1OOVH24XW2cLVZRn6eNvPOBNQrGmY3SVI",# Yogi
            "https://drive.google.com/uc?export=view&id=1OQ1GkBjruA_RaG9iEk5mrJ-20YtPd1LF",#ramadhita
            "https://drive.google.com/uc?export=view&id=1NcJfN-xkWu1y9njNatbBeJbbmCMO8JFT",#nazwa
            "https://drive.google.com/uc?export=view&id=1Odax6b36JWJoWpOgyh8UpWjve1gQRrmm",#bastian
            "https://drive.google.com/uc?export=view&id=1O4Tum2_C6G-XwbEoFlq4OrDDxL2FY5ms",#dea
            "https://drive.google.com/uc?export=view&id=1NwMEj_VuNnsz5Wtl6bfxdazooNv_m0bj",#esteria
            "https://drive.google.com/uc?export=view&id=1NeENi6sCHEr1zzWfUj-iyWqSIjJ1IjOC",#natasya
            "https://drive.google.com/uc?export=view&id=1NcJfN-xkWu1y9njNatbBeJbbmCMO8JFT",#novelia
            "https://drive.google.com/uc?export=view&id=1NzTSPwtFsV1rNcfK-Zr3MZnzoNhWgD7l",#ratu keisha
            "https://drive.google.com/uc?export=view&id=1OauKHpTOdJcBUN8TCN_xabLJOrDdeCZg",#tobias 
            "https://drive.google.com/uc?export=view&id=1OIcIj_-fgKRzmxqvCDXRSShgcMdkkuP5",#yohana
            "https://drive.google.com/uc?export=view&id=1OoeUwYlJTv7acKMP6hNR8dbS-kudne5N",#rizxky
            "https://drive.google.com/uc?export=view&id=1OSpp7O_Wbuz_s9Qgho7Cj5oFAeGTK6KA",#bang arafi
            "https://drive.google.com/uc?export=view&id=1Op0t0HbX8LmvAqCzAMEPlNnQgCwsDIz0",#asa
            "https://drive.google.com/uc?export=view&id=1OgMSzXcFg0TPI8yzGt6-ueAiyjntbK_l",#chalifia
            "https://drive.google.com/uc?export=view&id=1O6LE0N8WhM9x9ixwY5IC8pNONWl0QoMG",#irvan
            "https://drive.google.com/uc?export=view&id=1Oa-J3GtWw1Ei9ngFVHB1Fod4bO4tyXZJ",#izza
            "https://drive.google.com/uc?export=view&id=1OR9EUoJhc-YlNmLUdHVpTInfyuvoD4x7",#khalisah
            "https://drive.google.com/uc?export=view&id=1OLggTws0v1xisO29P3uaNb3yul6f6Fgu",#raid
            "https://drive.google.com/uc?export=view&id=1OLsWv1PG0ljrRMIXfAt1abgReI9sTcvn",#tria
        ]
        data_list = [
            {
                "nama": "Yogi Sae Tama",#                "jabatan": "Kepala Departemen"
                "nim": "121450041",
                "umur": "21 Tahun",
                "asal": "Tangerang",
                "alamat": "Jatimulyo",
                "hobbi": "Bangun pagi",
                "sosmed": "@yogyyyyyy",
                "kesan": "Kalian keren banget, tiap orang bawa vibe dan energi positif masing-masing! Tim jadi makin solid berkat kontribusi kalian semua",
                "pesan": "Keep up the good work, jangan lupa seru-seruan dan saling support! Semangat terus buat kita semua! 🎉",
            },
            {
                "nama": "Ramadhita Atifa Hendri",#                "jabatan": "Sekretaris Departemen"
                "nim": "121450131",
                "umur": "21 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan": "Kalian keren banget, tiap orang bawa vibe dan energi positif masing-masing! Tim jadi makin solid berkat kontribusi kalian semua",
                "pesan": "Keep up the good work, jangan lupa seru-seruan dan saling support! Semangat terus buat kita semua! 🎉",
            },
            {
                "nama": "Nazwa Nabila",#                "jabatan": "Kepala Divisi Hubungan Luar"
                "nim": "121450122",
                "umur": "21 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Way kandis",
                "hobbi": "belajar",
                "sosmed": "@nazwanbilla",
                "kesan": "Kalian keren banget, tiap orang bawa vibe dan energi positif masing-masing! Tim jadi makin solid berkat kontribusi kalian semua",
                "pesan": "Keep up the good work, jangan lupa seru-seruan dan saling support! Semangat terus buat kita semua! 🎉",
            },
            {
                "nama": "Bastian Heskia Silaban",#                "jabatan": "Staff Divisi Hubungan Luar"
                "nim": "122450130",
                "umur": "21 Tahun",
                "asal": "Batam, Kep. Riau",
                "alamat": "Belwis",
                "hobbi": "main game",
                "sosmed": "@bastiansilaban_",
                "kesan": "Kalian keren banget, tiap orang bawa vibe dan energi positif masing-masing! Tim jadi makin solid berkat kontribusi kalian semua",
                "pesan": "Keep up the good work, jangan lupa seru-seruan dan saling support! Semangat terus buat kita semua! 🎉",
            },
            {
                "nama": "Dea Mutia Risani", #                "jabatan": "Staff Divisi Hubungan Luar"
                "nim": "122450099",
                "umur": "20 Tahun",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "dengerin musik",
                "sosmed": "@deaa.rsn",
                "kesan": "Kalian keren banget, tiap orang bawa vibe dan energi positif masing-masing! Tim jadi makin solid berkat kontribusi kalian semua",
                "pesan": "Keep up the good work, jangan lupa seru-seruan dan saling support! Semangat terus buat kita semua! 🎉",
            },
            {
                "nama": "Esteria Rohanauli Sidauruk",#                "jabatan": "Staff Divisi Hubungan Luar"
                "nim": "122450025",
                "umur": "19 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Belwis",
                "hobbi": "kirim bc-an",
                "sosmed": "@esteriars",
                "kesan": "Kalian keren banget, tiap orang bawa vibe dan energi positif masing-masing! Tim jadi makin solid berkat kontribusi kalian semua",
                "pesan": "Keep up the good work, jangan lupa seru-seruan dan saling support! Semangat terus buat kita semua! 🎉",
            },
            {
                "nama": "Natasya Ega Lina",#                "jabatan": "Staff Divisi Hubungan Luar"
                "nim": "122450024",
                "umur": "19 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi": "jadi humas",
                "sosmed": "@nateee__15",
                "kesan": "Kalian keren banget, tiap orang bawa vibe dan energi positif masing-masing! Tim jadi makin solid berkat kontribusi kalian semua",
                "pesan": "Keep up the good work, jangan lupa seru-seruan dan saling support! Semangat terus buat kita semua! 🎉",
            },
            {
                "nama": "Novelia Adinda",#                "jabatan": "Staff Divisi Hubungan Luar"
                "nim": "122450104",
                "umur": "21 Tahun",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "Kalian keren banget, tiap orang bawa vibe dan energi positif masing-masing! Tim jadi makin solid berkat kontribusi kalian semua",
                "pesan": "Keep up the good work, jangan lupa seru-seruan dan saling support! Semangat terus buat kita semua! 🎉",
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",#                "jabatan": "Staff Divisi Hubungan Luar"
                "nim": "122450106",
                "umur": "20 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Main sepak takraw",
                "sosmed": "@jasminednva",
                "kesan": "Kalian keren banget, tiap orang bawa vibe dan energi positif masing-masing! Tim jadi makin solid berkat kontribusi kalian semua",
                "pesan": "Keep up the good work, jangan lupa seru-seruan dan saling support! Semangat terus buat kita semua! 🎉",
            },
            {
                "nama": "Tobias David Manogari",#                "jabatan": "Staff Divisi Hubungan Luar"
                "nim": "122450091",
                "umur": "20 Tahun",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Jogging",
                "sosmed": "@tobiassiagian",
                "kesan": "Kalian keren banget, tiap orang bawa vibe dan energi positif masing-masing! Tim jadi makin solid berkat kontribusi kalian semua",
                "pesan": "Keep up the good work, jangan lupa seru-seruan dan saling support! Semangat terus buat kita semua! 🎉",
            },
            {
                "nama": "Yohana Manik",#                "jabatan": "Staff Divisi Hubungan Luar"
                "nim": "122450126",
                "umur": "19 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi": "Main Bowling",
                "sosmed": "@yo_annamnk",
                "kesan": "Kalian keren banget, tiap orang bawa vibe dan energi positif masing-masing! Tim jadi makin solid berkat kontribusi kalian semua",
                "pesan": "Keep up the good work, jangan lupa seru-seruan dan saling support! Semangat terus buat kita semua! 🎉",
            },
            {
                "nama": "Rizky Adrian Bennovry",#                "jabatan": "Kepala Divisi Pengabdian Masyarakat"
                "nim": "121450073",
                "umur": "21 Tahun",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobbi": "Bikin portofolio",
                "sosmed": "@rzkdrnnn",
                "kesan": "Kalian keren banget, tiap orang bawa vibe dan energi positif masing-masing! Tim jadi makin solid berkat kontribusi kalian semua",
                "pesan": "Keep up the good work, jangan lupa seru-seruan dan saling support! Semangat terus buat kita semua! 🎉",
            },
            {
                "nama": "Arafi Ramadhan Maulana",#                "jabatan": "Staff Divisi Pengabdian Masyarakat"
                "nim": "122450002",
                "umur": "20 Tahun",
                "asal": "Bandung",
                "alamat": "Way Huwi",
                "hobbi": "Bertani",
                "sosmed": "@rafiramadhanmaulana",
                "kesan": "Kalian keren banget, tiap orang bawa vibe dan energi positif masing-masing! Tim jadi makin solid berkat kontribusi kalian semua",
                "pesan": "Keep up the good work, jangan lupa seru-seruan dan saling support! Semangat terus buat kita semua! 🎉",
            },
            {
                "nama": "Asa Do'a Uyi",#                "jabatan": "Staff Divisi Pengabdian Masyarakat"
                "nim": "122450005",
                "umur": "20 Tahun",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobbi": "Tepuk Semangat",
                "sosmed": "@u_yippy",
                "kesan": "Kalian keren banget, tiap orang bawa vibe dan energi positif masing-masing! Tim jadi makin solid berkat kontribusi kalian semua",
                "pesan": "Keep up the good work, jangan lupa seru-seruan dan saling support! Semangat terus buat kita semua! 🎉",
            },
            {
                "nama": "Chalifia Wananda",#                "jabatan": "Staff Divisi Pengabdian Masyarakat"
                "nim": "122450076",
                "umur": "20 Tahun",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Q Time",
                "sosmed": "@chlfawww",
                "kesan": "Kalian keren banget, tiap orang bawa vibe dan energi positif masing-masing! Tim jadi makin solid berkat kontribusi kalian semua",
                "pesan": "Keep up the good work, jangan lupa seru-seruan dan saling support! Semangat terus buat kita semua! 🎉",
            },
            {
                "nama": "Irvan Alfaritzi",#                "jabatan": "Staff Divisi Pengabdian Masyarakat"
                "nim": "122450093",
                "umur": "21 Tahun",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton youtube, main game",
                "sosmed": "@alfaritziirvan",
                "kesan": "Kalian keren banget, tiap orang bawa vibe dan energi positif masing-masing! Tim jadi makin solid berkat kontribusi kalian semua",
                "pesan": "Keep up the good work, jangan lupa seru-seruan dan saling support! Semangat terus buat kita semua! 🎉",
            },
            {
                "nama": "Izza Lutfia",#                "jabatan": "Staff Divisi Pengabdian Masyarakat"
                "nim": "122450090",
                "umur": "20 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Main Rubik",
                "sosmed": "@izzalutfia",
                "kesan": "Kalian keren banget, tiap orang bawa vibe dan energi positif masing-masing! Tim jadi makin solid berkat kontribusi kalian semua",
                "pesan": "Keep up the good work, jangan lupa seru-seruan dan saling support! Semangat terus buat kita semua! 🎉",
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",#                "jabatan": "Staff Divisi Pengabdian Masyarakat"
                "nim": "122450034",
                "umur": "20 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "belajar",
                "sosmed": "@alyaavanevi",
                "kesan": "Kalian keren banget, tiap orang bawa vibe dan energi positif masing-masing! Tim jadi makin solid berkat kontribusi kalian semua",
                "pesan": "Keep up the good work, jangan lupa seru-seruan dan saling support! Semangat terus buat kita semua! 🎉",
            },
            {
                "nama": "Raid Muhammad Naufal",#                "jabatan": "Staff Divisi Pengabdian Masyarakat"
                "nim": "122450027",
                "umur": "20 Tahun",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "telat",
                "sosmed": "@rayths_",
                "kesan": "Kalian keren banget, tiap orang bawa vibe dan energi positif masing-masing! Tim jadi makin solid berkat kontribusi kalian semua",
                "pesan": "Keep up the good work, jangan lupa seru-seruan dan saling support! Semangat terus buat kita semua! 🎉",
            },
            {
                "nama": "Tria Yunanni",#                "jabatan": "Staff Divisi Pengabdian Masyarakat"
                "nim": "122450062",
                "umur": "20 Tahun",
                "asal": "Way Kanan",
                "alamat": "Sukarame",
                "hobbi": "Baca Buku",
                "sosmed": "@tria_y062",
                "kesan": "Kalian keren banget, tiap orang bawa vibe dan energi positif masing-masing! Tim jadi makin solid berkat kontribusi kalian semua",
                "pesan": "Keep up the good work, jangan lupa seru-seruan dan saling support! Semangat terus buat kita semua! 🎉",
                },
                ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1hi9jNp7u4KmN0fvwBCTTL00UeF7VOPQH", #bang dimas dn
            "https://drive.google.com/uc?export=view&id=1hdYOkoXTiMMSr-54YkuYFIslV7iU-iM8", #kak catherine dn
            "https://drive.google.com/uc?export=view&id=1EE7StOlt1N2Tn_SSrx07x8xxjKHD5YvR", #bang akbar dn
            "https://drive.google.com/uc?export=view&id=1gpTEaGemMNk7eHO9Rkj6NLSBgU3MwjVs", #kak rani dn
            "https://drive.google.com/uc?export=view&id=1gZOWFstg2C12uoN2I1381NmTAAym1Kkx", #bang rendra dn
            "https://drive.google.com/uc?export=view&id=1h01FiQlWbAasOuSXvHlaFPBD-AB87Qp-", #kak salwa dn
            "https://drive.google.com/uc?export=view&id=1gelq-qUPXICBQPaqJYkUkeoNLGETzxsa", #bang yosia dn
            "https://drive.google.com/uc?export=view&id=1hbEykSfWgDAWo62ix9EwhAJmQuOa73tt", #bang ari dn
            "https://drive.google.com/uc?export=view&id=1h0NEuayFGDMqj9EY87PCA8tPdrPX4dSL", #kak azizah dn
            "https://drive.google.com/uc?export=view&id=1hTfN61spe7bDE_ejjFkPX3ZW8jALJkTh", #kak meira dn
            "https://drive.google.com/uc?export=view&id=1hGKu3Yd95N7zFO08SE6EbnEgdt9ET7YV", #bang rendi dn
            "https://drive.google.com/uc?export=view&id=1gTN4w8tf_6yXtLCt7HbKhn5XwP6rKgpc", #kak renta dn
            "https://drive.google.com/uc?export=view&id=1hOzRGJxQTf8DjpBO_E1wwFmBBXmZOc0J", #bang josua dn

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
                "kesan" : "Banyak pelajaran yang bisa diambil.",  
                "pesan" : "Semoga kakak selalu sukses dan diberkahi",
            },
            {
                "nama"  : "Catherine Firdhasari Maulina Sinaga",
                "nim"   : "121450071",
                "umur"  : "20",
                "asal"  : "Sumatera Utara",
                "alamat": "Airan",
                "hobbi" : "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan" : "Banyak pelajaran yang bisa diambil.",  
                "pesan" : "Semoga kakak selalu sukses dan diberkahi",
            },
            {
                "nama"  : "Akbar Resdika",
                "nama"  : "M.Akbar Resdika",
                "nim"   : "121450066",
                "umur"  : "20",
                "asal"  : "Lampung Barat (Way Tenun)",
                "alamat": "Labuhan Dalam (Untung)",
                "hobbi" : "Suka kucing tapi gak suka ngurusnya",
                "sosmed": "@akbar_resdika",
                "kesan" : "Banyak pelajaran yang bisa diambil.",  
                "pesan" : "Semoga kakak selalu sukses dan diberkahi",
            },
            {
                "nama"  : "Rani Puspita sari",
                "nim"   : "122450030",
                "umur"  : "20",
                "asal"  : "Kota Metro",
                "alamat": "Rajabasa",
                "hobbi" : "Dengar musik",
                "sosmed": "@ranniu",
                "kesan" : "Banyak pelajaran yang bisa diambil.",  
                "pesan" : "Semoga kakak selalu sukses dan diberkahi",
            },
            {
                "nama"  : "Rendra Eka Prayoga",
                "nim"   : "122450112",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Belwis",
                "hobbi" : "Mancing Ikan Mas",
                "sosmed": "@rendraepr",
                "kesan" : "Banyak pelajaran yang bisa diambil.",  
                "pesan" : "Semoga kakak selalu sukses dan diberkahi",
            },
            {
                "nama"  : "Salwa Farhanatussaidah",
                "nim"   : "122450055",
                "umur"  : "20",
                "asal"  : "Pesawaran",
                "alamat": "Airan",
                "hobbi" : "Nonton",
                "sosmed": "@slwfhn_694",
                "kesan" : "Banyak pelajaran yang bisa diambil.",  
                "pesan" : "Semoga kakak selalu sukses dan diberkahi",
            },
            {
                "nama"  : "Yosia Letare Banurea",
                "nim"   : "121450149",
                "umur"  : "20",
                "asal"  : "Dairi, Sumatera Utara",
                "alamat": "Perum Griya Indah",
                "hobbi" : "Tidur",
                "sosmed": "@yosiabanurea",
                "kesan" : "Banyak pelajaran yang bisa diambil.",  
                "pesan" : "Semoga kakak selalu sukses dan diberkahi",
            },
            {
                "nama"  : "Ari Sigit",
                "nim"   : "121450069",
                "umur"  : "23",
                "asal"  : "Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobbi" : "Futsal",
                "sosmed": "@ari_sigit17",
                "kesan" : "Banyak pelajaran yang bisa diambil.",  
                "pesan" : "Semoga kakak selalu sukses dan diberkahi",
            },
            {
                "nama"  : "Azizah Kusumah Putri",
                "nim"   : "122450068",
                "umur"  : "21",
                "asal"  : "Lampung Selatan",
                "alamat": "Natar",
                "hobbi" : "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan" : "Banyak pelajaran yang bisa diambil.",  
                "pesan" : "Semoga kakak selalu sukses dan diberkahi",
            },
            {
                "nama"  : "Meira Listyaningrum",
                "nim"   : "122450011",
                "umur"  : "20",
                "asal"  : "Pesawaran",
                "alamat": "Airan",
                "hobbi" : "Membaca",
                "sosmed": "@meirasty_",
                "kesan" : "Banyak pelajaran yang bisa diambil.",  
                "pesan" : "Semoga kakak selalu sukses dan diberkahi",
            },
            {
                "nama"  : "Rendi Alexander Hutagalung",
                "nim"   : "122450057",
                "umur"  : "20",
                "asal"  : "Tangerang",
                "alamat": "Kost Benawang",
                "hobbi" : "Menyanyi",
                "sosmed": "@rexander",
                "kesan" : "Banyak pelajaran yang bisa diambil.",  
                "pesan" : "Semoga kakak selalu sukses dan diberkahi",
            },
            {
                "nama"  : "Renta Siahaan",
                "nim"   : "122450070",
                "umur"  : "21",
                "asal"  : "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi" : "Membaca dan Memancing",
                "sosmed": "@renta.shn",
                "kesan" : "Banyak pelajaran yang bisa diambil.",  
                "pesan" : "Semoga kakak selalu sukses dan diberkahi",
            },
            {
                "nama"  : "Josua Panggabean",
                "nim"   : "122450061",
                "umur"  : "21",
                "asal"  : "Pematang Siantar",
                "alamat": "Gerbang Barat",
                "hobbi" : "Menonton",
                "sosmed": "@josuapanggabean_",
               "kesan" : "Banyak pelajaran yang bisa diambil.",  
                "pesan" : "Semoga kakak selalu sukses dan diberkahi",
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()   

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1fC6cDxuKmBVU0EC837EX3ytqIfkkqAuq", #bang andrian dn
            "https://drive.google.com/uc?export=view&id=1fLn6EXzapj0dbLL_QvA1MjgDj7yCMmmT", #kak adisty dn
            "https://drive.google.com/uc?export=view&id=1f8JAU8QN8cIQ0y9TSq3F0eqNCkBMRopR", #kak nabilla dn
            "https://drive.google.com/uc?export=view&id=1f6Wi6fe0jrK9lDTqY3lM2-tf5xiEHLZG", #bang danang dn
            "https://drive.google.com/uc?export=view&id=1f6StG3aPF4DTwHszIcm5ECPEsyqtgfYv", #bang farrel dn
            "https://drive.google.com/uc?export=view&id=1fH9Ct2x-F8EIulKT4YQ_1DRLqxrQgBDU", #kak nabilah dn
            "https://drive.google.com/uc?export=view&id=1f29nTAtWWUhm2cgZY4EUGBVeBCQyhmcp", #kak alvia dn
            "https://drive.google.com/uc?export=view&id=1gLyAS8aQNDB4skr4-bGcA-VeBplxW1is", #bang dhafin dn
            "https://drive.google.com/uc?export=view&id=1f3kd4q0Nro7dDbTGq0XrGvubd69DCev7", #kak elia dn


        ]
        data_list = [
            {
                "nama"  : "Andrian Agustinus Lumban Gaol",
                "nim"   : "121450090",
                "umur"  : "21",
                "asal"  : "Sidikalang",
                "alamat": "Dekat Penjara",
                "hobbi" : "Lagi nyari",
                "sosmed": "@andriangaol",
                "kesan" : "Sungguh menyenangkan bisa belajar banyak dari pengalaman kakak.",  
                "pesan" : "Semangat terus, Kak, dalam menjalani setiap aktivitas! Semoga selalu diberi kelancaran dan kemudahan dalam tugas."
            },
            {
                "nama"  : "Adisty Syawaida Ariyanto",
                "nim"   : "121450136",
                "umur"  : "22",
                "asal"  : "Metro",
                "alamat": "Sukarame ",
                "hobbi" : "Nonton Film",
                "sosmed": "@adistysa_",
                "kesan" : "Sangat informatif dalam menjelaskan sesuatu dan banyak memberikan motivasi",  
                "pesan" : "Semoga kegiatannya di dalam maupun di luar perkuliahan tetap lancar dan tetap semangat kak"
            },
            {
                "nama"  : "Nabila Azhari",
                "nim"   : "121450029",
                "umur"  : "21",
                "asal"  : "Simalungun",
                "alamat": "Airan ",
                "hobbi" : "Menghitung Uang",
                "sosmed": "@zhjung",
                "kesan" : "Sungguh menyenangkan bisa belajar banyak dari pengalaman kakak.",  
                "pesan" : "Semangat terus, Kak, dalam menjalani setiap aktivitas! Semoga selalu diberi kelancaran dan kemudahan dalam tugas."
            },
            {
                "nama"  : "Danang Hilal Kurniawan",
                "nim"   : "122450085",
                "umur"  : "21",
                "asal"  : "Bandar Lampung",
                "alamat": "Airan",
                "hobbi" : "Belajar",
                "sosmed": "@dananghk_",
                "kesan" : "Sungguh menyenangkan bisa belajar banyak dari pengalaman kakak.",  
                "pesan" : "Semangat terus, Kak, dalam menjalani setiap aktivitas! Semoga selalu diberi kelancaran dan kemudahan dalam tugas."
            },
            {
                "nama"  : "Farrel Julio Akbar",
                "nim"   : "122450110",
                "umur"  : "20",
                "asal"  : "Bogor",
                "alamat": "Lapas",
                "hobbi" : "Kayang",
                "sosmed": "@farel_julio",
                "kesan" : "Sungguh menyenangkan bisa belajar banyak dari pengalaman kakak.",  
                "pesan" : "Semangat terus, Kak, dalam menjalani setiap aktivitas! Semoga selalu diberi kelancaran dan kemudahan dalam tugas."
            },
            {
                "nama"  : "Nabilah Andika Fitriati",
                "nim"   : "121450139",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi" : "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan" : "Sungguh menyenangkan bisa belajar banyak dari pengalaman kakak.",  
                "pesan" : "Semangat terus, Kak, dalam menjalani setiap aktivitas! Semoga selalu diberi kelancaran dan kemudahan dalam tugas."
            },
            {
                "nama"  : "Alvia Asrinda Br.Gintng",
                "nim"   : "122450077",
                "umur"  : "20",
                "asal"  : "Binjai",
                "alamat": "Korpri",
                "hobbi" : "Nonton Winda",
                "sosmed": "@alviagnting",
                "kesan" : "Sungguh menyenangkan bisa belajar banyak dari pengalaman kakak.",  
                "pesan" : "Semangat terus, Kak, dalam menjalani setiap aktivitas! Semoga selalu diberi kelancaran dan kemudahan dalam tugas."
            },
            {
                "nama"  : "Dhafin Razaqa Luthfi",
                "nim"   : "122450133",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi" : "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan" : "Sungguh menyenangkan bisa belajar banyak dari pengalaman kakak.",  
                "pesan" : "Semangat terus, Kak, dalam menjalani setiap aktivitas! Semoga selalu diberi kelancaran dan kemudahan dalam tugas."
            },
            {
                "nama"  : "Elia Meylani Simanjuntak",
                "nim"   : "122450026",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Korpri",
                "hobbi" : "Main Alat Musik",
                "sosmed": "@meylanielia",
                "kesan" : "Sungguh menyenangkan bisa belajar banyak dari pengalaman kakak.",  
                "pesan" : "Semangat terus, Kak, dalam menjalani setiap aktivitas! Semoga selalu diberi kelancaran dan kemudahan dalam tugas."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd() 
# Tambahkan menu lainnya sesuai kebutuhan
