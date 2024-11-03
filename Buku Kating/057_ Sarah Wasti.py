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
            "https://drive.google.com/uc?export=view&id=1FC0o-0-4tSDVLPYCJK2GheYdEXN9Ixsv",
            "https://drive.google.com/uc?export=view&id=1ZvUYRbEPxpN20VoRnerU7v9wwQ3jpbMe",
            "https://drive.google.com/uc?export=view&id=1K5L7UYfcYg2JLSv3CBMGZwUNYmuCJlbB",
            "https://drive.google.com/uc?export=view&id=11A3TriXDF-MGKaSaNy9c6LnDDW0-vRK9",
            "https://drive.google.com/uc?export=view&id=1eQdjCP-ZP7YoL3h3DhUQLKEYHXtSycBm",
            "https://drive.google.com/uc?export=view&id=17VP3i6VgnlJzYBUl3U1dJJqglnoIF2nD",
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
                "kesan" : "Sangat informatif saat menjelaskan berbagai kegiatan dalam organisasi",  
                "pesan" : "Tetap semangat dan terus menginspirasi banyak orang!  "
            },
            {
                "nama"  : "Pandra Insani Putra Azwan",
                "nim"   : "121450137",
                "umur"  : "21",
                "asal"  : "Bukit Kemuning, Lampung Utara",
                "alamat": "Bawen 2",
                "hobbi" : "Bermain gitar dan menyanyi",
                "sosmed": "@pandrainsni27",
                "kesan" : "Baik dan mengasyikkan",  
                "pesan" : "Semoga makin hebat dan berkembang.  "
            },
            {
                "nama"  : "Meliza Wulandari",
                "nim"   : "121450065",
                "umur"  : "20",
                "asal"  : "Pagar Alam, Sumatera Selatan",
                "alamat": "Kotabaru",
                "hobbi" : "Nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan" : " informasi yang diberikan sangat jelas dan mudah dipahami.  ",  
                "pesan" : "Semoga masa depan selalu cerah dan bahagia.  "
            },
            {
                "nama"  : "Putri Maulida Chairani",
                "nim"   : "121450050",
                "umur"  : "21",
                "asal"  : "Payakumbuh, Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi" : "Dengerin bang pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan" : "Bisa menyelesaikan masalah dengan cepat dan efektif.  ",  
                "pesan" : "Terus tambah ilmu dan pengalaman.  "
            },
            {
                "nama"  : "Hartiti Fadilah",
                "nim"   : "121450031",
                "umur"  : "21",
                "asal"  : "Palembang",
                "alamat": "Pemda",
                "hobbi" : "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan" : "Selalu memotivasi teman-teman untuk lebih semangat.  ",  
                "pesan" : "Tetap rendah hati meskipun makin sukses.  "
            },
            {
                "nama"  : "Nadilla Andara Putri",
                "nim"   : "121450003",
                "umur"  : "21",
                "asal"  : "Metro",
                "alamat": "KotaBaru",
                "hobbi" : "Membaca",
                "sosmed": "@ndillaandr26",
                "kesan" : "Semangat dalam berorganisasi sangat menginspirasi.  ",  
                "pesan" : "Teruslah jadi teladan bagi yang lain.  "
            }
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1rxqb-OqWtJntjnSwxinZfyYHU7wKN-bi",
            "https://drive.google.com/uc?export=view&id=1c6m03MGoE0Kqt5U33GUH4mB83cSARTxb",
            "https://drive.google.com/uc?export=view&id=1hAcluyoZcHOU8_7-wH0hIkQYXoZlYwst",
            "https://drive.google.com/uc?export=view&id=1knSocyRB6XgJOT11SC_643f7Z4mXa3lV",
            "https://drive.google.com/uc?export=view&id=1MPBwBHbjJLmlRqoAv-FUN0O9vPiYN0Jz",
            "https://drive.google.com/uc?export=view&id=1Xj22CiSViRFDkS85UdDTSf8WLjkwqESm",
            "https://drive.google.com/uc?export=view&id=1_uToG0XQjllKnKdPPaWUgG-K2dBn3qoW",
            "https://drive.google.com/uc?export=view&id=1rD9X1LDjMyq_1W8UYnpzAUlyvIu0Fig5",
            "https://drive.google.com/uc?export=view&id=1D-yixrP26gEsuZ__7UY67JQyY5haPe2P",
            "https://drive.google.com/uc?export=view&id=1CqURnu7K8GUMnr3qWhZk_PwyrSkO7CZ3",
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
                "kesan" : "Mampu membuat suasana jadi seru dan menyenangkan",  
                "pesan" : "Semoga makin hebat dan berkembang"
            },
            {
                "nama"  : "Annisa Cahyani Surya",
                "nim"   : "121450114",
                "umur"  : "21",
                "asal"  : "Tanggerang Selatan",
                "alamat": "Way Huwi",
                "hobbi" : "Membaca, Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan" : "Memberikan banyak pelajaran berharga tentang organisasi",  
                "pesan" : "Semoga masa depan selalu cerah dan bahagia"
            },
            {
                "nama"  : "Wulan Sabina",
                "nim"   : "121450150",
                "umur"  : "21",
                "asal"  : "Medan",
                "alamat": "Raden Saleh",
                "hobbi" : "Nonton Drakor",
                "sosmed": "@wlnsbn0",
                "kesan" : "informasi yang diberikan sangat jelas dan mudah dipahami",  
                "pesan" : "Semoga semua cita-cita tercapai"
            },
            {
                "nama"  : "Annisa Dini Amaliya",
                "nim"   : "121450081",
                "umur"  : "21",
                "asal"  : "Tanggerang",
                "alamat": "Jati Agung",
                "hobbi" : "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan" : "Memiliki jiwa kepemimpinan yang kuat dan menginspirasi",  
                "pesan" : "Teruslah jadi teladan bagi yang lain"
            },
            {
                "nama"  : "Anisa Fitriyani",
                "nim"   : "121450150",
                "umur"  : "21",
                "asal"  : "Medan",
                "alamat": "Raden Saleh",
                "hobbi" : "Nonton Drakor",
                "sosmed": "@wlnsbn0",
                "kesan" : "Selalu memotivasi teman-teman untuk lebih semangat",  
                "pesan" : "Semoga selalu dikelilingi orang-orang baik"
            },
            {
                "nama"  : "Mirzan Yusuf Rabbani",
                "nim"   : "122450118",
                "umur"  : "20",
                "asal"  : "Jakarta",
                "alamat": "Korpri",
                "hobbi" : "Main Kucing",
                "sosmed": "@myrrinn",
                "kesan" : "Baik dan mengasyikkan",  
                "pesan" : "Semoga selalu semangat dalam segala hal!"
            },
            {
                "nama"  : "Dhea Amelia Putri",
                "nim"   : "122450004",
                "umur"  : "20",
                "asal"  : "Sukabumi, Jawa Barat",
                "alamat": "Natar",
                "hobbi" : "Suka Ikut Tes SKD",
                "sosmed": "@dhea_wedding",
                "kesan" : "Ramah dan tidak membuat orang lain merasa sungkan",  
                "pesan" : "Semoga selalu produktif dan berhasil"
            },
            {
                "nama"  : "Muhammad Fahrul Aditya",
                "nim"   : "121450156",
                "umur"  : "22",
                "asal"  : "Surakarta, Jawa Tengah",
                "alamat": "Pahoman",
                "hobbi" : "Melukis, badminton, hiking, ngopi, dengerin music, nonton film dan ngoding",
                "sosmed": "@fhrul.pdf",
                "kesan" : "Bisa menyelesaikan masalah dengan cepat dan efektif",  
                "pesan" : "Semoga perjalanan selalu diberi kelancaran"
            },
            {
                "nama"  : "Berlianda Enda Putri",
                "nim"   : "122450065",
                "umur"  : "21",
                "asal"  : "Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi" : "Main Game",
                "sosmed": "@berlyyanda",
                "kesan" : "Mudah diajak bicara dan sangat terbuka",  
                "pesan" : "Semoga setiap langkah selalu diberi kemudahan dan keberhasilan"
            },
            {
                "nama"  : "Jeremia Susanto",
                "nim"   : "122450022",
                "umur"  : "20",
                "asal"  : " Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi" : "Marah-marah",
                "sosmed": "@jeremia_s_",
                "kesan" : "Selalu aktif dan terlibat di setiap kegiatan",  
                "pesan" : "Teruslah jadi teladan bagi yang lain"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1CSsEA0-NWvuNOVxvc7jsZfwqxMSRgdZg", #kak lutfi
            "https://drive.google.com/uc?export=view&id=15MRLcffUlDsarELQERBs_zVligThYCAK", #bang bintang
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
                "kesan" : "Memiliki jiwa kepemimpinan yang kuat dan menginspirasi",  
                "pesan" : "Terus tambah ilmu dan pengalaman"
            },
            {
                "nama"  : "Rian Bintang Wijaya",
                "nim"   : "122450094",
                "umur"  : "20",
                "asal"  : "Palembang, Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi" : "Mendengar Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan" : "Memberikan banyak pelajaran berharga tentang organisasi",  
                "pesan" : "Semoga bisa jadi pemimpin hebat nanti"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=15G5gWwqZ_i3P91T0U3kGPHUvm9gSPrry", #bang erickson dn
            "https://drive.google.com/uc?export=view&id=1317np3cGoLXKwb4hTgWxGUCKFXH_zifP", #kak abeth dn
            "https://drive.google.com/uc?export=view&id=19HXwQ17-H-zxOWmvy4ofKxTn2cd6ER13", #kak afifah dn
            "https://drive.google.com/uc?export=view&id=19B2VS3abmnrClvfdLapqfkHC4ijGv1g2", #kak allya dn
            "https://drive.google.com/uc?export=view&id=18ynFqgoQvLtkhYF0IyNHL3CCGSnHNfEg", #kak hanum dn
            "https://drive.google.com/uc?export=view&id=18zGbuZLe2ZXTOfKaGYEjK2rx5R207iPw", #bang ferdy dn
            "https://drive.google.com/uc?export=view&id=18zwo5YLJpFvwfKD6QbMmcUSMt9KRkLsc", #bang deri dn
            "https://drive.google.com/uc?export=view&id=18vUVGasuQGoseCzdb60TIX8MDBJPno7y", #kak oktavia dn
            "https://drive.google.com/uc?export=view&id=18iBGTdpxm5O9Gzq9j_m0O1NxEmy3OJ-i", #bang deyvan dn
            "https://drive.google.com/uc?export=view&id=18LJFuV51EAgu2w_g_H0c4vXSoRHHsGi2", #bang ibnu dn
            "https://drive.google.com/uc?export=view&id=18huF9kPMSzcCdLWHWAjKDfpHjw-ffXFe", #bang jo dn
            "https://drive.google.com/uc?export=view&id=18WkbFNnpl1tcvrJCw0FYJZMIchf35eFm", #bang kemas dn
            "https://drive.google.com/uc?export=view&id=18650__CX7w3w93FrE-2MJfZXnjr5VYPl", #bang leonard dn
            "https://drive.google.com/uc?export=view&id=17zQAMk5LOcE7vOvtVdtvEYQ2pFyI6KQr", #kak presilia dn
            "https://drive.google.com/uc?export=view&id=18GdFd1GQeVcNvjxwGgPBvGKEOMa_a5AE", #kak rafa dn
            "https://drive.google.com/uc?export=view&id=18GbgQya1pc6mSMBr1hbknyWIjxn9jc_A", #bang sahid dn
            "https://drive.google.com/uc?export=view&id=183S3i_Mg8yFnYRVQC15VvJ9mQotN7cKP", #kak vanes dn
            "https://drive.google.com/uc?export=view&id=19PyAvkJlPXtevYTNr4Lztv2Khb8XFNhw", #bang ateng dn
            "https://drive.google.com/uc?export=view&id=19rqKEL2LvSjwDILmKVKVZ5zYkhQ7cgm2", #kak jaclin dn
            "https://drive.google.com/uc?export=view&id=19N9RjDPtdzbtpx2mb1IQPAR9YeXnQ-yr", #bang rafly dn
            "https://drive.google.com/uc?export=view&id=19saoChO8I3FoQ0gNlaO98EB3Ldn5vAHG", #kak dini dn

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
                "kesan" : "Selalu memotivasi teman-teman untuk lebih semangat",  
                "pesan" : "Semoga selalu produktif dan berhasil"
            },
            {
                "nama"  : "Elisabeth Claudia Simanjuntak",
                "nim"   : "122450123",
                "umur"  : "18",
                "asal"  : "Pekanbaru",
                "alamat": "Sukarame",
                "hobbi" : "Memancing keributan",
                "sosmed": "@celisabethh_",
                "kesan" : "informasi yang diberikan sangat jelas dan mudah dipahami",  
                "pesan" : "Terus tambah ilmu dan pengalaman"
            },
            {
                "nama"  : "Nisrina Nur Afifah",
                "nim"   : "122450052",
                "umur"  : "19",
                "asal"  : "Bekasi",
                "alamat": "Sukarame",
                "hobbi" : "Nabok orang",
                "sosmed": "@afifahhnsrn",
                "kesan" : "Mudah diajak bicara dan sangat terbuka",  
                "pesan" : "Tetap sukses dalam studi dan karier"
            },
            {
                "nama"  : "Allya Nurul Islami Pasha",
                "nim"   : "122450033",
                "umur"  : "20",
                "asal"  : "Sumatera Barat",
                "alamat": "Gang Perwira, Belwis",
                "hobbi" : "Nonton Dracin",
                "sosmed": "@allyaislami_",
                "kesan" : "Bisa menyelesaikan masalah dengan cepat dan efektif.",  
                "pesan" : "Semoga masa depan selalu cerah dan bahagia"
            },
            {
                "nama"  : "Farahanum Afifah Ardiansyah",
                "nim"   : "122450056",
                "umur"  : "20",
                "asal"  : "Padang, Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi" : "Tidur",
                "sosmed": "@farahanumafifahh",
                "kesan" : "Ramah dan tidak membuat orang lain merasa sungkan",  
                "pesan" : "Semoga selalu diberkahi dalam segala usaha"
            },
            {
                "nama"  : "Ferdy Kevin Naibaho",
                "nim"   : "122450107",
                "umur"  : "19",
                "asal"  : "Medan, Sumatera Utara",
                "alamat": "Jalan Senopati Raya 18",
                "hobbi" : "Dengerin Rocky Gerung",
                "sosmed": "@ferdy_kevin",
                "kesan" : "Baik dan mengasyikkan",  
                "pesan" : "Semoga semua kebaikan selalu dibalas"
            },
            {
                "nama"  : "M. Deriansyah Okutra",
                "nim"   : "122450101",
                "umur"  : "19",
                "asal"  : "Kayu Agung",
                "alamat": "Jalan Pagar Alam",
                "hobbi" : "Bercerita horror",
                "sosmed": "@dransyh_",
                "kesan" : "Mudah diajak bicara dan sangat terbuka",  
                "pesan" : "Tetap rendah hati meskipun makin sukses"
            },
            {
                "nama"  : "Oktavia Nurwenda Puspita Sari",
                "nim"   : "122450041",
                "umur"  : "20",
                "asal"  : "Lampung Timur",
                "alamat": "Way Hui",
                "hobbi" : "Memasak",
                "sosmed": "@_oktavianrwnda_",
                "kesan" : "Selalu memotivasi teman-teman untuk lebih semangat",  
                "pesan" : "Semoga selalu produktif dan berhasil"
            },
            {
                "nama"  : "Deyvan Loxefal",
                "nim"   : "121450148",
                "umur"  : "21",
                "asal"  : "Riau",
                "alamat": "Pulau Damar",
                "hobbi" : "Belajar",
                "sosmed": "@depanloo",
                "kesan" : "Selalu memotivasi teman-teman untuk lebih semangat",  
                "pesan" : "Semoga makin hebat dan berkembang"
            },
            {
                "nama"  : "Ibnu Farhan Al-Ghifari",
                "nim"   : "121450121",
                "umur"  : "21",
                "asal"  : "Jambi",
                "alamat": "Pulau Damar, Kobam",
                "hobbi" : "Bermain Game Online",
                "sosmed": "@al_ghifari032",
                "kesan" : "informasi yang diberikan sangat jelas dan mudah dipahami",  
                "pesan" : "Semoga masa depan selalu cerah dan bahagia"
            },
             {
                "nama"  : "Johannes Krisjon Silitonga",
                "nim"   : "122450043",
                "umur"  : "19",
                "asal"  : "Tanggerang",
                "alamat": "Jalan Lapas",
                "hobbi" : "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan" : "Semangat dalam berorganisasi sangat menginspirasi",  
                "pesan" : "Semoga semua cita-cita tercapai"
            },
            {
                "nama"  : "Kemas Veriandra Ramadhan",
                "nim"   : "122450016",
                "umur"  : "19",
                "asal"  : "Bekasi",
                "alamat": "Golf Asri",
                "hobbi" : "Bermain ular python digital",
                "sosmed": "@kemasverii",
                "kesan" : "Sangat informatif saat menjelaskan sesuatu",  
                "pesan" : "Terus tambah ilmu dan pengalaman"
            },
            {
                "nama"  : "Leonard Andreas Napitupulu",
                "nim"   : "121450153",
                "umur"  : "21",
                "asal"  : "Sumatera Utara",
                "alamat": "Kobam",
                "hobbi" : "Belajar",
                "sosmed": "@lnrd.__",
                "kesan" : "informasi yang diberikan sangat jelas dan mudah dipahami",  
                "pesan" : "Semoga semua kebaikan selalu dibalas"
            },
            {
                "nama"  : "Presilia",
                "nim"   : "122450081",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Kota Baru",
                "hobbi" : "Tidur",
                "sosmed": "@presiliamg",
                "kesan" : "Semangat dalam berorganisasi sangat menginspirasi",  
                "pesan" : "Semoga makin hebat dan berkembang"
            },
            {
                "nama"  : "Rafa Aqilla Jungjunan",
                "nim"   : "122450148",
                "umur"  : "20",
                "asal"  : "Riau",
                "alamat": "Belwis",
                "hobbi" : "Membaca webtoon",
                "sosmed": "@rafaaqilla",
                "kesan" : "Selalu memotivasi teman-teman untuk lebih semangat",  
                "pesan" : "Terus jadi sumber semangat bagi orang lain"
            },
            {
                "nama"  : "Sahid Maulana",
                "nim"   : "122450109",
                "umur"  : "21",
                "asal"  : "Depok, Jawa Barat",
                "alamat": "Airan Raya",
                "hobbi" : "Bermain Game",
                "sosmed": "@sahid_maul19",
                "kesan" : "Sangat menginspirasi dalam kehidupan",  
                "pesan" : "Bisa menyelesaikan masalah dengan cepat dan efektif"
            },
            {
                "nama"  : "Vanessa Olivia Rose",
                "nim"   : "121450068",
                "umur"  : "20",
                "asal"  : "Jakarta",
                "alamat": "Perumahan Korpri",
                "hobbi" : "Belajar",
                "sosmed": "@roselivnes__",
                "kesan" : "Memberikan banyak pelajaran berharga tentang organisasi",  
                "pesan" : "Semoga selalu diberkahi dalam segala usaha"
            },
            {
                "nama"  : "M. Farhan Athaulloh",
                "nim"   : "121450117",
                "umur"  : "21",
                "asal"  : "Bandar Lampung",
                "alamat": "Kota Baru",
                "hobbi" : "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan" : "Sangat membantu dalam menjelaskan informasi",  
                "pesan" : "Semoga perjalanan selalu diberi kelancaran"
            },
            {
                "nama"  : "Jaclin Alcavella",
                "nim"   : "122450015",
                "umur"  : "19",
                "asal"  : "Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi" : "Berenang",
                "sosmed": "@jaclinalcv_",
                "kesan" : "Murah senyum dan mengasyikkan",  
                "pesan" : "Semangat kak dalam menjalani hari-harinya, semoga urusannya dalam dunia perkuliahan dapat diselesaikan dengan mudah"
            },
            {
                "nama"  : "Rafly Prabu Darmawan",
                "nim"   : "122450140",
                "umur"  : "20",
                "asal"  : "Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi" : "Main Game",
                "sosmed": "@raflyy_pd2684",
                "kesan" : "Semangat dalam berorganisasi sangat menginspirasi",  
                "pesan" : "Semoga kebaikan selalu berlipat ganda."
            },
            {
                "nama"  : "Syalaisha Andini Putriansyah",
                "nim"   : "122450111",
                "umur"  : "21",
                "asal"  : "Tanggerang",
                "alamat": "Sukarame",
                "hobbi" : "Membaca",
                "sosmed": "@syalaisha.i__",
                "kesan" : "Ramah dan tidak membuat orang lain merasa sungkan",  
                "pesan" : "Semoga karier makin cemerlang ke depannya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1Hbo0qAGTd4HffVVAJmPgUITABetAGSta", #kak anisa dn
            "https://drive.google.com/uc?export=view&id=1HGhcMhE_--xP55CfUBIHOTe5_w1-04QY", #bang ahmad dn
            "https://drive.google.com/uc?export=view&id=1HU4PAGuR7OZxKM9VF1M-4UFyxluvJlTa", #bang fadhil dn
            "https://drive.google.com/uc?export=view&id=1HUG0GwuywRv-ELRPhWYo3Hkv4o4NEQKm", #kak dina dn
            "https://drive.google.com/uc?export=view&id=1HdrrEeseiuh6jLtSR7St_cgM8u5MYGng", #kak dinda dn
            "https://drive.google.com/uc?export=view&id=1HWMoNkzyFfJuE14nTkMcu9mrf1DElMgM", #kak marleta dn
            "https://drive.google.com/uc?export=view&id=1Hm8-P6pXiHDKQS_wyawAhdypb5WeW8oO", #kak rut junita dn
            "https://drive.google.com/uc?export=view&id=1Hegb855X9PNZiPUhzWR7ENb66Bq3PZip", #kak syadza dn
            "https://drive.google.com/uc?export=view&id=1HeH8oXF5QhsnBo86_JLvFjC5W5w45Ka9", #kak febiya dn
            "https://drive.google.com/uc?export=view&id=1HSX_Mdw8AHtMO-GDLLouRGOqU3Mc07ch", #kak happy syahrul dn
            "https://drive.google.com/uc?export=view&id=1HTagRSousqsesIXAp7JVWgLWzaiH3Qjo", #bang randa dn

        ]
        data_list = [
            {
                "nama"  : "Annisa Novantika",
                "nim"   : "121450005",
                "umur"  : "21",
                "asal"  : "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi" : "Memasak",
                "sosmed": "@anovavona",
                "kesan" : "Sangat baik, informatif dalam menerangkan suatu permasalahan dan sangat menginspirasi",  
                "pesan" : "Tetap semangat kak dalam menjalani harinya, semoga urusannya baik di akademik maupun non akademik dapat berjalan dengan lancar"
            },
            {
                "nama"  : "Ahmad Sahidin Akbar",
                "nim"   : "122450044",
                "umur"  : "20",
                "asal"  : "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi" : "Olahraga",
                "sosmed": "@sahid22__",
                "kesan" : "Sangat informatif dalam menjelaskan sesuatu dan banyak memberikan motivasi",  
                "pesan" : "Semoga kegiatannya di dalam maupun di luar perkuliahan tetap lancar dan tetap semangat kak"
            },
            {
                "nama"  : "Fadhil Fitra Wijaya",
                "nim"   : "122450082",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Teluk Betung",
                "hobbi" : "Main game",
                "sosmed": "@fadhilfwee",
                "kesan" : "Sangat baik, informatif dalam menerangkan suatu permasalahan dan sangat menginspirasi",  
                "pesan" : "Tetap semangat kak dalam menjalani harinya, semoga urusannya baik di akademik maupun non akademik dapat berjalan dengan lancar"
            },
            {
                "nama"  : "Syalaisha Andina Putriansyah",
                "nim"   : "122450121",
                "umur"  : "21",
                "asal"  : "Tangerang",
                "alamat": "Gang Yudhistira",
                "hobbi" : "Baca jurnal",
                "sosmed": "@dkselsd_31",
                "kesan" : "Sangat informatif dalam menerangkan sesuatu dan sangat menginspirasi",  
                "pesan" : "Semoga selalu dilancarkan semua urusannya kak, jangan lupa untuk tetap semangat kak dalam menjalani kehidupan"
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
                "kesan" : "Sangat menginspirasi dalam kehidupan ",  
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
                "kesan" : "Sangat baik dan sangat mengasyikkan ",  
                "pesan" : "Semangat terus kak dalam menjalani perkuliahannya serta jangan lupa untuk jaga kesehatan"
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
            "https://drive.google.com/uc?export=view&id=1EYVPRjGGN2UqCXMImbRTxBQNbJQj_ZPB", #bang wahyu dn
            "https://drive.google.com/uc?export=view&id=1DymZqnFdZHlz--TD2LXtmuE-SAr9-dCg", #kak elok dn
            "https://drive.google.com/uc?export=view&id=1EZigzqqgL2k9lZTmzvZrgzDsv2qOPlRP", #kak arsyiah dn
            "https://drive.google.com/uc?export=view&id=1iZCVODlHOPMrxfEH6NAhE6GVtkb9__ro", #kak cintya dn
            "https://drive.google.com/uc?export=view&id=1EE94AVHOpZG_qSZfj8Y2YpBXkLtPv0sN", #kak najla dn
            "https://drive.google.com/uc?export=view&id=14GMJ0OGre2CDZUGnvA5jhrjIKMBtQ7cF", #kak rahma dn
            "https://drive.google.com/uc?export=view&id=1ELFjZ2_kMnXxJPmU7me-6WWVHe3e_vTK", #kak try yani dn
            "https://drive.google.com/uc?export=view&id=1ETtJjULpaUtR8djdYLgo1_44gL52iZC-", #bang kaisar dn
            "https://drive.google.com/uc?export=view&id=1Dxnyf0RZIVokRPOPrQ7kZr-dRn52Oyze", #kak dwi dn
            "https://drive.google.com/uc?export=view&id=1ERkAQj0G-Znq1BYKWiWen03El64JU956", #bang gym dn
            "https://drive.google.com/uc?export=view&id=1EY_2XJRBZ3RhLw6XmsQsQTiXbfj6qpBR", #kak nasywa dn
            "https://drive.google.com/uc?export=view&id=1EG8SrWwNq-81Jl_PhyaUrftzAb-5Vqfo", #kak priska dn
            "https://drive.google.com/uc?export=view&id=1Ef5FXmWWT0wj9T5nCEd65aoyh5Qr3trl", #bang arsal dn
            "https://drive.google.com/uc?export=view&id=1EnkLXwUAlRGieym8ZJjJc8yI5FR3po2L", #bang abit dn
            "https://drive.google.com/uc?export=view&id=1EhD2-zwHU-FHi5FvmKSiuyahIGgyyHaD", #bang akmal dn
            "https://drive.google.com/uc?export=view&id=1EkD-jdKuwzenCXVY3LFnA8aFZxdQU8HT", #bang hermawan dn
            "https://drive.google.com/uc?export=view&id=1Tqb5oGKYjxkC2dWk5y2snAlfuBSe5nRP", #kak nisa dn
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
                "kesan" : "Selalu baik dan ramah kepada semua orang",  
                "pesan" : "Semoga selalu sukses ke depannya"
            },
            {
                "nama"  : "Elok Fiola",
                "nim"   : "122450051",
                "umur"  : "19",
                "asal"  : "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi" : "Editing",
                "sosmed": "@elokfiola",
                "kesan" : "Sangat informatif saat menjelaskan berbagai kegiatan dalam organisasi",  
                "pesan" : "Tetap semangat dan terus menginspirasi banyak orang!"
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
                "kesan" : "Ramah dan tidak membuat orang lain merasa sungkan",  
                "pesan" : "Semoga makin hebat dan berkembang"
            },
            {
                "nama"  : "Najla Juwairia",
                "nim"   : "122450037",
                "umur"  : "19",
                "asal"  : "Sumatera Utara",
                "alamat": "Airan",
                "hobbi" : "Menulis, Membaca, Fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan" : "Semangat dalam berorganisasi sangat menginspirasi",  
                "pesan" : "Terus tambah ilmu dan pengalaman"
            },
            {
                "nama"  : "Rahma Neliyana",
                "nim"   : "122450036",
                "umur"  : "20",
                "asal"  : "Lampung",
                "alamat": "Sukarame",
                "hobbi" : "Baca Coding",
                "sosmed": "@rahmanellyana",
                "kesan" : "Selalu aktif dan terlibat di setiap kegiatan",  
                "pesan" : "Semoga selalu semangat dalam segala hal!"
            },
            {
                "nama"  : "Try Yani Rizki Nur Rohmah",
                "nim"   : "122450020",
                "umur"  : "20",
                "asal"  : "Lampung Barat",
                "alamat": "Korpri",
                "hobbi" : "Bernyanyi dan Menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan" : "informasi yang diberikan sangat jelas dan mudah dipahami",  
                "pesan" : "Tetap sukses dalam studi dan karier"
            },
            {
                "nama"  : "Muhammad Kaisar Firdaus",
                "nim"   : "121450135",
                "umur"  : "21",
                "asal"  : "Pesawaran",
                "alamat": "Pulau Damar",
                "hobbi" : "Lagi nyari",
                "sosmed": "@dino_lapet",
                "kesan" : "Mampu membuat suasana jadi seru dan menyenangkan",  
                "pesan" : "Teruslah jadi teladan bagi yang lain"
            },
            {
                "nama"  : "Dwi Ratna Anggraeni",
                "nim"   : "122450008",
                "umur"  : "20",
                "asal"  : "Jambi",
                "alamat": "Jalan Durian 5 Pemda",
                "hobbi" : "Membaca",
                "sosmed": "@dwiratnn_",
                "kesan" : "Selalu memotivasi teman-teman untuk lebih semangat",  
                "pesan" : "Semoga selalu diberkahi dalam segala usaha"
            },
            {
                "nama"  : "Gymnastiar Al Khoarizmy",
                "nim"   : "122450096",
                "umur"  : "20",
                "asal"  : "Serang",
                "alamat": "Lapangan Golf UIN",
                "hobbi" : "Baca komik",
                "sosmed": "@jimnn.as",
                "kesan" : "Mudah diajak bicara dan sangat terbuka.",  
                "pesan" : "Semoga semua cita-cita tercapai"
            },
             {
                "nama"  : "Nasywa Nur Afifah",
                "nim"   : "122450125",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Jalan Durian 1 Pemda",
                "hobbi" : "Nonton drakor",
                "sosmed": "@nsywanaf",
                "kesan" : "Memberikan banyak pelajaran berharga tentang organisasi",  
                "pesan" : "Semoga masa depan selalu cerah dan bahagia"
            },
            {
                "nama"  : "Priska Silvia Ferantiana",
                "nim"   : "122450053",
                "umur"  : "19",
                "asal"  : "Palembang",
                "alamat": "Jalan Nangka 2",
                "hobbi" : "Baca novel yang bikin nangis",
                "sosmed": "@prskslv",
                "kesan" : "Memiliki jiwa kepemimpinan yang kuat dan menginspirasi",  
                "pesan" : "Tetap konsisten dan terus berprestasi"
            },
            {
                "nama"  : "Muhammad Arsal Ranjana Utama",
                "nim"   : "121450111",
                "umur"  : "21",
                "asal"  : "Depok",
                "alamat": "Jalan Nangka 4",
                "hobbi" : "Ngoding",
                "sosmed": "@arsal.utama",
                "kesan" : "Bisa menyelesaikan masalah dengan cepat dan efektif",  
                "pesan" : "Semoga bisa jadi pemimpin hebat nanti"
            },
            {
                "nama"  : "Abit Ahmad Oktarian",
                "nim"   : "122450042",
                "umur"  : "19",
                "asal"  : "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi" : "Ngoding, Gaming",
                "sosmed": "@abitahmad",
                "kesan" : "Selalu memberi semangat agar tidak mudah menyerah",  
                "pesan" : "Semoga selalu sehat dan bersemangat"
            },
            {
                "nama"  : "Akmal Faiz Abdillah",
                "nim"   : "122450114",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi" : "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan" : "Baik dan mengasyikkan",  
                "pesan" : "Terus berbagi ilmu dan pengalaman dengan yang lain"
            },
            {
                "nama"  : "Hermawan Manurung",
                "nim"   : "122450069",
                "umur"  : "20",
                "asal"  : "Bogor",
                "alamat": "Dekat jalan tol, Wisma Hana Hani",
                "hobbi" : "Bengong dan membaca buku",
                "sosmed": "@hermawan.mnrng",
                "kesan" : "Ramah dan suka membantu",  
                "pesan" : "Semoga semua kebaikan selalu dibalas"
            },
            {
                "nama"  : "Khusnun Nisa",
                "nim"   : "122450078",
                "umur"  : "20",
                "asal"  : "Lampung Selatan",
                "alamat": "Belwis",
                "hobbi" : "Mengerjakan tugas",
                "sosmed": "@khusnun_nisa335",
                "kesan" : "Murah senyum dan informatif dalam menjelaskan",  
                "pesan" : "Semoga selalu produktif dan berhasil"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=16sdGgLRlge4iPT2_DnkR6AgJD7pkij7y", #bang yogy dn
            "https://drive.google.com/uc?export=view&id=16pzCxl4NGJYR8FN1qDcJV_zlsQaqte8w", #kak ramadhita dn
            "https://drive.google.com/uc?export=view&id=17-3vbBVgnMyWVunpnmoKkJ-2Cz9_OnHD", #kak nazwa dn
            "https://drive.google.com/uc?export=view&id=16yN0tJYcGj6E95T1xZdNeIQrr4erGNgU", #bang bastian dn
            "https://drive.google.com/uc?export=view&id=173sRsfB_gjdutcgsjM4U0oUJLKpKlvZy", #kak dea dn
            "https://drive.google.com/uc?export=view&id=17-pmeEWHtyaGrrHfqrrKFKax_39-x9yI", #kak esteria dn
            "https://drive.google.com/uc?export=view&id=17309Qi7sVDFxBMbzj4Sj0mYOXXICFxXm", #kak natasya ega dn
            "https://drive.google.com/uc?export=view&id=16zghz-S7zeIHT0ELOjBrOM6ZllF1QCKd", #kak novelia dn
            "https://drive.google.com/uc?export=view&id=16p7rmYQ5g9vovwaF_9p4oUP2VPNAIJqD", #kak jasmine dn
            "https://drive.google.com/uc?export=view&id=16zJ8JfLRK8ZuNTMPQPtE2WNoO5e12nJu", #bang tobias dn
            "https://drive.google.com/uc?export=view&id=174UbMIUTcj-J8onBo5LBzk1087ne52J9", #kak yohana dn
            "https://drive.google.com/uc?export=view&id=17OqnEatY-K892dqejHSaW6sJhUKZSNNl", #bang rizki dn
            "https://drive.google.com/uc?export=view&id=16pr-bZlwHw07t1ntxlHEnS2wIObxuFa9", #bang arafi dn
            "https://drive.google.com/uc?export=view&id=17DcqG0kUgDOchmktI6wxg16-i9AHJtOQ", #kak uyi dn
            "https://drive.google.com/uc?export=view&id=1768qC5FG1FS3cYefADL2DZI7SmBu1Tvf", #kak chalifia dn
            "https://drive.google.com/uc?export=view&id=16slsqUPL8qmfeeHc1kAkknMLrOhvj10X", #bang irvan dn
            "https://drive.google.com/uc?export=view&id=16wrCcLUKtl2w2VfJSu7_ETmtgPDMud7W", #kak izza dn
            "https://drive.google.com/uc?export=view&id=16w2E3zZsagZZ1w9A1OtLm2Q4b036GJLw", #kak zuhrah dn
            "https://drive.google.com/uc?export=view&id=16v_jGDyIk2MSoSQoNOFsG2tdWqsec_eU", #kak tria dn
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
                "kesan" : "Memberikan banyak pelajaran berharga tentang organisasi",  
                "pesan" : "Tetap sukses dalam studi dan karier"
            },
            {
                "nama"  : "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan" : "Selalu aktif dan terlibat di setiap kegiatan",  
                "pesan" : "Semoga selalu sehat dan bersemangat"
            },
            {
                "nama"  : "Nazwa Nabilla",
                "nim": "121450122",
                "umur": "21 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Way kandis",
                "hobbi": "Belajar",
                "sosmed": "@nazwanbilla",
                "kesan" : "Bisa menyelesaikan masalah dengan cepat dan efektif",  
                "pesan" : "Semoga selalu dikelilingi orang-orang baik"
            },
            {
                "nama"  : "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21 Tahun",
                "asal": "Batam, Kepulauan Riau",
                "alamat": "Belwis",
                "hobbi": "Main game",
                "sosmed": "@bastiansilaban_",
                "kesan" : "Selalu memotivasi teman-teman untuk lebih semangat",  
                "pesan" : "Semoga tetap kompak dan solid bersama tim"
            },
            {
                "nama"  : "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20 Tahun",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Dengerin musik",
                "sosmed": "@deaa.rsn",
                "kesan" : "Selalu memberi semangat agar tidak mudah menyerah",  
                "pesan" : "Jangan berhenti berkarya dan berinovasi"
            },
            {
                "nama"  : "Esteria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "19 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Belwis",
                "hobbi": "Main golf bareng kadiv",
                "sosmed": "@esteriars",
                "kesan" : "Semangat dalam berorganisasi sangat menginspirasi",  
                "pesan" : "Terus jadi sumber semangat bagi orang lain"
            },
            {
                "nama"  : "Natasya Ega Lina",
                "nim": "122450024",
                "umur": "19 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Belwis",
                "hobbi": "Jadi humas",
                "sosmed": "@nateee__15",
                "kesan" : "Mudah diajak bicara dan sangat terbuka",  
                "pesan" : "Semoga kebaikan selalu berlipat ganda"
            },
            {
                "nama"  : "Novelia Adinda",
                "nim": "122450104",
                "umur": "21 Tahun",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan" : "Memiliki jiwa kepemimpinan yang kuat dan menginspirasi",  
                "pesan" : "Semoga perjalanan selalu diberi kelancaran"
            },
            {
                "nama"  : "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Main sepak takraw",
                "sosmed": "@jasminednva",
                "kesan" : "informasi yang diberikan sangat jelas dan mudah dipahami",  
                "pesan" : "Terus bawa aura positif di mana pun berada"
            },
            {
                "nama"  : "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20 Tahun",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Jogging",
                "sosmed": "@tobiassiagian",
                "kesan" : "Ramah dan tidak membuat orang lain merasa sungkan",  
                "pesan" : "Semoga semua kebaikan selalu dibalas"
            },
             {
                "nama"  : "Yohana Manik",
                "nim": "122450126",
                "umur": "19 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi": "Main Bowling",
                "sosmed": "@yo_annamnk",
                "kesan" : "Selalu baik dan ramah kepada semua orang",  
                "pesan" : "Semoga selalu produktif dan berhasil"
            },
            {
                "nama"  : "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21 Tahun",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobbi": "Bikin portofolio",
                "sosmed": "@rzkdrnnn",
                "kesan" : "Sangat informatif saat menjelaskan berbagai kegiatan dalam organisasi",  
                "pesan" : "Teruslah menginspirasi banyak orang"
            },
            {
                "nama"  : "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20 Tahun",
                "asal": "Bandung",
                "alamat": "Way Huwi",
                "hobbi": "Bertani",
                "sosmed": "@rafiramadhanmaulana",
                "kesan" : "Baik dan mengasyikkani",  
                "pesan" : "Semoga selalu diberkahi dalam segala usaha"
            },
            {
                "nama"  : "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20 Tahun",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobbi": "Tepuk Semangat",
                "sosmed": "@u_yippy",
                "kesan" : "Selalu aktif dan terlibat di setiap kegiatan",  
                "pesan" : "Teruslah jadi teladan bagi yang lain"
            },
            {
                "nama"  : "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20 Tahun",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Q Time",
                "sosmed": "@chlfawww",
                "kesan" : "Memberikan banyak pelajaran berharga tentang organisasi",  
                "pesan" : "Semoga bisa jadi pemimpin hebat nanti"
            },
            {
                "nama"  : "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21 Tahun",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton youtube, main game",
                "sosmed": "@alfaritziirvan",
                "kesan" : "Mampu membuat suasana jadi seru dan menyenangkan",  
                "pesan" : "Terus tambah ilmu dan pengalaman"
            },
            {
                "nama"  : "Izza Lutfia",
                "nim": "122450090",
                "umur": "20 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Main Rubik",
                "sosmed": "@izzalutfia",
                "kesan" : "Ramah dan tidak membuat orang lain merasa sungkan",  
                "pesan" : "Semoga semua cita-cita tercapai"
            },
            {
                "nama"  : "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@alyaavanevi",
                "kesan" : "Sangat informatif saat menjelaskan berbagai kegiatan dalam organisasi",  
                "pesan" : "Semoga semua kebaikan selalu dibalas"
            },
            {
                "nama"  : "Tria Yunanni",
                "nim": "122450062",
                "umur": "20 Tahun",
                "asal": "Way Kanan",
                "alamat": "Sukarame",
                "hobbi": "Baca Buku",
                "sosmed": "@tria_y062",
                "kesan" : "Bisa menyelesaikan masalah dengan cepat dan efektif",  
                "pesan" : "Semoga setiap masalah selalu bisa diselesaikan dengan baik"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()  

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1DOBrhmwwjyXqCuVi28tXwMdcWtNqTe0r", #bang dimas dn
            "https://drive.google.com/uc?export=view&id=1BuaiyOhaN5h3hFeDw3fIbj0JA4fOM-pd", #kak catherine dn
            "https://drive.google.com/uc?export=view&id=1hZSTS0WazaRgCGBRa2zdzkODuKtcSDZn", #bang akbar dn
            "https://drive.google.com/uc?export=view&id=1DUQGPmMEJWYB7z5UNqQJBAIaSM8SOvVE", #kak rani dn
            "https://drive.google.com/uc?export=view&id=1QISrxIp1Lzp4AUkNGBXFFDNtnrwI6WF9", #bang rendra dn
            "https://drive.google.com/uc?export=view&id=1DXQqfYU56qlGWgLA2BXoEusKwyDtuP_k", #kak salwa dn
            "https://drive.google.com/uc?export=view&id=1DMnFR1VA4gcHE9mx4bdZcc0cJCNDlIYt", #bang yosia dn
            "https://drive.google.com/uc?export=view&id=1xEAUB1Tnx652juGlve8J-jVsBDuBZwxD", #bang ari dn
            "https://drive.google.com/uc?export=view&id=1DjJJ8pOtAEhL_J1XWesqi83RbMHfDKqR", #kak azizah dn
            "https://drive.google.com/uc?export=view&id=1DjdahvMPIhLDa9z0cwvlAkPIuoksJNVk", #kak meira dn
            "https://drive.google.com/uc?export=view&id=1Dd4-wVXEmxWDf6-AH41LvhDRsD_Pff6U", #bang rendi dn
            "https://drive.google.com/uc?export=view&id=1lF2zy1jd3HyREyo8-xZNblynw5tUwyZh", #kak renta dn
            "https://drive.google.com/uc?export=view&id=1n08un1kU2ZBtERgp5hFU84-iokYg0-pp", #bang josua dn

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
                "kesan" : "Memiliki jiwa kepemimpinan yang kuat dan menginspirasi",  
                "pesan" : "Semoga selalu semangat dalam segala hal!"
            },
            {
                "nama"  : "Catherine Firdhasari Maulina Sinaga",
                "nim"   : "121450071",
                "umur"  : "20",
                "asal"  : "Sumatera Utara",
                "alamat": "Airan",
                "hobbi" : "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan" : "Mudah diajak bicara dan sangat terbuka",  
                "pesan" : "Teruslah jadi teladan bagi yang lain"
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
                "kesan" : "Memberikan banyak pelajaran berharga tentang organisasi",  
                "pesan" : "Semoga masa depan selalu cerah dan bahagia"
            },
            {
                "nama"  : "Rani Pkuspita sari",
                "nim"   : "122450030",
                "umur"  : "20",
                "asal"  : "Kota Metro",
                "alamat": "Rajabasa",
                "hobbi" : "Dengar musik",
                "sosmed": "@ranniu",
                "kesan" : "Selalu aktif dan terlibat di setiap kegiatan",  
                "pesan" : "Semoga makin hebat dan berkembang"
            },
            {
                "nama"  : "Rendra Eka Prayoga",
                "nim"   : "122450112",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Belwis",
                "hobbi" : "Mancing Ikan Mas",
                "sosmed": "@rendraepr",
                "kesan" : "Selalu memotivasi teman-teman untuk lebih semangat",  
                "pesan" : "Tetap semangat dan terus menginspirasi banyak orang!"
            },
            {
                "nama"  : "Salwa Farhanatussaidah",
                "nim"   : "122450055",
                "umur"  : "20",
                "asal"  : "Pesawaran",
                "alamat": "Airan",
                "hobbi" : "Nonton",
                "sosmed": "@slwfhn_694",
                "kesan" : "informasi yang diberikan sangat jelas dan mudah dipahami",  
                "pesan" : "Semoga karier makin cemerlang ke depannya"
            },
            {
                "nama"  : "Yosia Letare Banurea",
                "nim"   : "121450149",
                "umur"  : "20",
                "asal"  : "Dairi, Sumatera Utara",
                "alamat": "Perum Griya Indah",
                "hobbi" : "Tidur",
                "sosmed": "@yosiabanurea",
                "kesan" : "Bisa menyelesaikan masalah dengan cepat dan efektif",  
                "pesan" : "Semoga selalu diberkahi dalam segala usaha"
            },
            {
                "nama"  : "Ari Sigit",
                "nim"   : "121450069",
                "umur"  : "23",
                "asal"  : "Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobbi" : "Futsal",
                "sosmed": "@ari_sigit17",
                "kesan" : "Semangat dalam berorganisasi sangat menginspirasi",  
                "pesan" : "Semoga sukses dalam semua hal yang dikerjakan"
            },
            {
                "nama"  : "Azizah Kusumah Putri",
                "nim"   : "122450068",
                "umur"  : "21",
                "asal"  : "Lampung Selatan",
                "alamat": "Natar",
                "hobbi" : "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan" : "Ramah dan tidak membuat orang lain merasa sungkan",  
                "pesan" : "Terus tambah ilmu dan pengalaman"
            },
            {
                "nama"  : "Meira Listyaningrum",
                "nim"   : "122450011",
                "umur"  : "20",
                "asal"  : "Pesawaran",
                "alamat": "Airan",
                "hobbi" : "Membaca",
                "sosmed": "@meirasty_",
                "kesan" : "Selalu memberi semangat agar tidak mudah menyerah",  
                "pesan" : "Semoga semua cita-cita tercapai"
            },
            {
                "nama"  : "Rendi Alexander Hutagalung",
                "nim"   : "122450057",
                "umur"  : "20",
                "asal"  : "Tangerang",
                "alamat": "Kost Benawang",
                "hobbi" : "Menyanyi",
                "sosmed": "@rexander",
                "kesan" : "Sangat informatif saat menjelaskan berbagai kegiatan dalam organisasi",  
                "pesan" : "Tetap konsisten dan terus berprestasi"
            },
            {
                "nama"  : "Renta Siahaan",
                "nim"   : "122450070",
                "umur"  : "21",
                "asal"  : "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi" : "Membaca dan Memancing",
                "sosmed": "@renta.shn",
                "kesan" : "Selalu baik dan ramah kepada semua orang",  
                "pesan" : "Semoga selalu sehat dan bersemangat"
            },
            {
                "nama"  : "Josua Panggabean",
                "nim"   : "122450061",
                "umur"  : "21",
                "asal"  : "Pematang Siantar",
                "alamat": "Gerbang Barat",
                "hobbi" : "Menonton",
                "sosmed": "@josuapanggabean_",
                "kesan" : "Sangat baik, informatif dalam menerangkan suatu permasalahan dan sangat menginspirasi",  
                "pesan" : "Mampu membuat suasana jadi seru dan menyenangkan"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()   

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=16dN0wFBDhjGdgQX1vht1wFOQRYVX8aQy", #bang andrian dn
            "https://drive.google.com/uc?export=view&id=16hEUxpNpsBmPlSK_4uvf5voGRSK0uWda", #kak adisty dn
            "https://drive.google.com/uc?export=view&id=16mGz1gkpXHr44fG_2wgrqa7gFt-nGxVT", #kak nabilla dn
            "https://drive.google.com/uc?export=view&id=16nBt4S4lEwpU2cZ9yxTkXSwLA_Ip79wb", #bang danang dn
            "https://drive.google.com/uc?export=view&id=16a75WKcBYUGk7PYqWDzi2jMqWXRha_36", #kak nabilah dn
            "https://drive.google.com/uc?export=view&id=16gyHYrLSFnXtwWXN9QwBP1JF0LG-jM28", #bang dhafin dn
            "https://drive.google.com/uc?export=view&id=16dajxX5XG1hZGOmD5IWrSvEbyK0DVZ5j", #kak elia dn


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
                "kesan" : "Memberikan banyak pelajaran berharga tentang organisasi",  
                "pesan" : "Semoga kebaikan selalu berlipat ganda"
            },
            {
                "nama"  : "Adisty Syawaida Ariyanto",
                "nim"   : "121450136",
                "umur"  : "22",
                "asal"  : "Metro",
                "alamat": "Sukarame ",
                "hobbi" : "Nonton Film",
                "sosmed": "@adistysa_",
                "kesan" : "Selalu memotivasi teman-teman untuk lebih semangat",  
                "pesan" : "Semoga semua kebaikan selalu dibalas"
            },
            {
                "nama"  : "Nabila Azhari",
                "nim"   : "121450029",
                "umur"  : "21",
                "asal"  : "Simalungun",
                "alamat": "Airan ",
                "hobbi" : "Menghitung Uang",
                "sosmed": "@zhjung",
                "kesan" : "Memiliki jiwa kepemimpinan yang kuat dan menginspirasi",  
                "pesan" : "Terus jadi sumber semangat bagi orang lain"
            },
            {
                "nama"  : "Danang Hilal Kurniawan",
                "nim"   : "122450085",
                "umur"  : "21",
                "asal"  : "Bandar Lampung",
                "alamat": "Airan",
                "hobbi" : "Belajar",
                "sosmed": "@dananghk_",
                "kesan" : "Bisa menyelesaikan masalah dengan cepat dan efektif",  
                "pesan" : "Semoga selalu produktif dan berhasil"
            },
            {
                "nama"  : "Nabilah Andika Fitriati",
                "nim"   : "121450139",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi" : "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan" : "Selalu aktif dan terlibat di setiap kegiatan",  
                "pesan" : "Semoga selalu dikelilingi orang-orang baik"
            },
            {
                "nama"  : "Dhafin Razaqa Luthfi",
                "nim"   : "122450133",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi" : "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan" : "Ramah dan tidak membuat orang lain merasa sungkan",  
                "pesan" : "Terus bawa aura positif di mana pun berada"
            },
            {
                "nama"  : "Elia Meylani Simanjuntak",
                "nim"   : "122450026",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Korpri",
                "hobbi" : "Main Alat Musik",
                "sosmed": "@meylanielia",
                "kesan" : "Sangat informatif saat menjelaskan berbagai kegiatan dalam organisasi",  
                "pesan" : "Teruslah menginspirasi banyak orang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()    
# Tambahkan menu lainnya sesuai kebutuhan


# Tambahkan menu lainnya sesuai kebutuhan
