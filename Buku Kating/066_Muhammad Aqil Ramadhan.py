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
            "https://drive.google.com/uc?export=view&id=1x-M7M5WQKZv7KvXZxZe_yyAC8oLF212Q",##Kahim
            "https://drive.google.com/uc?export=view&id=1UwbdQo3OVBIGYhOWbTnfnthruSs7wFu2",##Sekjen
            "https://drive.google.com/uc?export=view&id=1PPi5U1VBCrsKHD-do4Z71da4t5oFId82",##Sekretaris kak meliza
            "https://drive.google.com/uc?export=view&id=17_6MoWlr0u7809BuxfjB5DVJXtyy3La5",##Sekretaris kak putri 
            "https://drive.google.com/uc?export=view&id=1Mwj1UGpcod1PO3v1xSDhFcgz4JDGwlht",##Bendahara kak hartiti
            "https://drive.google.com/uc?export=view&id=1HAKWJBEnemtlX3bRtiBKt3ws7zDcw-4S",##Bendahara kak nadilla
        ]
        data_list = [
            {
                "nama": "Kharisma Gumilang",
                "nim": "121450137",
                "umur": "20",
                "asal":"Palembang",
                "alamat": "Kandis",
                "hobbi": "Denger musik",
                "sosmed": "@gumilangkharisma",
                "kesan": "Salut banget sih, ada  orang yang bisa ngimbangin akademik dan organisasi",  
                "pesan":"semangat terus kuliahnya bang kalau semoga sukses selalu !!!"# 1
            },
            {
                "nama": "Pandra Insani Putra Azwar",
                "nim": "121450000",
                "umur": "18",
                "asal":"Bukit Kemuning, Lampung Utara",
                "alamat": "Bawen 2",
                "hobbi": "Bermain gitar dan menyanyi",
                "sosmed": "@pandrainsni27",
                "kesan": "Bang pandra orangnya kocak dan humble",  
                "pesan":"semoga sukses bang !!!"# 1
            },
            {
                "nama"  : "Meliza Wulandari",
                "nim"   : "121450065",
                "umur"  : "20",
                "asal"  : "Pagar Alam, Sumatera Selatan",
                "alamat": "Kotabaru",
                "hobbi" : "Nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan" : "Kakaknya ramah",  
                "pesan" : "Semoga sukses selalu kak"
            },
            {
                "nama"  : "Putri Maulida Chairani",
                "nim"   : "121450050",
                "umur"  : "21",
                "asal"  : "Payakumbuh, Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi" : "Dengerin bang pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan" : "Kakaknya baik",  
                "pesan" : "Semoga lancar terus urusannya kak"
            },
            {
                "nama"  : "Hartiti Fadilah",
                "nim"   : "121450031",
                "umur"  : "21",
                "asal"  : "Palembang",
                "alamat": "Pemda",
                "hobbi" : "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan" : "Kakaknya keliatan pendiam",  
                "pesan" : "Semoga pada bayar uang kas ya kak"
            },
            {
                "nama"  : "Nadilla Andara Putri",
                "nim"   : "121450003",
                "umur"  : "21",
                "asal"  : "Metro",
                "alamat": "KotaBaru",
                "hobbi" : "Membaca",
                "sosmed": "@ndillaandr26",
                "kesan" : "Kakaknya ceria",  
                "pesan" : "Semoga lancar kuliahnya kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1LpfwkByDgjua2Qdvi7dBsjPpwepMo5Lr",#tri murniya
            "https://drive.google.com/uc?export=view&id=1LU46zfayQSlc5pqpNSkH_IB5OYwN8MZg",#Annisa cahyani
            "https://drive.google.com/uc?export=view&id=1LN5T3pH4lLNDC0VRBcyQv3QbsSpFONFn",#wulan
            "https://drive.google.com/uc?export=view&id=1L5lydkK5Ha_6cFs1a93_ODL7FsJt1hDQ",#dini
            "https://drive.google.com/uc?export=view&id=1Li6N-OHXzonZudRNaLJlmpVoy60og503",#fitri
            "https://drive.google.com/uc?export=view&id=1LmSyKXe4yWSYOU-V7lGaJWBUZPjQHgqz",#yusuf
            "https://drive.google.com/uc?export=view&id=1LZQ57AWcaGoJA2MwF729N-2pHR6YOE6m",#dhea
            "https://drive.google.com/uc?export=view&id=1L80ZhFvWg3JTzmT6gXi9E9MnWNfaogtS",#fahrul
            "https://drive.google.com/uc?export=view&id=1L1jmA9ztT18UT7S8Xes_slXhWEX5i2ji",#kak
            "https://drive.google.com/uc?export=view&id=1Ls4GrldeD_WFNyisUWU77I4Cu92tK21Q",#jeremia
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
            {
                "nama"  : "Wulan Sabina",
                "nim"   : "121450150",
                "umur"  : "21",
                "asal"  : "Medan",
                "alamat": "Raden Saleh",
                "hobbi" : "Nonton Drakor",
                "sosmed": "@wlnsbn0",
                "kesan" : "kakaknya lucu",  
                "pesan" : "semoga lancar kuliahnya"
            },
            {
                "nama"  : "Anisa Dini Amaliya",
                "nim"   : "121450081",
                "umur"  : "21",
                "asal"  : "Tanggerang",
                "alamat": "Jati Agung",
                "hobbi" : "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan" : "kakaknya keren",  
                "pesan" : "semoga lancar kuliahnya"
            },
            {
                "nama"  : "Anisa Fitriyani",
                "nim"   : "122450019",
                "umur"  : "20",
                "asal"  : "Batam",
                "alamat": "Kalianda",
                "hobbi" : "Membaca Al-Waqiah setiap maghrib",
                "sosmed": "@ansftynn_",
                "kesan" : "kakaknya asik",  
                "pesan" : "semoga menang lain kali mainn unonya"
            },
            {
                "nama"  : "Mirzan Yusuf Rabbani",
                "nim"   : "122450118",
                "umur"  : "20",
                "asal"  : "Jakarta",
                "alamat": "Korpri",
                "hobbi" : "Main Kucing",
                "sosmed": "@myrrinn",
                "kesan" : "soft boy banget abangnya",  
                "pesan" :"semoga lancar kuliahnya bang"
            },
            {
                "nama"  : "Dhea Amelia Putri",
                "nim"   : "122450004",
                "umur"  : "20",
                "asal"  : "Sukabumi, Jawa Barat",
                "alamat": "Natar",
                "hobbi" : "Suka Ikut Tes SKD",
                "sosmed": "@dhea_wedding",
                "kesan" : "kakaknya baik",  
                "pesan" : "semoga lancar kuliahnya kak"
            },
            {
                "nama"  : "Muhammad Fahrul Aditya",
                "nim"   : "121450156",
                "umur"  : "22",
                "asal"  : "Surakarta, Jawa Tengah",
                "alamat": "Pahoman",
                "hobbi" : "Melukis, badminton, hiking, ngopi, dengerin music, nonton film dan ngoding",
                "sosmed": "@fhrul.pdf",
                "kesan" : "abangnya sigma banget",  
                "pesan" : "semoga sehat selalu bang"
            },
            {
                "nama"  : "Berliana Enda Putri",
                "nim"   : "122450065",
                "umur"  : "21",
                "asal"  : "Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi" : "Main Game",
                "sosmed": "@berlyyanda",
                "kesan" : "kakaknya baik banget",  
                "pesan" : "semoga kuliahnya lancar"
            },
            {
                "nama"  : "Jeremia Susanto",
                "nim"   : "122450022",
                "umur"  : "20",
                "asal"  : " Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi" : "Marah-marah",
                "sosmed": "@jeremia_s_",
                "kesan" : "abangnya ramah",  
                "pesan" : "semoga lancar terus kuliahnya bang"
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
                "nama"  : "Annisa Luthfi Alifia",
                "nim"   : "121450093",
                "umur"  : "22",
                "asal"  : "Lampung Tengah",
                "alamat": "Kost Putri Rahayu",
                "hobbi" : "Dengerin bang Bintang nyanyi",
                "sosmed": "@annisalutfi_",
                "kesan" : "kakaknya keren tegas dan memiliki pengalaman yang banyak",  
                "pesan" : "Semoga makin ga sibuk kak jadi senatornya"
            },
            {
                "nama"  : "Rian Bintang Wijaya",
                "nim"   : "122450094",
                "umur"  : "20",
                "asal"  : "Palembang",
                "alamat": "Kotabaru",
                "hobbi" : "Menyanyi",
                "sosmed": "@bintangtwinkle",
                "kesan" : "Abangnya keren dan tegas",  
                "pesan" : "semangat terus bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1sLYbSVFwB_2C423efb93yT8fZMhGjyD9", #bang erickson dn
            "https://drive.google.com/uc?export=view&id=1TMmizhNOQCk3YBUP9x5RzgwGTiX5fwiD", #kak abeth dn
            "https://drive.google.com/uc?export=view&id=1kP_rZJ4uYD70WS81tGmNPMjwncIDuYBb", #kak afifah dn
            "https://drive.google.com/uc?export=view&id=1wmqNdpCEZEd1A3AuqJqQ-A6YuN1swlOX", #kak allya dn
            "https://drive.google.com/uc?export=view&id=17sIZULdykYwVKanybUBkH7BgSFjGx-MP", #kak hanum dn
            "https://drive.google.com/uc?export=view&id=1EliQwf7iGYygjVj1IaJsxag_om0YO08m", #bang ferdy dn
            "https://drive.google.com/uc?export=view&id=17NOyEJfJFYhttIsKa5Ww9lh4Q8hBf0eh", #bang deri dn
            "https://drive.google.com/uc?export=view&id=17nrWrPlUQgdd52MXrqNWkTsDD1QQRU7x", #kak oktavia dn
            "https://drive.google.com/uc?export=view&id=1Fp4NR-rQjm7mGQ_XWlxiwJhrMYk7dmOZ", #bang deyvan dn
            "https://drive.google.com/uc?export=view&id=1RqEX9rc5F2mSvUvNbb2LgFk1fDyWuv6e", #bang ibnu dn
            "https://drive.google.com/uc?export=view&id=1ypgQXcoQtMBq-KBuN396pF_z7cZVdOyg", #bang jo dn
            "https://drive.google.com/uc?export=view&id=1EoI42P3koniH1b9PqnxI9O2sdsO0sK_R", #bang kemas dn
            "https://drive.google.com/uc?export=view&id=1Qrz2n7lAlicPwsrIkD6ErNrzSaHZGVuC", #bang leonard dn
            "https://drive.google.com/uc?export=view&id=1sid7TtS7H22e0UXwXUQaXjKZ-VcyGyW8", #kak presilia dn
            "https://drive.google.com/uc?export=view&id=1dLc5NA43Ew_FbIQpJ-aFegnh0psWlE2r", #kak rafa dn
            "https://drive.google.com/uc?export=view&id=15ypP5vMOCfdCXCv_y68Q5wbbiP5iSAju", #bang sahid dn
            "https://drive.google.com/uc?export=view&id=1aW2AtCG7ob5zZucRT1F3Y-Rs1j7FFzpl", #kak vanes dn
            "https://drive.google.com/uc?export=view&id=1xQ7TINfYmJ8KGzJkP-EI0SRkqEGsyg6R", #bang ateng dn
            "https://drive.google.com/uc?export=view&id=1GOqNgXPpNWuZFyhfajTvx9a2TwlSxCF0", #bang gede dn
            "https://drive.google.com/uc?export=view&id=1eiwoSCBXJc4duVdxQChzaJBGGLlcsu0V", #kak jaclin dn
            "https://drive.google.com/uc?export=view&id=1Xf126OmIWCEb1mp9szHQNKwWv0iHJ31-", #kak dini dn

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
                "kesan" : "Abangnya baik dan solutif",  
                "pesan" : "Semangat terus bang teruskan apa yang telah dilakukan"
            },
            {
                "nama"  : "Elisabeth Claudia Simanjuntak",
                "nim"   : "122450123",
                "umur"  : "18",
                "asal"  : "Pekanbaru",
                "alamat": "Sukarame",
                "hobbi" : "Memancing keributan",
                "sosmed": "@celisabethh_",
                "kesan" : "Kakaknya bisa ceria dan bisa tegas kkeren ",  
                "pesan" : "Semangat terus kak kuliahnya"
            },
            {
                "nama"  : "Nisrina Nur Afifah",
                "nim"   : "122450052",
                "umur"  : "19",
                "asal"  : "Bekasi",
                "alamat": "Sukarame",
                "hobbi" : "Nabok orang",
                "sosmed": "@afifahhnsrn",
                "kesan" : "Sangat baik,dan ramah bisa menyesuaikan keadaan ",  
                "pesan" : "Tetap semangat kak dalam menjalani harinya, semoga urusannya baik di akademik maupun non akademik dapat berjalan dengan lancar"
            },
            {
                "nama"  : "Allya Nurul Islami Pasha",
                "nim"   : "122450033",
                "umur"  : "20",
                "asal"  : "Sumatera Barat",
                "alamat": "Gang Perwira, Belwis",
                "hobbi" : "Nonton Dracin",
                "sosmed": "@allyaislami_",
                "kesan" : "kakaknya tegas tapi aslinya baik banget",  
                "pesan" : "semangat dalam menjalankan tugas kuliah dan lainnya kak"
            },
            {
                "nama"  : "Farahanum Afifah Ardiansyah",
                "nim"   : "122450056",
                "umur"  : "20",
                "asal"  : "Padang, Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi" : "Tidur",
                "sosmed": "@farahanumafifahh",
                "kesan" : "baik dan ceria",  
                "pesan" : "semangat kuliahnya kak"
            },
            {
                "nama"  : "Ferdy Kevin Naibaho",
                "nim"   : "122450107",
                "umur"  : "19",
                "asal"  : "Medan, Sumatera Utara",
                "alamat": "Jalan Senopati Raya 18",
                "hobbi" : "Dengerin Rocky Gerung",
                "sosmed": "@ferdy_kevin",
                "kesan" : "abangnya lucu dan chill ",  
                "pesan" : "Semangat terus bang kuliahnya"
            },
            {
                "nama"  : "M. Deriansyah Okutra",
                "nim"   : "122450101",
                "umur"  : "19",
                "asal"  : "Kayu Agung",
                "alamat": "Jalan Pagar Alam",
                "hobbi" : "Bercerita horror",
                "sosmed": "@dransyh_",
                "kesan" : "Abangnya kocak",  
                "pesan" : "Semangat selalu bang "
            },
            {
                "nama"  : "Oktavia Nurwinda Puspita Sari",
                "nim"   : "122450041",
                "umur"  : "20",
                "asal"  : "Lampung Timur",
                "alamat": "Way Hui",
                "hobbi" : "Memasak",
                "sosmed": "@_oktavianrwnda_",
                "kesan" : "kakaknya keren",  
                "pesan" : "Semangat terus kuliah dan semoga lancar terus urusannya kak"
            },
            {
                "nama"  : "Deyvan Loxefal",
                "nim"   : "121450148",
                "umur"  : "21",
                "asal"  : "Riau",
                "alamat": "Pulau Damar",
                "hobbi" : "Belajar",
                "sosmed": "@depanloo",
                "kesan" : "abang paling humble dan lucu, sama-sama dari riau juga",  
                "pesan" : "tetaplah sebarkan positive vibbesnya bang"
            },
            {
                "nama"  : "Ibnu Farhan Al-Ghifari",
                "nim"   : "121450121",
                "umur"  : "21",
                "asal"  : "Jambi",
                "alamat": "Pulau Damar, Kobam",
                "hobbi" : "Bermain Game Online",
                "sosmed": "@al_ghifari032",
                "kesan" : "Sangat baik dan sangat mengasyikkan",  
                "pesan" : "Semangat bang dalam menjalani hari-harinya"
            },
             {
                "nama"  : "Johannes Krisjon Silitonga",
                "nim"   : "122450043",
                "umur"  : "19",
                "asal"  : "Tanggerang",
                "alamat": "Jalan Lapas",
                "hobbi" : "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan" : "abang ini kayaknya bisa bagi waktu dengan baik banget. akademik,organisasi dan olahraganya bagus semua ",  
                "pesan" : "Tetap semangat dan sukses selalu"
            },
            {
                "nama"  : "Kemas Veriandra Ramadhan",
                "nim"   : "122450016",
                "umur"  : "19",
                "asal"  : "Bekasi",
                "alamat": "Golf Asri",
                "hobbi" : "Bermain ular python digital",
                "sosmed": "@kemasverii",
                "kesan" : "Sangat informatif dalam menjelaskan sesuatu dan banyak memberikan motivasi",  
                "pesan" : "Semoga makin gacor kuliahnya bang"
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
                "pesan" : "semoga urusannya baik di akademik maupun non akademik dapat berjalan dengan lancar"
            },
            {
                "nama"  : "Presilia",
                "nim"   : "122450081",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Kota Baru",
                "hobbi" : "Tidur",
                "sosmed": "@presiliamg",
                "kesan" : "Kakaknya ceria dan ramah",  
                "pesan" : "tetap semangat kak dalam menjalani kehidupan"
            },
            {
                "nama"  : "Rafa Aqilla Jungjunan",
                "nim"   : "122450142",
                "umur"  : "20",
                "asal"  : "Riau",
                "alamat": "Belwis",
                "hobbi" : "Membaca webtoon",
                "sosmed": "@rafaaqilla",
                "kesan" : "kakaknya penndiam dan ramah",  
                "pesan" : "semoga kakaknya sehat selalu dan lancar kuliahnya"
            },
            {
                "nama"  : "Sahid Maulana",
                "nim"   : "122450109",
                "umur"  : "21",
                "asal"  : "Depok, Jawa Barat",
                "alamat": "Airan Raya",
                "hobbi" : "Bermain Game",
                "sosmed": "@sahid_maul19",
                "kesan" : "Abangnya ramah ",  
                "pesan" : "Semangat terus bang kuliahnya"
            },
            {
                "nama"  : "Vanessa Olivia Rose",
                "nim"   : "121450108",
                "umur"  : "20",
                "asal"  : "Jakarta",
                "alamat": "Perumahan Korpri",
                "hobbi" : "Belajar",
                "sosmed": "@roselivnes__",
                "kesan" : "kakaknya keren dan disiplin ",  
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
                "kesan" : "abangnya seru",  
                "pesan" : "semoga urusannya selalu dilancarkan bang"
            },
            {
                "nama"  : "Gede Moena",
                "nim"   : "121450014",
                "umur"  : "21",
                "asal"  : "Bekasi",
                "alamat": "Korpri Raya",
                "hobbi" : "Belajar dan main game",
                "sosmed": "@gedemoenaa",
                "kesan" : "abangnya baik",  
                "pesan" : "Semangat terus bang dalam menjalani hari-harinya"
            },
            {
                "nama"  : "Jaclin Alcavella",
                "nim"   : "122450015",
                "umur"  : "19",
                "asal"  : "Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi" : "Berenang",
                "sosmed": "@jaclinalcv_",
                "kesan" : "kakaknya asik",  
                "pesan" : "semoga urusannya dalam dunia perkuliahan dapat diselesaikan dengan mudah"
            },
            {
                "nama"  : "Syalaisha Andini Putriansyah",
                "nim"   : "122450111",
                "umur"  : "21",
                "asal"  : "Tanggerang",
                "alamat": "Sukarame",
                "hobbi" : "Membaca",
                "sosmed": "@syalaisha.i__",
                "kesan" : "Sangat baik dan sangat mengasyikkan",  
                "pesan" : "Semangat kak dalam menjalani hari-harinya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1IoVBew1AqFQ_o-3WvVia5LSlsYSYYG94", #bang rafi dn
            "https://drive.google.com/uc?export=view&id=1IE128ZihG3n4X1eHqWjGSf1ien8RQfD_", #kak anisa dn
            "https://drive.google.com/uc?export=view&id=1Icd615DLv4MLFWxghHbIiHzRGQeAf_D0", #bang ahmad dn
            "https://drive.google.com/uc?export=view&id=1IUWWpCtg8Pk-I6-JTashDqng2XZMhKwR", #bang fadhil dn
            "https://drive.google.com/uc?export=view&id=1HvMiz30PIOyJqRJN8mXYYjvIRzEQ-MIt", #kak dina dn
            "https://drive.google.com/uc?export=view&id=1II9TldgcjVSVCaJ2_9d6yKVMZQAJMhRf", #kak dinda dn
            "https://drive.google.com/uc?export=view&id=1HuBlGyQCw4ykqqWTnjUrc0Qssf2Ryxki", #kak marleta dn
            "https://drive.google.com/uc?export=view&id=1HkUF-YhUbz-kudtfA71LuU4L4ec9GKiv", #kak rut junita dn
            "https://drive.google.com/uc?export=view&id=1HteHqTsUaROd1ghHv_ivxndmcnidoL5D", #kak syadza dn
            "https://drive.google.com/uc?export=view&id=1IqwwK_PizE2USqYLWTKMDRKaLlB2pkg6", #bang eggi dn
            "https://drive.google.com/uc?export=view&id=1J4Ah9dZHWMj101cKsTUpPZyHf8WcQ8Jv", #kak febiya dn
            "https://drive.google.com/uc?export=view&id=1IlNQXb84YQydUaDXYuAP8IUPKYTgqHEw", #kak happy syahrul dn
            "https://drive.google.com/uc?export=view&id=1IkTiqMzfh2OaXnPxhenojAKDm8GHBIqr", #bang randa dn

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
                "kesan" : "abangnya baik dan care ",  
                "pesan" : "selesaikan apa yang telah dimulai bang, semangat jadi kadep"
            },
            {
                "nama"  : "Annisa Novantika",
                "nim"   : "121450005",
                "umur"  : "21",
                "asal"  : "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi" : "Memasak",
                "sosmed": "@anovavona",
                "kesan" : "Sangat baik dan sangat mengasyikkan",  
                "pesan" : "semangat terus kuliahnya kak"
            },
            {
                "nama"  : "Ahmad Sahidin Akbar",
                "nim"   : "122450044",
                "umur"  : "20",
                "asal"  : "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi" : "Olahraga",
                "sosmed": "@sahid22__",
                "kesan" : "abangnya baik dan ramah daplok kelompok sebelah wkwwk",  
                "pesan" : "jangan pernah cape jadi orang baik bang"
            },
            {
                "nama"  : "Fadhil Fitra Wijaya",
                "nim"   : "122450082",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Teluk Betung",
                "hobbi" : "Main game",
                "sosmed": "@fadhilfwee",
                "kesan" : "abangnya baik",  
                "pesan" : "Semangat terus bang kuliahnya"
            },
            {
                "nama"  : "Syalaisha Andina Putriansyah",
                "nim"   : "122450121",
                "umur"  : "21",
                "asal"  : "Tangerang",
                "alamat": "Gang Yudhistira",
                "hobbi" : "Baca jurnal",
                "sosmed": "@dkselsd_31",
                "kesan" : "kaget rupanya kakak ini kembar",  
                "pesan" : "lancar terus kak kuliahnya semangat terus"
            },
            {
                "nama"  : "Dinda Nababan",
                "nim"   : "122450120",
                "umur"  : "20",
                "asal"  : "Medan, Sumatera Utara",
                "alamat": "Jalan Lapas",
                "hobbi" : "Belajar",
                "sosmed": "@dindanababan_",
                "kesan" : "kakaknya baik dan ramah",  
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
                "kesan" : "kakaknya kooperatif dan ramah",  
                "pesan" : "Tetap semangat kak dalam menjalani dunia perkuliahan"
            },
            {
                "nama"  : "Rut Junita Sari Siburian",
                "nim"   : "122450103",
                "umur"  : "20",
                "asal"  : "Batam, Kepulauan Riau",
                "alamat": "Gang Nangka 3",
                "hobbi" : "Review Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan" : "kakaknya baik dan seru",  
                "pesan" : "lancar terus kak kuliahnya semangat terus"
            },
            {
                "nama"  : "Syadza Puspadari Azhar",
                "nim"   : "122450072",
                "umur"  : "20",
                "asal"  : "Palembang",
                "alamat": "Belwis",
                "hobbi" : "Resume SG",
                "sosmed": "@puspadrr",
                "kesan" : "kakaknya seru ",  
                "pesan" : "semoga urusannya selalu dilancarkan"
            },
            {
                "nama"  : "Eggi satria",
                "nim"   : "122450032",
                "umur"  : "20",
                "asal"  : "Sukabumi",
                "alamat": "Korpri",
                "hobbi" : "Ngoding WISATA",
                "sosmed": "@egistr",
                "kesan" : "definisi kakak tingkat, solutif dan mendengarkan aspirasi dari anak-anaknya,beribawa keren dan thebest bapak daplok",  
                "pesan" : "semangat terus bang menghadapi perkuliahhannya dan jangan pernah cape kalau soal markov hehe"
            },
            {
                "nama"  : "Febiya Jomy Pratiwi",
                "nim"   : "122450074",
                "umur"  : "20",
                "asal"  : "Tulang Bawang",
                "alamat": "Jalan Kelengkeng Raya",
                "hobbi" : "Review jurnal",
                "sosmed": "@pratiwifebiya",
                "kesan" : "kakaknya baik dan sangat mengasyikkan",  
                "pesan" : "lancar terus kak kuliahnya semangat terus"
            },
             {
                "nama"  : "Happy Syahrul Ramadhan",
                "nim"   : "122450013",
                "umur"  : "20",
                "asal"  : "Lampung Timur",
                "alamat": "Karang Anyar",
                "hobbi" : "Main game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan" : "abangnya baik dan keren",  
                "pesan" : "Tetap semangat terus kuliahnya bang"
            },
            {
                "nama"  : "Randa Andriana Putra",
                "nim"   : "122450083",
                "umur"  : "21",
                "asal"  : "Banten",
                "alamat": "Sukarame",
                "hobbi" : "Tidur dan berkembang",
                "sosmed": "@randaandriana_",
                "kesan" : "abangnya ahli dalam menjelaskan sesuatu",  
                "pesan" : "tetap semangat selalu bang kuliah dan kehidupannya"
            },

        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen MEDKRAF":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Hlj68iVYFsB1-U_72D3UtRU4JQiD1RV7", #bang wahyu dn
            "https://drive.google.com/uc?export=view&id=1HLKHwGjevbqrSJt-trhMqxZy7a8gH32q", #kak elok dn
            "https://drive.google.com/uc?export=view&id=1n_hajO8TmAWh4WTg-z4KanAuCtgx9ez6", #kak arsyiah dn
            "https://drive.google.com/uc?export=view&id=105qmjA6sBLNdYdy_tVVxcfkz5LwMOPr_", #kak cintya dn
            "https://drive.google.com/uc?export=view&id=1b2qa2VnNgxUDgus2Pekeee490GaJfpcU", #kak najla dn
            "https://drive.google.com/uc?export=view&id=1WczWBs_rdl_3whUbPB2ddFvhzx-8d9Nr", #kak rahma dn
            "https://drive.google.com/uc?export=view&id=18SJFgL9hXzP_vpDdzoeYfrSOV0fEJO7N", #kak try yani dn
            "https://drive.google.com/uc?export=view&id=1ndodXthAAhUmcTBVEi9beY09Tu3pebjt", #bang kaisar dn
            "https://drive.google.com/uc?export=view&id=1okC4w0wm44ED8DSftQdv0A-xdWaN3099", #kak dwi dn
            "https://drive.google.com/uc?export=view&id=1o3qlJUh5cz8BIoHIMS9U0UdgdDuyag8Q", #bang gym dn
            "https://drive.google.com/uc?export=view&id=1oHYT3TuRjeDFMiTw8WAxHW5KCzJgynHM", #kak nasywa dn
            "https://drive.google.com/uc?export=view&id=1oT0VGQgA2zn4vdsmTcxt9E_pqQAJdV9o", #kak priska dn
            "https://drive.google.com/uc?export=view&id=1nVxMrtGcWwn-bGpLMMi5qo5mJq2IO6-M", #bang arsal dn
            "https://drive.google.com/uc?export=view&id=1oMCF7hDGLogqBdEs1uBFQ2_ohf-VAxQg", #bang abit dn
            "https://drive.google.com/uc?export=view&id=1oFKT-b5xP-5QI8nM3TQsDywbR9PH2OOE", #bang akmal dn
            "https://drive.google.com/uc?export=view&id=1nxJHtCk5zk6FEQtd0jX_uoAd03O6PQcZ", #bang hermawan dn
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
                "kesan" : "abangnya lucu dan humble",  
                "pesan" : "Tetap semangat bang dalam menjalani hari-harinya, semoga diperlancar dalam menyelesaikan tugas dan tanggung jawab yang sedang di emban"
            },
            {
                "nama"  : "Elok Fiola",
                "nim"   : "122450051",
                "umur"  : "19",
                "asal"  : "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi" : "Editing",
                "sosmed": "@elokfiola",
                "kesan" : "kakaknya ceria dan ramah",  
                "pesan" : "Semoga lancar terus kuliahnya kak"
            },
            {
                "nama"  : "Arsyiah Azahra",
                "nim"   : "121450035",
                "umur"  : "21",
                "asal"  : "Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi" : "Nugas",
                "sosmed": "@arsyiah.__",
                "kesan" : "kakknya keren",  
                "pesan" : "semoga kuliahnya lancar  kak"
            },
            {
                "nama"  : "Cintya Bella",
                "nim"   : "122450066",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Teluk",
                "hobbi" : "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan" : "kakaknya tinggi banget",  
                "pesan" : "semoga kuliahnya lancar selalu kak"
            },
            {
                "nama"  : "Najla Juwairia",
                "nim"   : "122450037",
                "umur"  : "19",
                "asal"  : "Sumatera Utara",
                "alamat": "Airan",
                "hobbi" : "Menulis, Membaca, Fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan" : "kakaknya baik",  
                "pesan" : "semoga kuliahnya lancar selalu kak"
            },
            {
                "nama"  : "Rahma Neliyana",
                "nim"   : "122450036",
                "umur"  : "20",
                "asal"  : "Lampung",
                "alamat": "Sukarame",
                "hobbi" : "Baca Coding",
                "sosmed": "@rahmanellyana",
                "kesan" : "sangat peduli dan selalu ceria di segala situasi, mendengarkan pikiran ramai orang, benar-benar menggambarkan ibu daplok terbaik",  
                "pesan" : "Semangat terus kuliahnya kak jangan cape jadi orang baik dan sabar menghadapi kami "
            },
            {
                "nama"  : "Try Yani Rizki Nur Rohmah",
                "nim"   : "122450020",
                "umur"  : "20",
                "asal"  : "Lampung Barat",
                "alamat": "Korpri",
                "hobbi" : "Bernyanyi dan Menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan" : "kakaknya baik dan ramah ",  
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
                "kesan" : "abangnya kocak",  
                "pesan" : "semoga urusannya selalu dilancarkan"
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
                "pesan" : "semoga lancar terus kuliahnya bang"
            },
             {
                "nama"  : "Nasywa Nur Afifah",
                "nim"   : "122450125",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Jalan Durian 1 Pemda",
                "hobbi" : "Nonton drakor",
                "sosmed": "@nsywanaf",
                "kesan" : "kakaknya asik",  
                "pesan" : "semoga kuliahnya lancar selalu kak"
            },
            {
                "nama"  : "Priska Silvia Ferantiana",
                "nim"   : "122450053",
                "umur"  : "19",
                "asal"  : "Palembang",
                "alamat": "Jalan Nangka 2",
                "hobbi" : "Baca novel yang bikin nangis",
                "sosmed": "@prskslv",
                "kesan" : "Sangat informatif dalam menjelaskan sesuatu",  
                "pesan" : "Semoga kperkuliahannya tetap lancar dan tetap semangat kak"
            },
            {
                "nama"  : "Muhammad Arsal Ranjana Utama",
                "nim"   : "121450111",
                "umur"  : "21",
                "asal"  : "Depok",
                "alamat": "Jalan Nangka 4",
                "hobbi" : "Ngoding",
                "sosmed": "@arsal.utama",
                "kesan" : "abangnya ramah",  
                "pesan" : "semoga urusannya baik di akademik maupun non akademik dapat berjalan dengan lancar"
            },
            {
                "nama"  : "Abit Ahmad Oktarian",
                "nim"   : "122450042",
                "umur"  : "19",
                "asal"  : "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi" : "Ngoding, Gaming",
                "sosmed": "@abitahmad",
                "kesan" : "abangnya ramah dan enak diajak ngobrol",  
                "pesan" : "Semoga LMD kita dapet A bang"
            },
            {
                "nama"  : "Akmal Faiz Abdillah",
                "nim"   : "122450114",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi" : "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan" : "abangnya baik dan keren",  
                "pesan" : "semangat selalu bang kuliahnhya"
            },
            {
                "nama"  : "Hermawan Manurung",
                "nim"   : "122450069",
                "umur"  : "20",
                "asal"  : "Bogor",
                "alamat": "Dekat jalan tol, Wisma Hana Hani",
                "hobbi" : "Bengong dan membaca buku",
                "sosmed": "@hermawan.mnrng",
                "kesan" : "abangnya super duper baik",  
                "pesan" : "semoga kuliahnya lancar dan makin sukse bang"
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1JsQ2HGVBJ9RfcdwXgXY5HDseQOPT-l2I", #bang yogy dn
            "https://drive.google.com/uc?export=view&id=1KD_2RolEttB4wjVyc6-VRPdrOaP8jVY_", #kak ramadhita dn
            "https://drive.google.com/uc?export=view&id=1LZrihCrVNbu-4aA7aOOh11ailBcPsxAK", #kak nazwa dn
            "https://drive.google.com/uc?export=view&id=1Ld4cpmYRGB7kSo1sokcDmco6tSafFQuF", #bang bastian dn
            "https://drive.google.com/uc?export=view&id=1LI5EOfW7Z36AmKkGR99vF4hmzeicpPof", #kak dea dn
            "https://drive.google.com/uc?export=view&id=1LVu_icWuORMjmCaao9vZR00mM1FjSyZb", #kak esteria dn
            "https://drive.google.com/uc?export=view&id=1LJEZLYSko5eOXnWjLHkxU9d8wa0Cz72_", #kak natasya ega dn
            "https://drive.google.com/uc?export=view&id=1L4OyNbhX1Yi_vwKjQb9B4RcoRma5xhHN", #kak novelia dn
            "https://drive.google.com/uc?export=view&id=1LGrlHcoElk8GhIvhlB81o-2o5u-oR2De", #kak jasmine dn
            "https://drive.google.com/uc?export=view&id=1LgtIq65sJysETNp4ciWms8TnaMB4xRoA", #bang tobias dn
            "https://drive.google.com/uc?export=view&id=1LwX3Kbd8ZriOFB2CKG-PqZuxhC7sM_7t", #bang rizki dn
            "https://drive.google.com/uc?export=view&id=1JsQ2HGVBJ9RfcdwXgXY5HDseQOPT-l2I", #bang arafi dn
            "https://drive.google.com/uc?export=view&id=1Lp23nGW7QG-qHpOYWa531H7GBjpLpxTs", #kak uyi dn
            "https://drive.google.com/uc?export=view&id=1M1LSU6Q5WLGSCHw4FiwqRjwJoTcSeNFx", #kak chalifia dn
            "https://drive.google.com/uc?export=view&id=1Kwsffr5luMLmhXOAsErtYkyd4wqK9s10", #bang irvan dn
            "https://drive.google.com/uc?export=view&id=1Kv2k9ljykQRJV1IxTma83iQclBdNvEKq", #kak izza dn
            "https://drive.google.com/uc?export=view&id=1KaqNMKlelilbgQseBKbsGFjrOSf8QLZM", #kak zuhrah dn
            "https://drive.google.com/uc?export=view&id=1Kmtx8P01U7QJYRUU0Pj61N9WOw-DL5rM", #bang raid dn
            "https://drive.google.com/uc?export=view&id=1K_0H6j10O0LU3A6Ur3K8Cb8Dqdyd54nl", #kak tria dn
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
                "kesan" : "Abangnya baik dan keren",  
                "pesan" : "Semangat terus kak kuliahnya"
            },
            {
                "nama"  : "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan" : "Abangnya ramah dan baik",  
                "pesan" : "Semoga kegiatannya diperlancar bang"
            },
            {
                "nama"  : "Nazwa Nabilla",
                "nim": "121450122",
                "umur": "21 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Way kandis",
                "hobbi": "Belajar",
                "sosmed": "@nazwanbilla",
                "kesan" : "kakaknya baik dan ramah",
                "pesan" : "semoga kakaknya sehat selalu dan lancar kuliahnya"

            },
            {
                "nama"  : "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21 Tahun",
                "asal": "Batam, Kepulauan Riau",
                "alamat": "Belwis",
                "hobbi": "Main game",
                "sosmed": "@bastiansilaban_",
                "kesan" : "Abangnya ramah dan baik",
                "pesan" : "Semangat terus bang kuliahnya"

            },
            {
                "nama"  : "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20 Tahun",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Dengerin musik",
                "sosmed": "@deaa.rsn",
                "kesan" : "Sangat baik dan sangat menginspirasi dalam kehidupan",  
                "pesan" : "Tetap semangat dalam menjalani perkuliahannya kak dan jangan lupa jaga kesehatan"
            },
            {
                "nama"  : "Esteria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "19 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Belwis",
                "hobbi": "Main golf bareng kadiv",
                "sosmed": "@esteriars",
                "kesan" : "kakanya baik dan ramah ",  
                "pesan" : "semanagat terus kuliahnya kak"
            },
            {
                "nama"  : "Natasya Ega Lina",
                "nim": "122450024",
                "umur": "19 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Belwis",
                "hobbi": "Jadi humas",
                "sosmed": "@nateee__15",
                "kesan" : "kakaknya informatif ",  
                "pesan" : "jaga kesehatannya dan semangat selalu kak"
            },
            {
                "nama"  : "Novelia Adinda",
                "nim": "122450104",
                "umur": "21 Tahun",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan" : "kakaknya keren",  
                "pesan" : "Semangat terus kuliahnya kak jangan lupa jaga kesehatan"
            },
            {
                "nama"  : "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Main sepak takraw",
                "sosmed": "@jasminednva",
                "kesan" : "kakaknya ramah",  
                "pesan" : "Semangat terus kuliahnya kak semoga lancar terus kegiatannya"
            },
            {
                "nama"  : "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20 Tahun",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Jogging",
                "sosmed": "@tobiassiagian",
                "kesan" : "abangnya humble dan asprak ads yang baik",  
                "pesan" : "Semangat terus bang semoga sukses"
            },
            {
                "nama"  : "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21 Tahun",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobbi": "Bikin portofolio",
                "sosmed": "@rzkdrnnn",
                "kesan" : "abangnya keren",  
                "pesan" : "Semangat terus kuliahnya bang"
            },
            {
                "nama"  : "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20 Tahun",
                "asal": "Bandung",
                "alamat": "Way Huwi",
                "hobbi": "Bertani",
                "sosmed": "@rafiramadhanmaulana",
                "kesan" : "abangnya baik",  
                "pesan" : "lancar terus kuliahnya "
            },
            {
                "nama"  : "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20 Tahun",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobbi": "Tepuk Semangat",
                "sosmed": "@u_yippy",
                "kesan" : "kakaknnya ceria",  
                "pesan" : "Semangat terus kuliahnya kak "
            },
            {
                "nama"  : "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20 Tahun",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Q Time",
                "sosmed": "@chlfawww",
                "kesan" : "kakaknya baik dan ramah",  
                "pesan" : "semangat kuliahannya kak dan jangan lupa jaga kesehatan"
            },
            {
                "nama"  : "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21 Tahun",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton youtube, main game",
                "sosmed": "@alfaritziirvan",
                "kesan" : "abangnya humble ",  
                "pesan" : "Semangat terus kuliahnya bang semoga makin jadi lebih bagus"
            },
            {
                "nama"  : "Izza Lutfia",
                "nim": "122450090",
                "umur": "20 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Main Rubik",
                "sosmed": "@izzalutfia",
                "kesan" : "kakaknya sangat baik dan sangat mengasyikkan ",  
                "pesan" : "Semangat terus kuliahnya kak "
            },
            {
                "nama"  : "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@alyaavanevi",
                "kesan" : "kakaknya lucu",  
                "pesan" : "Semangat terus kuliahnya kak jaga kesehatannya"
            },
            {
                "nama"  : "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20 Tahun",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "telat",
                "sosmed": "@rayths_",
                "kesan" : "abangnya ramah",  
                "pesan" : "semoga selalu lancar kuliahnya bang"
            },
            {
                "nama"  : "Tria Yunanni",
                "nim": "122450062",
                "umur": "20 Tahun",
                "asal": "Way Kanan",
                "alamat": "Sukarame",
                "hobbi": "Baca Buku",
                "sosmed": "@tria_y062",
                "kesan" : "kakaknya ramah",  
                "pesan" : "Semangat kak kuliahnya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()  

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1IR2dWOsjsI0fAKqUcKuYCvfV_NXkzOAO", #bang dimas dn
            "https://drive.google.com/uc?export=view&id=1c3XU8qgsC0rooc7eRp2Gb2GMUYiODvV0", #kak catherine dn
            "https://drive.google.com/uc?export=view&id=1Lx8F4D468NT-AONayV_2iu8BghEu_dPz", #bang akbar dn
            "https://drive.google.com/uc?export=view&id=1CYk06dCSXOSoAMuG9ItP6bnWeZKw1bxK", #kak rani dn
            "https://drive.google.com/uc?export=view&id=16w3csUyMSWSipPCtBIvjWH1SHYEr4clV", #bang rendra dn
            "https://drive.google.com/uc?export=view&id=1kFfaQQG9GkUUztl5nt-xvfEPNDrmu6Ja", #kak salwa dn
            "https://drive.google.com/uc?export=view&id=1R1rHlVo9lMw1OYdBDuckNTzeCofjrUzC", #bang yosia dn
            "https://drive.google.com/uc?export=view&id=103XjxM98bCMzzq3-a7bzI9v2NRode7vS", #bang ari dn
            "https://drive.google.com/uc?export=view&id=1V06BbPGsyKDOQhxqd9vkdJCyhgQBYvo3", #kak azizah dn
            "https://drive.google.com/uc?export=view&id=15yrHZuQ71vhJS5q82IYOunf-9WZCZHYr", #kak meira dn
            "https://drive.google.com/uc?export=view&id=1J-XmHPXbvMAGuuTJ1LenJ4x_npMPivsx", #bang rendi dn
            "https://drive.google.com/uc?export=view&id=1bTJpTj6Me7AvXY0bQQ1BSZJLcQennRgJ", #kak renta dn
            "https://drive.google.com/uc?export=view&id=1zFiHOeZsB4afPcCDR29OFgVY2SYh51Xp", #bang josua dn

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
                "kesan" : "abangnya keren dan menginspirasi",  
                "pesan" : "semangat terus bag kuliahnya"
            },
            {
                "nama"  : "Catherine Firdhasari Maulina Sinaga",
                "nim"   : "121450072",
                "umur"  : "20",
                "asal"  : "Sumatera Utara",
                "alamat": "Airan",
                "hobbi" : "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan" : "kakaknya ramah",  
                "pesan" : "Semoga kegiatannya di dalam maupun di luar perkuliahan tetap lancar dan tetap semangat kak"
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
                "kesan" : "abangnya lucu",  
                "pesan" : "semoga urusan kuliahnya berjalan dengan lancar"
            },
            {
                "nama"  : "Rani Puspita sari",
                "nim"   : "122450030",
                "umur"  : "20",
                "asal"  : "Kota Metro",
                "alamat": "Rajabasa",
                "hobbi" : "Dengar musik",
                "sosmed": "@ranniu",
                "kesan" : "Sangat informatif dalam menerangkan sesuatu dan sangat menginspirasi",  
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
                "kesan" : "abangnya ramah dan kocak",  
                "pesan" : "semangat kuliahnya bang jangan lupa jaga kesehatan"
            },
            {
                "nama"  : "Salwa Farhanatussaidah",
                "nim"   : "122450055",
                "umur"  : "20",
                "asal"  : "Pesawaran",
                "alamat": "Airan",
                "hobbi" : "Nonton",
                "sosmed": "@slwfhn_694",
                "kesan" : "kakaknya seru ",  
                "pesan" : "semangat kuliahnya bang jangan lupa jaga kesehatan"
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
                "pesan" : "semangat kuliahnya kak jangan lupa jaga kesehatan"
            },
            {
                "nama"  : "Ari Sigit",
                "nim"   : "121450069",
                "umur"  : "23",
                "asal"  : "Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobbi" : "Futsal",
                "sosmed": "@ari_sigit17",
                "kesan" : "abangnya murah senyum",  
                "pesan" : "semangat kuliahnya bang jangan lupa jaga kesehatan"
            },
            {
                "nama"  : "Azizah Kusumah Putri",
                "nim"   : "122450068",
                "umur"  : "21",
                "asal"  : "Lampung Selatan",
                "alamat": "Natar",
                "hobbi" : "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan" : "kakaknya baik",  
                "pesan" : "semoga kuliahnya lancar kak"
            },
            {
                "nama"  : "Meira Listyaningrum",
                "nim"   : "122450011",
                "umur"  : "20",
                "asal"  : "Pesawaran",
                "alamat": "Airan",
                "hobbi" : "Membaca",
                "sosmed": "@meirasty_",
                "kesan" : "kakaknya chill",  
                "pesan" : "semangat kuliahnya kak jangan lupa jaga kesehatan"
            },
            {
                "nama"  : "Rendi Alexander Hutagalung",
                "nim"   : "122450057",
                "umur"  : "20",
                "asal"  : "Tangerang",
                "alamat": "Kost Benawang",
                "hobbi" : "Menyanyi",
                "sosmed": "@rexander",
                "kesan" : "abangnya baik",  
                "pesan" : "semangat terus bang semoga sukses"
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
                "kesan" : "abangnya cool banget",  
                "pesan" : "semangat kuliahnya bang jangan lupa jaga kesehatan"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()   

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1pRwVLeUXrDyFoEv4tuXS0EATkFKl3w2P", #bang andrian dn
            "https://drive.google.com/uc?export=view&id=1pBAfpLvjQO-T3SUvlNDP_FPU_yQOWmXx", #kak adisty dn
            "https://drive.google.com/uc?export=view&id=1pDdvmF33ih0ShwAWcxU6nX-V2PSNX4ju", #kak nabilla dn
            "https://drive.google.com/uc?export=view&id=1pMgEihp9myjzyc-eajN8dDMAPm0pqZZg", #bang danang dn
            "https://drive.google.com/uc?export=view&id=1ounsRKm5OV-sUK6fgKfskJgdeBiCLzVp", #bang farrel dn
            "https://drive.google.com/uc?export=view&id=1pQ9BsKiyDKBc2aisW5O_ks_BKfBKgBRp", #kak nabilah dn
            "https://drive.google.com/uc?export=view&id=1p8jdZMPSi2z78trvM4kKaxkB-GOr08V5", #kak alvia dn
            "https://drive.google.com/uc?export=view&id=1p4_IXh01bFsOflgQCvjw38v_DzS2QK_1", #bang dhafin dn
            "https://drive.google.com/uc?export=view&id=1oxAiarhEjp_2LiNJvTd1R4nQ6FNYozTf", #kak elia dn


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
                "kesan" : "abangnya informatif dalam menjelaskan sesuatu dan memberi banyak pengetahuan baru",  
                "pesan" : "sukses selalu bang kuliahnya"
            },
            {
                "nama"  : "Adisty Syawalda Ariyanto",
                "nim"   : "121450136",
                "umur"  : "22",
                "asal"  : "Metro",
                "alamat": "Sukarame ",
                "hobbi" : "Nonton Film",
                "sosmed": "@adistysa_",
                "kesan" : "kakaknya ramah",  
                "pesan" : "semoga lancar terus kulliahnya dan jangan lupa jaga kesehatan selalu kak"
            },
            {
                "nama"  : "Nabila Azhari",
                "nim"   : "121450029",
                "umur"  : "21",
                "asal"  : "Simalungun",
                "alamat": "Airan ",
                "hobbi" : "Menghitung Uang",
                "sosmed": "@zhjung",
                "kesan" : "kakaknya punya banyak daerah asal jadi bingung",  
                "pesan" : "semoga lancar terus kulliahnya dan jangan lupa jaga kesehatan selalu kak"
            },
            {
                "nama"  : "Danang Hilal Kurniawan",
                "nim"   : "122450085",
                "umur"  : "21",
                "asal"  : "Bandar Lampung",
                "alamat": "Airan",
                "hobbi" : "Belajar",
                "sosmed": "@dananghk_",
                "kesan" : "Sangat informatif dalam menerangkan sesuatu dan sangat menginspirasi",  
                "pesan" : "Semoga lancar terus bang jualannya dan semangat kuliahnya"
            },
            {
                "nama"  : "Farrel Julio Akbar",
                "nim"   : "122450110",
                "umur"  : "20",
                "asal"  : "Bogor",
                "alamat": "Lapas",
                "hobbi" : "Kayang",
                "sosmed": "@farel_julio",
                "kesan" : "abangnya ramah dan baik",  
                "pesan" : "semoga lancar terus kulliahnya dan jangan lupa jaga kesehatan selalu bang"
            },
            {
                "nama"  : "Nabilah Andika Fitriati",
                "nim"   : "121450139",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi" : "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan" : "kakaknya keren ",  
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
                "kesan" : "kakaknya ramah ",  
                "pesan" : "semoga lancar terus kulliahnya dan jangan lupa jaga kesehatan selalu kak"
            },
            {
                "nama"  : "Dhafin Razaqa Luthfi",
                "nim"   : "122450133",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi" : "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan" : "abangnya lucu",  
                "pesan" : "semoga lancar terus kulliahnya dan jangan lupa jaga kesehatan selalu kak"
            },
            {
                "nama"  : "Elia Meylani Simanjuntak",
                "nim"   : "122450026",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Korpri",
                "hobbi" : "Main Alat Musik",
                "sosmed": "@meylanielia",
                "kesan" : "kakaknya baik",  
                "pesan" : "semoga lancar terus kulliahnya dan jangan lupa jaga kesehatan selalu kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()    