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
            "https://drive.google.com/uc?export=view&id=1tmN3d-aXahG2ViiF8XHk-BCqMzwqzT_y", #bg gumilang
            "https://drive.google.com/uc?export=view&id=1b6nAr_o7GU7G7JzJVgb7q8DP_30AVrxQ", #bg pandra
            "https://drive.google.com/uc?export=view&id=1ksHpkcakOkFEiXWcdcDx01cvuQ2ZAe5J",
            "https://drive.google.com/uc?export=view&id=1Ter7Ycr-UzOxIADrKwNNyYbE4uumuner",
            "https://drive.google.com/uc?export=view&id=1xvdUhnFJadhHUqDtv5v2BHLHFRePt0OY",
            "https://drive.google.com/uc?export=view&id=1zoqxT1d7MKrhcgDUXTJsFaVDm9plB2sm",
        ]
        data_list = [
            {
                "nama": "Kharisma Gumilang",
                "nim": "121450142",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Kandis",
                "hobbi": "Denger musik",
                "sosmed": "@gumilangkharisma",
                "kesan": "abang Keren abisss",  
                "pesan": "Semoga abang tetap menjaga semangat dan antusiasme dalam segala hal yang dilakukan"
            },
            {
                "nama": "Pandra Insani Putra Azwan",
                "nim": "121450137",
                "umur": "21",
                "asal":"Bukit Kemuning (Lampung Utara)",
                "alamat": "Bawen 2",
                "hobbi": "Bermain gitar dan menyanyi",
                "sosmed": "@pandrainsni27",
                "kesan": "Abang sangat menginspirasi dalam menjelaskan peran kesekjenan, terutama tentang manajemen waktu dan koordinasi antar bidang. Saya jadi paham betul bagaimana pentingnya peran kesekjenan dalam kelancaran kegiatan himpunan",  
                "pesan": "Semoga abang selalu diberikan kemudahan dalam menjalankan amanah di kesekjenan dan sukses dalam studi serta karirnya ke depan"
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal": "Pagar Alam (Sumatera Selatan)",
                "alamat": "Kota baru",
                "hobbi": "Nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "Wawancara dengan kakak sangat menyenangkan, banyak pelajaran berharga tentang manajemen administrasi dan pengarsipan dalam himpunan yang bisa saya ambil",  
                "pesan": "Semoga kakak terus bersemangat dalam menjalankan tugas di kesekjenan dan sukses dalam segala hal yang kakak lakukan"
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal": "Payakumbuh (Sumatera Barat)",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin bang pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "Kakak sangat detail dalam menjelaskan alur kerja kesekjenan, membuat saya memahami betapa pentingnya administrasi yang baik dalam sebuah organisasi",  
                "pesan": "Semoga kakak selalu diberi kelancaran dalam menjalankan tugas di kesekjenan dan sukses mencapai cita-cita"
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "Sangat terkesan dengan dedikasi kakak dalam menjalankan tugas di kesekjenan, terutama dalam hal keuangan di dalam himpunan",  
                "pesan": "Semoga kakak tetap konsisten dalam memberikan yang terbaik untuk himpunan dan sukses dalam perjalanan karir ke depannya"
            },
            {
                "nama": "Nadilla Andara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal": "Metro",
                "alamat": "Kota Baru",
                "hobbi": "Membaca",
                "sosmed": "@ndillaandr26",
                "kesan": "Kakak memberikan banyak insight berharga tentang pentingnya komunikasi dan koordinasi dalam kesekjenan, sangat membantu pemahaman saya tentang sistem kerja himpunan",  
                "pesan": "Semoga kakak selalu diberikan kemudahan dalam menjalankan amanah dan sukses dalam mencapai semua impian"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1xRrbHeHAkVuL1TeTvuLpXp3MCqFJqqpq",
            "https://drive.google.com/uc?export=view&id=1xjPPuhgeGi2EgB21kLVSXnDXXww1e0kC",
            "https://drive.google.com/uc?export=view&id=1xQ7n4Hw3extNnr3F14UOWiz1v6DlID83",
            "https://drive.google.com/uc?export=view&id=1xK4PvHBWapVhlkSr41tyjUtzqE6xrcU4",
            "https://drive.google.com/uc?export=view&id=1xFub_YxLeJVHHso5Ah9ABBqGluBlZJ1y",
            "https://drive.google.com/uc?export=view&id=1xRHPRnwAwbueZ-l6vnkLf62ICn2S13Lw",
            "https://drive.google.com/uc?export=view&id=1xf7pRpTaJSevirLT0F6bbAlHfydimuR9",
            "https://drive.google.com/uc?export=view&id=1xbafHzpWhWYckSosBQ9ZJnSCZKIYrD6U",
            "https://drive.google.com/uc?export=view&id=1xMCyjRsS5koATh6hfwu_DssScwCK6oGR",
            "https://drive.google.com/uc?export=view&id=1azGGQxAwR-VcSlkP4_az859r9b_uXkVT",
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
                "kesan" : "Kakak sangat detail dalam menjelaskan proses legislasi di himpunan, membuat saya jadi paham betul alur pembuatan kebijakan",
                "pesan" : "Semoga kakak bisa terus berkontribusi dalam membuat kebijakan yang bermanfaat untuk HMSD kedepannya"
            },
            {
                "nama"  : "Annisa Cahyani Surya", 
                "nim"   : "121450114",
                "umur"  : "21",
                "asal"  : "Tanggerang Selatan",
                "alamat": "Way Huwi",
                "hobbi" : "Membaca, Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan" : "Wawancara dengan kakak sangat menyenangkan, banyak insight baru tentang peran legislatif di himpunan",
                "pesan" : "Terus semangat kak dalam menjalankan amanah di baleg, semoga sukses selalu"
            },
            {
                "nama"  : "Wulan Sabina",
                "nim"   : "121450150", 
                "umur"  : "21",
                "asal"  : "Medan",
                "alamat": "Raden Saleh",
                "hobbi" : "Nonton Drakor",
                "sosmed": "@wlnsbn0",
                "kesan" : "Kakak sangat inspiratif dalam menjelaskan pentingnya fungsi pengawasan di himpunan",
                "pesan" : "Semoga ilmu yang kakak bagikan bisa bermanfaat untuk kemajuan HMSD kedepannya"
            },
            {
                "nama"  : "Annisa Dini Amaliya",
                "nim"   : "121450081",
                "umur"  : "21", 
                "asal"  : "Tanggerang",
                "alamat": "Jati Agung",
                "hobbi" : "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan" : "Banyak pelajaran berharga tentang fungsi baleg yang kakak bagikan selama wawancara",
                "pesan" : "Tetap semangat menjalankan tugas di baleg kak, semoga selalu diberi kemudahan"
            },
            {
                "nama"  : "Anisa Fitriyani",
                "nim"   : "121450150",
                "umur"  : "21",
                "asal"  : "Medan", 
                "alamat": "Raden Saleh",
                "hobbi" : "Nonton Drakor",
                "sosmed": "@wlnsbn0",
                "kesan" : "Kakak sangat baik dalam membimbing dan menjelaskan tugas-tugas di badan legislatif",
                "pesan" : "Semoga kakak selalu diberi kesehatan dan kelancaran dalam bertugas"
            },
            {
                "nama"  : "Mirzan Yusuf Rabbani",
                "nim"   : "122450118",
                "umur"  : "20",
                "asal"  : "Jakarta",
                "alamat": "Korpri",
                "hobbi" : "Main Kucing",
                "sosmed": "@myrrinn",
                "kesan" : "Abang memberikan perspektif baru tentang pentingnya legislasi dalam organisasi kemahasiswaan",
                "pesan" : "Terus berkarya bang dalam membuat peraturan yang progresif untuk HMSD"
            },
            {
                "nama"  : "Dhea Amelia Putri",
                "nim"   : "122450004",
                "umur"  : "20",
                "asal"  : "Sukabumi, Jawa Barat",
                "alamat": "Natar",
                "hobbi" : "Suka Ikut Tes SKD",
                "sosmed": "@dhea_wedding",
                "kesan" : "Kakak sangat detail menjelaskan mekanisme pembuatan peraturan di himpunan",
                "pesan" : "Semoga kakak selalu diberikan keberkahan dalam menjalankan amanah"
            },
            {
                "nama"  : "Muhammad Fahrul Aditya",
                "nim"   : "121450156",
                "umur"  : "22",
                "asal"  : "Surakarta, Jawa Tengah",
                "alamat": "Pahoman",
                "hobbi" : "Melukis, badminton, hiking, ngopi, dengerin music, nonton film dan ngoding",
                "sosmed": "@fhrul.pdf",
                "kesan" : "Abang memberikan wawasan mendalam tentang peran strategis baleg dalam himpunan",
                "pesan" : "Terus berkontribusi untuk kemajuan HMSD melalui kebijakan yang inovatif bang"
            },
            {
                "nama"  : "Berlianda Enda Putri",
                "nim"   : "122450065",
                "umur"  : "21",
                "asal"  : "Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi" : "Main Game",
                "sosmed": "@berlyyanda",
                "kesan" : "Kakak sangat inspiratif dalam menjelaskan fungsi pengawasan dan legislasi",
                "pesan" : "Semoga kakak selalu diberi kemudahan dalam menjalankan tugas di baleg"
            },
            {
                "nama"  : "Jeremia Susanto",
                "nim"   : "122450022",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi" : "Marah-marah",
                "sosmed": "@jeremia_s_",
                "kesan" : "Abang memberikan pemahaman yang jelas tentang proses pembuatan kebijakan",
                "pesan" : "Terus semangat bang dalam mengawal kebijakan untuk kemajuan HMSD"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1GqJ_6TFrHfqplxpOdVE_aoj_HZUXfbpg", #kak lutfi dn
            "https://drive.google.com/uc?export=view&id=1GbioT1naHmK-sAiXrS7zn5uNNAFBb0y7", #bang bintang dn
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
                "kesan" : "Kakak sangat menginspirasi dalam memberikan wawasan dan pengalaman yang berharga. Cara kakak menyampaikan cerita membuat saya termotivasi untuk terus berkembang",
                "pesan" : "Semoga kakak selalu diberikan kesehatan, keberkahan, dan kesuksesan dalam setiap langkah. Terima kasih atas ilmu dan pengalaman yang telah dibagikan"
            },
            {
                "nama"  : "Rian Bintang Wijaya",
                "nim"   : "122450094",
                "umur"  : "20", 
                "asal"  : "Palembang, Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi" : "Mendengar Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan" : "Abang adalah sosok yang sangat inspiratif dan memotivasi. Sharing pengalaman dan cerita dari abang membuat saya lebih berani untuk mencoba hal baru yang positif",
                "pesan" : "Semoga abang selalu diberi kemudahan dalam menggapai cita-cita dan impian. Terus berbagi pengalaman yang berharga untuk adik-adik tingkat ya bang!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1RWgqyusXGPJClnVVjn_s3MCSm63iQ-Fy", #bang erickson dn
            "https://drive.google.com/uc?export=view&id=1Q1dMAamIvkG3oXI5nB-6V2EHzmyorTT2", #kak abeth dn 
            "https://drive.google.com/uc?export=view&id=19JjlQtmiZ-1WvgpdvA8P1Xd2Kb_dbyOE", #kak afifah dn 
            "https://drive.google.com/uc?export=view&id=1GB7cGU1BeN9orY_y4VH41T40soab7nte", #kak allya dn 
            "https://drive.google.com/uc?export=view&id=1gnMsLqa1EMqPUGlY9DRtMM8yDSRW0ahV", #kak hanum dn 
            "https://drive.google.com/uc?export=view&id=1BHdS3-OKOrWmlSZO7ATf_GCMfNT2yx1V", #bang ferdy dn 
            "https://drive.google.com/uc?export=view&id=1WPGXifHQ5eb4F-GvghQAVGBFdSUMsZnY", #bang deri dn 
            "https://drive.google.com/uc?export=view&id=1yaAofgqhaSNEePpBd6Oh0hqmrE5P0KGD", #kak oktavia dn 
            "https://drive.google.com/uc?export=view&id=1AZwMhxy7RxGpwSxDms7t0YHMHpleWkxP", #bang deyvan 
            "https://drive.google.com/uc?export=view&id=1Acm2Yfszz9v4Y2enVMQH6fsVro_SKwKs", #bang ibnu 
            "https://drive.google.com/uc?export=view&id=1A2mG8BTa1uSJ2Z_cL3rkNeAKD7ML4CwM", #bang jo 
            "https://drive.google.com/uc?export=view&id=1Aa9kqXI314m8Oq9XkCy9E6LGhwhQXp6E", #bang kemas 
            "https://drive.google.com/uc?export=view&id=1Al1XL1H2o4TzFG7Ukvci6I-CYR6X0VXN", #bang leonard 
            "https://drive.google.com/uc?export=view&id=1Aaaww68KgDglkkHd-KQwG6d2LWLXNQLH", #kak presilia 
            "https://drive.google.com/uc?export=view&id=1AWHxqpKFr9Zqoor-TCHPagBz_m7M_Os9", #kak rafa 
            "https://drive.google.com/uc?export=view&id=1WdYZpDI9qwAJYrp70ZS3CY8BKXclLHJh", #bang sahid dn 
            "https://drive.google.com/uc?export=view&id=1AH-9bGUPkAGp1ayKp0_qc2rKX8mD-3DI", #kak vanes 
            "https://drive.google.com/uc?export=view&id=151nlaE_-CU-_DSePFKXXuLRvikeFn3Ah", #bang ateng dn 
            "https://drive.google.com/uc?export=view&id=1in5H609G7RZ8htW0aBePB1hltrMrNwDy", #bang gede dn 
            "https://drive.google.com/uc?export=view&id=1p2e6X0AbZ2DDvvsL1kYr6kgU7R8leIJd", #kak jaclin dn 
            "https://drive.google.com/uc?export=view&id=1ClRuZzmVlNQHPfX6oKdJt-1X4l1gzAJK", #bang rafly dn 
            "https://drive.google.com/uc?export=view&id=1peUDX5MK8Hmy0ZCJY8-vMGDUu3YrN6tl", #kak dini dn 

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
                "kesan" : "Abang sangat menginspirasi dalam memimpin dan mengelola sumber daya anggota himpunan. Cara abang memotivasi dan membimbing anggota sangat membangun",
                "pesan" : "Semoga abang selalu diberi kemudahan dalam menjalankan amanah sebagai kepala departemen PSDA. Terus semangat dalam membangun dan mengembangkan potensi anggota himpunan!"
            },
            {
                "nama"  : "Elisabeth Claudia Simanjuntak",
                "nim"   : "121450114",
                "umur"  : "21",
                "asal"  : "Tanggerang Selatan",
                "alamat": "Way Huwi",
                "hobbi" : "Membaca, Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan" : "walaupun belum mewawancarai kakak, saya yakin pengalaman yang kakak ceritakan pasti sangat menginspirasi",  
                "pesan" : "Semoga dilancarkan semua kegiatannya di dalam maupun di luar perkuliahan dan tetap semangat kak"
            },
            {
                "nama"  : "Nisrina Nur Afifah",
                "nim"   : "122450052",
                "umur"  : "19",
                "asal"  : "Bekasi",
                "alamat": "Sukarame",
                "hobbi" : "Nabok orang",
                "sosmed": "@afifahhnsrn",
                "kesan" : "Setelah wawancara dengan kakak, saya mendapat banyak insight tentang bagaimana cara berorganisasi yang baik dan benar di Himpunan",  
                "pesan" : "Semoga kakak selalu diberikan kesehatan dan kemudahan dalam menjalani perkuliahan. Terima kasih atas ilmu dan pengalaman yang telah dibagikan"
            },
            {
                "nama"  : "Allya Nurul Islami Pasha",
                "nim"   : "122450033",
                "umur"  : "20",
                "asal"  : "Sumatera Barat",
                "alamat": "Gang Perwira, Belwis",
                "hobbi" : "Nonton Dracin",
                "sosmed": "@allyaislami_",
                "kesan" : "Wawancara dengan kakak sangat berkesan karena kakak membagikan pengalaman yang menarik tentang bagaimana kaderisasi berlangsung",
                "pesan" : "Semoga kakak selalu diberi kelancaran dalam menyelesaikan tugas kuliah dan organisasi"
            },
            {
                "nama"  : "Farahanum Afifah Ardiansyah",
                "nim"   : "122450056",
                "umur"  : "20",
                "asal"  : "Padang, Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi" : "Tidur",
                "sosmed": "@farahanumafifahh",
                "kesan" : "Kakak sangat ramah dan terbuka dalam membagikan pengalaman selama di HMSD",  
                "pesan" : "Semoga kakak sukses dalam perkuliahan dan karirnya ke depan."
            },
            {
                "nama"  : "Ferdy Kevin Naibaho",
                "nim"   : "122450107",
                "umur"  : "19",
                "asal"  : "Medan, Sumatera Utara",
                "alamat": "Jalan Senopati Raya 18",
                "hobbi" : "Dengerin Rocky Gerung",
                "sosmed": "@ferdy_kevin",
                "kesan" : "Wawancara dengan abang memberikan pandangan baru tentang sistem kaderisasi di HMSD dan lebih mengenal bagaimana divisi kaderisasi bekerja.",  
                "pesan" : "Semoga kakak selalu diberi kemudahan dalam menggapai cita-cita. Terus berkarya dan menginspirasi orang lain"
            },
            {
                "nama"  : "M. Deriansyah Okutra",
                "nim"   : "122450101",
                "umur"  : "19",
                "asal"  : "Kayu Agung",
                "alamat": "Jalan Pagar Alam",
                "hobbi" : "Bercerita horror",
                "sosmed": "@dransyh_",
                "kesan" : "Abang sangat inspiratif dalam membagikan pengalaman di HMSD.",  
                "pesan" : "Semoga kakak selalu sukses dalam setiap langkah yang diambil. Terima kasih atas waktu dan ilmunya"
            },
            {
                "nama"  : "Oktavia Nurwenda Puspita Sari",
                "nim"   : "122450041",
                "umur"  : "20",
                "asal"  : "Lampung Timur",
                "alamat": "Way Hui",
                "hobbi" : "Memasak",
                "sosmed": "@_oktavianrwnda_",
                "kesan" : "walaupun saya belum mewawancarai kakak,saya yakin kakak juga akan membagikan pengalaman yang menarik tentang bagaimana divisi PSDA melaksanakan tugas",  
                "pesan" : "Semoga kakak selalu diberkahi kesuksesan dalam setiap langkah."
            },
            {
                "nama"  : "Deyvan Loxefal",
                "nim"   : "121450148", 
                "umur"  : "21",
                "asal"  : "Riau",
                "alamat": "Pulau Damar",
                "hobbi" : "Belajar",
                "sosmed": "@depanloo",
                "kesan" : "Wawancara dengan abang sangat menarik, banyak insight tentang bagaimana divisi minat bakat mengembangkan potensi mahasiswa Sains Data",
                "pesan" : "Semoga abang selalu diberikan kesehatan dan kesuksesan dalam menjalankan amanah di divisi minat bakat"
            },
            {
                "nama"  : "Ibnu Farhan Al-Ghifari",
                "nim"   : "121450121",
                "umur"  : "21", 
                "asal"  : "Jambi",
                "alamat": "Pulau Damar, Kobam",
                "hobbi" : "Bermain Game Online",
                "sosmed": "@al_ghifari032",
                "kesan" : "Abang memberikan penjelasan yang detail tentang program kerja divisi minat bakat yang sangat bermanfaat",
                "pesan" : "Semoga abang tetap semangat dalam mengembangkan bakat mahasiswa Sains Data melalui program-program yang inovatif"
            },
             {
                "nama"  : "Johannes Krisjon Silitonga",
                "nim"   : "122450043",
                "umur"  : "19",
                "asal"  : "Tanggerang", 
                "alamat": "Jalan Lapas",
                "hobbi" : "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan" : "Sangat terkesan dengan dedikasi abang dalam memfasilitasi pengembangan minat dan bakat mahasiswa",
                "pesan" : "Terus berkarya dalam memajukan potensi mahasiswa Sains Data abang dan selalu dimudahkan dalam segala urusannya"
            },
            {
                "nama"  : "Kemas Veriandra Ramadhan",
                "nim"   : "122450016",
                "umur"  : "19",
                "asal"  : "Bekasi",
                "alamat": "Golf Asri",
                "hobbi" : "Bermain ular python digital",
                "sosmed": "@kemasverii",
                "kesan" : "Wawancara dengan abang membuka wawasan tentang pentingnya mengembangkan soft skill melalui kegiatan minat bakat",
                "pesan" : "Semoga dimudahkan dalam segala hal yang di cita-citakan"
            },
            {
                "nama"  : "Leonard Andreas Napitupulu",
                "nim"   : "121450153",
                "umur"  : "21",
                "asal"  : "Sumatera Utara",
                "alamat": "Kobam",
                "hobbi" : "Belajar",
                "sosmed": "@lnrd.__",
                "kesan" : "Abang sangat inspiratif dalam menjelaskan bagaimana divisi minat bakat berperan dalam pengembangan mahasiswa",
                "pesan" : "Terus semangat dalam melakukan segala hal bang!!"
            },
            {
                "nama"  : "Presilia",
                "nim"   : "121450081",
                "umur"  : "21",
                "asal"  : "Tanggerang",
                "alamat": "Jati Agung",
                "hobbi" : "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan" : "Mendapat banyak pembelajaran tentang bagaimana divisi minat bakat membantu mahasiswa mengembangkan potensi diri",
                "pesan" : "Semoga kakak selalu diberi kemudahan dalam melakukan segala hal yang di cita-citakan"
            },
            {
                "nama"  : "Rafa Aqilla Jungjunan",
                "nim"   : "122450148",
                "umur"  : "20",
                "asal"  : "Riau",
                "alamat": "Belwis",
                "hobbi" : "Membaca webtoon",
                "sosmed": "@rafaaqilla",
                "kesan" : "Terkesan dengan dedikasi kakak dalam mengembangkan minat dan bakat mahasiswa Sains Data",
                "pesan" : "Tetap semangat dalam hal apapun kak"
            },
            {
                "nama"  : "Sahid Maulana",
                "nim"   : "122450109",
                "umur"  : "21",
                "asal"  : "Depok, Jawa Barat",
                "alamat": "Airan Raya",
                "hobbi" : "Bermain Game",
                "sosmed": "@sahid_maul19",
                "kesan" : "Wawancara dengan abang memberikan gambaran yang jelas tentang peran penting divisi minat bakat",
                "pesan" : "Semoga abang selalu sukses dalam mengembangkan potensi mahasiswa melalui program-program yang menarik dan selalu dimudahkan mencapai segala sesuatu"
            },
            {
                "nama"  : "Vanessa Olivia Rose",
                "nim"   : "121450068",
                "umur"  : "20",
                "asal"  : "Jakarta",
                "alamat": "Perumahan Korpri",
                "hobbi" : "Belajar",
                "sosmed": "@roselivnes__",
                "kesan" : "Sangat menginspirasi mendengar pengalaman kakak dalam mengelola kegiatan minat bakat di HMSD",
                "pesan" : "Terus semangat dalam melakukan segala hal kak!!"
            },
            {
                "nama"  : "M. Farhan Athaulloh",
                "nim"   : "121450156", 
                "umur"  : "22",
                "asal"  : "Surakarta, Jawa Tengah",
                "alamat": "Pahoman",
                "hobbi" : "Melukis, badminton, hiking, ngopi, dengerin music, nonton film dan ngoding",
                "sosmed": "@fhrul.pdf",
                "kesan" : "Sangat terkesan dengan dedikasi abang dalam mengembangkan minat olahraga dan kompetisi mahasiswa Sains Data",
                "pesan" : "Semoga abang selalu diberi kemudahan dalam menjalankan amanah dan terus bersemangat memajukan prestasi mahasiswa"
            },
            {
                "nama"  : "Gede Moana",
                "nim"   : "122450065",
                "umur"  : "21", 
                "asal"  : "Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi" : "Main Game",
                "sosmed": "@berlyyanda",
                "kesan" : "Wawancara dengan abang memberikan insight baru tentang pentingnya keseimbangan antara akademik dan prestasi non-akademik",
                "pesan" : "Terus berkarya dan menginspirasi adik-adik untuk berprestasi dalam bidang olahraga dan kompetisi bang!"
            },
            {
                "nama"  : "Jaclin Alcavella",
                "nim"   : "122450022",
                "umur"  : "20",
                "asal"  : " Bandar Lampung", 
                "alamat": "Kemiling",
                "hobbi" : "Marah-marah",
                "sosmed": "@jeremia_s_",
                "kesan" : "Kagum dengan penjelasan kakak mengenai program-program yang dijalankan divisi olahraga dan perlombaan untuk mengembangkan potensi mahasiswa",
                "pesan" : "Semoga kakak selalu sukses dan bisa terus memotivasi mahasiswa untuk aktif dalam kegiatan olahraga dan kompetisi"
            },
            {
                "nama"  : "Rafly Prabu Darmawan",
                "nim"   : "122450065",
                "umur"  : "21",
                "asal"  : "Sumatera Barat",
                "alamat": "Way Huwi", 
                "hobbi" : "Main Game",
                "sosmed": "@berlyyanda",
                "kesan" : "Terinspirasi dengan semangat abang dalam memfasilitasi mahasiswa untuk berkembang melalui olahraga dan kompetisi",
                "pesan" : "Tetap semangat menjalankan program-program yang bermanfaat untuk mahasiswa Sains Data bang!"
            },
            {
                "nama"  : "Syalaisha Andini Putriansyah",
                "nim"   : "122450022",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi" : "Marah-marah", 
                "sosmed": "@jeremia_s_",
                "kesan" : "Mendapat banyak pembelajaran tentang bagaimana divisi olahraga dan perlombaan berperan dalam pengembangan soft skill mahasiswa",
                "pesan" : "Semoga kakak selalu diberi kelancaran dalam mengemban amanah dalam menjalankan tugas"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1H2u71MT9pnWkuLZcovctHTEMHc8Tq4MH", #bang rafi dn 
            "https://drive.google.com/uc?export=view&id=1Hb3I2xJ_SIMTFTk97j4a0ZIPwgVWjUtU", #kak okta dn 
            "https://drive.google.com/uc?export=view&id=1HG__86bGzPwGpMtx77-AKtAHb_QGxHSq", #bang ahmad dn 
            "https://drive.google.com/uc?export=view&id=1HYl7-3ylnSmkRgDaS9zRkuObesugjKTO", #kak fadhil dn 
            "https://drive.google.com/uc?export=view&id=1HS1xzs4OUCKYuMDcCOAUgC92bFJ9Cyar", #kak syalaisha dn 
            "https://drive.google.com/uc?export=view&id=1H_-QKrFcZIvvs0hR_zngPc2qeGUM8rs1", #kak dinda dn 
            "https://drive.google.com/uc?export=view&id=1HUpA4eNdLqQk5uK7oKeO_QQVgw739e6a", #kak marleta dn 
            "https://drive.google.com/uc?export=view&id=1Hk-4IMGGQnZXQBqj42EdBpbovo8J-9Ex", #kak rut junita dn 
            "https://drive.google.com/uc?export=view&id=1HakAaJGccfqwmyQZG7ofNTFtos54mvYf", #kak syadza dn 
            "https://drive.google.com/uc?export=view&id=1H9MeCzL9N4ODgAslrKS-3Dj-CCkqlCAF", #bang eggi dn 
            "https://drive.google.com/uc?export=view&id=1HspJcvrDjnVCzlESaKP8vPikA-OC1TFa", #kak febiya dn 
            "https://drive.google.com/uc?export=view&id=1HQpDeadQ5q_Wi2qsQIYw5x0hnWksrOSb", #kak happy syahrul dn 
            "https://drive.google.com/uc?export=view&id=1HZIzXu9YUxfiBL1QwRo51piheouiV4tg", #bang randa dn 
        
        ]
        data_list = [
            {
                "nama"  : "Rafi Fadhlillah",
                "nim"   : "121450038", 
                "umur"  : "21",
                "asal"  : "Bogor",
                "alamat": "Raden Saleh",
                "hobbi" : "Kalo ke coffe shop pesen red velvet bukan kopi",
                "sosmed": "@trimurniyaa",
                "kesan" : "Abang sangat menginspirasi dalam memimpin departemen akademik dan keprofesian.",
                "pesan" : "Semoga abang selalu diberi kemudahan dalam menjalankan amanah sebagai kepala departemen akademik dan keprofesian. Terus semangat dalam membangun dan mengembangkan potensi akademik anggota himpunan!"
            },
            {
                "nama"  : "Annisa Novantika",
                "nim"   : "121450005",
                "umur"  : "21",
                "asal"  : "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi" : "Memasak",
                "sosmed": "@anovavona",
                "kesan" : "kakaknya ramah dan ilmu yang dibagikan sangat bermanfaat",  
                "pesan" : "semoga selalu dilancarkan segala sesuatu yang di semogakan"
            },
            {
                "nama"  : "Ahmad Sahidin Akbar",
                "nim"   : "121450114",
                "umur"  : "21",
                "asal"  : "Tanggerang Selatan",
                "alamat": "Way Huwi",
                "hobbi" : "Membaca, Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan" : "ilmu yang abang berikan sangat bermanfaat",  
                "pesan" : "Semoga kegiatannya di dalam maupun di luar perkuliahan tetap lancar dan tetap semangat bang"
            },
            {
                "nama"  : "Fadhil Fitra Wijaya",
                "nim"   : "122450052",
                "umur"  : "19",
                "asal"  : "Bekasi",
                "alamat": "Sukarame",
                "hobbi" : "Nabok orang",
                "sosmed": "@afifahhnsrn",
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
                "pesan" : "Semoga urusan kakakbaik di akademik maupun non akademik dapat berjalan dengan lancar"
            },
            {
                "nama"  : "Syalaisha Andina Putriansyah",
                "nim"   : "122450033",
                "umur"  : "20",
                "asal"  : "Sumatera Barat",
                "alamat": "Gang Perwira, Belwis",
                "hobbi" : "Nonton Dracin",
                "sosmed": "@allyaislami_",
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
                "pesan" : "Semoga selalu dilancarkan semua urusannya kak, jangan lupa untuk tetap semangat kak dalam menjalani kehidupan"
            },
            {
                "nama"  : "Dinda Nababan",
                "nim"   : "122450056", 
                "umur"  : "20",
                "asal"  : "Padang, Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi" : "Tidur",
                "sosmed": "@farahanumafifahh",
                "kesan" : "Kakak sangat menginspirasi dalam menjelaskan pentingnya inovasi dan kajian akademik untuk pengembangan keilmuan sains data.",
                "pesan" : "Semoga kakak selalu diberi kemudahan dalam menjalankan tugas di divisi PIKA. Terus semangat dalam mengembangkan inovasi di HMSD!"
            },
            {
                "nama"  : "Marleta Cornelia Leander",
                "nim"   : "122450107",
                "umur"  : "19",
                "asal"  : "Medan, Sumatera Utara", 
                "alamat": "Jalan Senopati Raya 18",
                "hobbi" : "Dengerin Rocky Gerung",
                "sosmed": "@ferdy_kevin",
                "kesan" : "Kakak sangat detail dalam menjelaskan proses pengembangan inovasi akademik. Pengetahuan yang kakak bagikan sangat bermanfaat untuk pengembangan skill akademik saya",
                "pesan" : "Semoga kakak terus produktif menghasilkan karya inovatif yang berkualitas. Sukses selalu dalam segala hal kak!"
            },
            {
                "nama"  : "Rut Junita Sari Siburian",
                "nim"   : "122450101",
                "umur"  : "19",
                "asal"  : "Kayu Agung",
                "alamat": "Jalan Pagar Alam",
                "hobbi" : "Bercerita horror",
                "sosmed": "@dransyh_",
                "kesan" : "Kakak sangat inspiratif dalam menjelaskan bagaimana divisi pusat inovasi dan kajian akademik bekerja sama dalam mengembangkan potensi akademik mahasiswa",
                "pesan" : "Semoga kakak selalu sukses dalam menjalankan tugas. Terus berbagi ilmu dan pengalaman untuk adik-adik tingkat ya kak!"
            },
            {
                "nama"  : "Syadza Puspadari Azhar",
                "nim"   : "122450041",
                "umur"  : "20",
                "asal"  : "Lampung Timur",
                "alamat": "Way Hui",
                "hobbi" : "Memasak",
                "sosmed": "@_oktavianrwnda_",
                "kesan" : "Kakak sangat kompeten dalam menjelaskan inovasi untuk pengembangan akademik. Wawasan yang kakak berikan sangat membantu pemahaman saya tentang pentingnya inovasi dalam bidang akademik",
                "pesan" : "Semoga ilmu yang kakak miliki terus berkembang dan bermanfaat untuk kemajuan inovasi di HMSD. Tetap semangat membimbing adik-adik tingkat!"
            },
            {
                "nama"  : "Eggi satria",
                "nim"   : "121450148", 
                "umur"  : "21",
                "asal"  : "Riau",
                "alamat": "Pulau Damar",
                "hobbi" : "Belajar",
                "sosmed": "@depanloo",
                "kesan" : "Abang sangat menginspirasi dalam menjelaskan pentingnya riset dan survei untuk pengembangan keilmuan sains data. Cara abang menyampaikan materi sangat mudah dipahami",
                "pesan" : "Semoga abang selalu diberi kemudahan dalam menjalankan tugas di divisi survei dan riset. Terus semangat dalam mengembangkan penelitian di HMSD!"
            },
            {
                "nama"  : "Febiya Jomy Pratiwi",
                "nim"   : "121450121",
                "umur"  : "21", 
                "asal"  : "Jambi",
                "alamat": "Pulau Damar, Kobam",
                "hobbi" : "Bermain Game Online",
                "sosmed": "@al_ghifari032",
                "kesan" : "Kakak sangat inspiratif dalam menjelaskan bagaimana divisi survei dan riset bekerja sama.",
                "pesan" : "Semoga kakak selalu sukses dalam menjalankan tugas. Terus berbagi ilmu dan pengalaman untuk adik-adik tingkat ya kak!"
            },
             {
                "nama"  : "Happy Syahrul Ramadhan",
                "nim"   : "122450043",
                "umur"  : "19",
                "asal"  : "Tanggerang",
                "alamat": "Jalan Lapas",
                "hobbi" : "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan" : "Abang sangat detail dalam menjelaskan teknik pengambilan dan analisis data survei. Pengetahuan yang abang bagikan sangat bermanfaat untuk pengembangan skill riset saya",
                "pesan" : "Semoga abang terus produktif menghasilkan karya yang berkualitas. Sukses selalu dalam segala hal bang!"
            },
            {
                "nama"  : "Randa Andriana Putra",
                "nim"   : "122450016",
                "umur"  : "19",
                "asal"  : "Bekasi",
                "alamat": "Golf Asri",
                "hobbi" : "Bermain ular python digital",
                "sosmed": "@kemasverii",
                "kesan" : "Abang sangat kompeten dalam menjelaskan riset untuk pengolahan data .yang abang berikan sangat membantu pemahaman saya",
                "pesan" : "Semoga ilmu yang abang miliki terus berkembang dan bermanfaat untuk kemajuan riset di HMSD. Tetap semangat membimbing adik-adik tingkat!"
            },
            
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen MEDKRAF":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1lfbm8rMsq_PPMqZ3XhpizIdcLoKhRW_G", #bang wahyu dn
            "https://drive.google.com/uc?export=view&id=1ng8SxMVN9MvRKi1jKaDSjrO3SHdydfGM", #kak elok dn
            "https://drive.google.com/uc?export=view&id=1nWRru3kwDS0t3fwcADbtzQPV_7z3A_rv", #kak arsyiah dn 
            "https://drive.google.com/uc?export=view&id=1lv63M0mDLn1lQedKluSfOTdM0r-PuEIq", #kak cintya dn
            "https://drive.google.com/uc?export=view&id=1K2E-AZhCCE3V23g3ehfEBF41WB0pEJOj", #kak najla dn
            "https://drive.google.com/uc?export=view&id=1Ww7ASpdqAyTlouwF6mAGTf0WbY_7XMcZ", #kak rahma dn
            "https://drive.google.com/uc?export=view&id=1vur5YKOeG_2rvrbvCO62QthTj57WhoM4", #kak try yani dn
            "https://drive.google.com/uc?export=view&id=1nd9HvBU-YheRE2tw5bOWxuA6ZIteCxLw", #bang kaisar dn
            "https://drive.google.com/uc?export=view&id=1o_mPAD9C9ZLRkFlMoPNGgipRRo4reihF", #kak dwi dn
            "https://drive.google.com/uc?export=view&id=1o2ccX2CxyEJXDLXgcbmnz0OnbagzAlHD", #bang gym dn
            "https://drive.google.com/uc?export=view&id=1oFDlt28u4JyTRJOJAGR0fP3ciWDzHv2P", #kak nasywa dn
            "https://drive.google.com/uc?export=view&id=1oQO9hr1jt2awHetHyiBvlSUJBT5gYZb0", #kak priska dn
            "https://drive.google.com/uc?export=view&id=1nVhnCUcwfTUV4Ka4gVIVM--k6yGhUhOO", #bang arsal dn
            "https://drive.google.com/uc?export=view&id=1oKdzl2ZrxqBy8bwN6DQccS_jkSStTorQ", #bang abit dn
            "https://drive.google.com/uc?export=view&id=1n62r1WS79pdWmrjWkibt4Bok2UwQ0qLX", #bang akmal dn
            "https://drive.google.com/uc?export=view&id=1nzSqWj5o1eGb2fNuqT07o2EZbXO7J3rh", #bang hermawan dn
            "https://drive.google.com/uc?export=view&id=1XxRetWr1ZjdcFqSriDJuk43QtXuRVANp", #kak nisa dn
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
                "kesan" : "Pengalaman yang abang bagikan sangat bermanfaat dan membantu mengenai dunia kreatif",  
                "pesan" : "Tetap semangat bang dalam berkarya!!"
            },
            {
                "nama"  : "Elok Fiola",
                "nim"   : "122450051",
                "umur"  : "19",
                "asal"  : "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi" : "Editing",
                "sosmed": "@elokfiola",
                "kesan" : "Ilmu yang kakak bagikan sangat membantu saya memahami dunia kreatif",  
                "pesan" : "Semoga kakak terus berkarya dan menginspirasi banyak orang dengan kreativitas kakak. Sukses selalu!"
            },
            {
                "nama"  : "Arsyiah Azahra",
                "nim"   : "121450035",
                "umur"  : "21",
                "asal"  : "Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi" : "Nugas",
                "sosmed": "@arsyiah.__",
                "kesan" : "Sharing pengalaman kakak sangat bermanfaat",  
                "pesan" : "Semoga selalu diberikan kemudahan dalam menjalankan segala hal kak"
            },
            {
                "nama"  : "Cintya Bella",
                "nim"   : "122450066",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Teluk",
                "hobbi" : "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan" : "Kakak sangat baik dalam memberikan tips membuat konten menarik. Pengetahuan yang kakak bagikan sangat bermanfaat",  
                "pesan" : "Semoga kakak selalu semangat berkreasi dan menginspirasi banyak orang dengan karya-karya kakak"
            },
            {
                "nama"  : "Najla Juwairia",
                "nim"   : "122450037",
                "umur"  : "19",
                "asal"  : "Sumatera Utara",
                "alamat": "Airan",
                "hobbi" : "Menulis, Membaca, Fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan" : "Kakak sangat informatif dalam menjelaskan pembuatan konten yang menarik. Ilmu yang kakak bagikan sangat bermanfaat",  
                "pesan" : "Teruslah berkarya dan menginspirasi kak. Semoga selalu diberikan kesuksesan dalam berkarir di bidang kreatif"
            },
            {
                "nama"  : "Rahma Neliyana",
                "nim"   : "122450036",
                "umur"  : "20",
                "asal"  : "Lampung",
                "alamat": "Sukarame",
                "hobbi" : "Baca Coding",
                "sosmed": "@rahmanellyana",
                "kesan" : "Sharing pengalaman bersama kakak sangat memotivasi dan seru abissss!!",  
                "pesan" : "Semoga kakak semakin kreatif dalam berkarya. Sukses selalu untuk kakak!"
            },
            {
                "nama"  : "Try Yani Rizki Nur Rohmah",
                "nim"   : "122450020",
                "umur"  : "20",
                "asal"  : "Lampung Barat",
                "alamat": "Korpri",
                "hobbi" : "Bernyanyi dan Menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan" : "Kakak sangat detail dalam menjelaskan proses kreatif pembuatan konten. Ilmu yang kakak bagikan sangat bermanfaat",  
                "pesan" : "Terus berkarya dan menginspirasi kak. Semoga selalu diberikan ide-ide segar dalam berkreasi"
            },
            {
                "nama"  : "Muhammad Kaisar Firdaus",
                "nim"   : "121450135",
                "umur"  : "21",
                "asal"  : "Pesawaran",
                "alamat": "Pulau Damar",
                "hobbi" : "Lagi nyari",
                "sosmed": "@dino_lapet",
                "kesan" : "Abang sangat kompeten dalam menjelaskan teknik fotografi dan videografi. Pengalaman yang abang bagikan sangat berharga",  
                "pesan" : "Tetap semangat berkarya bang. Semoga selalu sukses dalam mengembangkan skill di bidang kreatif"
            },
            {
                "nama"  : "Dwi Ratna Anggraeni",
                "nim"   : "122450008",
                "umur"  : "20",
                "asal"  : "Jambi",
                "alamat": "Jalan Durian 5 Pemda",
                "hobbi" : "Membaca",
                "sosmed": "@dwiratnn_",
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
                "pesan" : "Semoga kakak terus berkarya dan dimudahkan dalam mencapai impian. Sukses selalu kak!!"
            },
            {
                "nama"  : "Gymnastiar Al Khoarizmy",
                "nim"   : "122450096",
                "umur"  : "20",
                "asal"  : "Serang",
                "alamat": "Lapangan Golf UIN",
                "hobbi" : "Baca komik",
                "sosmed": "@jimnn.as",
                "kesan" : "Pengalaman yang abang bagikan sangat bermanfaat",  
                "pesan" : "Terus berkarya dan menginspirasi bang. Semoga selalu sukses dalam mengembangkan kreativitas"
            },
            {
                "nama"  : "Nasywa Nur Afifah",
                "nim"   : "122450125",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Jalan Durian 1 Pemda",
                "hobbi" : "Nonton drakor",
                "sosmed": "@nsywanaf",
                "kesan" : "Sharing pengalaman kakak sangat memotivasi",  
                "pesan" : "Semoga kakak selalu semangat berkarya dan menginspirasi banyak orang. Sukses terus!"
            },
            {
                "nama"  : "Priska Silvia Ferantiana",
                "nim"   : "122450053",
                "umur"  : "19",
                "asal"  : "Palembang",
                "alamat": "Jalan Nangka 2",
                "hobbi" : "Baca novel yang bikin nangis",
                "sosmed": "@prskslv",
                "kesan" : "Ilmu yang kakak bagikan sangat bermanfaat",  
                "pesan" : "Terus berkarya dan berkembang kak. Semoga selalu sukses dalam mencapai impian"
            },
            {
                "nama"  : "Muhammad Arsal Ranjana Utama",
                "nim"   : "121450111",
                "umur"  : "21",
                "asal"  : "Depok",
                "alamat": "Jalan Nangka 4",
                "hobbi" : "Ngoding",
                "sosmed": "@arsal.utama",
                "kesan" : "Abang sangat menginspirasi dalam menjelaskan pentingnya inovasi dalam berkarya. Pengalaman yang abang bagikan sangat berharga",  
                "pesan" : "Semoga abang terus berkarya dan di mudahkan mencapai impian. Sukses selalu!"
            },
            {
                "nama"  : "Abit Ahmad Oktarian",
                "nim"   : "122450042",
                "umur"  : "19",
                "asal"  : "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi" : "Ngoding, Gaming",
                "sosmed": "@abitahmad",
                "kesan" : "Abang sangat detail dalam menjelaskan teknik desain grafis. Ilmu yang abang bagikan sangat membantu",  
                "pesan" : "Tetap semangat berkarya bang. Semoga selalu sukses dalam mengembangkan kreativitas"
            },
            {
                "nama"  : "Akmal Faiz Abdillah",
                "nim"   : "122450114",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi" : "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan" : "Abang sangat kompeten dalam menjelaskan proses pembuatan desain grafis. Sharing pengalaman abang sangat bermanfaat",  
                "pesan" : "Terus berkarya dan menginspirasi bang. Semoga selalu diberikan ide-ide segar dalam berkreasi"
            },
            {
                "nama"  : "Hermawan Manurung",
                "nim"   : "122450069",
                "umur"  : "20",
                "asal"  : "Bogor",
                "alamat": "Dekat jalan tol, Wisma Hana Hani",
                "hobbi" : "Bengong dan membaca buku",
                "sosmed": "@hermawan.mnrng",
                "kesan" : "Abang sangat inspiratif dalam menjelaskan pentingnya personal branding sejak dini. Pengalaman yang abang bagikan sangat memotivasi",  
                "pesan" : "Semoga abang terus berkembang dan semakin kreatif dalam berkarya. Sukses selalu!"
            },
            {
                "nama"  : "Khusnun Nisa",
                "nim"   : "122450078",
                "umur"  : "20",
                "asal"  : "Lampung Selatan",
                "alamat": "Belwis",
                "hobbi" : "Mengerjakan tugas",
                "sosmed": "@khusnun_nisa335",
                "kesan" : "Ilmu yang kakak bagikan sangat bermanfaat dan seru",  
                "pesan" : "Terus berkarya dan menginspirasi kak. Semoga selalu sukses dalam mengembangkan kreativitas"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1KRJnBqOrpDGUgbJjFBgl53l6N7hjTt_a", #bang yogy dn 
            "https://drive.google.com/uc?export=view&id=1JxoAydMaakJxWJYy43aOstZB3aKoHeNr", #kak ramadhita dn 
            "https://drive.google.com/uc?export=view&id=1LaJStnx96SeihXcW9gIwaN94GlSRCea5", #kak nazwa dn 
            "https://drive.google.com/uc?export=view&id=1LdZDWHzjGdYy327Zg8XBa1wdHNNllA-Q", #bang bastian dn 
            "https://drive.google.com/uc?export=view&id=1LMkJa2SmuB4n3tsiPWG3KyJ1ill6MZjl", #kak dea dn 
            "https://drive.google.com/uc?export=view&id=1LVQuMnFmdbeB6cBRr44Kh5_K4papgozh", #kak esteria dn 
            "https://drive.google.com/uc?export=view&id=1LPH6QWdTjAKtVwVB327DwctNT9HI4p8v", #kak natasya ega dn 
            "https://drive.google.com/uc?export=view&id=1KxKT0xmHTqUuiu6w8y2qSCWiv3YiK7j0", #kak novelia dn 
            "https://drive.google.com/uc?export=view&id=1LGmFrZdfQfRMwh-Lr90TtdJVNH6uiUui", #kak jasmine dn 
            "https://drive.google.com/uc?export=view&id=1LmXY0D2ra6W25v-htcFXFMy76oO7bbCc", #bang tobias dn 
            "https://drive.google.com/uc?export=view&id=1L582x1ZkcRH7kCnF15067kqqBpvbebth", #kak yohana dn 
            "https://drive.google.com/uc?export=view&id=1LyxkXLGIpFeDvq_DNBrGWoX5joV96DKB", #bang rizki dn 
            "https://drive.google.com/uc?export=view&id=1JumBzSBB7HrzKjOfeNLQQIaSf-BURYmE", #bang arafi dn 
            "https://drive.google.com/uc?export=view&id=1Lw9ct7Wp3amZqHxFPTV9AjB3QKWJp0q3", #kak uyi dn 
            "https://drive.google.com/uc?export=view&id=1M0fgPiUHRHDp3Qfs6cd3zxlpCE94F4nJ", #kak chalifia dn 
            "https://drive.google.com/uc?export=view&id=1KwYWpyCIPSagtW3_555ZdFNLQZXmoDhs", #bang irvan dn 
            "https://drive.google.com/uc?export=view&id=1KsGU2uDIlaXYRaGHffgzT_bpDN-pqwQd", #kak izza dn 
            "https://drive.google.com/uc?export=view&id=1KbarKt6nz5LPM3KB-ipZLMORiBd5XQub", #kak zuhrah dn 
            "https://drive.google.com/uc?export=view&id=1Kqay263YzMPdQfDeRZD129l9up1wWLpL", #bang raid dn 
            "https://drive.google.com/uc?export=view&id=1KaZpD2i9trKuvrG1FDoJeDALPj4aY-9O", #kak tria dn
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
                "kesan" : "Abang sangat menginspirasi dalam menjelaskan pentingnya kolaborasi dengan pihak luar untuk memajukan himpunan",  
                "pesan" : "Semoga abang selalu diberikan kesehatan dan keberkahan dalam menjalani perkuliahan. Terima kasih atas ilmu dan pengalamannya yang berharga"
            },
            {
                "nama"  : "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan" : "Kakak sangat baik dalam memberikan wawasan tentang pentingnya membangun relasi dengan pihak eksternal",  
                "pesan" : "Teruslah bersinar dan menginspirasi orang lain kak. Semoga sukses selalu dalam setiap langkah yang kakak ambil"
            },
            {
                "nama"  : "Nazwa Nabilla",
                "nim": "121450122",
                "umur": "21 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Way kandis",
                "hobbi": "belajar",
                "sosmed": "@nazwanbilla",
                "kesan" : "Pengalaman kakak dalam menjalin hubungan dengan pihak luar sangat berharga untuk dipelajari",  
                "pesan" : "Kakak adalah inspirasi bagi kami semua. Semoga kakak selalu diberkahi kesuksesan dalam setiap usaha"
            },
            {
                "nama"  : "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21 Tahun",
                "asal": "Batam, Kep. Riau",
                "alamat": "Belwis",
                "hobbi": "main game",
                "sosmed": "@bastiansilaban_",
                "kesan" : "Abang memberikan insight yang bagus tentang cara membangun networking yang baik dengan pihak eksternal",  
                "pesan" : "Terima kasih telah menjadi panutan yang luar biasa bang. Semoga abang terus berkembang dan mencapai impian"
            },
            {
                "nama"  : "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20 Tahun",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "dengerin musik",
                "sosmed": "@deaa.rsn",
                "kesan" : "Kakak sangat detail dalam menjelaskan pentingnya menjaga hubungan baik dengan stakeholder eksternal",  
                "pesan" : "Kakak adalah contoh pemimpin yang luar biasa. Semoga kakak selalu diberi kemudahan dalam menggapai cita-cita"
            },
            {
                "nama"  : "Esteria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "19 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Belwis",
                "hobbi": "Main golf bareng kadiv",
                "sosmed": "@esteriars",
                "kesan" : "Kakak memberikan pemahaman yang baik tentang cara berkomunikasi efektif dengan pihak eksternal",  
                "pesan" : "Teruslah menjadi pribadi yang menginspirasi kak. Semoga kakak selalu diberikan kebahagiaan dalam setiap langkah"
            },
            {
                "nama"  : "Natasya Ega Lina",
                "nim": "122450024",
                "umur": "19 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi": "jadi humas",
                "sosmed": "@nateee__15",
                "kesan" : "Pengalaman kakak dalam menangani hubungan eksternal sangat inspiratif dan bermanfaat",  
                "pesan" : "Kakak adalah inspirasi dalam kepemimpinan. Semoga kakak terus bersinar dan menginspirasi banyak orang"
            },
            {
                "nama"  : "Novelia Adinda",
                "nim": "122450104",
                "umur": "21 Tahun",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan" : "Kakak sangat baik dalam menjelaskan strategi membangun kerjasama dengan pihak luar",  
                "pesan" : "Terima kasih atas dedikasi dan inspirasinya kak. Semoga kakak selalu diberkahi dalam setiap langkah kehidupan"
            },
            {
                "nama"  : "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Main sepak takraw",
                "sosmed": "@jasminednva",
                "kesan" : "Kakak memberikan wawasan yang luas tentang pentingnya membangun relasi eksternal yang berkelanjutan",  
                "pesan" : "Kakak adalah teladan dalam memimpin. Semoga kakak terus sukses dan bahagia dalam menjalani hidup"
            },
            {
                "nama"  : "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20 Tahun",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Jogging",
                "sosmed": "@tobiassiagian",
                "kesan" : "Abang sangat detail dalam menjelaskan cara menjalin hubungan profesional dengan pihak eksternal",  
                "pesan" : "Terima kasih telah menjadi mentor yang luar biasa bang. Semoga abang selalu diberkahi kesuksesan"
            },
             {
                "nama"  : "Yohana Manik",
                "nim": "122450126",
                "umur": "19 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi": "Main Bowling",
                "sosmed": "@yo_annamnk",
                "kesan" : "Kakak memberikan insight yang bagus tentang pentingnya menjaga profesionalitas dengan pihak eksternal",  
                "pesan" : "Kakak adalah inspirasi dalam berorganisasi. Semoga kakak terus diberi kemudahan dalam mencapai impian"
            },
            {
                "nama"  : "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21 Tahun",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobbi": "Bikin portofolio",
                "sosmed": "@rzkdrnnn",
                "kesan" : "Abang sangat inspiratif dalam menjelaskan pentingnya networking yang baik untuk kemajuan himpunan",  
                "pesan" : "Terima kasih atas bimbingan dan inspirasinya bang. Semoga abang selalu sukses dalam setiap usaha"
            },
            {
                "nama"  : "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20 Tahun",
                "asal": "Bandung",
                "alamat": "Way Huwi",
                "hobbi": "Bertani",
                "sosmed": "@rafiramadhanmaulana",
                "kesan" : "Abang memberikan pemahaman yang baik tentang pentingnya kolaborasi dengan pihak eksternal",  
                "pesan" : "Abang adalah panutan dalam berorganisasi. Semoga abang terus diberkahi dalam setiap langkah kehidupan"
            },
            {
                "nama"  : "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20 Tahun",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobbi": "Tepuk Semangat",
                "sosmed": "@u_yippy",
                "kesan" : "Kakak sangat baik dalam menjelaskan cara membangun hubungan yang berkelanjutan dengan stakeholder",  
                "pesan" : "Kakak adalah inspirasi dalam memimpin. Semoga kakak selalu bahagia dan sukses dalam menggapai mimpi"
            },
            {
                "nama"  : "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20 Tahun",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Q Time",
                "sosmed": "@chlfawww",
                "kesan" : "Kakak memberikan insight yang berharga tentang pentingnya komunikasi efektif dengan pihak luar",  
                "pesan" : "Terima kasih telah menjadi mentor yang hebat kak. Semoga kakak selalu diberi kemudahan dalam setiap usaha"
            },
            {
                "nama"  : "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21 Tahun",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton youtube, main game",
                "sosmed": "@alfaritziirvan",
                "kesan" : "Abang sangat detail dalam menjelaskan strategi membangun relasi yang baik dengan pihak eksternal",  
                "pesan" : "Abang adalah teladan dalam berorganisasi. Semoga abang terus sukses dan menginspirasi banyak orang"
            },
            {
                "nama"  : "Izza Lutfia",
                "nim": "122450090",
                "umur": "20 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Main Rubik",
                "sosmed": "@izzalutfia",
                "kesan" : "Kakak memberikan pemahaman yang baik tentang pentingnya menjaga profesionalitas dalam hubungan eksternal",  
                "pesan" : "Kakak adalah inspirasi dalam kepemimpinan. Semoga kakak selalu diberkahi kebahagiaan dan kesuksesan"
            },
            {
                "nama"  : "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@alyaavanevi",
                "kesan" : "Kakak sangat inspiratif dalam menjelaskan cara membangun networking yang berkelanjutan",  
                "pesan" : "Terima kasih atas dedikasi dan inspirasinya kak. Semoga kakak terus bersinar dalam menggapai cita-cita"
            },
            {
                "nama"  : "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20 Tahun",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "telat",
                "sosmed": "@rayths_",
                "kesan" : "Abang memberikan wawasan yang luas tentang pentingnya kolaborasi dengan berbagai pihak eksternal",  
                "pesan" : "Abang adalah panutan yang luar biasa. Semoga abang selalu diberi kemudahan dalam mencapai impian"
            },
            {
                "nama"  : "Tria Yunanni",
                "nim": "122450062",
                "umur": "20 Tahun",
                "asal": "Way Kanan",
                "alamat": "Sukarame",
                "hobbi": "Baca Buku",
                "sosmed": "@tria_y062",
                "kesan" : "Kakak sangat baik dalam menjelaskan strategi membangun dan menjaga hubungan dengan stakeholder eksternal",  
                "pesan" : "Kakak adalah inspirasi bagi kami semua. Semoga kakak terus sukses dan bahagia dalam menjalani hidup"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()  

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1EeVG7gClrdJi4MCq_CpfQd480uw1p5dw", #bang dimas dn 
            "https://drive.google.com/uc?export=view&id=1iYWuL5DV8E-dINZXRAF2qVaO070tHMdi", #kak catherine dn 
            "https://drive.google.com/uc?export=view&id=1X4xkhwXl1SGQpLCRBQVxBa1RHnSRvvk0", #bang akbar dn 
            "https://drive.google.com/uc?export=view&id=1bbO-Ld98EkvOiXuev4nBYcTSc8lNbk9X", #kak rani dn 
            "https://drive.google.com/uc?export=view&id=1_m6gCZpn32Rg2pc0wyW-UOL1TaaeXKcl", #bang rendra dn 
            "https://drive.google.com/uc?export=view&id=1wABUc8w7sb2v-hBj8VdEir7ukNMJPwG9", #kak salwa dn 
            "https://drive.google.com/uc?export=view&id=1dV29MMU89WLIV7RCo07KJ47O8QWeQ1tn", #bang yosia dn 
            "https://drive.google.com/uc?export=view&id=1p40VrYL9jw59ewSi_214B3-BVjKMyNIg", #bang ari dn 
            "https://drive.google.com/uc?export=view&id=1VSWoTQcZZhR3SmY-WAAeWfwcgiOZKMu1", #kak azizah dn 
            "https://drive.google.com/uc?export=view&id=1iJ8iUfwGD5nwBHyxBjiS5FQmBNdP9aYG", #kak meira dn 
            "https://drive.google.com/uc?export=view&id=1RNXXnTMV-RXGD-TYs7dC6iUDm84J_e2X", #bang rendi dn 
            "https://drive.google.com/uc?export=view&id=17EOxwfebAx-ohTFM-fPYbeGx9RZ5TMC4", #kak renta dn 
            "https://drive.google.com/uc?export=view&id=1kAc7X5QFIX0lRmHrDIalsF5qpxucBQJ7", #bang josua dn 

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
                "kesan" : "Abang sangat menginspirasi dalam membangun keharmonisan antar anggota himpunan. Cara abang memimpin dan mengelola internal sangat baik",
                "pesan" : "Semoga abang selalu diberi kemudahan dalam menjalankan amanah sebagai kepala departemen internal. Terus semangat dalam membangun keharmonisan HMSD!"
            },
            {
                "nama"  : "Catherine Firdhasari Maulina Sinaga",
                "nim"   : "121450071",
                "umur"  : "20",
                "asal"  : "Sumatera Utara",
                "alamat": "Airan",
                "hobbi" : "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan" : "Kakak sangat baik dalam menjelaskan pentingnya menjaga keharmonisan antar anggota himpunan. Pengalaman kakak sangat berharga",
                "pesan" : "Semoga kakak selalu diberikan kesehatan dan keberkahan. Terima kasih atas ilmu dan pengalamannya"
            },
            {
                "nama"  : "Akbar Resdika",
                "nim"   : "121450066",
                "umur"  : "20",
                "asal"  : "Lampung Barat (Way Tenun)",
                "alamat": "Labuhan Dalam (Untung)",
                "hobbi" : "Suka kucing tapi gak suka ngurusnya",
                "sosmed": "@akbar_resdika",
                "kesan" : "Abang memberikan pemahaman yang mendalam tentang pentingnya menjaga kekompakan dan keharmonisan dalam internal himpunan",
                "pesan" : "Terus berkarya bang dalam membangun HMSD yang solid. Semoga selalu diberi kemudahan dalam setiap langkah"
            },
            {
                "nama"  : "Rani Puspita sari",
                "nim"   : "122450033", 
                "umur"  : "20",
                "asal"  : "Sumatera Barat",
                "alamat": "Gang Perwira, Belwis",
                "hobbi" : "Nonton Dracin",
                "sosmed": "@allyaislami_",
                "kesan" : "Kakak sangat detail dalam menjelaskan mekanisme kerja internal dan pentingnya menjaga hubungan baik antar anggota",
                "pesan" : "Semoga kakak selalu sukses dan bahagia. Terima kasih telah berbagi pengalaman yang berharga tentang internal HMSD"
            },
            {
                "nama"  : "Rendra Eka Prayoga",
                "nim"   : "122450112",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Belwis",
                "hobbi" : "Mancing Ikan Mas",
                "sosmed": "@rendraepr",
                "kesan" : "Abang memberikan wawasan yang luas tentang pentingnya koordinasi dan komunikasi dalam menjaga keharmonisan internal",
                "pesan" : "Terus semangat bang dalam mengembangkan internal HMSD. Semoga selalu diberi kelancaran dalam setiap kegiatan"
            },
            {
                "nama"  : "Salwa Farhanatussaidah",
                "nim"   : "122450055",
                "umur"  : "20",
                "asal"  : "Pesawaran",
                "alamat": "Airan",
                "hobbi" : "Nonton",
                "sosmed": "@slwfhn_694",
                "kesan" : "Kakak sangat inspiratif dalam menjelaskan cara membangun hubungan yang harmonis antar anggota himpunan",
                "pesan" : "Semoga kakak selalu diberi keberkahan dan kesuksesan. Terima kasih atas ilmu tentang pentingnya keharmonisan dalam internal"
            },
            {
                "nama"  : "Yosia Letare Banurea",
                "nim"   : "121450149",
                "umur"  : "20",
                "asal"  : "Dairi, Sumatera Utara",
                "alamat": "Perum Griya Indah",
                "hobbi" : "Tidur",
                "sosmed": "@yosiabanurea",
                "kesan" : "Abang memberikan insight yang bagus tentang pentingnya menjaga kekompakan dan kebersamaan dalam internal himpunan",
                "pesan" : "Terus berkarya bang dalam membangun internal yang solid. Semoga selalu diberi kemudahan dalam menjalankan amanah"
            },
            {
                "nama"  : "Ari Sigit",
                "nim"   : "121450069", 
                "umur"  : "23",
                "asal"  : "Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobbi" : "Futsal",
                "sosmed": "@ari_sigit17",
                "kesan" : "Abang memberikan wawasan yang mendalam tentang pentingnya menjaga keseimbangan antara nilai-nilai spiritual dalam dunia perkuliahan",
                "pesan" : "Terus berkarya bang dalam mengembangkan kerohanian HMSD. Semoga selalu diberi keberkahan dalam setiap langkah"
            },
            {
                "nama"  : "Azizah Kusumah Putri",
                "nim"   : "122450068",
                "umur"  : "21", 
                "asal"  : "Lampung Selatan",
                "alamat": "Natar",
                "hobbi" : "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan" : "Kakak sangat inspiratif dalam menjelaskan bagaimana memadukan nilai-nilai agama dengan aktivitas perkuliahan",
                "pesan" : "Semoga kakak selalu diberi kemudahan dalam menjalankan amanah. Terima kasih telah berbagi pengalaman yang berharga"
            },
            {
                "nama"  : "Meira Listyaningrum",
                "nim"   : "122450011",
                "umur"  : "20",
                "asal"  : "Pesawaran", 
                "alamat": "Airan",
                "hobbi" : "Membaca",
                "sosmed": "@meirasty_",
                "kesan" : "Kakak memberikan pemahaman yang baik tentang pentingnya keseimbangan antara kegiatan kerohanian dan organisasi",
                "pesan" : "Semoga kakak selalu diberi keberkahan dan kesuksesan. Terus semangat dalam mengembangkan kerohanian HMSD"
            },
            {
                "nama"  : "Rendi Alexander Hutagalung",
                "nim"   : "122450057",
                "umur"  : "20",
                "asal"  : "Tangerang",
                "alamat": "Kost Benawang",
                "hobbi" : "Menyanyi",
                "sosmed": "@rexander",
                "kesan" : "Abang memberikan insight yang bagus tentang bagaimana membangun karakter anggota himpunan melalui kegiatan kerohanian yang positif",
                "pesan" : "Terus berkarya bang dalam membangun spiritualitas anggota HMSD. Semoga selalu diberi kemudahan dalam setiap langkah"
            },
            {
                "nama"  : "Renta Siahaan",
                "nim"   : "122450070",
                "umur"  : "21",
                "asal"  : "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi" : "Membaca dan Memancing",
                "sosmed": "@renta.shn",
                "kesan" : "Kakak sangat detail dalam menjelaskan pentingnya nilai-nilai spiritual dalam membangun internal himpunan yang harmonis",
                "pesan" : "Semoga kakak selalu diberi keberkahan dalam menjalankan amanah. Terima kasih telah berbagi pengalaman yang berharga"
            },
            {
                "nama"  : "Josua Panggabean",
                "nim"   : "122450061",
                "umur"  : "21",
                "asal"  : "Pematang Siantar",
                "alamat": "Gerbang Barat", 
                "hobbi" : "Menonton",
                "sosmed": "@josuapanggabean_",
                "kesan" : "Abang memberikan pemahaman yang mendalam tentang bagaimana memadukan nilai kerohanian dengan aktivitas organisasi",
                "pesan" : "Semoga abang selalu diberi kelancaran dalam setiap kegiatan"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()   

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1pc74lNi5aNSRmPrhiIjLvmeJixfXgC2R", #bang andrian dn
            "https://drive.google.com/uc?export=view&id=1pCNAryY9N4_Mf0HeeHyS5XARkmDmOo3P", #kak adisty dn
            "https://drive.google.com/uc?export=view&id=1pHkwF3p5Gp-ItWl4sfg9vuJa2RjfIYA-", #kak nabilla dn
            "https://drive.google.com/uc?export=view&id=1pP9LFPBQjIQYAO_gu6gALEaNeNkWec06", #bang danang dn
            "https://drive.google.com/uc?export=view&id=1OJWzKE6lG69lKci3LV7JmBodagbw-bAN", #bang farrel dn
            "https://drive.google.com/uc?export=view&id=1pRp03Cgz2DItjwdTvcAtwi_qXbpk1yN-", #kak nabilah dn
            "https://drive.google.com/uc?export=view&id=1pB2jnFMVEZFpfEYKmHZP8xbFAiKheypn", #kak alvia dn
            "https://drive.google.com/uc?export=view&id=1p7vC7lbPxmFVaPAElQv42zBAXNixGI0E", #bang dhafin dn
            "https://drive.google.com/uc?export=view&id=1oxOoFFY0_whch5PiLJcjthjrVLiir6wg", #kak elia dn


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
                "kesan" : "pengalaman yang abang ceritakan sangat menginspirasi terutama bagaimana agar dapat memanfaatkan produk yang telah di buat",  
                "pesan" : "Semoga diperlancar dalam menyelesaikan tugas dan tanggung jawab yang sedang di emban"
            },
            {
                "nama"  : "Adisty Syawaida Ariyanto",
                "nim"   : "121450136",
                "umur"  : "22",
                "asal"  : "Metro",
                "alamat": "Sukarame ",
                "hobbi" : "Nonton Film",
                "sosmed": "@adistysa_",
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
                "pesan" : "Semoga selalu dilancarkan kegiatannya di dalam maupun di luar perkuliahan "
            },
            {
                "nama"  : "Nabila Azhari",
                "nim"   : "121450029",
                "umur"  : "21",
                "asal"  : "Simalungun",
                "alamat": "Airan ",
                "hobbi" : "Menghitung Uang",
                "sosmed": "@zhjung",
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi dan bermanfaat",  
                "pesan" : "Semoga urusannya baik di akademik maupun non akademik dapat berjalan dengan lancar"
            },
            {
                "nama"  : "Danang Hilal Kurniawan",
                "nim"   : "122450085",
                "umur"  : "21",
                "asal"  : "Bandar Lampung",
                "alamat": "Airan",
                "hobbi" : "Belajar",
                "sosmed": "@dananghk_",
                "kesan" : "pengalaman yang abang ceritakan sangat menginspirasi terutama dalam perdagangan produk yang baik dan benar",  
                "pesan" : "Semoga selalu dilancarkan semua urusannya kak, jangan lupa untuk tetap semangat kak dalam menjalani perkuliahan"
            },
            {
                "nama"  : "Farrel Julio Akbar",
                "nim"   : "122450110",
                "umur"  : "20",
                "asal"  : "Bogor",
                "alamat": "Lapas",
                "hobbi" : "Kayang",
                "sosmed": "@farel_julio",
                "kesan" : "pengalaman yang abang ceritakan sangat menginspirasi terutama dalam hal pemasaran produk",  
                "pesan" : "Tetap semangat dalam menjalani perkuliahannya bang!"
            },
            {
                "nama"  : "Nabilah Andika Fitriati",
                "nim"   : "121450139",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi" : "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan" : "Kakak sangat menginspirasi dalam memberikan wawasan tentang cara mencari sponsor dan menjalin kerjasama yang baik dengan pihak luar",  
                "pesan" : "Semoga kakak selalu diberi kemudahan dalam menjalankan tugas perkuliahan dan organisasi."
            },
            {
                "nama"  : "Alvia Asrinda Br.Gintng",
                "nim"   : "122450077",
                "umur"  : "20",
                "asal"  : "Binjai",
                "alamat": "Korpri",
                "hobbi" : "Nonton Winda",
                "sosmed": "@alviagnting",
                "kesan" : "Sharing pengalaman kakak tentang strategi pendekatan ke calon sponsor sangat bermanfaat dan membuka wawasan baru",  
                "pesan" : "Tetap jaga kesehatan kak di tengah kesibukan kuliah dan organisasi. Semoga sukses selalu dalam setiap langkah!"
            },
            {
                "nama"  : "Dhafin Razaqa Luthfi",
                "nim"   : "122450133",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi" : "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan" : "Abang memberikan insight yang sangat berharga tentang teknik negosiasi dan cara meyakinkan sponsor untuk bekerjasama",  
                "pesan" : "Semoga abang selalu diberikan kelancaran dalam menyelesaikan studi dan amanah di organisasi. Terus berbagi ilmu yang bermanfaat!"
            },
            {
                "nama"  : "Elia Meylani Simanjuntak",
                "nim"   : "122450026",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Korpri",
                "hobbi" : "Main Alat Musik",
                "sosmed": "@meylanielia",
                "kesan" : "Kakak sangat detail dalam menjelaskan proses pembuatan proposal sponsorship yang menarik dan profesional",  
                "pesan" : "Semoga kakak selalu diberi kesehatan dan kemudahan dalam menggapai cita-cita. Terima kasih atas ilmu yang dibagikan!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()    
# Tambahkan menu lainnya sesuai kebutuhan
