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
            "https://drive.google.com/uc?export=view&id=1ej7DmMzYHXwadapoaPvJlZdmKtzVLTFn", #bggumilang
            "https://drive.google.com/uc?export=view&id=1eiIt1-2UZUwFwOlVQZLFyuqcZ6GpOu3l", #bgpandra
            "https://drive.google.com/uc?export=view&id=1etruHRzcR2-lYFdecuhA8kav7T6vmODx", #kkmeliza
            "https://drive.google.com/uc?export=view&id=1W5lHqLHi4H-FDyk7QAOplHotSYpEjHCo", #kak putri
            "https://drive.google.com/uc?export=view&id=1edMtSywTfMR0wHOjjXpPRw5JY3kNCFO5", #kak hartiti
            "https://drive.google.com/uc?export=view&id=1RWzfvmts6Hp_U_STpy_2Xgs1opq5WXx_", #kak nadilla
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
                "kesan" : "kok mirip sama bang pandra",  
                "pesan" :"abang nya asik parah, semangat bang"
            },
            {
                "nama"  : "Pandra Insani Putra Azwan",
                "nim"   : "121450137",
                "umur"  : "21",
                "asal"  : "Bukit Kemuning, Lampung Utara",
                "alamat": "Bawen 2",
                "hobbi" : "Bermain gitar dan menyanyi",
                "sosmed": "@pandrainsni27",
                "kesan" : "abangnya tegas ui",  
                "pesan" : " semoga jalan kedepannya selalu dipermudah yaa bang"
            },
            {
                "nama"  : "Meliza Wulandari",
                "nim"   : "121450065",
                "umur"  : "20",
                "asal"  : "Pagar Alam, Sumatera Selatan",
                "alamat": "Kotabaru",
                "hobbi" : "Nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan" : "kirain kakanya pemarah",  
                "pesan" : "kakaknya asikk bgt.. tetap ceria terus ya kak"
            },
            {
                "nama"  : "Putri Maulida Chairani",
                "nim"   : "121450050",
                "umur"  : "21",
                "asal"  : "Payakumbuh, Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi" : "Dengerin bang pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan" : "di awal kakaknya terlihat jutek, ternyata ramah dan lemah lembut masyaallah",  
                "pesan" : "semangat selalu kakak "
            },
            {
                "nama"  : "Hartiti Fadilah",
                "nim"   : "121450031",
                "umur"  : "21",
                "asal"  : "Palembang",
                "alamat": "Pemda",
                "hobbi" : "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan" : "kakaknya  murah senyum dan manies sekali",  
                "pesan" : "semoga kita semua selalu di beri kemudahan ya kak dalam segala urusan"
            },
            {
                "nama"  : "Nadilla Andara Putri",
                "nim"   : "121450003",
                "umur"  : "21",
                "asal"  : "Metro",
                "alamat": "KotaBaru",
                "hobbi" : "Membaca",
                "sosmed": "@ndillaandr26",
                "kesan" : "kakaknya sangat tegas",  
                "pesan" : "tetap senyum selalu kakak.."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1f3zOYm4yR6u9QGhEuYWLNxbrZiBRt2uF", #kak tri
            "https://drive.google.com/uc?export=view&id=1f68XRRXCMQmZp881tK6DMUfBc6BOOykK", #kak anissa cahyani surya
            "https://drive.google.com/uc?export=view&id=1f8oqie2-0vPk_2nGQC9eLrL0xsBTIHYe", #kak wulan sabina
            "https://drive.google.com/uc?export=view&id=1ex5xNKfVnijxF-mRdk23P4OIiIJA4n3w", #kak anisa dini amalia
            "https://drive.google.com/uc?export=view&id=1fEKdLdLpYvg9g7FWjdx7c6lDXav-xg37", #kak anisa fitriyani
            "https://drive.google.com/uc?export=view&id=1f2I2hXTF1mIhUXE1ewVK5ICoB0OTgCVY", #bang mirzan
            "https://drive.google.com/uc?export=view&id=1f9oav-29ff0MC-H7vvvxGAkuA0NdUEFg", #kak dhea
            "https://drive.google.com/uc?export=view&id=1exRvElnVsm-1Z-Sdw6MJOlRLspZV5OOm", #bang fahrul
            "https://drive.google.com/uc?export=view&id=1eyqdJ7r8HkM0PsMZThhAdHwRWQg7JFeL", #bang berliana
            "https://drive.google.com/uc?export=view&id=1f0MwA1vJt77jB6KEmFcGNRt73C8zA1M4", #bang jeremi
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
                "kesan" : "waw kakaknya kayanya pemarah nih, ternyata aasik poll ",  
                "pesan" : "tegasnya kakak menurut zahra sangat berwibawa sekali, tutor dong kak, semoga bisa kaya kakak"
            },
            {
                "nama"  : "Annisa Cahyani Surya",
                "nim"   : "121450114",
                "umur"  : "21",
                "asal"  : "Tanggerang Selatan",
                "alamat": "Way Huwi",
                "hobbi" : "Membaca, Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan" : "asik bgt, dari awal datang wwc langsung asikeun ",  
                "pesan" : "senang bertemu dan kenal dengan kak nisaa"
            },
            {
                "nama"  : "Wulan Sabina",
                "nim"   : "121450150",
                "umur"  : "21",
                "asal"  : "Medan",
                "alamat": "Raden Saleh",
                "hobbi" : "Nonton Drakor",
                "sosmed": "@wlnsbn0",
                "kesan" : "kakaknya kalem, dan cantik masyallah",  
                "pesan" : " mau dung kak di ajarin terus ngodingnya.. sabar2 dalam menghadapi zahra ya kak"
            },
            {
                "nama"  : "Anisa Dini Amaliya",
                "nim"   : "121450081",
                "umur"  : "21",
                "asal"  : "Tanggerang",
                "alamat": "Jati Agung",
                "hobbi" : "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan" : "kakaknya baik dan perhatian",  
                "pesan" : "tetap semangat kakak dan semoga sukses selalu"
            },
            {
                "nama"  : "Anisa Fitriyani",
                "nim"   : "122450019",
                "umur"  : "20",
                "asal"  : "Batam",
                "alamat": "Kalianda",
                "hobbi" : "Membaca Al-Waqiah setiap maghrib",
                "sosmed": "@ansftynn_",
                "kesan" : "agak susah membedakan banyak sekali yang namanya annisa, tapi kakak ini n nya ga double",  
                "pesan" : "semangat selalu kak dan semoga sellau di berikan kelancaran "
            },
            {
                "nama"  : "Mirzan Yusuf Rabbani",
                "nim"   : "122450118",
                "umur"  : "20",
                "asal"  : "Jakarta",
                "alamat": "Korpri",
                "hobbi" : "Main Kucing",
                "sosmed": "@myrrinn",
                "kesan" : "abangnya baik dan kiyowo",  
                "pesan" :"tetap semangat dan senyum selalu bang"
            },
            {
                "nama"  : "Dhea Amelia Putri",
                "nim"   : "122450004",
                "umur"  : "20",
                "asal"  : "Sukabumi, Jawa Barat",
                "alamat": "Natar",
                "hobbi" : "Suka Ikut Tes SKD",
                "sosmed": "@dhea_wedding",
                "kesan" : "kakaknya baik dan sangat manies ",  
                "pesan" : "tetap tersenyum selalu kak dan jdilah pribadi yang kuat selalu"
            },
            {
                "nama"  : "Muhammad Fahrul Aditya",
                "nim"   : "121450156",
                "umur"  : "22",
                "asal"  : "Surakarta, Jawa Tengah",
                "alamat": "Pahoman",
                "hobbi" : "Melukis, badminton, hiking, ngopi, dengerin music, nonton film dan ngoding",
                "sosmed": "@fhrul.pdf",
                "kesan" : "abangnya kocak abis, hobinya banyak ",  
                "pesan" : "tetap optimis bang dan semangat selalu"
            },
            {
                "nama"  : "Berliana Enda Putri",
                "nim"   : "122450065",
                "umur"  : "21",
                "asal"  : "Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi" : "Main Game",
                "sosmed": "@berlyyanda",
                "kesan" : " takut bgtt, soalnya kakaknya agak keliatan judes, ternyata asikkeun ",  
                "pesan" : "senyum selalu kak dan tetap semangatt"
            },
            {
                "nama"  : "Jeremia Susanto",
                "nim"   : "122450022",
                "umur"  : "20",
                "asal"  : " Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi" : "Marah-marah",
                "sosmed": "@jeremia_s_",
                "kesan" : "abang asprak sayaa yg baik niehh",  
                "pesan" : "yang sabar ya bang kalau ngasprakin RB"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()
    
elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=13BjPv4iNx2UnI1ehlw8Gsg3o6hICWZA6", #kak lutfi
            "https://drive.google.com/uc?export=view&id=13C_WIjzAqNkXWTYWJsfvuHYsslyqtv9o", #bang bintang
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
                "kesan" : "kakaknya sangat inspiratif dan suka sama pembawaan kakaknya ",  
                "pesan" : "semangat semester akhirnya kak dan semoga selalu diberikan kelancaran dan kemudahan"
            },
            {
                "nama"  : "Rian Bintang Wijaya",
                "nim"   : "122450094",
                "umur"  : "20",
                "asal"  : "Palembang, Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi" : "Mendengar Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan" : "suka dengan cara abangnya dalam memaparkan penjelasan",  
                "pesan" : "Semoga kegiatannya di dalam maupun di luar perkuliahan tetap lancar yaa bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=123bAJPBTF6IqLOqjENneznuTJzW5QehH", #bang erickson dn
            "https://drive.google.com/uc?export=view&id=10jBDbbml3Jzk2NVwgT1h3sV6cNDJSuQv", #kak abeth dn
            "https://drive.google.com/uc?export=view&id=10ywwj9ykjxLuGAGMsQF2QOycfgLMW7Tt", #kak afifah dn
            "https://drive.google.com/uc?export=view&id=110_qUI8dW7E_6bOu0QdW3vvZTzWxVhDx", #kak allya dn
            "https://drive.google.com/uc?export=view&id=118JB-uYuDjEob0zFkSE1QJLZ_0Qnr0kE", #kak hanum dn
            "https://drive.google.com/uc?export=view&id=112xp2BBaqTI-eWyrYxA4IVJqYsJ-nVj2", #bang ferdy dn
            "https://drive.google.com/uc?export=view&id=113bOmgspLhGRy5wPLXi7Zmx5YTGMJCJH", #bang deri dn
            "https://drive.google.com/uc?export=view&id=11-00iNPJgMWpvluYjQ6kgWxUt46G6YNd", #kak oktavia dn
            "https://drive.google.com/uc?export=view&id=10u6f2RtxsP9OHNCjMh9oitU1VX2ufiMT", #bang deyvan dn
            "https://drive.google.com/uc?export=view&id=10pzmKogL70jLHVMZN2PE7Uh_muMpjfQt", #bang ibnu dn
            "https://drive.google.com/uc?export=view&id=10sZnyggi9uotUitjNXus3JILGP50JIWI", #bang jo dn
            "https://drive.google.com/uc?export=view&id=10tiW55xdN2f7tS5GGNu2LYNKuEeybIsC", #bang kemas dn
            "https://drive.google.com/uc?export=view&id=10m8hdh-oEEycxCNnJHtzQyYlQ6XxCGo4", #bang leonard dn
            "https://drive.google.com/uc?export=view&id=10k4Qu5zCk3hng_avwjxU_dkiEcnlVKGW", #kak presilia dn
            "https://drive.google.com/uc?export=view&id=10sEWijNMDc8dD5HOEwZo8E9XDWEz8FVu", #kak rafa dn
            "https://drive.google.com/uc?export=view&id=10oO7FsHkzQJIHDh5U_tLc-ll8RIWO5Qm", #bang sahid dn
            "https://drive.google.com/uc?export=view&id=10k7c3y3AfD_v6daByhkhEvRGvelZuRjY", #kak vanes dn
            "https://drive.google.com/uc?export=view&id=11H434a0pD5k9SPOTVQLU2mebBD7Qx-f5", #bang ateng dn
            "https://drive.google.com/uc?export=view&id=11Ife0mgFDCoKjOgWEQExQ4eoIOnkMx2J", #bang gede dn
            "https://drive.google.com/uc?export=view&id=13GQ_Oi24RK2WjEtF0u1eUvdF_D-bRZNx", #kak jaclin dn
            "https://drive.google.com/uc?export=view&id=11Aw2vJjnf-8Nj36DOvXhqMdb2_8UnI39", #bang rafly dn
            "https://drive.google.com/uc?export=view&id=11FcCPX_bVz1qCmyO5zNxIrlN3L_MLKvi", #kak dini dn

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
                "kesan" : "abangnya sangat tegas dan sangat berwibawa dalam memaparkan informasi ",  
                "pesan" : " tetap semangat dalam menjalankan amanah nya bang dan semoga segala urusannya di permudah"
            },
            {
                "nama"  : "Elisabeth Claudia Simanjuntak",
                "nim"   : "122450123",
                "umur"  : "18",
                "asal"  : "Pekanbaru",
                "alamat": "Sukarame",
                "hobbi" : "Memancing keributan",
                "sosmed": "@celisabethh_",
                "kesan" : "kakak abeth cantik banget dan murah senyum masyaallah",  
                "pesan" : "semangat terus kak "
            },
            {
                "nama"  : "Nisrina Nur Afifah",
                "nim"   : "122450052",
                "umur"  : "19",
                "asal"  : "Bekasi",
                "alamat": "Sukarame",
                "hobbi" : "Nabok orang",
                "sosmed": "@afifahhnsrn",
                "kesan" : "kakak fifah baik, asik, dan cantik beut ui",  
                "pesan" : "tetap senyum selaluu kak fifah, jaga kesehatan ya kak"
            },
            {
                "nama"  : "Allya Nurul Islami Pasha",
                "nim"   : "122450033",
                "umur"  : "20",
                "asal"  : "Sumatera Barat",
                "alamat": "Gang Perwira, Belwis",
                "hobbi" : "Nonton Dracin",
                "sosmed": "@allyaislami_",
                "kesan" : "sangat tegas dan serius dalam segala hal, dan informatif",  
                "pesan" : "semangat selalu kak allya, semoga segala langkahnya di permudah allah"
            },
            {
                "nama"  : "Farahanum Afifah Ardiansyah",
                "nim"   : "122450056",
                "umur"  : "20",
                "asal"  : "Padang, Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi" : "Tidur",
                "sosmed": "@farahanumafifahh",
                "kesan" : "kakaknya asik bgt, baik dan cantik oi",  
                "pesan" : "tetap semngat kakak dan tetap tersenyumm"
            },
            {
                "nama"  : "Ferdy Kevin Naibaho",
                "nim"   : "122450107",
                "umur"  : "19",
                "asal"  : "Medan, Sumatera Utara",
                "alamat": "Jalan Senopati Raya 18",
                "hobbi" : "Dengerin Rocky Gerung",
                "sosmed": "@ferdy_kevin",
                "kesan" : "abangnya cool bgt ui, ga banyak bicara",  
                "pesan" : "jaga kesehatan bang dan senyum selalu "
            },
            {
                "nama"  : "M. Deriansyah Okutra",
                "nim"   : "122450101",
                "umur"  : "19",
                "asal"  : "Kayu Agung",
                "alamat": "Jalan Pagar Alam",
                "hobbi" : "Bercerita horror",
                "sosmed": "@dransyh_",
                "kesan" : "abangnya asik dan inspiratif",  
                "pesan" : "semangat kuliahnyaa bang"
            },
            {
                "nama"  : "Oktavia Nurwinda Puspita Sari",
                "nim"   : "122450041",
                "umur"  : "20",
                "asal"  : "Lampung Timur",
                "alamat": "Way Hui",
                "hobbi" : "Memasak",
                "sosmed": "@_oktavianrwnda_",
                "kesan" : "Sangat seru dan informatif dalam menjelaskan sesuatu",  
                "pesan" : "Jangan lupa untuk tetap semangat dalam menjalani dunia perkuliahan kak, semoga urusannya selalu dilancarkan"
            },
            {
                "nama"  : "Deyvan Loxefal",
                "nim"   : "121450148",
                "umur"  : "21",
                "asal"  : "Riau",
                "alamat": "Pulau Damar",
                "hobbi" : "Belajar",
                "sosmed": "@depanloo",
                "kesan" : "ternyata kitaa dari daerah yang samaa yaa bang",  
                "pesan" : "semangat semester akhirnya ya bang, semoga selalu di permudah, info pulang kampung bareng lahhh"
            },
            {
                "nama"  : "Ibnu Farhan Al-Ghifari",
                "nim"   : "121450121",
                "umur"  : "21",
                "asal"  : "Jambi",
                "alamat": "Pulau Damar, Kobam",
                "hobbi" : "Bermain Game Online",
                "sosmed": "@al_ghifari032",
                "kesan" : "abangnya ganteng, dan asik serta inspiratif ",  
                "pesan" : "jaga kesehatan bang, dan semangat semester akhirnya"
            },
             {
                "nama"  : "Johannes Krisjon Silitonga",
                "nim"   : "122450043",
                "umur"  : "19",
                "asal"  : "Tanggerang",
                "alamat": "Jalan Lapas",
                "hobbi" : "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan" : "abangnya tegas, tetapi lemah lembut, dan serius dalam menjelaskaan segala sesuatu",  
                "pesan" : "tetap semangat bang dan jaga kak abeth "
            },
            {
                "nama"  : "Kemas Veriandra Ramadhan",
                "nim"   : "122450016",
                "umur"  : "19",
                "asal"  : "Bekasi",
                "alamat": "Golf Asri",
                "hobbi" : "Bermain ular python digital",
                "sosmed": "@kemasverii",
                "kesan" : "bang kemash sangat inspiratif apalagi dalam percodingan",  
                "pesan" : "semangat yaa bangg dan jaga kesehatan "
            },
            {
                "nama"  : "Leonard Andreas Napitupulu",
                "nim"   : "121450153",
                "umur"  : "21",
                "asal"  : "Sumatera Utara",
                "alamat": "Kobam",
                "hobbi" : "Belajar",
                "sosmed": "@lnrd.__",
                "kesan" : "Sangat baik, informatif dalam menerangkan suatu permasalahan dan sangat menginspirasi",  
                "pesan" : "Tetap semangat bang dalam menjalani harinya, semoga urusannya baik di akademik maupun non akademik dapat berjalan dengan lancar"
            },
            {
                "nama"  : "Presilia",
                "nim"   : "122450081",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Kota Baru",
                "hobbi" : "Tidur",
                "sosmed": "@presiliamg",
                "kesan" : "kakaknya cantik sekali masyallah",  
                "pesan" : "semangat kuliahnya kak, jaga kesehatan yah"
            },
            {
                "nama"  : "Rafa Aqilla Jungjunan",
                "nim"   : "122450142",
                "umur"  : "20",
                "asal"  : "Riau",
                "alamat": "Belwis",
                "hobbi" : "Membaca webtoon",
                "sosmed": "@rafaaqilla",
                "kesan" : "Syok kakaknya juga satu daerah sama akuuu",  
                "pesan" : "semangatt kak kulyah nyaa dan infokan pulbar"
            },
            {
                "nama"  : "Sahid Maulana",
                "nim"   : "122450109",
                "umur"  : "21",
                "asal"  : "Depok, Jawa Barat",
                "alamat": "Airan Raya",
                "hobbi" : "Bermain Game",
                "sosmed": "@sahid_maul19",
                "kesan" : "Sabangnya asik dan menginspirasi ",  
                "pesan" : "jaga kesehatan bang semangat selalu"
            },
            {
                "nama"  : "Vanessa Olivia Rose",
                "nim"   : "121450108",
                "umur"  : "20",
                "asal"  : "Jakarta",
                "alamat": "Perumahan Korpri",
                "hobbi" : "Belajar",
                "sosmed": "@roselivnes__",
                "kesan" : "Sangat baik dan sangat mengasyikkan ",  
                "pesan" : "Semangat terus kak dalam menjalani perkuliahannya serta jangan lupa untuk jaga kesehatan"
            },
            {
                "nama"  : "M. Farhan Athaulloh",
                "nim"   : "121450117",
                "umur"  : "21",
                "asal"  : "Bandar Lampung",
                "alamat": "Kota Baru",
                "hobbi" : "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan" : "abangnya asik dan lucu ",  
                "pesan" : "semangat semester akhirnya ya bang dan lanjutkan hobbynya bang"
            },
            {
                "nama"  : "Gede Moena",
                "nim"   : "121450014",
                "umur"  : "21",
                "asal"  : "Bekasi",
                "alamat": "Korpri Raya",
                "hobbi" : "Belajar dan main game",
                "sosmed": "@gedemoenaa",
                "kesan" : "abangnya baik dan tegas dalam ",  
                "pesan" : "jaga kesehatan dan semangat terus bang "
            },
            {
                "nama"  : "Jaclin Alcavella",
                "nim"   : "122450015",
                "umur"  : "19",
                "asal"  : "Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi" : "Berenang",
                "sosmed": "@jaclinalcv_",
                "kesan" : "kaknya manie bgt dan asik ",  
                "pesan" : "jaga jesehatan dan smeoga segala urusan kita di permudah allah "
            },
            {
                "nama"  : "Rafly Prabu Darmawan",
                "nim"   : "122450140",
                "umur"  : "20",
                "asal"  : "Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi" : "Main Game",
                "sosmed": "@raflyy_pd2684",
                "kesan" : "abangnya baik dan sangat informatif dalam meenjelaskan sesuatu ",  
                "pesan" : "jaga kesehatan dan semangat terus bang"
            },
            {
                "nama"  : "Syalaisha Andini Putriansyah",
                "nim"   : "122450111",
                "umur"  : "21",
                "asal"  : "Tanggerang",
                "alamat": "Sukarame",
                "hobbi" : "Membaca",
                "sosmed": "@syalaisha.i__",
                "kesan" : "kakaknya pendiam tetapi kalau sekali menjelaskan sesuatu sangat isnpiratif ",  
                "pesan" : " jaga kesehatan dan semoga segala urusan  kita dipermudah "
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=12NrIxITy9fhjtrhCzViu8fnPtOQBPcHY", #bang rafi dn
            "https://drive.google.com/uc?export=view&id=1290B0LKeZudQl8gWNGF5DL-CznRhnJLC", #bang ahmad dn
            "https://drive.google.com/uc?export=view&id=12IIr9ijQwSzvQTXt1ELp5F0ES2YQ1qyh", #bang fadhil dn
            "https://drive.google.com/uc?export=view&id=12F8TC9Kls54jGfZ-5hnuBqKDGZp27r5g", #kak dina dn
            "https://drive.google.com/uc?export=view&id=12BMIz8OoXWImNlRSH_q7KqG0sxBGQaGc", #kak dinda dn
            "https://drive.google.com/uc?export=view&id=126aoCGLPMfsdL2JTi2v_zV2hroD5cmx_", #kak marleta dn
            "https://drive.google.com/uc?export=view&id=12GcdqIkOWMlJk8jRkHm4PywA_qOlSmDH", #kak rut junita dn
            "https://drive.google.com/uc?export=view&id=126Xdb8oQLXuU1zcjsRT4RXMbA8yDoDOW", #kak syadza dn
            "https://drive.google.com/uc?export=view&id=12O3iE5QF7V-yhnrqi6R4L9lGDDZThH9o", #bang eggi dn
            "https://drive.google.com/uc?export=view&id=12Ju45BdS1rNBio52bMKmEZ8SfqlVzbFu", #kak febiya dn
            "https://drive.google.com/uc?export=view&id=126Iobj6mikUfBZ-ZEoB0FtWuQcXWNc1l", #kak happy syahrul dn
            "https://drive.google.com/uc?export=view&id=12JMZdhVJ7W8lh8f4cbzrnQisWB_awJY7", #bang randa dn
            "https://drive.google.com/uc?export=view&id=12G87S0jK9h59TfRmgV6ME7YjipdT4nSg", #kak vita dn
            
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
                "kesan" : "abangnya asik dalam menjelaskan sesuatu sangat rinci dan sangat informatif ",  
                "pesan" : "tetap semnat dan semoga amanah dalam mengemban tanaggung jawab bang "
            },
            {
                "nama"  : "Annisa Novantika",
                "nim"   : "121450005",
                "umur"  : "21",
                "asal"  : "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi" : "Memasak",
                "sosmed": "@anovavona",
                "kesan" : "kakaknya baik dan cantik",  
                "pesan" : "tetap semangat kakak dan tetap tersenyum selalu "
            },
            {
                "nama"  : "Ahmad Sahidin Akbar",
                "nim"   : "122450044",
                "umur"  : "20",
                "asal"  : "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi" : "Olahraga",
                "sosmed": "@sahid22__",
                "kesan" : "abangnya baik dan informatif ",  
                "pesan" : "semangat kuliahnya baang semoga setiap langkah selalu di permudah allah "
            },
            {
                "nama"  : "Fadhil Fitra Wijaya",
                "nim"   : "122450082",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Teluk Betung",
                "hobbi" : "Main game",
                "sosmed": "@fadhilfwee",
                "kesan" : "abangnya terlihat pendiam, tetapi asik dan sangat mengasyikkan ",  
                "pesan" : "semaangat abang kuliahnya semoga semuanya selalu di perlancar allah "
            },
            {
                "nama"  : "Syalaisha Andina Putriansyah",
                "nim"   : "122450121",
                "umur"  : "21",
                "asal"  : "Tangerang",
                "alamat": "Gang Yudhistira",
                "hobbi" : "Baca jurnal",
                "sosmed": "@dkselsd_31",
                "kesan" : "kirain kakaknya pendiam, ternyata asik poll dan sangat menginspiratif",  
                "pesan" : "tetap senyum selalu dan semoga segala langkahnya dipermudah allah"
            },
            {
                "nama"  : "Dinda Nababan",
                "nim"   : "122450120",
                "umur"  : "20",
                "asal"  : "Medan, Sumatera Utara",
                "alamat": "Jalan Lapas",
                "hobbi" : "Belajar",
                "sosmed": "@dindanababan_",
                "kesan" : "Sangat baik dan sangat menginspirasi dalam kehidupan",  
                "pesan" : "Tetap semangat dalam menjalani perkuliahannya kak dan jangan lupa jaga kesehatan"
            },
            {
                "nama"  : "Marleta Cornelia Leander",
                "nim"   : "122450092",
                "umur"  : "20",
                "asal"  : "Depok, Jawa Barat",
                "alamat": "Gang Nangka 3",
                "hobbi" : "Review Jurnal",
                "sosmed": "@marletacornelia",
                "kesan" : "kakaknya baik dan ramah sekali",  
                "pesan" : "semangat kakak kuliahnya "
            },
            {
                "nama"  : "Rut Junita Sari Siburian",
                "nim"   : "122450103",
                "umur"  : "20",
                "asal"  : "Batam, Kepulauan Riau",
                "alamat": "Gang Nangka 3",
                "hobbi" : "Review Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan" : "kakaknya manis sekali dan sangat menginspirasi",  
                "pesan" : "tetap senyum selalu kak dan semangat"
            },
            {
                "nama"  : "Syadza Puspadari Azhar",
                "nim"   : "122450072",
                "umur"  : "20",
                "asal"  : "Palembang",
                "alamat": "Belwis",
                "hobbi" : "Resume SG",
                "sosmed": "@puspadrr",
                "kesan" : "Sangat seru dan informatif dalam menjelaskan sesuatu",  
                "pesan" : "Jangan lupa untuk tetap semangat dalam menjalani dunia perkuliahan kak, semoga urusannya selalu dilancarkan"
            },
            {
                "nama"  : "Eggi satria",
                "nim"   : "122450032",
                "umur"  : "20",
                "asal"  : "Sukabumi",
                "alamat": "Korpri",
                "hobbi" : "Ngoding WISATA",
                "sosmed": "@egistr",
                "kesan" : "abang eggi sangat menginspiraatif dan asyik sekali",  
                "pesan" : "semangat kuliahnyaa abang, infokan jadwal tutor nyaaa"
            },
            {
                "nama"  : "Febiya Jomy Pratiwi",
                "nim"   : "122450074",
                "umur"  : "20",
                "asal"  : "Tulang Bawang",
                "alamat": "Jalan Kelengkeng Raya",
                "hobbi" : "Review jurnal",
                "sosmed": "@pratiwifebiya",
                "kesan" : "kakaknya baik dan manies masyallah",  
                "pesan" : "senyum selalu kak dan jangan lupa jaga kesehatan yahh"
            },
             {
                "nama"  : "Happy Syahrul Ramadhan",
                "nim"   : "122450013",
                "umur"  : "20",
                "asal"  : "Lampung Timur",
                "alamat": "Karang Anyar",
                "hobbi" : "Main game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan" : "abangnya ganteng, manies dan sangat mengisnpirasi",  
                "pesan" : "semangat bang kuliahnya dan jangan lupa janaga kesehatan "
            },
            {
                "nama"  : "Randa Andriana Putra",
                "nim"   : "122450083",
                "umur"  : "21",
                "asal"  : "Banten",
                "alamat": "Sukarame",
                "hobbi" : "Tidur dan berkembang",
                "sosmed": "@randaandriana_",
                "kesan" : "abangnya sangat pintar oii, mentor matdas 1 waktu tpb",  
                "pesan" : "semangatt yaa bang randa kuliahnyaa, infokan reuni tpb 1"
            },

        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen MEDKRAF":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=13AP46Z7Y78mJmwUBk-0CqmnhuIoMha1I", #bang wahyu dn
            "https://drive.google.com/uc?export=view&id=1334ZLuoRyAqiCvkItikhgYUzyOYwUySd", #kak elok dn
            "https://drive.google.com/uc?export=view&id=12ZtA-WjDA7uVgMDYZBVdLw-KPh3EZsMM", #kak arsyiah dn
            "https://drive.google.com/uc?export=view&id=12YH8hkEdOiqizXJkJc9ZliUgxiqPEAIE", #kak cintya dn
            "https://drive.google.com/uc?export=view&id=136lAl1dCoAT_a5jyIaWUi1jh9f3VRndM", #kak najla dn
            "https://drive.google.com/uc?export=view&id=137MbJFSxUeKFGHK077-HP6rxw0z6ooeT", #kak rahma dn
            "https://drive.google.com/uc?export=view&id=13AmNbsm_dDV_QH2LxEHrPF4CV1mNXWPa", #kak try yani dn
            "https://drive.google.com/uc?export=view&id=12kvFQZiyalGX6rHefrMU6_caTSyy6nSy", #bang kaisar dn
            "https://drive.google.com/uc?export=view&id=12xcRcIb304wdPANr_asMgtxhLrpKvbJi", #kak dwi dn
            "https://drive.google.com/uc?export=view&id=12pQEeSsK1uQmtxUiNskZZYzyovrTZydu", #bang gym dn
            "https://drive.google.com/uc?export=view&id=13-vm0jOIdlauXEE95iW31PBR-yd-a20Y", #kak nasywa dn
            "https://drive.google.com/uc?export=view&id=12dvU5_PkFCYlOKyuw00V7i010hSAKvEd", #kak priska dn
            "https://drive.google.com/uc?export=view&id=132KBFRY3pSI7kpONV75pFPbfJYKET9_l", #bang arsal dn
            "https://drive.google.com/uc?export=view&id=12mRl4wPdJskqmTYm-zvSW3czK2iHjeYO", #bang abit dn
            "https://drive.google.com/uc?export=view&id=12xuH5YX2XuLRGXaBPk0qd0qFEfGbPGJj", #bang akmal dn
            "https://drive.google.com/uc?export=view&id=134x0Kzc1qfK6UVHJn6FKh1Ff4mW19V3l", #bang hermawan dn
            "https://drive.google.com/uc?export=view&id=12YklnAr3TfAgjLQo4nxZhQYKgykN999R", #kak nisa dn
        ]
        data_list = [
            {
                "nama"  : "Wahyudiyanto",
                "nim"   : "121450040",
                "umur"  : "22",
                "asal"  : "Makassar ",
                "alamat": "Sukarame",
                "hobbi" : "Menonton Film",
                "sosmed": "@wayyulaja",
                "kesan" : "abangnya asik dan sangat sangat care ",  
                "pesan" : "jaga kesehatan yaa bang dan semoga segaloa langkahnya di permudah allah "
            },
            {
                "nama"  : "Elok Fiola",
                "nim"   : "122450051",
                "umur"  : "19",
                "asal"  : "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi" : "Editing",
                "sosmed": "@elokfiola",
                "kesan" : "Sangat informatif dalam menjelaskan sesuatu dan banyak memberikan motivasi",  
                "pesan" : "Semoga kegiatannya di dalam maupun di luar perkuliahan tetap lancar dan tetap semangat kak"
            },
            {
                "nama"  : "Arsyiah Azahra",
                "nim"   : "121450035",
                "umur"  : "21",
                "asal"  : "Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi" : "Nugas",
                "sosmed": "@arsyiah.__",
                "kesan" : "Sangat baik, informatif dalam menerangkan suatu permasalahan dan sangat menginspirasi",  
                "pesan" : "Tetap semangat kak dalam menjalani harinya, semoga urusannya baik di akademik maupun non akademik dapat berjalan dengan lancar"
            },
            {
                "nama"  : "Cintya Bella",
                "nim"   : "122450066",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Teluk",
                "hobbi" : "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan" : "Sangat informatif dalam menerangkan sesuatu dan sangat menginspirasi",  
                "pesan" : "Semoga selalu dilancarkan semua urusannya kak, jangan lupa untuk tetap semangat kak dalam menjalani kehidupan"
            },
            {
                "nama"  : "Najla Juwairia",
                "nim"   : "122450037",
                "umur"  : "19",
                "asal"  : "Sumatera Utara",
                "alamat": "Airan",
                "hobbi" : "Menulis, Membaca, Fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan" : "Sangat baik dan sangat menginspirasi dalam kehidupan",  
                "pesan" : "Tetap semangat dalam menjalani perkuliahannya kak dan jangan lupa jaga kesehatan"
            },
            {
                "nama"  : "Rahma Neliyana",
                "nim"   : "122450036",
                "umur"  : "20",
                "asal"  : "Lampung",
                "alamat": "Sukarame",
                "hobbi" : "Baca Coding",
                "sosmed": "@rahmanellyana",
                "kesan" : "Ibundanya markov nihh sangat sangat asik sekali ",  
                "pesan" : "Tetap semangat kak dalam menjalani dunia perkuliahan nyaa kak nel"
            },
            {
                "nama"  : "Try Yani Rizki Nur Rohmah",
                "nim"   : "122450020",
                "umur"  : "20",
                "asal"  : "Lampung Barat",
                "alamat": "Korpri",
                "hobbi" : "Bernyanyi dan Menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan" : "Sangat baik dan sangat mengasyikkan ",  
                "pesan" : "Semangat terus kak dalam menjalani perkuliahannya serta jangan lupa untuk jaga kesehatan"
            },
            {
                "nama"  : "Muhammad Kaisar Firdaus",
                "nim"   : "121450135",
                "umur"  : "21",
                "asal"  : "Pesawaran",
                "alamat": "Pulau Damar",
                "hobbi" : "Lagi nyari",
                "sosmed": "@dino_lapet",
                "kesan" : "Sangat seru dan informatif dalam menjelaskan sesuatu",  
                "pesan" : "Jangan lupa untuk tetap semangat dalam menjalani dunia perkuliahan kak, semoga urusannya selalu dilancarkan"
            },
            {
                "nama"  : "Dwi Ratna Anggraeni",
                "nim"   : "122450008",
                "umur"  : "20",
                "asal"  : "Jambi",
                "alamat": "Jalan Durian 5 Pemda",
                "hobbi" : "Membaca",
                "sosmed": "@dwiratnn_",
                "kesan" : "Sangat baik dan sangat informatif dalam menjelaskan sesuatu",  
                "pesan" : "Semangat terus kak dalam menjalani hari-harinya, semoga semua tugas dan tanggung jawab yang diemban dapat diselesaikan dengan lancar"
            },
            {
                "nama"  : "Gymnastiar Al Khoarizmy",
                "nim"   : "122450096",
                "umur"  : "20",
                "asal"  : "Serang",
                "alamat": "Lapangan Golf UIN",
                "hobbi" : "Baca komik",
                "sosmed": "@jimnn.as",
                "kesan" : "Sangat baik dan sangat mengasyikkan",  
                "pesan" : "Semangat kak dalam menjalani hari-harinya, semoga urusannya dalam dunia perkuliahan dapat diselesaikan dengan mudah"
            },
             {
                "nama"  : "Nasywa Nur Afifah",
                "nim"   : "122450125",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Jalan Durian 1 Pemda",
                "hobbi" : "Nonton drakor",
                "sosmed": "@nsywanaf",
                "kesan" : "kakanya baik dan asik",  
                "pesan" : "Tetap semangat kak dalam menjalani hari-harinya, semoga diperlancar dalam menyelesaikan tugas dan tanggung jawab yang sedang di emban"
            },
            {
                "nama"  : "Priska Silvia Ferantiana",
                "nim"   : "122450053",
                "umur"  : "19",
                "asal"  : "Palembang",
                "alamat": "Jalan Nangka 2",
                "hobbi" : "Baca novel yang bikin nangis",
                "sosmed": "@prskslv",
                "kesan" : "kakanya baik da cantik",  
                "pesan" : "semangat kuliahnya kak"
            },
            {
                "nama"  : "Muhammad Arsal Ranjana Utama",
                "nim"   : "121450111",
                "umur"  : "21",
                "asal"  : "Depok",
                "alamat": "Jalan Nangka 4",
                "hobbi" : "Ngoding",
                "sosmed": "@arsal.utama",
                "kesan" : "abangnya pintar dan sangat menginspirasi",  
                "pesan" : "semangat kuliahnya bang dan jaga kesehatan yaww"
            },
            {
                "nama"  : "Abit Ahmad Oktarian",
                "nim"   : "122450042",
                "umur"  : "19",
                "asal"  : "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi" : "Ngoding, Gaming",
                "sosmed": "@abitahmad",
                "kesan" : "abangnya pintar dan sangat menginspirasi ",  
                "pesan" : "semangat abang kuliahnya, jangan lupa jaga kesehatan"
            },
            {
                "nama"  : "Akmal Faiz Abdillah",
                "nim"   : "122450114",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi" : "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan" : "abanya asik dan ramah serta sabar sekali dalam menghadapi anak rb",  
                "pesan" : "semangat kuliahnya bang akmal dan jaga kesehatan"
            },
            {
                "nama"  : "Hermawan Manurung",
                "nim"   : "122450069",
                "umur"  : "20",
                "asal"  : "Bogor",
                "alamat": "Dekat jalan tol, Wisma Hana Hani",
                "hobbi" : "Bengong dan membaca buku",
                "sosmed": "@hermawan.mnrng",
                "kesan" : "abangnya seru banget dan  humoris",  
                "pesan" : "jaga kesehatan dan semangat terus bang"
            },
            {
                "nama"  : "Khusnun Nisa",
                "nim"   : "122450078",
                "umur"  : "20",
                "asal"  : "Lampung Selatan",
                "alamat": "Belwis",
                "hobbi" : "Mengerjakan tugas",
                "sosmed": "@khusnun_nisa335",
                "kesan" : "kakanya ucul dan manis ",  
                "pesan" : "semangat kuliahnya kak nun "
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=13zadnRLz461g-smod9yAfKlVMF-NzYI2", #bang yogy dn
            "https://drive.google.com/uc?export=view&id=145rXKd0SqktFF1EeCjNDx5yOHRPuPX3r", #kak ramadhita dn
            "https://drive.google.com/uc?export=view&id=13xKrAtmFRsiLdM-FaRZHRUuFh0BjdkhK", #kak nazwa dn
            "https://drive.google.com/uc?export=view&id=13yj4P5U31wf_5-iK0UYlsbzmBPivrcpQ", #bang bastian dn
            "https://drive.google.com/uc?export=view&id=13uJqCVddkb4I9QchMg4r5V1rWyFQSxsE", #kak dea dn
            "https://drive.google.com/uc?export=view&id=13uSPqNTpPCcv0YJ6nv96RbZZTaIiFQT2", #kak esteria dn
            "https://drive.google.com/uc?export=view&id=13vm-Aj-OPWMDEDjnCuPLuYYvT6j6aEuO", #kak natasya ega dn
            "https://drive.google.com/uc?export=view&id=13yJB9ZwPP2Keoc2ulLqYmbVhxD_0-q9h", #kak novelia dn
            "https://drive.google.com/uc?export=view&id=143gwxi4FhAm42SHAAi0VBVtTv0jm2kEI", #kak jasmine dn
            "https://drive.google.com/uc?export=view&id=13xoAb9-nO3YFGCUZV74KCGx-SXhxyrxd", #bang tobias dn
            "https://drive.google.com/uc?export=view&id=13tJ_0OJLO1fuKNJnSlniwWbLMKvVBzyF", #kak yohana dn
            "https://drive.google.com/uc?export=view&id=13rqqc5bi_3XRgQNBu_NgGPkQ0-CFDJwu", #bang rizki dn
            "https://drive.google.com/uc?export=view&id=149Ia6LMc6akXYruh49sahKbohO8T0NZv", #bang arafi dn
            "https://drive.google.com/uc?export=view&id=13szg4La6ZEV-S0RFYSyJHH2KZaZ7lXyx", #kak uyi dn
            "https://drive.google.com/uc?export=view&id=14B-XTBQ9tJCYYw1RtUGc5MgBGte62nGA", #kak chalifia dn
            "https://drive.google.com/uc?export=view&id=14D5zQIjeZALGUWn7mT-INFZcpzCMdvHc", #bang irvan dn
            "https://drive.google.com/uc?export=view&id=13ysjxJIAMpNLePj3qwVwROSvbSB2ziJF", #kak izza dn
            "https://drive.google.com/uc?export=view&id=143fUyjMSmISrWV2TajNaNAPCiHLXj20V", #kak zuhrah dn
            "https://drive.google.com/uc?export=view&id=14-VM5QDpMWdhrSuE17XDOiJTJfFLU5aV", #bang raid dn
            "https://drive.google.com/uc?export=view&id=140LUfKgUap8kNtZiRyMAXisFR01hq40C", #kak tria dn
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
                "kesan" : "abangnya asik dan sangat menginspirasi",  
                "pesan" : " tetap semangat bang dalam mengemban amanah dan tanggung jawab "
            },
            {
                "nama"  : "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan" : "kakanya tegas tapi asik sekali",  
                "pesan" : "semangat kakak jangan lupa tersenyum selalu "
            },
            {
                "nama"  : "Nazwa Nabilla",
                "nim": "121450122",
                "umur": "21 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Way kandis",
                "hobbi": "belajar",
                "sosmed": "@nazwanbilla",
                "kesan" : "Sangat baik, informatif dalam menerangkan suatu permasalahan dan sangat menginspirasi",  
                "pesan" : "Tetap semangat kak dalam menjalani harinya, semoga urusannya baik di akademik maupun non akademik dapat berjalan dengan lancar"
            },
            {
                "nama"  : "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21 Tahun",
                "asal": "Batam, Kep. Riau",
                "alamat": "Belwis",
                "hobbi": "main game",
                "sosmed": "@bastiansilaban_",
                "kesan" : "abangnya keliatan pendiaam, tapi sekalinya bicara sangat menginspirasi",  
                "pesan" : "jaga kesehatan yaa bang semangatt"
            },
            {
                "nama"  : "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20 Tahun",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "dengerin musik",
                "sosmed": "@deaa.rsn",
                "kesan" : "kakak pj waktu pplk prodi, inget bgtt",  
                "pesan" : "tetap semangat kakak dan selalu tersenyum yaaa"
            },
            {
                "nama"  : "Esteria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "19 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Belwis",
                "hobbi": "Main golf bareng kadiv",
                "sosmed": "@esteriars",
                "kesan" : "Sangat menginspirasi dalam kehidupan ",  
                "pesan" : "Tetap semangat kak dalam menjalani dunia perkuliahan"
            },
            {
                "nama"  : "Natasya Ega Lina",
                "nim": "122450024",
                "umur": "19 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi": "jadi humas",
                "sosmed": "@nateee__15",
                "kesan" : "kakaknya seruu abies",  
                "pesan" : "semangatt kuliahnyaa kakakk"
            },
            {
                "nama"  : "Novelia Adinda",
                "nim": "122450104",
                "umur": "21 Tahun",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan" : "kakanya anggunly sekali",  
                "pesan" : "semangat kakakk jaga kesehatan yah"
            },
            {
                "nama"  : "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Main sepak takraw",
                "sosmed": "@jasminednva",
                "kesan" : "kakak asprak ads yang sangat sabar dan seru abies",  
                "pesan" : "Semangat terus kak dalam menjalani hari-harinya, semoga semua tugas dan tanggung jawab yang diemban dapat diselesaikan dengan lancar"
            },
            {
                "nama"  : "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20 Tahun",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Jogging",
                "sosmed": "@tobiassiagian",
                "kesan" : "Sabangnya tegas dan berwibawa",  
                "pesan" : "selalu semangat dan jaga kesehatan ya bang "
            },
             {
                "nama"  : "Yohana Manik",
                "nim": "122450126",
                "umur": "19 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi": "Main Bowling",
                "sosmed": "@yo_annamnk",
                "kesan" : "kakaknya manies dan asik",  
                "pesan" : "Tetap semangat kak dalam menjalani hari-harinya, semoga diperlancar dalam menyelesaikan tugas dan tanggung jawab yang sedang di emban"
            },
            {
                "nama"  : "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21 Tahun",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobbi": "Bikin portofolio",
                "sosmed": "@rzkdrnnn",
                "kesan" : "Sangat informatif dalam menjelaskan sesuatu dan banyak memberikan motivasi",  
                "pesan" : "Semoga kegiatannya di dalam maupun di luar perkuliahan tetap lancar dan tetap semangat kak"
            },
            {
                "nama"  : "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20 Tahun",
                "asal": "Bandung",
                "alamat": "Way Huwi",
                "hobbi": "Bertani",
                "sosmed": "@rafiramadhanmaulana",
                "kesan" : "abangnya unik dan humoris ",  
                "pesan" : "semanagt kuliahnya bangg"
            },
            {
                "nama"  : "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20 Tahun",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobbi": "Tepuk Semangat",
                "sosmed": "@u_yippy",
                "kesan" : "kakanya unik banget dan asyikk",  
                "pesan" : "semangat selalu kak uyii dan jangan lupa jaga kesehatan yach"
            },
            {
                "nama"  : "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20 Tahun",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Q Time",
                "sosmed": "@chlfawww",
                "kesan" : "Sangat baik dan sangat menginspirasi dalam kehidupan",  
                "pesan" : "Tetap semangat dalam menjalani perkuliahannya kak dan jangan lupa jaga kesehatan"
            },
            {
                "nama"  : "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21 Tahun",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton youtube, main game",
                "sosmed": "@alfaritziirvan",
                "kesan" : "abangnya baik dan seruu",  
                "pesan" : "Tetap semangat bang dalam menjalani dunia perkuliahan"
            },
            {
                "nama"  : "Izza Lutfia",
                "nim": "122450090",
                "umur": "20 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Main Rubik",
                "sosmed": "@izzalutfia",
                "kesan" : "kakak yang sangat sangat aktif dan super asik",  
                "pesan" : "Semangat terus kak dalam menjalani perkuliahannya serta jangan lupa untuk jaga kesehatan"
            },
            {
                "nama"  : "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@alyaavanevi",
                "kesan" : "kakaknya cantik dan baik",  
                "pesan" : "Jangan lupa untuk tetap semangat dalam menjalani dunia perkuliahan kak, semoga urusannya selalu dilancarkan"
            },
            {
                "nama"  : "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20 Tahun",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "telat",
                "sosmed": "@rayths_",
                "kesan" : "abangnyabhumoris dan seru poll",  
                "pesan" : "tetap semangat dan lanjutkan amanah serta tanggung jawab yang diemban"
            },
            {
                "nama"  : "Tria Yunanni",
                "nim": "122450062",
                "umur": "20 Tahun",
                "asal": "Way Kanan",
                "alamat": "Sukarame",
                "hobbi": "Baca Buku",
                "sosmed": "@tria_y062",
                "kesan" : "kak yunaa orngnya ramah dan selalu tersenyum manis",  
                "pesan" : "semangat selalu kakak jaga keshatan ya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()  

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=14fMGnW66fSMDeYUUyJJYOmFoE7ZwOlRI", #bang dimas dn
            "https://drive.google.com/uc?export=view&id=13PvX_jmcJ2EvmaIOTznNTYK6Ufemfo_p", #kak catherine dn
            "https://drive.google.com/uc?export=view&id=13KWS2iJZtQnfCRPvekT2WelTOeTkvOzk", #bang akbar dn
            "https://drive.google.com/uc?export=view&id=14ZT_laxsZylJXy8lvtoPI0ezDZjUyghz", #kak rani dn
            "https://drive.google.com/uc?export=view&id=13L1043qUl60rKRVgol38JhuyL5C73Gw-", #bang rendra dn
            "https://drive.google.com/uc?export=view&id=14cIfgcmhoyc1USA9OO7OqXk3c9nTG7hv", #kak salwa dn
            "https://drive.google.com/uc?export=view&id=13H4dALsMhNcdlz6ykACKaw1qcSIJnhsc", #bang yosia dn
            "https://drive.google.com/uc?export=view&id=13hdqV_uBoNbas1j7THIRqtCnzBtmT6nS", #bang ari dn
            "https://drive.google.com/uc?export=view&id=14YeP1PwghOzuqM329c9aQrJ-sq3ACJ4N", #kak azizah dn
            "https://drive.google.com/uc?export=view&id=14ZNN83kNM_Xk-WBE1N9GCLbCJ2OOozwd", #kak meira dn
            "https://drive.google.com/uc?export=view&id=14XinaZ0ccX-2asciiLbFdrbU9UE0Hoty", #bang rendi dn
            "https://drive.google.com/uc?export=view&id=13gghvfckEJB1sOQk2InQDBArnYFG0nsV", #kak renta dn
            "https://drive.google.com/uc?export=view&id=13TPtFht0dJevmHP_qOLd4F6dsOxun4qD", #bang josua dn

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
                "kesan" : "bang dimas yang super duper seru dan asik kalau cerita ",  
                "pesan" : "yang semangat ya bang kuliahnyaa, semoga segala langkahnya dipermudah"
            },
            {
                "nama"  : "Catherine Firdhasari Maulina Sinaga",
                "nim"   : "121450072",
                "umur"  : "20",
                "asal"  : "Sumatera Utara",
                "alamat": "Airan",
                "hobbi" : "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan" : "kaknya anggun sekali, dan cantik",  
                "pesan" : "semangat kuliahnyaa kakak dan semoga kuliahnya diperlancar"
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
                "kesan" : "kirain bang akbar type orng yg pendiam, ternyata seru abiezz",  
                "pesan" : "semangat bang kuliahnyaa jaga kesehatan ya"
            },
            {
                "nama"  : "Rani Puspita sari",
                "nim"   : "122450030",
                "umur"  : "20",
                "asal"  : "Kota Metro",
                "alamat": "Rajabasa",
                "hobbi" : "Dengar musik",
                "sosmed": "@rannipu",
                "kesan" : "kakanya sangat informatif dan seru",  
                "pesan" : "Semoga selalu dilancarkan semua urusannya kak, jangan lupa untuk tetap semangat kak dalam menjalani kehidupan"
            },
            {
                "nama"  : "Rendra Eka Prayoga",
                "nim"   : "122450112",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Belwis",
                "hobbi" : "Mancing Ikan Mas",
                "sosmed": "@rendraepr",
                "kesan" : "abangnya ramah abies dan manies",  
                "pesan" : "senyum selalu yaa bang, jaga kesehatan"
            },
            {
                "nama"  : "Salwa Farhanatussaidah",
                "nim"   : "122450055",
                "umur"  : "20",
                "asal"  : "Pesawaran",
                "alamat": "Airan",
                "hobbi" : "Nonton",
                "sosmed": "@slwfhn_694",
                "kesan" : "Sangat menginspirasi dalam kehidupan ",  
                "pesan" : "Tetap semangat kak dalam menjalani dunia perkuliahan"
            },
            {
                "nama"  : "Yosia Letare Banurea",
                "nim"   : "121450149",
                "umur"  : "20",
                "asal"  : "Dairi, Sumatera Utara",
                "alamat": "Perum Griya Indah",
                "hobbi" : "Tidur",
                "sosmed": "@yosiabanurea",
                "kesan" : "Sangat baik dan sangat mengasyikkan ",  
                "pesan" : "Semangat terus kak dalam menjalani perkuliahannya serta jangan lupa untuk jaga kesehatan"
            },
            {
                "nama"  : "Ari Sigit",
                "nim"   : "121450069",
                "umur"  : "23",
                "asal"  : "Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobbi" : "Futsal",
                "sosmed": "@ari_sigit17",
                "kesan" : "abangnya adem banget di pandnang masyaallah, serta sangat inspiratif dan asik",  
                "pesan" : "jaga mata jaga hati ya bang, semoga abang sehat sellau dan diberi kelancaran di semester akhirnya "
            },
            {
                "nama"  : "Azizah Kusumah Putri",
                "nim"   : "122450068",
                "umur"  : "21",
                "asal"  : "Lampung Selatan",
                "alamat": "Natar",
                "hobbi" : "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan" : "kakanya kalem dan manies sekali",  
                "pesan" : "Semangat terus kak dalam menjalani hari-harinya, semoga semua tugas dan tanggung jawab yang diemban dapat diselesaikan dengan lancar"
            },
            {
                "nama"  : "Meira Listyaningrum",
                "nim"   : "122450011",
                "umur"  : "20",
                "asal"  : "Pesawaran",
                "alamat": "Airan",
                "hobbi" : "Membaca",
                "sosmed": "@meirasty_",
                "kesan" : "Sangat baik dan sangat mengasyikkan",  
                "pesan" : "semangat kuliahnya kak, jangan lupa jaga kesehatan yahh"
            },
            {
                "nama"  : "Rendi Alexander Hutagalung",
                "nim"   : "122450057",
                "umur"  : "20",
                "asal"  : "Tangerang",
                "alamat": "Kost Benawang",
                "hobbi" : "Menyanyi",
                "sosmed": "@rexander",
                "kesan" : "abangnya lucu dan baik, serta sangat mengisnpirasi",  
                "pesan" : "Tetap semangat kak dalam menjalani hari-harinya, semoga diperlancar dalam menyelesaikan tugas dan tanggung jawab yang sedang di emban"
            },
            {
                "nama"  : "Renta Siahaan",
                "nim"   : "122450070",
                "umur"  : "21",
                "asal"  : "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi" : "Membaca dan Memancing",
                "sosmed": "@renta.shn",
                "kesan" : "Sangat informatif dalam menjelaskan sesuatu dan banyak memberikan motivasi",  
                "pesan" : "Semoga kegiatannya di dalam maupun di luar perkuliahan tetap lancar dan tetap semangat kak"
            },
            {
                "nama"  : "Josua Panggabean",
                "nim"   : "122450061",
                "umur"  : "21",
                "asal"  : "Pematang Siantar",
                "alamat": "Gerbang Barat",
                "hobbi" : "Menonton",
                "sosmed": "@josuapanggabean_",
                "kesan" : "abangnya baik dan seru serta mengisnpirasi",  
                "pesan" : "Tetap semangat bang dalam menjalani harinya, semoga urusannya baik di akademik maupun non akademik dapat berjalan dengan lancar"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()   

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=14W3US5EG1MhkK9uQClpwEPIH64e5y3C4", #bang andrian dn
            "https://drive.google.com/uc?export=view&id=14I1xjdErOcCCu5cIVG8_oCet3hN47b8M", #kak adisty dn
            "https://drive.google.com/uc?export=view&id=14LHGkFGcxtiJ7IQ5LbD-fH-eaFnBTd7X", #kak nabilla dn
            "https://drive.google.com/uc?export=view&id=14Gx6qhSfTVj2uKzz-m3sn2PIJZBz6Kr-", #bang danang dn
            "https://drive.google.com/uc?export=view&id=14VWmAra8M9OioXI67hAjeQNPT0PWr2dx", #bang farrel dn
            "https://drive.google.com/uc?export=view&id=14F-nIzFwQJpOZTTxe36DCT2p-PGPXb_E", #kak nabilah dn
            "https://drive.google.com/uc?export=view&id=14M-4ZrTQ_0kd_sh9V8ZoJl5m3TtHXXEs", #kak alvia dn
            "https://drive.google.com/uc?export=view&id=14MyNyKcgiMBe8kz7GIyTtxfzt1PZuCX4", #bang dhafin dn
            "https://drive.google.com/uc?export=view&id=14gOiyw999q8_JUK7u9bm74Fa0q_-Zc38", #kak elia dn


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
                "kesan" : "abangnya seru abis dan sangat mengispirasi",  
                "pesan" : "semangat semester akhirnya bang"
            },
            {
                "nama"  : "Adisty Syawalda Ariyanto",
                "nim"   : "121450136",
                "umur"  : "22",
                "asal"  : "Metro",
                "alamat": "Sukarame ",
                "hobbi" : "Nonton Film",
                "sosmed": "@adistysa_",
                "kesan" : "kakaknya cantik dan manies sekali ",  
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
                "kesan" : "Sangat baik, informatif dalam menerangkan suatu permasalahan dan sangat menginspirasi",  
                "pesan" : "Tetap semangat kak dalam menjalani harinya, semoga urusannya baik di akademik maupun non akademik dapat berjalan dengan lancar"
            },
            {
                "nama"  : "Danang Hilal Kurniawan",
                "nim"   : "122450085",
                "umur"  : "21",
                "asal"  : "Bandar Lampung",
                "alamat": "Airan",
                "hobbi" : "Belajar",
                "sosmed": "@dananghk_",
                "kesan" : "abangnya seru dan humoris ",  
                "pesan" : "Semoga selalu dilancarkan semua urusannya bang, jangan lupa untuk tetap semangat kak dalam menjalani kehidupan"
            },
            {
                "nama"  : "Farrel Julio Akbar",
                "nim"   : "122450110",
                "umur"  : "20",
                "asal"  : "Bogor",
                "alamat": "Lapas",
                "hobbi" : "Kayang",
                "sosmed": "@farel_julio",
                "kesan" : "Sangat baik dan sangat menginspirasi dalam kehidupan",  
                "pesan" : "Tetap semangat dalam menjalani perkuliahannya kak dan jangan lupa jaga kesehatan"
            },
            {
                "nama"  : "Nabilah Andika Fitriati",
                "nim"   : "121450139",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi" : "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan" : "Sangat menginspirasi dalam kehidupan ",  
                "pesan" : "Tetap semangat kak dalam menjalani dunia perkuliahan"
            },
            {
                "nama"  : "Alvia Asrinda Br.Gintng",
                "nim"   : "122450077",
                "umur"  : "20",
                "asal"  : "Binjai",
                "alamat": "Korpri",
                "hobbi" : "Nonton Winda",
                "sosmed": "@alviagnting",
                "kesan" : "Sangat baik dan sangat mengasyikkan ",  
                "pesan" : "Semangat terus kak dalam menjalani perkuliahannya serta jangan lupa untuk jaga kesehatan"
            },
            {
                "nama"  : "Dhafin Razaqa Luthfi",
                "nim"   : "122450133",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi" : "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan" : "Sangat seru dan informatif dalam menjelaskan sesuatu",  
                "pesan" : "Jangan lupa untuk tetap semangat dalam menjalani dunia perkuliahan kak, semoga urusannya selalu dilancarkan"
            },
            {
                "nama"  : "Elia Meylani Simanjuntak",
                "nim"   : "122450026",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Korpri",
                "hobbi" : "Main Alat Musik",
                "sosmed": "@meylanielia",
                "kesan" : "kakaknya lucu dan cantik sekali masyaallah",  
                "pesan" : "tetap selalu tersenyum kak, jangan lupa jaga kesehatan"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()    
# Tambahkan menu lainnya sesuai kebutuhan
