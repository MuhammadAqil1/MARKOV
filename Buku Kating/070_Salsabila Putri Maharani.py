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
            "https://drive.google.com/uc?export=view&id=1sBQzX-V3RmLTOHzbIe1RuqK5bZsYKCNN", #kak tri
            "https://drive.google.com/uc?export=view&id=1-WudblXJAT3lhDi2rr4wf305DYX7LEmK", #kak annisa cahya
            "https://drive.google.com/uc?export=view&id=1yjXLjN0jUwGgqe-nY6i1XRjvj6R3Hyj3", #kak wulan 
            "https://drive.google.com/uc?export=view&id=14oUGJl9x_YzpjmsxkjRT2NSCvJ1yi2wF", #kak anisa dini
            "https://drive.google.com/uc?export=view&id=1Yc_tOSxcUKbk2lKYaA3sNI4b8Qy-Ob8z", #kak anisa fitriyani
            "https://drive.google.com/uc?export=view&id=1yJQJFhIUkMmNEBluUc6W_87wCz8ZEHGJ", #bang mirzan
            "https://drive.google.com/uc?export=view&id=1WFgX0N42ZNFKw9rg9_b8JbwLIXbEGUcN", #kak dhea
            "https://drive.google.com/uc?export=view&id=1TLaCfP3PJlp_xWekGsdowmzy9PMj2bam", #bang fahrul
            "https://drive.google.com/uc?export=view&id=1SsbuhirfvLG948n5u4S5S2kCPHTBi_lk", #kak berlin
            "https://drive.google.com/uc?export=view&id=1Oy7t7LDHTaO6t0peA5nBWaLhYW5jP_nO", #bang jere
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


elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1vDD_Nbe2VEnvA3RVD0dSKF3wmOEPlx_A", #kak lutfi
            "https://drive.google.com/uc?export=view&id=11cXT1MTnkbTuDOeNI5DoRVvyVJDaWaI0", #bang bintang
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
                "kesan" : "Sanggat memberikan inspirasi dan menambahkan ilmu baru",  
                "pesan" : "semoga diperlancar dalam menyelesaikan tugas dan tanggung jawab"
            },
            {
                "nama"  : "Rian Bintang Wijaya",
                "nim"   : "122450094",
                "umur"  : "20",
                "asal"  : "Palembang, Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi" : "Mendengar Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan" : "Sangat mengambarkan sosok pemimpin",  
                "pesan" : "Semoga selalu sehat dan tetap semangat kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()
    
elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1bw0LhtwyUWSf3YKT3i5AaMOvaw645Oe-", #bang erickson dn
            "https://drive.google.com/uc?export=view&id=1HIFEYonzZOmvnj5Fb9--Q2ZD5aFbjcWH", #kak abeth dn
            "https://drive.google.com/uc?export=view&id=1O6ITsKwWppLfJ0412kLZAzwb7ySqsV0h", #kak afifah dn
            "https://drive.google.com/uc?export=view&id=10CYzoZXloeK2-i6cKqWlXAUkr4EiPm4Z", #kak allya dn
            "https://drive.google.com/uc?export=view&id=1rwDEOsqyus-1br76uBRZ_HAM-qpnvvCC", #kak hanum dn
            "https://drive.google.com/uc?export=view&id=17zW3V8Qe862o8L_ICOi3IixakruaHJY6", #bang dery dn
            "https://drive.google.com/uc?export=view&id=1wnySYGd0MO5v-01lIbkrFgrvOPJuKCTc", #bang ferdy dn
            "https://drive.google.com/uc?export=view&id=1r7nqJnRL_WeEYytkyGgGTU3Kqapdz6uD", #kak oktavia dn
            "https://drive.google.com/uc?export=view&id=1SF3UPg85jQNXorEWHKQ1Q3CfsKw5tglp", #bang deyvan dn
            "https://drive.google.com/uc?export=view&id=1w7VyqFLXGkZZNg9WpGSMH3S3iAJQfqmN", #bang ibnu dn
            "https://drive.google.com/uc?export=view&id=1TEV31zUz0CpjE_nraDydIZGFDyIMuiI9", #bang jo dn
            "https://drive.google.com/uc?export=view&id=1KRxPz5a1NbSwDgSvDG9Kc69O_BQUg002", #bang kemas dn
            "https://drive.google.com/uc?export=view&id=1x25qot4WsYxNvPBaRmmSNHpvuHo5U2f9", #bang leonard dn
            "https://drive.google.com/uc?export=view&id=18ZbktXUrj05R0VISnQFmKZow2yu1L7sT", #kak presilia dn
            "https://drive.google.com/uc?export=view&id=15am-0FtlLJRueO_6WipAKDyWZWWeADKg", #kak rafa dn
            "https://drive.google.com/uc?export=view&id=1Sd3WYl4SPbBx9CckuVgiTaUljxNG4-oq", #bang sahid dn
            "https://drive.google.com/uc?export=view&id=13jR4OtqDdZ3_Ta6bZ_hF2j4smi-2m_sW", #kak vanes dn
            "https://drive.google.com/uc?export=view&id=1RG9_225bWxRfH0ry-IF4GsHt6z0rbbAH", #bang ateng dn
            "https://drive.google.com/uc?export=view&id=19W1F3f2DeWnChxutAXAtur4KpLG7nbpB", #bang gede dn
            "https://drive.google.com/uc?export=view&id=1HdaKm9LgUO3eru7v85AUIHKHUkvibsdZ", #kak jaclin dn
            "https://drive.google.com/uc?export=view&id=1x_oizKw2h8b9w5ZxiHn6b4Gb_ADVeU7q", #bang rafly dn
            "https://drive.google.com/uc?export=view&id=1Tr8lup6DB9XGxm-wZjglNczl3wXRSHuJ", #kak dini dn

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
                "kesan" : "Sangat mengambarkan sosok yan tegas dan penuh semanggat",  
                "pesan" : "semoga bahagia selalu dan tetap sehat"
            },
            {
                "nama"  : "Elisabeth Claudia Simanjuntak",
                "nim"   : "121450114",
                "umur"  : "21",
                "asal"  : "Tanggerang Selatan",
                "alamat": "Way Huwi",
                "hobbi" : "Membaca, Nonton",
                "sosmed": "@celisabethh_",
                "kesan" : "imut sekali dan lucu",  
                "pesan" : "Semoga bahagia selalu dan tetap ceria"
            },
            {
                "nama"  : "Nisrina Nur Afifah",
                "nim"   : "122450052",
                "umur"  : "19",
                "asal"  : "Bekasi",
                "alamat": "Sukarame",
                "hobbi" : "Nabok orang",
                "sosmed": "@afifahhnsrn",
                "kesan" : "Sanggat inspiratif dan menebarkan senyum",  
                "pesan" : "Tetap semangat kak dalam menjalani harinya, dan bahagia"
            },
            {
                "nama"  : "Allya Nurul Islami Pasha",
                "nim"   : "122450033",
                "umur"  : "20",
                "asal"  : "Sumatera Barat",
                "alamat": "Gang Perwira, Belwis",
                "hobbi" : "Nonton Dracin",
                "sosmed": "@allyaislami_",
                "kesan" : "tegas namun baik hatinya",  
                "pesan" : "jangan lupa untuk tetap semangat kak dalam menjalani kehidupan"
            },
            {
                "nama"  : "Farahanum Afifah Ardiansyah",
                "nim"   : "122450056",
                "umur"  : "20",
                "asal"  : "Padang, Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi" : "Tidur",
                "sosmed": "@farahanumafifahh",
                "kesan" : "Positive vibe dan mengispirasi",  
                "pesan" : "Tetap semangat dalam menjalani perkuliahannya kak dan jangan lupa jaga kesehatan"
            },
            {
                "nama"  : "Ferdy Kevin Naibaho",
                "nim"   : "122450107",
                "umur"  : "19",
                "asal"  : "Medan, Sumatera Utara",
                "alamat": "Jalan Senopati Raya 18",
                "hobbi" : "Dengerin Rocky Gerung",
                "sosmed": "@ferdy_kevin",
                "kesan" : "baik dan menyenangkan",  
                "pesan" : "Semoga kuat sampai akhir"
            },
            {
                "nama"  : "M. Deriansyah Okutra",
                "nim"   : "122450101",
                "umur"  : "19",
                "asal"  : "Kayu Agung",
                "alamat": "Jalan Pagar Alam",
                "hobbi" : "Bercerita horror",
                "sosmed": "@dransyh_",
                "kesan" : "Sangat baik dan sangat mengasyikkan ",  
                "pesan" : "Tetap bahagia selalu"
            },
            {
                "nama"  : "Oktavia Nurwenda Puspita Sari",
                "nim"   : "122450041",
                "umur"  : "20",
                "asal"  : "Lampung Timur",
                "alamat": "Way Hui",
                "hobbi" : "Memasak",
                "sosmed": "@_oktavianrwnda_",
                "kesan" : "Baik dan ramah ",  
                "pesan" : "Semoga urusannya selalu dilancarkan"
            },
            {
                "nama"  : "Deyvan Loxefal",
                "nim"   : "121450148",
                "umur"  : "21",
                "asal"  : "Riau",
                "alamat": "Pulau Damar",
                "hobbi" : "Belajar",
                "sosmed": "@depanloo",
                "kesan" : "Sangat informatif dalam menjelaskan sesuatu",  
                "pesan" : "jangan sedih dan bahagia selalu"
            },
            {
                "nama"  : "Ibnu Farhan Al-Ghifari",
                "nim"   : "121450121",
                "umur"  : "21",
                "asal"  : "Jambi",
                "alamat": "Pulau Damar, Kobam",
                "hobbi" : "Bermain Game Online",
                "sosmed": "@al_ghifari032",
                "kesan" : "Baik dan memberikan ilmu yang bermanfaat",  
                "pesan" : "Teruslah menjadi dirimu sendiri"
            },
             {
                "nama"  : "Johannes Krisjon Silitonga",
                "nim"   : "122450043",
                "umur"  : "19",
                "asal"  : "Tanggerang",
                "alamat": "Jalan Lapas",
                "hobbi" : "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan" : "Tegas namun dan memberikan banyak ilmu di bidang non akademik",  
                "pesan" : "Semoga semanggatnya dijaga sampai akhir"
            },
            {
                "nama"  : "Kemas Veriandra Ramadhan",
                "nim"   : "122450016",
                "umur"  : "19",
                "asal"  : "Bekasi",
                "alamat": "Golf Asri",
                "hobbi" : "Bermain ular python digital",
                "sosmed": "@kemasverii",
                "kesan" : "Banyak memberikan ilmu dan jago ngoding",  
                "pesan" : "Semoga ilmunya dapat di terapkan dengan baik"
            },
            {
                "nama"  : "Leonard Andreas Napitupulu",
                "nim"   : "121450153",
                "umur"  : "21",
                "asal"  : "Sumatera Utara",
                "alamat": "Kobam",
                "hobbi" : "Belajar",
                "sosmed": "@lnrd.__",
                "kesan" : "Baik dan juga ceria",  
                "pesan" : "tetap rendah hati, dan jangan berhenti belajar"
            },
            {
                "nama"  : "Presilia",
                "nim"   : "121450081",
                "umur"  : "21",
                "asal"  : "Bekasi",
                "alamat": "Kota Baru",
                "hobbi" : "Dengerin sounder",
                "sosmed": "@Presiliamg",
                "kesan" : "Sangat menginspirasi",  
                "pesan" : "jangan lupa untuk tetap semangat kak dalam menjalani kehidupan"
            },
            {
                "nama"  : "Rafa Aqilla Jungjunan",
                "nim"   : "122450148",
                "umur"  : "20",
                "asal"  : "Riau",
                "alamat": "Belwis",
                "hobbi" : "Membaca webtoon",
                "sosmed": "@rafaaqilla",
                "kesan" : "pribadi yang penuh semangat ",  
                "pesan" : "jangan sia-siakan kesempatan untuk berkembang"
            },
            {
                "nama"  : "Sahid Maulana",
                "nim"   : "122450109",
                "umur"  : "21",
                "asal"  : "Depok, Jawa Barat",
                "alamat": "Airan Raya",
                "hobbi" : "Bermain Game",
                "sosmed": "@sahid_maul19",
                "kesan" : "selalu memberikan energi positif",  
                "pesan" : "jangan pernah berhenti belajar"
            },
            {
                "nama"  : "Vanessa Olivia Rose",
                "nim"   : "121450068",
                "umur"  : "20",
                "asal"  : "Jakarta",
                "alamat": "Perumahan Korpri",
                "hobbi" : "Belajar",
                "sosmed": "@roselivnes__",
                "kesan" : "Pribadi yang penuh semangat",  
                "pesan" : "Jangan pernah takut untuk menghadapi tantangan baru"
            },
            {
                "nama"  : "M. Farhan Athaulloh",
                "nim"   : "121450156",
                "umur"  : "22",
                "asal"  : "Surakarta, Jawa Tengah",
                "alamat": "Pahoman",
                "hobbi" : "Melukis, badminton, hiking, ngopi, dengerin music, nonton film dan ngoding",
                "sosmed": "@fhrul.pdf",
                "kesan" : "orang yang penuh semangat dan energi positif",  
                "pesan" : "semoga urusannya selalu dilancarkan"
            },
            {
                "nama"  : "Gede Moana",
                "nim"   : "122450065",
                "umur"  : "21",
                "asal"  : "Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi" : "Main Game",
                "sosmed": "@gedemoenaa",
                "kesan" : "kerja keras yang sangat menginspirasi",  
                "pesan" : "Tetaplah menjadi pribadi yang selalu terbuka untuk belajar ,"
            },
            {
                "nama"  : "Jaclin Alcavella",
                "nim"   : "122450022",
                "umur"  : "20",
                "asal"  : " Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi" : "Marah-marah",
                "sosmed": "@jeremia_s_",
                "kesan" : "sosok yang penuh inisiatif dan selalu berpikir ke depan",  
                "pesan" : "Tetap konsisten dan jangan menyerah"
            },
            {
                "nama"  : "Rafly Prabu Darmawan",
                "nim"   : "122450065",
                "umur"  : "21",
                "asal"  : "Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi" : "Main Game",
                "sosmed": "@berlyyanda",
                "kesan" : "pekerja keras dan selalu bisa diandalkan",  
                "pesan" : "Semoga kamu terus berkembang dan meraih impianmu"
            },
            {
                "nama"  : "Syalaisha Andini Putriansyah",
                "nim"   : "122450022",
                "umur"  : "20",
                "asal"  : " Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi" : "Marah-marah",
                "sosmed": "@jeremia_s_",
                "kesan" : "Sanggat lembut dan baik",  
                "pesan" : "Jangan takut menghadapi tantangan baru"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()
    
elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1TQ2Pl2LgsprdO6oT67R2IPE8NrpDGnEE", #bang rafi dn
            "https://drive.google.com/uc?export=view&id=1TyEqevuC-V8PGH3HuZ-CVjAqAkq5YaMi", #kak vita dn
            "https://drive.google.com/uc?export=view&id=1ThXSL76RMngXthBAazgmlbXnf04RLS8m", #bang ahmad
            "https://drive.google.com/uc?export=view&id=1TUPqY78ahD31e0tOKEVlpr9NaMGucNjD", #bang fadhil dn
            "https://drive.google.com/uc?export=view&id=1TXvWp53_nrOnErOiUvFbMfeNSOte9Wtd", #kak dina dn
            "https://drive.google.com/uc?export=view&id=1TzaLzuYXXc03HgZpJYhNH7q6xOgJnqiK", #kak dinda dn
            "https://drive.google.com/uc?export=view&id=1TXoC6KrwFa-KH1EGrrOuHErHDfvDY3jy", #kak marleta dn
            "https://drive.google.com/uc?export=view&id=1Sxl9kSHonrVnnHaSoGn_4VIyH9DhTrHw", #kak rut junita dn
            "https://drive.google.com/uc?export=view&id=1SwHdEjPkUv1mHRoZe48YP_fgRIBCADeq", #kak syadza dn
            "https://drive.google.com/uc?export=view&id=1TTHyPVNn00PISLjZMEF1G3ln2jXB9LRZ", #bang eggi dn
            "https://drive.google.com/uc?export=view&id=1SoBZX9aNZJhH7zf8PnHXqtQb6kBqlYOQ", #kak febiya dn
            "https://drive.google.com/uc?export=view&id=1TalzBLl1mHZ844DAmoW6MLU-6HVgzTdY", #bang happy syahrul dn
            "https://drive.google.com/uc?export=view&id=1TF96CqvXcgzx1BtdYSQ-g5f0X-hqTQk0", #bang randa dn
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
                "kesan" : "sosok yang penuh inisiatif dan selalu berpikir ke depan",  
                "pesan" : "menjadi pribadi yang selalu terbuka untuk belajar dan berbagi pengetahuan"
            },
            {
                "nama"  : "Annisa Novantika",
                "nim"   : "121450005",
                "umur"  : "21",
                "asal"  : "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi" : "Memasak",
                "sosmed": "@anovavona",
                "kesan" : "pekerja keras dan selalu bisa diandalkan",  
                "pesan" : "Setiap pengalaman adalah kesempatan untuk menambah pengetahuan"
            },
            {
                "nama"  : "Ahmad Sahidin Akbar",
                "nim"   : "122450044",
                "umur"  : "20",
                "asal"  : "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi" : "Olahraga",
                "sosmed": "@sahid22__",
                "kesan" : "berbagi pengalaman nyata yang membantu memahami tantangan yang akan dihadapi",  
                "pesan" : "semangat pantang menyerah adalah kunci "
            },
            {
                "nama"  : "Fadhil Fitra Wijaya",
                "nim"   : "122450082",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Teluk Betung",
                "hobbi" : "Main game",
                "sosmed": "@fadhilfwee",
                "kesan" : "memberikan gambaran bahwa keseimbangan adalah kunci untuk sukses di kampus",  
                "pesan" : "Jangan ragu untuk mengejar hal-hal baru"
            },
            {
                "nama"  : "Syalaisha Andina Putriansyah",
                "nim"   : "122450121",
                "umur"  : "21",
                "asal"  : "Tangerang",
                "alamat": "Gang Yudhistira",
                "hobbi" : "Baca jurnal",
                "sosmed": "@dkselsd_31",
                "kesan" : "Ide-ide kreatifmu membuat banyak hal menjadi lebih baik",  
                "pesan" : "Semoga sukses selalu menyertaimu"
            },
            {
                "nama"  : "Dinda Nababan",
                "nim"   : "122450120",
                "umur"  : "20",
                "asal"  : "Medan, Sumatera Utara",
                "alamat": "Jalan Lapas",
                "hobbi" : "Belajar",
                "sosmed": "@dindanababan_",
                "kesan" : "memberi inspirasi dengan bimbingan dan pengalaman yang sangat berarti",  
                "pesan" : "Semoga kakak sukses di masa depan dan terus menginspirasi orang di sekitarnya"
            },
            {
                "nama"  : "Marleta Cornelia Leander",
                "nim"   : "122450092",
                "umur"  : "20",
                "asal"  : "Depok, Jawa Barat",
                "alamat": "Gang Nangka 3",
                "hobbi" : "Review Jurnal",
                "sosmed": "@marletacornelia",
                "kesan" : "sosok yang ramah dan selalu bersedia membantu saat dibutuhkan",  
                "pesan" : "Semoga kakak bisa mencapai semua yang dicita-citakan"
            },
            {
                "nama"  : "Rut Junita Sari Siburian",
                "nim"   : "122450103",
                "umur"  : "20",
                "asal"  : "Batam, Kepulauan Riau",
                "alamat": "Gang Nangka 3",
                "hobbi" : "Review Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan" : "memberi contoh yang baik dalam menjalani perkuliahan dan organisasi",  
                "pesan" : "Semangat terus kak dalam menjalani perkuliahannya"
            },
            {
                "nama"  : "Syadza Puspadari Azhar",
                "nim"   : "122450072",
                "umur"  : "20",
                "asal"  : "Palembang",
                "alamat": "Belwis",
                "hobbi" : "Resume SG",
                "sosmed": "@puspadrr",
                "kesan" : "selalu memberi motivasi dan dorongan ",  
                "pesan" : "Teruslah berprestasi dan semoga kakak meraih semua impian"
            },
            {
                "nama"  : "Eggi satria",
                "nim"   : "122450032",
                "umur"  : "20",
                "asal"  : "Sukabumi",
                "alamat": "Korpri",
                "hobbi" : "Ngoding WISATA",
                "sosmed": "@egistr",
                "kesan" : "selalu mengayomi dan membantu kami saat menghadapi kesulitan",  
                "pesan" : "selalu diberi kemudahan dalam setiap langkah karier dan kehidupan"
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
                "pesan" : "semoga urusannya dalam dunia perkuliahan dapat diselesaikan dengan mudah"
            },
             {
                "nama"  : "Happy Syahrul Ramadhan",
                "nim"   : "122450013",
                "umur"  : "20",
                "asal"  : "Lampung Timur",
                "alamat": "Karang Anyar",
                "hobbi" : "Main game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan" : "selalu memberi semangat dan arahan yang sangat membantu",  
                "pesan" : "Jangan pernah berhenti menginspirasi"
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
            "https://drive.google.com/uc?export=view&id=1X58k8IpybfkBsyBZ-8gNmDRDdNzsDBE2", #bang wahyu dn
            "https://drive.google.com/uc?export=view&id=1h6hqmijctiQKrL4kcOBJ2iINLJo0YTXp", #kak elok dn
            "https://drive.google.com/uc?export=view&id=18xM8cQUd6ohlnNJDmd0_kB_LsOjeVTep", #kak arsyiah dn
            "https://drive.google.com/uc?export=view&id=1qJKc5dxk8NekWP6FMExuWmS1MxSJ9NQq", #kak cintya dn
            "https://drive.google.com/uc?export=view&id=1FSEJsJ4eCQRF_j76tcbVbGNTVgB4c1Bx", #kak najla dn
            "https://drive.google.com/uc?export=view&id=12aPCNRPwkt8nG6ORc2vG-n6wQKGMCvqe", #kak rahma dn
            "https://drive.google.com/uc?export=view&id=1-eN_Ohd6DLSlT1nbKfY7b-Dxo0wdfY6o", #kak try yani dn
            "https://drive.google.com/uc?export=view&id=1FgHTwxIwJ54QUvP3AEyP65zawS5fLZ_y", #bang kaisar dn
            "https://drive.google.com/uc?export=view&id=1DGDy2JQ4yZ9TRejeI0pzH3kXxQRQUyv1", #kak dwi dn
            "https://drive.google.com/uc?export=view&id=1q0F6qesq_aYA2Z1FfGglYVoA-mQBL7cc", #bang gym dn
            "https://drive.google.com/uc?export=view&id=17_cRmRoO3eyDuKgO6K8CfU6_KvcCNW5A", #kak nasywa dn
            "https://drive.google.com/uc?export=view&id=1r4xMUGTN5sqQr8-MfM4GwsFBn4PIHygO", #kak priska dn
            "https://drive.google.com/uc?export=view&id=1eUlUImY5MyEAxY5CFsfAd4YroQ1iZxG6", #bang arsal dn
            "https://drive.google.com/uc?export=view&id=1xFO98SDwFrVQVy58v6TMgZlTN1dq2BHq", #bang abit dn
            "https://drive.google.com/uc?export=view&id=1ogD-gKZgcWLcpT4IQKgjxhj48fYU3WEM", #bang akmal dn
            "https://drive.google.com/uc?export=view&id=1q0F6qesq_aYA2Z1FfGglYVoA-mQBL7cc", #bang hermawan dn
            "https://drive.google.com/uc?export=view&id=15cSh2Pzd0xhX2OXn7aKbKhbWfdDeBlHl", #kak nisa dn
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
                "kesan" : "Ide-ide kreatifmu membuat banyak hal menjadi lebih baik",  
                "pesan" : "Jangan ragu untuk mengejar hal-hal baru"
            },
            {
                "nama"  : "Elok Fiola",
                "nim"   : "122450051",
                "umur"  : "19",
                "asal"  : "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi" : "Editing",
                "sosmed": "@elokfiola",
                "kesan" : "selalu bekerja dengan penuh tanggung jawab",  
                "pesan" : "Semoga sukses selalu menyertaimu"
            },
            {
                "nama"  : "Arsyiah Azahra",
                "nim"   : "121450035",
                "umur"  : "21",
                "asal"  : "Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi" : "Nugas",
                "sosmed": "@arsyiah.__",
                "kesan" : "Kehangatan dan perhatian kakak membuat kami merasa dihargai dan nyaman",  
                "pesan" : "semoga kakak terus sukses di masa depan"
            },
            {
                "nama"  : "Cintya Bella",
                "nim"   : "122450066",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Teluk",
                "hobbi" : "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan" : "contoh yang luar biasa dalam hal tanggung jawab dan dedikasi",  
                "pesan" : "Semoga langkah-langkah kakak selalu dimudahkan"
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
                "pesan" : "jangan lupa jaga kesehatan"
            },
            {
                "nama"  : "Rahma Neliyana",
                "nim"   : "122450036",
                "umur"  : "20",
                "asal"  : "Lampung",
                "alamat": "Sukarame",
                "hobbi" : "Baca Coding",
                "sosmed": "@rahmanellyana",
                "kesan" : "Kakak selalu memberi semangat dan arahan yang sangat membantu",  
                "pesan" : "Tetap semangat dan teruslah berprestasi, Kak. Kami bangga bisa belajar dari kakak"
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
                "kesan" : "memberikan teladan yang baik dalam belajar dan berorganisasi",  
                "pesan" : "Semoga segala kerja keras Kakak selama ini membawa hasil yang terbaik"
            },
            {
                "nama"  : "Gymnastiar Al Khoarizmy",
                "nim"   : "122450096",
                "umur"  : "20",
                "asal"  : "Serang",
                "alamat": "Lapangan Golf UIN",
                "hobbi" : "Baca komik",
                "sosmed": "@jimnn.as",
                "kesan" : "memotivasi kami untuk ikut aktif dan berkontribusi",  
                "pesan" : "Teruslah menjadi kakak yang rendah hati dan peduli"
            },
             {
                "nama"  : "Nasywa Nur Afifah",
                "nim"   : "122450125",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Jalan Durian 1 Pemda",
                "hobbi" : "Nonton drakor",
                "sosmed": "@nsywanaf",
                "kesan" : "Kakak adalah sosok yang inspiratif",  
                "pesan" : "Semoga pengalaman dan ilmu yang Kakak peroleh selama di kampus bisa bermanfaat bagi orang banyak"
            },
            {
                "nama"  : "Priska Silvia Ferantiana",
                "nim"   : "122450053",
                "umur"  : "19",
                "asal"  : "Palembang",
                "alamat": "Jalan Nangka 2",
                "hobbi" : "Baca novel yang bikin nangis",
                "sosmed": "@prskslv",
                "kesan" : "memberikan teladan yang baik dalam belajar ",  
                "pesan" : " bisa mencapai cita-cita yang diimpikan"
            },
            {
                "nama"  : "Muhammad Arsal Ranjana Utama",
                "nim"   : "121450111",
                "umur"  : "21",
                "asal"  : "Depok",
                "alamat": "Jalan Nangka 4",
                "hobbi" : "Ngoding",
                "sosmed": "@arsal.utama",
                "kesan" : "sangat ramah dan selalu siap membantu kami",  
                "pesan" : "Semoga Kakak terus sukses di masa depan, baik dalam karier maupun kehidupan pribadi"
            },
            {
                "nama"  : "Abit Ahmad Oktarian",
                "nim"   : "122450042",
                "umur"  : "19",
                "asal"  : "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi" : "Ngoding, Gaming",
                "sosmed": "@abitahmad",
                "kesan" : "terbantu dengan nasihat-nasihat Kakak yang praktis",  
                "pesan" : "Semoga segala pengalaman Kakak selama di kampus bisa menjadi bekal yang kuat untuk meraih cita-cita"
            },
            {
                "nama"  : "Akmal Faiz Abdillah",
                "nim"   : "122450114",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi" : "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan" : "memberi contoh tentang kedisiplinan dan kerja keras yang harus kami terapkan",  
                "pesan" : "Kakak tetap rendah hati dan selalu mengingat kami di kampus ini"
            },
            {
                "nama"  : "Hermawan Manurung",
                "nim"   : "122450069",
                "umur"  : "20",
                "asal"  : "Bogor",
                "alamat": "Dekat jalan tol, Wisma Hana Hani",
                "hobbi" : "Bengong dan membaca buku",
                "sosmed": "@hermawan.mnrng",
                "kesan" : "Sangat menginspirasi dalam kehidupan",  
                "pesan" : "Tetap semangat kak dalam menjalani dunia perkuliahan"
            },
            {
                "nama"  : "Khusnun Nisa",
                "nim"   : "122450078",
                "umur"  : "20",
                "asal"  : "Lampung Selatan",
                "alamat": "Belwis",
                "hobbi" : "Mengerjakan tugas",
                "sosmed": "@khusnun_nisa335",
                "kesan" : "terinspirasi oleh pengalaman dan wawasan yang Kakak bagikan kepada kami",  
                "pesan" : "Kakak bisa terus menjadi panutan dan inspirasi"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()
    
elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1UEYgfO1iP_Yq_YC_zglPbsa2jmk2-_VR", #bang yogy dn
            "https://drive.google.com/uc?export=view&id=1UEhvEHYUI6glOv2NKv-_6Bvj5twDebqg", #kak ramadhita dn
            "https://drive.google.com/uc?export=view&id=1UHBPAuvadE-s0QuEHwvbrhqYz8ZbIlza", #kak nazwa dn
            "https://drive.google.com/uc?export=view&id=1UMjAVp9fQdQdScpRqxkkYjvK2QBMIS3c", #bang bastian dn
            "https://drive.google.com/uc?export=view&id=1UTHwXE78k6l5AhbvI80ysSzas6ZDp3x4", #kak dea dn
            "https://drive.google.com/uc?export=view&id=1UNYgn3FJMs0PoQpqlm7YZNVBAFuCxmeA", #kak esteria dn
            "https://drive.google.com/uc?export=view&id=1URbXC45Gb3ab_Hg5ihGvcK9BkSc6z6DI", #kak natasya ega dn
            "https://drive.google.com/uc?export=view&id=1Uf0A7nfO0z1Bumi-ifA2LbSKPeSnJuYE", #kak novelia dn
            "https://drive.google.com/uc?export=view&id=1UgT6d-kn6EZvq5EkWLl0UFgzFB4dmfm0", #kak jasmine dn
            "https://drive.google.com/uc?export=view&id=1Uk2muWXJwAzL0TQpiHZRul-iG6BQ8-0e", #bang tobias dn
            "https://drive.google.com/uc?export=view&id=1FJoJiSJ13b3aDbidC0zgr2f0ttpoRsuY", #kak yohana dn
            "https://drive.google.com/uc?export=view&id=1bHbRSfd_YprUO-c2Ax3dcOM1PjjqN7cT", #bang rizki dn
            "https://drive.google.com/uc?export=view&id=1UPzUg-IcC9vUcJfdV2PvcE7C_qzLeofI", #bang arafi dn
            "https://drive.google.com/uc?export=view&id=1UlRpXH8PRCr4ySR5yIokYKZoaKb7Saxb", #kak uyi dn
            "https://drive.google.com/uc?export=view&id=1FJoJiSJ13b3aDbidC0zgr2f0ttpoRsuY", #kak chalifia dn
            "https://drive.google.com/uc?export=view&id=1UmP7DcTrCOraC1TRxWZ-NzftQJEtB1D9", #bang irvan dn
            "https://drive.google.com/uc?export=view&id=1UNfCi9_JwE9t2xhDcXh1RmidqjHK__7B", #kak izza dn
            "https://drive.google.com/uc?export=view&id=1Ucr4u2a7t80c2cSCnwVITkoknuXo7Xkq", #kak zuhrah dn
            "https://drive.google.com/uc?export=view&id=1UmP7DcTrCOraC1TRxWZ-NzftQJEtB1D9", #bang raid dn
            "https://drive.google.com/uc?export=view&id=1UMnqDM1tavZepR7t6smmymJht4oBWnkX", #kak tria dn
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
                "kesan" : "terinspirasi oleh pengalaman dan wawasan yang Kakak bagikan",  
                "pesan" : "Teruslah menjadi kakak yang rendah hati dan peduli"
            },
            {
                "nama"  : "Ramadhita Atifa Hendri",
                "nim"   : "121450131",
                "umur"  : "21 Tahun",
                "asal"  : "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi" : "Jalan - Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan" : "sangat ramah dan selalu siap membantu kami",  
                "pesan" : "Semoga Kakak terus sukses di masa depan, baik dalam karier maupun kehidupan pribadi"
            },
            {
                "nama"  : "Nazwa Nabilla",
                "nim"   : "121450122",
                "umur"  : "21 Tahun",
                "asal"  : "Jakarta Selatan",
                "alamat": "Way kandis",
                "hobbi" : "Belajar",
                "sosmed": "@nazwanbilla",
                "kesan" : "terbantu dengan nasihat-nasihat Kakak yang praktis",  
                "pesan" : "Semoga segala pengalaman Kakak selama di kampus bisa menjadi bekal yang kuat untuk meraih cita-cita"
            },
            {
                "nama"  : "Bastian Heskia Silaban",
                "nim"   : "122450130",
                "umur"  : "21 Tahun",
                "asal"  : "Batam, Kepulauan Riau",
                "alamat": "Belwis",
                "hobbi" : "Main game",
                "sosmed": "@bastiansilaban_",
                "kesan" : "terinspirasi oleh prestasi dan kerja keras Kakak",  
                "pesan" : "Semoga Kakak bisa terus berkembang dan sukses di masa depan"
            },
            {
                "nama"  : "Dea Mutia Risani",
                "nim"   : "122450099",
                "umur"  : "20 Tahun",
                "asal"  : "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi" : "Dengerin musik",
                "sosmed": "@deaa.rsn",
                "kesan" : "Kami terinspirasi oleh prestasi dan kerja keras Kakak ",  
                "pesan" : "Tetap semangat dalam menjalani perkuliahannya kak dan jangan lupa jaga kesehatan"
            },
            {
                "nama"  : "Esteria Rohanauli Sidauruk",
                "nim"   : "122450025",
                "umur"  : "19 Tahun",
                "asal"  : "Jakarta Selatan",
                "alamat": "Belwis",
                "hobbi" : "Main golf bareng kadiv",
                "sosmed": "@esteriars",
                "kesan" : "memotivasi kami untuk selalu berusaha lebih baik",  
                "pesan" : "tetap menginspirasi banyak orang"
            },
            {
                "nama"  : "Natasya Ega Lina",
                "nim"   : "122450024",
                "umur"  : "19 Tahun",
                "asal"  : "Jakarta Selatan",
                "alamat": "Belwis",
                "hobbi" : "Jadi humas",
                "sosmed": "@nateee__15",
                "kesan" : "sosok yang tegas dan disiplin",  
                "pesan" : "selalu membawa kebaikan di mana pun berada"
            },
            {
                "nama"  : "Novelia Adinda",
                "nim"   : "122450104",
                "umur"  : "21 Tahun",
                "asal"  : "Jakarta Timur",
                "alamat": "Belwis",
                "hobbi" : "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan" : "penuh pengertian dan peduli pada adik-adiknya",  
                "pesan" : "Jangan lupa untuk tetap menjaga semangat"
            },
            {
                "nama"  : "Ratu Keisha Jasmine Deanova",
                "nim"   : "122450106",
                "umur"  : "20 Tahun",
                "asal"  : "Jakarta Selatan",
                "alamat": "Way Kandis",
                "hobbi" : "Main sepak takraw",
                "sosmed": "@jasminednva",
                "kesan" : "membuat suasana belajar lebih menyenangkan dan memberikan rasa nyaman",  
                "pesan" : "Jangan lupa untuk tetap menjaga semangat"
            },
            {
                "nama"  : "Tobias David Manogari",
                "nim"   : "122450091",
                "umur"  : "20 Tahun",
                "asal"  : "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi" : "Jogging",
                "sosmed": "@tobiassiagian",
                "kesan" : "memberikan motivasi yang membuat kami semangat",  
                "pesan" : "Semoga Kakak selalu diberikan keberhasilan dalam mencapai impian dan tujuan hidup"
            },
             {
                "nama"  : "Yohana Manik",
                "nim"   : "122450126",
                "umur"  : "19 Tahun",
                "asal"  : "Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi" : "Main Bowling",
                "sosmed": "@yo_annamnk",
                "kesan" : "Kehadiran Kakak benar-benar memberi contoh tentang kedisiplinan",  
                "pesan" : "Semoga Kakak terus diberi kesuksesan yang lebih besar ke depannya"
            },
            {
                "nama"  : "Rizki Adrian Bennovry",
                "nim"   : "121450073",
                "umur"  : "21 Tahun",
                "asal"  : "Bekasi",
                "alamat": "TVRI",
                "hobbi" : "Bikin portofolio",
                "sosmed": "@rzkdrnnn",
                "kesan" : "sosok yang tegas dan disiplin",  
                "pesan" : "Semoga Kakak bisa terus berkembang dan sukses di masa depan"
            },
            {
                "nama"  : "Arafi Ramadhan Maulana",
                "nim"   : "122450002",
                "umur"  : "20 Tahun",
                "asal"  : "Bandung",
                "alamat": "Way Huwi",
                "hobbi" : "Bertani",
                "sosmed": "@rafiramadhanmaulana",
                "kesan" : "penuh pengertian dan peduli pada adik-adiknya",  
                "pesan" : "Semoga Kakak selalu diberikan keberhasilan dalam mencapai impian dan tujuan hidup."
            },
            {
                "nama"  : "Asa Do'a Uyi",
                "nim"   : "122450005",
                "umur"  : "20 Tahun",
                "asal"  : "Muara Enim",
                "alamat": "Korpri",
                "hobbi" : "Tepuk Semangat",
                "sosmed": "@u_yippy",
                "kesan" : "terbantu dengan nasihat-nasihat Kakak yang praktis",  
                "pesan" : "Semoga segala pengalaman Kakak selama di kampus bisa menjadi bekal yang kuat untuk meraih cita-cita"
            },
            {
                "nama"  : "Chalifia Wananda",
                "nim"   : "122450076",
                "umur"  : "20 Tahun",
                "asal"  : "Padang",
                "alamat": "Sukarame",
                "hobbi" : "Q Time",
                "sosmed": "@chlfawww",
                "kesan" : "terinspirasi oleh pengalaman dan wawasan yang Kakak",  
                "pesan" : "Semoga pengalaman dan ilmu yang Kakak peroleh selama di kampus bisa bermanfaat bagi orang banyak"
            },
            {
                "nama"  : "Irvan Alfaritzi",
                "nim"   : "122450093",
                "umur"  : "21 Tahun",
                "asal"  : "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi" : "Nonton youtube, main game",
                "sosmed": "@alfaritziirvan",
                "kesan" : "memotivasi kami untuk ikut aktif dan berkontribusi",  
                "pesan" : " Kakak bisa terus menjadi panutan dan inspirasi, tidak hanya bagi adik tingkat, tapi juga bagi orang di sekitar"
            },
            {
                "nama"  : "Izza Lutfia",
                "nim"   : "122450090",
                "umur"  : "20 Tahun",
                "asal"  : "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi" : "Main Rubik",
                "sosmed": "@izzalutfia",
                "kesan" : "membantu kami lebih percaya diri dalam menjalani perkuliahan",  
                "pesan" : "Semangat terus kak dalam menjalani perkuliahannya serta jangan lupa untuk jaga kesehatan"
            },
            {
                "nama"  : "Khaalishah Zuhrah Alyaa Vanefi",
                "nim"   : "122450034",
                "umur"  : "20 Tahun",
                "asal"  : "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi" : "Mengaji",
                "sosmed": "@alyaavanevi",
                "kesan" : "sangat membantu dan inspiratif",  
                "pesan" : "semoga Kakak semakin sukses dan ilmunya bermanfaat"
            },
            {
                "nama"  : "Raid Muhammad Naufal",
                "nim"   : "122450027",
                "umur"  : "20 Tahun",
                "asal"  : "Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi" : "telat",
                "sosmed": "@rayths_",
                "kesan" : "membuat kami merasa lebih nyaman dan siap menghadapi perkuliahan",  
                "pesan" : "teruslah menginspirasi adik-adik tingkat"
            },
            {
                "nama"  : "Tria Yunanni",
                "nim"   : "122450062",
                "umur"  : "20 Tahun",
                "asal"  : "Way Kanan",
                "alamat": "Sukarame",
                "hobbi" : "Baca Buku",
                "sosmed": "@tria_y062",
                "kesan" : "Sangat baik dan sangat mengasyikkan",  
                "pesan" : "Semoga segala kerja keras Kakak selama ini membawa hasil yang terbaik"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()  
    
elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=11XUYXlRY2YXhVNQ03xmIrmvadc1NMWh2", #bang dimas dn
            "https://drive.google.com/uc?export=view&id=1OmYiSabOFNnuZG0POspfe1nAkKCfT7mq", #kak catherine dn
            "https://drive.google.com/uc?export=view&id=1amhxQe6qKkyOQtCGMFydCPU2A8-7mq3J", #bang akbar dn
            "https://drive.google.com/uc?export=view&id=1DGxq8vjPFIDmanhyz4UW962KSkxJQUP0", #kak rani dn
            "https://drive.google.com/uc?export=view&id=1DhS6kOPgBmIxFuiBhSGJVUtFGtGlUgom", #bang rendra dn
            "https://drive.google.com/uc?export=view&id=1cxCz4-PmU2Gk4Q3uAgmedoQa75GztOfk", #kak salwa dn
            "https://drive.google.com/uc?export=view&id=1h0E9cQFOC6aJpQJfTnT411LKtJpo58cO", #bang yosia dn
            "https://drive.google.com/uc?export=view&id=1gcT_MiTGSWNX6SEs3iOYTAP0M2NdsXIf", #bang ari dn
            "https://drive.google.com/uc?export=view&id=1VKD3Pfu1f1OvWqlbb4mw02bN0e2bEW-N", #kak azizah dn
            "https://drive.google.com/uc?export=view&id=1Y9UpwVioKbSTIL8y32bUrhAtRpL4Roo6", #kak meira dn
            "https://drive.google.com/uc?export=view&id=1BtDmZPjN2bFn2dDkeg2eKX0v4jCNBiVE", #bang rendi dn
            "https://drive.google.com/uc?export=view&id=1Gzudo0Nq1WgKiONZkLi0lMmRaqW4wmWq", #kak renta dn
            "https://drive.google.com/uc?export=view&id=1PFVQFVzmACQCzObdE3892PRLUPfPWcFe", #bang josua dn

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
                "kesan" : "memberikan teladan yang baik dalam belajar dan berorganisasi",  
                "pesan" : "Semoga Kakak sukses selalu dalam setiap langkah, baik di dunia akademik maupun karier di masa depan"
            },
            {
                "nama"  : "Catherine Firdhasari Maulina Sinaga",
                "nim"   : "121450071",
                "umur"  : "20",
                "asal"  : "Sumatera Utara",
                "alamat": "Airan",
                "hobbi" : "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan" : "terinspirasi oleh pengalaman dan wawasan yang Kakak bagikan kepada kami",  
                "pesan" : "Semoga kakak bisa meraih kesuksesan yang lebih besar di luar sana"
            },
            {
                "nama"  : "M.Akbar Resdika",
                "nim"   : "121450066",
                "umur"  : "20",
                "asal"  : "Lampung Barat (Way Tenun)",
                "alamat": "Labuhan Dalam (Untung)",
                "hobbi" : "Suka kucing tapi gak suka ngurusnya",
                "sosmed": "@akbar_resdika",
                "kesan" : "memberi contoh tentang kedisiplinan dan kerja keras yang harus kami terapkan",  
                "pesan" : "Semoga Kakak selalu diberikan keberhasilan dalam mencapai impian dan tujuan hidup"
            },
            {
                "nama"  : "Rani Puspita sari",
                "nim"   : "122450030",
                "umur"  : "20",
                "asal"  : "Kota Metro",
                "alamat": "Rajabasa",
                "hobbi" : "Dengar musik",
                "sosmed": "@ranniu",
                "kesan" : "sangat terbantu dengan nasihat-nasihat Kakak yang praktis ",  
                "pesan" : "tetap rendah hati dan selalu mengingat kami di kampus ini"
            },
            {
                "nama"  : "Rendra Eka Prayoga",
                "nim"   : "122450112",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Belwis",
                "hobbi" : "Mancing Ikan Mas",
                "sosmed": "@rendraepr",
                "kesan" : "memberikan motivasi yang membuat kami semangat untuk terus maju dan berkembang",  
                "pesan" : "Semoga pengalaman dan ilmu yang Kakak peroleh selama di kampus bisa bermanfaat bagi orang banyak"
            },
            {
                "nama"  : "Salwa Farhanatussaidah",
                "nim"   : "122450055",
                "umur"  : "20",
                "asal"  : "Pesawaran",
                "alamat": "Airan",
                "hobbi" : "Nonton",
                "sosmed": "@slwfhn_694",
                "kesan" : "antusiasme Kakak dalam kegiatan-kegiatan kampus benar-benar memotivasi kami untuk ikut aktif dan berkontribusi",  
                "pesan" : "Semoga Kakak sukses selalu dalam setiap langkah, baik di dunia akademik maupun karier di masa depan"
            },
            {
                "nama"  : "Yosia Letare Banurea",
                "nim"   : "121450149",
                "umur"  : "20",
                "asal"  : "Dairi, Sumatera Utara",
                "alamat": "Perum Griya Indah",
                "hobbi" : "Tidur",
                "sosmed": "@yosiabanurea",
                "kesan" : "terinspirasi oleh pengalaman dan wawasan yang Kakak bagikan kepada kami",  
                "pesan" : "Semoga pengalaman dan ilmu yang Kakak peroleh selama di kampus bisa bermanfaat bagi orang banyak"
            },
            {
                "nama"  : "Ari Sigit",
                "nim"   : "121450069",
                "umur"  : "23",
                "asal"  : "Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobbi" : "Futsal",
                "sosmed": "@ari_sigit17",
                "kesan" : "memberi contoh tentang kedisiplinan dan kerja keras yang harus kami terapkan",  
                "pesan" : "Semoga segala pengalaman Kakak selama di kampus bisa menjadi bekal yang kuat untuk meraih cita-cita"
            },
            {
                "nama"  : "Azizah Kusumah Putri",
                "nim"   : "122450068",
                "umur"  : "21",
                "asal"  : "Lampung Selatan",
                "alamat": "Natar",
                "hobbi" : "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan" : "mengingatkan kami untuk tetap fokus pada tujuan dan menjaga semangat dalam belajar",  
                "pesan" : "Semoga segala pengalaman Kakak selama di kampus bisa menjadi bekal yang kuat untuk meraih cita-cita"
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
                "pesan" : "Semoga Kakak selalu diberikan keberhasilan dalam mencapai impian dan tujuan hidup"
            },
            {
                "nama"  : "Rendi Alexander Hutagalung",
                "nim"   : "122450057",
                "umur"  : "20",
                "asal"  : "Tangerang",
                "alamat": "Kost Benawang",
                "hobbi" : "Menyanyi",
                "sosmed": "@rexander",
                "kesan" : "memberikan motivasi yang membuat kami semangat untuk terus maju dan berkembang",  
                "pesan" : "semoga segala pengalaman Kakak selama di kampus bisa menjadi bekal yang kuat untuk meraih cita-cita"
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
                "kesan" : "antusiasme Kakak dalam kegiatan-kegiatan kampus benar-benar memotivasi kami untuk ikut aktif dan berkontribusi",  
                "pesan" : "Teruslah menjadi sosok yang menginspirasi, dan jangan pernah berhenti belajar untuk menjadi yang terbaik"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()   
    
elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1WEKWen79W9UzOBhmc3Y4hzjhoLwHqXbi", #bang andrian dn
            "https://drive.google.com/uc?export=view&id=1UDSdxKpNlKTnr5bgB1_ir_P3ziotOhRH", #kak adisty dn
            "https://drive.google.com/uc?export=view&id=1YtkcM0rxUxDHbXBZJ52TTKjGyX9wL4L8", #kak nabilla dn
            "https://drive.google.com/uc?export=view&id=1rRPAK0Y5oHL1h4A9pVhFQp79GaJrx0hU", #bang danang dn
            "https://drive.google.com/uc?export=view&id=1z2V2-f7HIMXYemTbkUURq_GMqu9nHGXl", #bang farrel dn
            "https://drive.google.com/uc?export=view&id=1NsPm517FLLoTFP8SU1GdSOmTewmBTw62", #kak nabilah dn
            "https://drive.google.com/uc?export=view&id=10XLHXE22exPTzQDDmQC8ire2Rk2Entrn", #kak alvia dn
            "https://drive.google.com/uc?export=view&id=1_7BiISpQWiBwZZfp9He1j1NKyy658Esw", #bang dhafin dn
            "https://drive.google.com/uc?export=view&id=1qnHEPug1yCY_Rxfu20E3dVFve7-99j0g", #kak elia dn


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
                "kesan" : "Sangat informatif dalam menjelaskan sesuatu dan menjadi sosok yang memberikan banyak masukan serta motivasi melalui pengalaman yang telah dilakukan",  
                "pesan" : "Tetap semangat kak dalam menjalani hari-harinya, semoga diperlancar dalam menyelesaikan tugas dan tanggung jawab yang sedang di emban"
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
                "kesan" : "Sangat informatif dalam menerangkan sesuatu dan sangat menginspirasi",  
                "pesan" : "Semoga selalu dilancarkan semua urusannya kak, jangan lupa untuk tetap semangat kak dalam menjalani kehidupan"
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
                "kesan" : "Sangat baik dan sangat informatif dalam menjelaskan sesuatu",  
                "pesan" : "Semangat terus kak dalam menjalani hari-harinya, semoga semua tugas dan tanggung jawab yang diemban dapat diselesaikan dengan lancar"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()    

# Tambahkan menu lainnya sesuai kebutuhan