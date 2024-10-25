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
            "https://drive.google.com/uc?export=view&id=1Nx--psLqJlgjSl_I2eC2lWOXX1ajWUR2",
            "https://drive.google.com/uc?export=view&id=1NYmVkbSAF0bL0ak1psDs8rXY9rIt8Q0_",
            "https://drive.google.com/uc?export=view&id=1NeufUm5bJQXcc0o20_cDHeo2GWtzNprf",
            "https://drive.google.com/uc?export=view&id=1NnTJWNk33YJPLwuaSsGHEwyb6WTzb8uL"
            "https://drive.google.com/uc?export=view&id=1Ngv8jLz9LRJSlWAAA9IYvzL1hTCQgqGx"
            "https://drive.google.com/uc?export=view&id=1NbcBVdA7x0cEyUmafebvw_eKvMTUcSIy"
            "https://drive.google.com/uc?export=view&id=1O10hHuwPn9KXf9dD-ZnOOH9HEchNeXul"
            "https://drive.google.com/uc?export=view&id=1NtbEzuWdTv6k111aitYEwHJCT69JOWzi"
            "https://drive.google.com/uc?export=view&id=1O6b7JKU8EvnSnUSPviyWQI52bLWcD7gd"
            "https://drive.google.com/uc?export=view&id=1Njf8tb7nFCpd3vGlIb9k7N20r3U1sxJq"
 
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
                "nim"   : "121450150",
                "umur"  : "21",
                "asal"  : "Medan",
                "alamat": "Raden Saleh",
                "hobbi" : "Nonton Drakor",
                "sosmed": "@wlnsbn0",
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
            "https://drive.google.com/uc?export=view&id=1MKvTUMeJbuD0MixVvDtmS3jHsnDfoj_E",  # Yogi
            "https://drive.google.com/uc?export=view&id=1GZcOioJlC000XyfktJYUR2QJnDWhAuuM",
            "https://drive.google.com/uc?export=view&id=1GZcOioJlC000XyfktJYUR2QJnDWhAuuM",
            "https://drive.google.com/uc?export=view&id=1GZcOioJlC000XyfktJYUR2QJnDWhAuuM",
            "https://drive.google.com/uc?export=view&id=1GZcOioJlC000XyfktJYUR2QJnDWhAuuM",
            "https://drive.google.com/uc?export=view&id=1GZcOioJlC000XyfktJYUR2QJnDWhAuuM",
            "https://drive.google.com/uc?export=view&id=1GZcOioJlC000XyfktJYUR2QJnDWhAuuM",
            "https://drive.google.com/uc?export=view&id=1GZcOioJlC000XyfktJYUR2QJnDWhAuuM",
            "https://drive.google.com/uc?export=view&id=1GZcOioJlC000XyfktJYUR2QJnDWhAuuM",
            "https://drive.google.com/uc?export=view&id=1GZcOioJlC000XyfktJYUR2QJnDWhAuuM",
            "https://drive.google.com/uc?export=view&id=1GZcOioJlC000XyfktJYUR2QJnDWhAuuM",
            "https://drive.google.com/uc?export=view&id=1GZcOioJlC000XyfktJYUR2QJnDWhAuuM",
            "https://drive.google.com/uc?export=view&id=1GZcOioJlC000XyfktJYUR2QJnDWhAuuM",
            "https://drive.google.com/uc?export=view&id=1GZcOioJlC000XyfktJYUR2QJnDWhAuuM",
            "https://drive.google.com/uc?export=view&id=1GZcOioJlC000XyfktJYUR2QJnDWhAuuM",
            "https://drive.google.com/uc?export=view&id=1GZcOioJlC000XyfktJYUR2QJnDWhAuuM",
        ]
        data_list = [
            {
                "nama": "Yogi Sae Tama",#                "jabatan": "Kepala Departemen"
                "nim": "121450041",
                "umur": "21 Tahun",
                "asal": "Tangerang",
                "alamat": "Jatimulyo",
                "hobi": "Bangun pagi",
                "sosmed": "@yogyyyyyy",
                "kesan": "",
                "pesan": "",
            },
            {
                "nama": "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobi": "Jalan - Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan": "",
                "pesan": "",
                "jabatan": "Sekretaris Departemen"
            },
            {
                "nama": "Nazwa Nabila",#                "jabatan": "Kepala Divisi Hubungan Luar"
                "nim": "121450122",
                "umur": "21 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Way kandis",
                "hobi": "belajar",
                "sosmed": "@nazwanbilla",
                "kesan": "",
                "pesan": "",
            },
            {
                "nama": "Bastian Heskia Silaban",#                "jabatan": "Staff Divisi Hubungan Luar"
                "nim": "122450130",
                "umur": "21 Tahun",
                "asal": "Batam, Kep. Riau",
                "alamat": "Belwis",
                "hobi": "main game",
                "sosmed": "@bastiansilaban_",
                "kesan": "",
                "pesan": "",
            },
            {
                "nama": "Dea Mutia Risani", #                "jabatan": "Staff Divisi Hubungan Luar"
                "nim": "122450099",
                "umur": "20 Tahun",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobi": "dengerin musik",
                "sosmed": "@deaa.rsn",
                "kesan": "",
                "pesan": "",
            },
            {
                "nama": "Esteria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "19 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Belwis",
                "hobi": "Main golf bareng kadiv",
                "sosmed": "@esteriars",
                "kesan": "",
                "pesan": "",
                "jabatan": "Staff Divisi Hubungan Luar"
            },
            {
                "nama": "Natasya Ega Lina",
                "nim": "122450024",
                "umur": "19 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobi": "jadi humas",
                "sosmed": "@nateee__15",
                "kesan": "",
                "pesan": "",
                "jabatan": "Staff Divisi Hubungan Luar"
            },
            {
                "nama": "Novelia Adinda",
                "nim": "122450104",
                "umur": "21 Tahun",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "",
                "pesan": "",
                "jabatan": "Staff Divisi Hubungan Luar"
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Way Kandis",
                "hobi": "Main sepak takraw",
                "sosmed": "@jasminednva",
                "kesan": "",
                "pesan": "",
                "jabatan": "Staff Divisi Hubungan Luar"
            },
            {
                "nama": "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20 Tahun",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobi": "Jogging",
                "sosmed": "@tobiassiagian",
                "kesan": "",
                "pesan": "",
                "jabatan": "Staff Divisi Hubungan Luar"
            },
            {
                "nama": "Yohana Manik",
                "nim": "122450126",
                "umur": "19 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobi": "Main Bowling",
                "sosmed": "@yo_annamnk",
                "kesan": "",
                "pesan": "",
                "jabatan": "Staff Divisi Hubungan Luar"
            },
            {
                "nama": "Rizky Adrian Bennovry",
                "nim": "121450073",
                "umur": "21 Tahun",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobi": "Bikin portofolio",
                "sosmed": "@rzkdrnnn",
                "kesan": "",
                "pesan": "",
                "jabatan": "Kepala Divisi Pengabdian Masyarakat"
            },
            {
                "nama": "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20 Tahun",
                "asal": "Bandung",
                "alamat": "Way Huwi",
                "hobi": "Bertani",
                "sosmed": "@rafiramadhanmaulana",
                "kesan": "",
                "pesan": "",
                "jabatan": "Staff Divisi Pengabdian Masyarakat"
            },
            {
                "nama": "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20 Tahun",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobi": "Tepuk Semangat",
                "sosmed": "@u_yippy",
                "kesan": "",
                "pesan": "",
                "jabatan": "Staff Divisi Pengabdian Masyarakat"
            },
            {
                "nama": "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20 Tahun",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobi": "Q Time",
                "sosmed": "@chlfawww",
                "kesan": "",
                "pesan": "",
                "jabatan": "Staff Divisi Pengabdian Masyarakat"
            },
            {
                "nama": "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21 Tahun",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobi": "Nonton youtube, main game",
                "sosmed": "@alfaritziirvan",
                "kesan": "",
                "pesan": "",
                "jabatan": "Staff Divisi Pengabdian Masyarakat"
            },
            {
                "nama": "Izza Lutfia",
                "nim": "122450090",
                "umur": "20 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobi": "Main Rubik",
                "sosmed": "@izzalutfia",
                "kesan": "",
                "pesan": "",
                "jabatan": "Staff Divisi Pengabdian Masyarakat"
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobi": "Mengaji",
                "sosmed": "@alyaavanevi",
                "kesan": "",
                "pesan": "",
                "jabatan": "Staff Divisi Pengabdian Masyarakat"
            },
            {
                "nama": "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20 Tahun",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobi": "telat",
                "sosmed": "@rayths_",
                "kesan": "",
                "pesan": "",
                "jabatan": "Staff Divisi Pengabdian Masyarakat"
            },
            {
                "nama": "Tria Yunanni",
                "nim": "122450062",
                "umur": "20 Tahun",
                "asal": "Way Kanan",
                "alamat": "Sukarame",
                "hobi": "Baca Buku",
                "sosmed": "@tria_y062",
                "kesan": "",
                "pesan": "",
                "jabatan": "Staff Divisi Pengabdian Masyarakat"
                },
                ]
        display_images_with_data(gambar_urls, data_list)
        internal()

elif menu == "Departemen Internal":
    def internal():
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
    internal()

elif menu == "Departemen SSD":
    def ssd():
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