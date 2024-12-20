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
if menu == "Kesekjenan":#Kesan dan Pesan sudah
    def kesekjenan():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1PTrO8ors28_jtYNbO9Zpt2fse_mnGKme",
            "https://drive.google.com/uc?export=view&id=1z03M9vqZjdeii1QIx6Q_-bIEi043bQBd",
            "https://drive.google.com/uc?export=view&id=1EB0Dkp1aOFu3WJbyg7mcWq9CQNXFWqRH",
            "https://drive.google.com/uc?export=view&id=1NZBdwsk8Pi1dAoBXvs2_QjFg5KdBaiFf",
            "https://drive.google.com/uc?export=view&id=1ESOCuUbejJ1JKaj4H4mqpGYHmuT-z3LN",
            "https://drive.google.com/uc?export=view&id=1hN8tBfFsmMoB2tCWvwuNbfiHTKpGpfpg",
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
                "kesan" : "Seseorang dengan jiwa kepemimpinan",
                "pesan" :"Semoga dilancarkan segala urusannya"
            },
            {
                "nama"  : "Pandra Insani Putra Azwan",
                "nim"   : "121450137",
                "umur"  : "21",
                "asal"  : "Bukit Kemuning, Lampung Utara",
                "alamat": "Bawen 2",
                "hobbi" : "Bermain gitar dan menyanyi",
                "sosmed": "@pandrainsni27",
                "kesan" : "Hebat dalam membuat suasana menjadi menyengangkan",  
                "pesan" : "Semangat ngerjain tugas-tugasnya bang"
            },
            {
                "nama"  : "Meliza Wulandari",
                "nim"   : "121450065",
                "umur"  : "20",
                "asal"  : "Pagar Alam, Sumatera Selatan",
                "alamat": "Kotabaru",
                "hobbi" : "Nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan" : "Sangat informatif dalam menjelaskan sesuatu dan murah senyum",  
                "pesan" : "Semoga sukes ya kak"
            },
            {
                "nama"  : "Putri Maulida Chairani",
                "nim"   : "121450050",
                "umur"  : "21",
                "asal"  : "Payakumbuh, Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi" : "Dengerin bang pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan" : "Profesional dalam menjalankan tugas",  
                "pesan" : "Semoga apa yang diinginkan tercapai"
            },
            {
                "nama"  : "Hartiti Fadilah",
                "nim"   : "121450031",
                "umur"  : "21",
                "asal"  : "Palembang",
                "alamat": "Pemda",
                "hobbi" : "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan" : "Baik dan memiliki sikap yang tenang",  
                "pesan" : "Semoga dimudahkan segala urusannya"
            },
            {
                "nama"  : "Nadilla Andara Putri",
                "nim"   : "121450003",
                "umur"  : "21",
                "asal"  : "Metro",
                "alamat": "KotaBaru",
                "hobbi" : "Membaca",
                "sosmed": "@ndillaandr26",
                "kesan" : "Memberikan energi yang positif",  
                "pesan" : "Semoga selalu sukses dan bahagia"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":#Kesan dan pesan sudah selesai
    def baleg():
        gambar_urls = [
            
            "https://drive.google.com/uc?export=view&id=1SYkCZsxUbBj631in40QaDZT1Trc0qo7A",#DONE
            "https://drive.google.com/uc?export=view&id=1Sg0xgKC7BnUo-9IAI7stNIrLY22Ama0V",#DONE
            "https://drive.google.com/uc?export=view&id=1ScnthuYGyGUHFnF94Vq4aq5-TyFJ8dC-",#DONE
            "https://drive.google.com/uc?export=view&id=1S_VlFRvtm3hM3VAgoxpjBz4v74DxqYuG",#DONE 
            "https://drive.google.com/uc?export=view&id=1SrnWLYSpj9p72xqYBtI92AfOgV8gzCqA",#DONE
            "https://drive.google.com/uc?export=view&id=1SMSjSqhLUYK3XQio6vSko0ORkQ-bunUb",#DONE
            "https://drive.google.com/uc?export=view&id=1Sg2vJdBXj7CiEoWKCAugmoEjkPlhDaju",#DONE
            "https://drive.google.com/uc?export=view&id=1SaxeY8Xo_Hh5rclt16QVupw4ygkmaRfM",#DONE
            "https://drive.google.com/uc?export=view&id=1S_BtBdZADmPGuJ_wS0YCI8tgi1d_ImFW",#DONE
            "https://drive.google.com/uc?export=view&id=1SZAFLLIyI7lmTy2B4Mb4IXcAPBSpk3Hk",#DONE
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
                "kesan" : "Ramah dan murah senyum yang membuat suasana mnejadi menyenangkan",  
                "pesan" : "Semoga Kakak selalu diberkahi kesehatan dan kesuksesan"
            },
            {
                "nama"  : "Annisa Cahyani Surya",
                "nim"   : "121450114",
                "umur"  : "21",
                "asal"  : "Tanggerang Selatan",
                "alamat": "Way Huwi",
                "hobbi" : "Membaca, Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan" : "Selalu mendorong kami untuk lebih aktif",  
                "pesan" : "Semoga kakak dapat menggapai cita-citanya"
            },
            {
                "nama"  : "Wulan Sabina",
                "nim"   : "121450150",
                "umur"  : "21",
                "asal"  : "Medan",
                "alamat": "Raden Saleh",
                "hobbi" : "Nonton Drakor",
                "sosmed": "@wlnsbn0",
                "kesan" : "Sangat terbuka untuk membantu kami memahami banyak hal baru",  
                "pesan" : "Sukses selalu buat kakak"
            },
            {
                "nama"  : "Anisa Dini Amaliya",
                "nim"   : "121450081",
                "umur"  : "21",
                "asal"  : "Tanggerang",
                "alamat": "Jati Agung",
                "hobbi" : "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan" : "Perhatian terhadap kami",  
                "pesan" : "Semoga setiap kebaikan Kakak dibalas dengan yang lebih baik"
            },
            {
                "nama"  : "Anisa Fitriyani",
                "nim"   : "122450019",
                "umur"  : "20",
                "asal"  : "Batam",
                "alamat": "Kalianda",
                "hobbi" : "Membaca Al-Waqiah setiap maghrib",
                "sosmed": "@ansftynn_",
                "kesan" : "Peduli dengan kemajuan organisasi dan anggotanya",  
                "pesan" : "Semoga segala yang Kakak lakukan selalu membawa keberkahan"
            },
            {
                "nama"  : "Mirzan Yusuf Rabbani",
                "nim"   : "122450118",
                "umur"  : "20",
                "asal"  : "Jakarta",
                "alamat": "Korpri",
                "hobbi" : "Main Kucing",
                "sosmed": "@myrrinn",
                "kesan" : "Terbuka dan membantu kami memahami banyak hal baru",  
                "pesan" : "Semoga kakak selalu dilindungi dan diberkahi Tuhan!"
            },
            {
                "nama"  : "Dhea Amelia Putri",
                "nim"   : "122450004",
                "umur"  : "20",
                "asal"  : "Sukabumi, Jawa Barat",
                "alamat": "Natar",
                "hobbi" : "Suka Ikut Tes SKD",
                "sosmed": "@dhea_wedding",
                "kesan" : "Berwawasan luas dan mampu membimbing dengan baik",  
                "pesan" : "Semoga Kakak selalu dikelilingi oleh orang-orang baik!"
            },
            {
                "nama"  : "Muhammad Fahrul Aditya",
                "nim"   : "121450156",
                "umur"  : "22",
                "asal"  : "Surakarta, Jawa Tengah",
                "alamat": "Pahoman",
                "hobbi" : "Melukis, badminton, hiking, ngopi, dengerin music, nonton film dan ngoding",
                "sosmed": "@fhrul.pdf",
                "kesan" : "Selalu membangun dan mendorong kami untuk majuk",  
                "pesan" : "Semoga dapat lulus kuliah dengan ipk yang memuaskan"
            },
            {
                "nama"  : "Berliana Enda Putri",
                "nim"   : "122450065",
                "umur"  : "21",
                "asal"  : "Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi" : "Main Game",
                "sosmed": "@berlyyanda",
                "kesan" : "Rendah hati dan mudah bergaul",  
                "pesan" : "Semoga Kakak selalu sukses di setiap kesempatan"
            },
            {
                "nama"  : "Jeremia Susanto",
                "nim"   : "122450022",
                "umur"  : "20",
                "asal"  : " Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi" : "Marah-marah",
                "sosmed": "@jeremia_s_",
                "kesan" : "Profesionalisme dan sikapnya sangat patut dicontoh.",  
                "pesan" : "Semoga Kakak selalu dilancarkan dalam segala urusan"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":#Kesan dan Pesan sudah selesai
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ElGWcygCJvPwrK4mrQfOVokU1BKtyv6Q", #kak lutfi
            "https://drive.google.com/uc?export=view&id=1Emi9GPfMX_J2dkSjVkEO6zZVeBh9ytSx", #bang bintang
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
                "kesan" : "Sangat informatif dalam menjelaskan dan menginspirasi",  
                "pesan" : "Semangat terus kak menjalani tugas sebagai Senator dan semoga sukses dalam perjalanan kariranya"
            },
            {
                "nama"  : "Rian Bintang Wijaya",
                "nim"   : "122450094",
                "umur"  : "20",
                "asal"  : "Palembang, Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi" : "Mendengar Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan" : "Mengajarkan tanggung jawab",  
                "pesan" : "Semoga Kakak selalu dilancarkan rezekinya dan diberi kesehatan"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1ax_Ps7YnaAcP7U06G_0VWPB8iof2Y0z4", #bang erickson 2
            "https://drive.google.com/uc?export=view&id=1S-ezfEWT4GgVR7Bbq5hTznrQdXgKm7xB", #kak abeth 2
            "https://drive.google.com/uc?export=view&id=1xRt8cHOxsdhOz7T758eCegNEqpssCqEw", #kak afifah 2
            "https://drive.google.com/uc?export=view&id=1x5NC5e7fMQmfa6zjmSegMlj-FWrtMZjr", #kak allya 2
            "https://drive.google.com/uc?export=view&id=1LUV2WM5CBZ9_Y8EERXgUhCoEfJoQQV-7", #kak hanum 2
            "https://drive.google.com/uc?export=view&id=1EyD2sD7QqKxMT_P-OWaajj5C3q5lPzte", #bang ferdy 2
            "https://drive.google.com/uc?export=view&id=1X7CYYhvor76gOmCbwrz2XdZPYhebMCPX", #bang deri 2
            "https://drive.google.com/uc?export=view&id=1beIWrmOb7QHw92RwXUk-vaVnr4EqyYHh", #kak oktavia 2
            "https://drive.google.com/uc?export=view&id=1QvvY1-GvoQXb3X1EdGzk-MgzU1k6I1kH", #bang deyvan 2
            "https://drive.google.com/uc?export=view&id=12ZLUkNJSgiAD9GSU8_WonKZv4A_BOtkz", #bang ibnu 2
            "https://drive.google.com/uc?export=view&id=1mxbjWId1N2ONcabB_KsD-NBoz-jLUOxX", #bang jo 2
            "https://drive.google.com/uc?export=view&id=17n8ep4KRDYK7SutzwFeznsZwKMD-5jb2", #bang kemas 2
            "https://drive.google.com/uc?export=view&id=16uWR2TxVzle-kWDHgFRvr-FseF0-Hjer", #bang leonard 2
            "https://drive.google.com/uc?export=view&id=1uofKwdC57a_z7okOqsczHcplhB1RzGWU", #kak presilia 2
            "https://drive.google.com/uc?export=view&id=1GXsyyEp5HmJOCB0yGxRHieBIXszT1E4P", #kak rafa 2
            "https://drive.google.com/uc?export=view&id=1iQJwMSRBtSCAvfkgcDBK90EtG0YAzEV2", #bang sahid 2
            "https://drive.google.com/uc?export=view&id=1TDrmQMAV5UdoEBTEyprJ1RnACdQ0Y-ig", #kak vanes 2
            "https://drive.google.com/uc?export=view&id=1S9WrV9ittS8LUANRpZBHz4yX5sGf_XRp", #bang ateng 2
            "https://drive.google.com/uc?export=view&id=1gAhXLlEUJviDj9ftlaSpG6xAHwkEXs7K", #bang gede 2
            "https://drive.google.com/uc?export=view&id=1Ct4qSoD_GhLx66trRuToegZReRx2nUeO", #kak jaclin 2
            "https://drive.google.com/uc?export=view&id=1M0R8EL1tphDOqvYzt-0zesCsS-cqG_bD", #bang rafly 2
            "https://drive.google.com/uc?export=view&id=1pohCvKKc9v7zAiQ3u0V0i5n_GTOgNnJ0", #kak dini 2

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
                "kesan" : "Menghargai setiap pendapat dan masukan yang kami berikan",  
                "pesan" : "Semoga sukses selalu dalam studi dan kariernya"
            },
            {
                "nama"  : "Elisabeth Claudia Simanjuntak",
                "nim"   : "122450123",
                "umur"  : "18",
                "asal"  : "Pekanbaru",
                "alamat": "Sukarame",
                "hobbi" : "Memancing keributan",
                "sosmed": "@celisabethh_",
                "kesan" : "Tegas namun tetap ramah, jadi panutan dalam bersikap",  
                "pesan" : "Semoga selalu diberikan keberkahan dalam hidup"
            },
            {
                "nama"  : "Nisrina Nur Afifah",
                "nim"   : "122450052",
                "umur"  : "19",
                "asal"  : "Bekasi",
                "alamat": "Sukarame",
                "hobbi" : "Nabok orang",
                "sosmed": "@afifahhnsrn",
                "kesan" : "Profesional dalam menjalankan tugas",  
                "pesan" : "Semangat kak dalam menjalankan tugas-tugasnya"
            },
            {
                "nama"  : "Allya Nurul Islami Pasha",
                "nim"   : "122450033",
                "umur"  : "20",
                "asal"  : "Sumatera Barat",
                "alamat": "Gang Perwira, Belwis",
                "hobbi" : "Nonton Dracin",
                "sosmed": "@allyaislami_",
                "kesan" : "Mengajarkan pentingnya tanggung jawab dalam setiap tugas",  
                "pesan" : "Semoga selalu diberi kemudahan dalam setiap langkahnya"
            },
            {
                "nama"  : "Farahanum Afifah Ardiansyah",
                "nim"   : "122450056",
                "umur"  : "20",
                "asal"  : "Padang, Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi" : "Tidur",
                "sosmed": "@farahanumafifahh",
                "kesan" : "Memberi yang terbaik dan menunjukkan teladan dalam menjalankan tugas",  
                "pesan" : "Semoga sehat dan bahagia selalu"
            },
            {
                "nama"  : "Ferdy Kevin Naibaho",
                "nim"   : "122450107",
                "umur"  : "19",
                "asal"  : "Medan, Sumatera Utara",
                "alamat": "Jalan Senopati Raya 18",
                "hobbi" : "Dengerin Rocky Gerung",
                "sosmed": "@ferdy_kevin",
                "kesan" : "Sharing informasi yang sangat membantu",  
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
                "kesan" : "Profesional tapi tetap santai, nggak bikin canggung.",  
                "pesan" : "Semoga semua harapan dan cita-cita dapat tercapai"
            },
            {
                "nama"  : "Oktavia Nurwinda Puspita Sari",
                "nim"   : "122450041",
                "umur"  : "20",
                "asal"  : "Lampung Timur",
                "alamat": "Way Hui",
                "hobbi" : "Memasak",
                "sosmed": "@_oktavianrwnda_",
                "kesan" : "Murah senyum dan sabar dalam menjelaskan",  
                "pesan" : "Semangat dalam menjalankan tanggung jawabnya"
            },
            {
                "nama"  : "Deyvan Loxefal",
                "nim"   : "121450148",
                "umur"  : "21",
                "asal"  : "Riau",
                "alamat": "Pulau Damar",
                "hobbi" : "Belajar",
                "sosmed": "@depanloo",
                "kesan" : "Detail dalam menjelaskan informasi terkait divisinya",  
                "pesan" : "Semoga dilancarkan segala urusannya baik akademik maupun non-akademik"
            },
            {
                "nama"  : "Ibnu Farhan Al-Ghifari",
                "nim"   : "121450121",
                "umur"  : "21",
                "asal"  : "Jambi",
                "alamat": "Pulau Damar, Kobam",
                "hobbi" : "Bermain Game Online",
                "sosmed": "@al_ghifari032",
                "kesan" : "Membantu dalam memahami HMSD",  
                "pesan" : "Semoga sehat selalu"
            },
             {
                "nama"  : "Johannes Krisjon Silitonga",
                "nim"   : "122450043",
                "umur"  : "19",
                "asal"  : "Tanggerang",
                "alamat": "Jalan Lapas",
                "hobbi" : "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan" : "Membantu mengenalkan organisasi lebih dalam",  
                "pesan" : "Semangat terus kuliahnya dan semoga apa yang diinginkan tercapai"
            },
            {
                "nama"  : "Kemas Veriandra Ramadhan",
                "nim"   : "122450016",
                "umur"  : "19",
                "asal"  : "Bekasi",
                "alamat": "Golf Asri",
                "hobbi" : "Bermain ular python digital",
                "sosmed": "@kemasverii",
                "kesan" : "Mengajarkan banyak hal mengenai himpunan",  
                "pesan" : "Semoga terus membawa dampak positif dimanapun"
            },
            {
                "nama"  : "Leonard Andreas Napitupulu",
                "nim"   : "121450153",
                "umur"  : "21",
                "asal"  : "Sumatera Utara",
                "alamat": "Kobam",
                "hobbi" : "Belajar",
                "sosmed": "@lnrd.__",
                "kesan" : "Tenang dan bikin suasana jadi lebih santai",  
                "pesan" : "Semoga berkembang menjadi diri yang lebih baik terus"
            },
            {
                "nama"  : "Presilia",
                "nim"   : "122450081",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Kota Baru",
                "hobbi" : "Tidur",
                "sosmed": "@presiliamg",
                "kesan" : "Membawa energi yang positif",  
                "pesan" : "Semoga harapannya terwujud"
            },
            {
                "nama"  : "Rafa Aqilla Jungjunan",
                "nim"   : "122450142",
                "umur"  : "20",
                "asal"  : "Riau",
                "alamat": "Belwis",
                "hobbi" : "Membaca webtoon",
                "sosmed": "@rafaaqilla",
                "kesan" : "Murah senyum dan profesional menjalankan tugas-tugasnya",  
                "pesan" : "Semoga selalu termotivasi untuk terus belajar dan berkemnbang"
            },
            {
                "nama"  : "Sahid Maulana",
                "nim"   : "122450109",
                "umur"  : "21",
                "asal"  : "Depok, Jawa Barat",
                "alamat": "Airan Raya",
                "hobbi" : "Bermain Game",
                "sosmed": "@sahid_maul19",
                "kesan" : "Friendly dan asik",  
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
                "kesan" : "Baik, peduli, dan mudah untuk diajak ngobrol",  
                "pesan" : "Semangat terus menjalani aktivitas sehari-harinya"
            },
            {
                "nama"  : "M. Farhan Athaulloh",
                "nim"   : "121450117",
                "umur"  : "21",
                "asal"  : "Bandar Lampung",
                "alamat": "Kota Baru",
                "hobbi" : "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan" : "Menjelaskan dengan detail dan informatif dan tidak kaku",  
                "pesan" : "Semoga selalu diberikan kesabaran dalam menjalani setiap hal"
            },
            {
                "nama"  : "Gede Moena",
                "nim"   : "121450014",
                "umur"  : "21",
                "asal"  : "Bekasi",
                "alamat": "Korpri Raya",
                "hobbi" : "Belajar dan main game",
                "sosmed": "@gedemoenaa",
                "kesan" : "Tenang dan mudah bergaul",  
                "pesan" : "Semoga selalu dikelilingi orang-orang yang baik"
            },
            {
                "nama"  : "Jaclin Alcavella",
                "nim"   : "122450015",
                "umur"  : "19",
                "asal"  : "Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi" : "Berenang",
                "sosmed": "@jaclinalcv_",
                "kesan" : "Terbuka untuk sharing-sharing dan baik",  
                "pesan" : "Semoga diberi keberkahan dalam hidup"
            },
            {
                "nama"  : "Rafly Prabu Darmawan",
                "nim"   : "122450140",
                "umur"  : "20",
                "asal"  : "Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi" : "Main Game",
                "sosmed": "@raflyy_pd2684",
                "kesan" : "enang dan nggak pernah terburu-buru",  
                "pesan" : "Semangat terus mengejar cita-citanya"
            },
            {
                "nama"  : "Syalaisha Andini Putriansyah",
                "nim"   : "122450111",
                "umur"  : "21",
                "asal"  : "Tanggerang",
                "alamat": "Sukarame",
                "hobbi" : "Membaca",
                "sosmed": "@syalaisha.i__",
                "kesan" : "Membantu kami lebih mengenal organisasi",  
                "pesan" : "Semangat terus belajarnya, semoga dilancarkan"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1MF5ZMgVLcSbrNWMlLyPfi3ug2JRWvmBj", #bang rafi dn1
            "https://drive.google.com/uc?export=view&id=1MVtJ_jhRqL5tXcPqK3EpavbQiRjzgNft", #kak anisa dn1
            "https://drive.google.com/uc?export=view&id=1EqiZPIr9vqhl1qMh0v75OLLxFiZPxPZk", #bang ahmad dn1
            "https://drive.google.com/uc?export=view&id=12H9xuWYW-Vb3VN9pPVlrUE_JHBzp11Is", #bang fadhil 1
            "https://drive.google.com/uc?export=view&id=1r2uzj8zvD-21nS40Mb2uGjv-2vpSNRIq", #kak dina dn1
            "https://drive.google.com/uc?export=view&id=1eiREMtdmOHorGvwWDRFM4oQvrZm9fIJU", #kak dinda dn1
            "https://drive.google.com/uc?export=view&id=1p6a1U1yypun_NECjgRHMdW1lOdNe7N2O", #kak marleta dn1
            "https://drive.google.com/uc?export=view&id=17u3fjdcv3fnqkJEgc01UGGu56AYa6ZM3", #kak rut junita dn1
            "https://drive.google.com/uc?export=view&id=1sIg1fgG8BnsrNEOd-31o9xUmez_aLNgq", #kak syadza dn1
            "https://drive.google.com/uc?export=view&id=15QWpw3XXSDNfk11oxKF946snWmfFEWpj", #bang eggi dn1
            "https://drive.google.com/uc?export=view&id=19YP52Rie8WORQXYv5DNrieNqt9XIPzpr", #kak febiya dn1
            "https://drive.google.com/uc?export=view&id=1cOj0q6n23FZKSZlB5s50eDroflLGrIqO", #kak happy syahrul dn1
            "https://drive.google.com/uc?export=view&id=1WN3aocjwXZqfLtihhHaaeSfH2D1tSfCY", #bang randa dn1

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
                "kesan" : "Menjelaskan dengan detail mengenai departemen dan mudah bergaul",  
                "pesan" : "Semoga apa yang diinginkan dapat terkabulkan dan semangat terus kuliahnya bang"
            },
            {
                "nama"  : "Annisa Novantika",
                "nim"   : "121450005",
                "umur"  : "21",
                "asal"  : "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi" : "Memasak",
                "sosmed": "@anovavona",
                "kesan" : "Menyenangkan dan nggak bikin canggung",  
                "pesan" : "Semoga selalu dikelilingi oleh hal-hal baik."
            },
            {
                "nama"  : "Ahmad Sahidin Akbar",
                "nim"   : "122450044",
                "umur"  : "20",
                "asal"  : "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi" : "Olahraga",
                "sosmed": "@sahid22__",
                "kesan" : "Tenang dan tidak ragu untuk menjawab pertanyaan kami",  
                "pesan" : "Semoga sukses terus ya bang"
            },
            {
                "nama"  : "Fadhil Fitra Wijaya",
                "nim"   : "122450082",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Teluk Betung",
                "hobbi" : "Main game",
                "sosmed": "@fadhilfwee",
                "kesan" : "Pembawaannya bikin suasana jadi enak",  
                "pesan" : "Semoga hari-hari di depan selalu penuh makna dan kebahagiaan."
            },
            {
                "nama"  : "Syalaisha Andina Putriansyah",
                "nim"   : "122450121",
                "umur"  : "21",
                "asal"  : "Tangerang",
                "alamat": "Gang Yudhistira",
                "hobbi" : "Baca jurnal",
                "sosmed": "@dkselsd_31",
                "kesan" : "Baik dan mudah diajak ngobrol",  
                "pesan" : "Semangat terus dalam menjalani kegiatannya"
            },
            {
                "nama"  : "Dinda Nababan",
                "nim"   : "122450120",
                "umur"  : "20",
                "asal"  : "Medan, Sumatera Utara",
                "alamat": "Jalan Lapas",
                "hobbi" : "Belajar",
                "sosmed": "@dindanababan_",
                "kesan" : "Penyampaiannya mudah dipahami",  
                "pesan" : "Semoga sehat selalu"
            },
            {
                "nama"  : "Marleta Cornelia Leander",
                "nim"   : "122450092",
                "umur"  : "20",
                "asal"  : "Depok, Jawa Barat",
                "alamat": "Gang Nangka 3",
                "hobbi" : "Review Jurnal",
                "sosmed": "@marletacornelia",
                "kesan" : "Menjelaskan hal-hal dengan jelas",  
                "pesan" : "Semoga hari-harinya dipenuhi dengan keberkahan"
            },
            {
                "nama"  : "Rut Junita Sari Siburian",
                "nim"   : "122450103",
                "umur"  : "20",
                "asal"  : "Batam, Kepulauan Riau",
                "alamat": "Gang Nangka 3",
                "hobbi" : "Review Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan" : "Mendengarkan kami dengan baik",  
                "pesan" : "Semangat terus mengejar cita-citanya"
            },
            {
                "nama"  : "Syadza Puspadari Azhar",
                "nim"   : "122450072",
                "umur"  : "20",
                "asal"  : "Palembang",
                "alamat": "Belwis",
                "hobbi" : "Resume SG",
                "sosmed": "@puspadrr",
                "kesan" : "Tidak ragu untuk membantu menjelaskan sesuatu",  
                "pesan" : "Semoga dapat terus memberikan yang terbaik"
            },
            {
                "nama"  : "Eggi satria",
                "nim"   : "122450032",
                "umur"  : "20",
                "asal"  : "Sukabumi",
                "alamat": "Korpri",
                "hobbi" : "Ngoding WISATA",
                "sosmed": "@egistr",
                "kesan" : "Friendly, tidak sungkan untuk membantu, selalu mendorong untuk lebih aktif",  
                "pesan" : "Semangat bang terus bang ngodingnya"
            },
            {
                "nama"  : "Febiya Jomy Pratiwi",
                "nim"   : "122450074",
                "umur"  : "20",
                "asal"  : "Tulang Bawang",
                "alamat": "Jalan Kelengkeng Raya",
                "hobbi" : "Review jurnal",
                "sosmed": "@pratiwifebiya",
                "kesan" : "Menyampaikan hal-hal dengan sabar dan jelas",  
                "pesan" : "Semoga apa yang diinginkan dapat terwujud"
            },
             {
                "nama"  : "Happy Syahrul Ramadhan",
                "nim"   : "122450013",
                "umur"  : "20",
                "asal"  : "Lampung Timur",
                "alamat": "Karang Anyar",
                "hobbi" : "Main game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan" : "Mengenalkan HMSD dengan lebih jelas",  
                "pesan" : "Semoga tugas-tugasnya dapat terselesaikan dengan baik"
            },
            {
                "nama"  : "Randa Andriana Putra",
                "nim"   : "122450083",
                "umur"  : "21",
                "asal"  : "Banten",
                "alamat": "Sukarame",
                "hobbi" : "Tidur dan berkembang",
                "sosmed": "@randaandriana_",
                "kesan" : "Sangat menyambut, berwawasan luas dan penjelasannya mudah dipahami",  
                "pesan" : "Semoga kegiatannya di dalam maupun di luar perkuliahan tetap lancar dan tetap semangat kak"
            },

        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen MEDKRAF":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1caQ_kLWgNmCrSLbNj9cNO92PK-CzII-B", #bang wahyu dn1
            "https://drive.google.com/uc?export=view&id=1FxS9CPKOetpkoGuzYzvJOo26m1keHahI", #kak elok dn1
            "https://drive.google.com/uc?export=view&id=1F5IEBwESS9dZgaT18QdnUUr1gsS5BTgL", #kak arsyiah dn1
            "https://drive.google.com/uc?export=view&id=16eCLUnDzXmnE1kCN0HtWKTC5Oi1czPBY", #kak cintya dn1
            "https://drive.google.com/uc?export=view&id=15CJmhLpntqKBJFqpVuM4yiRwCJnbZEQD", #kak najla dn1
            "https://drive.google.com/uc?export=view&id=1Magph5j2YhewoMFvAZU0Nxcs7kiJw7eM", #kak rahma dn1
            "https://drive.google.com/uc?export=view&id=1FkNaarh8se5obHUKjYY91_V5ojc4C19C", #kak try yani dn1
            "https://drive.google.com/uc?export=view&id=1GAn3SPpDcH0DoAjx1jcO1W9C0zQKXopt", #bang kaisar dn1
            "https://drive.google.com/uc?export=view&id=1FIDCQyQdO3i9armO0F4mgy_FgV_PJs1P", #kak dwi dn1
            "https://drive.google.com/uc?export=view&id=1FkTkTGFILP0-vzZ1pSQevMszXxbkthdP", #bang gym dn1
            "https://drive.google.com/uc?export=view&id=1FbFhrzTVzeHdNBHUxJyoNbOPy4pRrW8i", #kak nasywa dn1
            "https://drive.google.com/uc?export=view&id=1FXraZ0ODFA6wTYbGPQlJu0h6LI5xPnxM", #kak priska dn1
            "https://drive.google.com/uc?export=view&id=1GF9irSfPmZ9VU4slGMIlHdJPi9aUQ0f8", #bang arsal dn1
            "https://drive.google.com/uc?export=view&id=1FFw0mpx4fMhs6Khpf46lawiAeA8HBrXI", #bang abit dn1
            "https://drive.google.com/uc?export=view&id=1F_88c_AfSKm7gYCQ9CHJyv9g5_MpMbIX", #bang akmal dn1
            "https://drive.google.com/uc?export=view&id=1FsPr8ESuHQcfa338z4o7bsGziUxUrClO", #bang hermawan dn1
            "https://drive.google.com/uc?export=view&id=1XSwYCXFWq_JC0zl-W1caiqQAXWgKCei9", #kak nisa dn1
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
                "kesan" : "Penjelasannya mudah dipahami dan tidak berbelit-belit",  
                "pesan" : "Jangan pernah berhenti untuk berbagi dan menginspirasi"
            },
            {
                "nama"  : "Elok Fiola",
                "nim"   : "122450051",
                "umur"  : "19",
                "asal"  : "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi" : "Editing",
                "sosmed": "@elokfiola",
                "kesan" : "Berbicara dengan tenang dan jelas, memberikan kesan baik",  
                "pesan" : "Semangat terus dalalm menjalani setiap kegiatannya"
            },
            {
                "nama"  : "Arsyiah Azahra",
                "nim"   : "121450035",
                "umur"  : "21",
                "asal"  : "Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi" : "Nugas",
                "sosmed": "@arsyiah.__",
                "kesan" : "Menjelaskan secara singkat tapi sangat informatif",  
                "pesan" : "Teruslah menjadi pribadi yang penuh semangat dan dedikasi"
            },
            {
                "nama"  : "Cintya Bella",
                "nim"   : "122450066",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Teluk",
                "hobbi" : "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan" : "Menyampaikan dengan tegas namun tetap sopan",  
                "pesan" : "Semoga selalu diberi semangat untuk berkembang dan maju"
            },
            {
                "nama"  : "Najla Juwairia",
                "nim"   : "122450037",
                "umur"  : "19",
                "asal"  : "Sumatera Utara",
                "alamat": "Airan",
                "hobbi" : "Menulis, Membaca, Fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan" : "Komunikasinya jelas, membuat kami lebih memahami konteks",  
                "pesan" : "Semoga perjalannya selalu lancar, baik di himpunan maupun di luar"
            },
            {
                "nama"  : "Rahma Neliyana",
                "nim"   : "122450036",
                "umur"  : "20",
                "asal"  : "Lampung",
                "alamat": "Sukarame",
                "hobbi" : "Baca Coding",
                "sosmed": "@rahmanellyana",
                "kesan" : "Friendly dan memberikan kesan yang positif",  
                "pesan" : "Semangat terus kak, semoga selalu diberkahi"
            },
            {
                "nama"  : "Try Yani Rizki Nur Rohmah",
                "nim"   : "122450020",
                "umur"  : "20",
                "asal"  : "Lampung Barat",
                "alamat": "Korpri",
                "hobbi" : "Bernyanyi dan Menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan" : "Menjelaskan dengan baik, mudah dipahami",  
                "pesan" : "Semoga harapannya dapat tewujud"
            },
            {
                "nama"  : "Muhammad Kaisar Firdaus",
                "nim"   : "121450135",
                "umur"  : "21",
                "asal"  : "Pesawaran",
                "alamat": "Pulau Damar",
                "hobbi" : "Lagi nyari",
                "sosmed": "@dino_lapet",
                "kesan" : "Dapat membuat suasana menjadi asik dan seru",  
                "pesan" : "Semoga segala tantangan yang dihadapi bisa dilalui dengan mudah"
            },
            {
                "nama"  : "Dwi Ratna Anggraeni",
                "nim"   : "122450008",
                "umur"  : "20",
                "asal"  : "Jambi",
                "alamat": "Jalan Durian 5 Pemda",
                "hobbi" : "Membaca",
                "sosmed": "@dwiratnn_",
                "kesan" : "Menghargai setiap tanggapan kami dengan baik",  
                "pesan" : "Semoga semua langkah ke depan berjalan dengan lancar."
            },
            {
                "nama"  : "Gymnastiar Al Khoarizmy",
                "nim"   : "122450096",
                "umur"  : "20",
                "asal"  : "Serang",
                "alamat": "Lapangan Golf UIN",
                "hobbi" : "Baca komik",
                "sosmed": "@jimnn.as",
                "kesan" : "Menunjukkan sikap terbuka untuk mendengar",  
                "pesan" : "Semoga selalu memiliki energi untuk mengejar impian yang lebih besar"
            },
             {
                "nama"  : "Nasywa Nur Afifah",
                "nim"   : "122450125",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Jalan Durian 1 Pemda",
                "hobbi" : "Nonton drakor",
                "sosmed": "@nsywanaf",
                "kesan" : "Menyampaikan informasi dengan penuh perhatian",  
                "pesan" : "Semoga selalu mampu menjaga semangat, bahkan di hari-hari sulit"
            },
            {
                "nama"  : "Priska Silvia Ferantiana",
                "nim"   : "122450053",
                "umur"  : "19",
                "asal"  : "Palembang",
                "alamat": "Jalan Nangka 2",
                "hobbi" : "Baca novel yang bikin nangis",
                "sosmed": "@prskslv",
                "kesan" : "Memberi arahan yang sangat jelas dan bermanfaat",  
                "pesan" : "Semoga hari-hari selalu penuh makna dan kelancaran"
            },
            {
                "nama"  : "Muhammad Arsal Ranjana Utama",
                "nim"   : "121450111",
                "umur"  : "21",
                "asal"  : "Depok",
                "alamat": "Jalan Nangka 4",
                "hobbi" : "Ngoding",
                "sosmed": "@arsal.utama",
                "kesan" : "Penyampaiannya mudah dipahami",  
                "pesan" : "Semoga hari-hari selalu penuh makna dan kelancaran"
            },
            {
                "nama"  : "Abit Ahmad Oktarian",
                "nim"   : "122450042",
                "umur"  : "19",
                "asal"  : "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi" : "Ngoding, Gaming",
                "sosmed": "@abitahmad",
                "kesan" : "Berbicara dengan tenang dan jelas",  
                "pesan" : "Semoga selalu temotivasi untuk terus berkembang"
            },
            {
                "nama"  : "Akmal Faiz Abdillah",
                "nim"   : "122450114",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi" : "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan" : "Memancarkan energi positif",  
                "pesan" : "Semoga selalu diberi kelancaran dalam setiap urusan"
            },
            {
                "nama"  : "Hermawan Manurung",
                "nim"   : "122450069",
                "umur"  : "20",
                "asal"  : "Bogor",
                "alamat": "Dekat jalan tol, Wisma Hana Hani",
                "hobbi" : "Bengong dan membaca buku",
                "sosmed": "@hermawan.mnrng",
                "kesan" : "Memberi kesan yang baik dan penuh perhatian",  
                "pesan" : "Semoga dipermudahkan dalam segala urusannya"
            },
            {
                "nama"  : "Khusnun Nisa",
                "nim"   : "122450078",
                "umur"  : "20",
                "asal"  : "Lampung Selatan",
                "alamat": "Belwis",
                "hobbi" : "Mengerjakan tugas",
                "sosmed": "@khusnun_nisa335",
                "kesan" : "Mendengarkan kami dengan baik",  
                "pesan" : "Semangat terus kak menjalani kuliahnya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1MKZog11Em9eBmhkMIrPFLYnuS04JAzLm", #bang yogy dn1
            "https://drive.google.com/uc?export=view&id=1MMAoQvGuz5jOXkkprOasPmjXZusLp8Xf", #kak ramadhita dn1
            "https://drive.google.com/uc?export=view&id=1Nyz-GQvzqXEK7dTe5UWIpI5WZPh48bl6", #kak nazwa dn1
            "https://drive.google.com/uc?export=view&id=1NcKRI4kz8h9LeaE7NrUm0iMl6SyBH6bO", #bang bastian dn1
            "https://drive.google.com/uc?export=view&id=1OLVezYCP62ROAu059b8fRpb-mIMsmirj", #kak dea dn1
            "https://drive.google.com/uc?export=view&id=1O0TZkX-i992YhjytYTijrywfPdbSrPlb", #kak esteria dn1
            "https://drive.google.com/uc?export=view&id=1O0G1nSf1m8_IjA_RhGOZFsk18LBzkGTJ", #kak natasya ega dn1
            "https://drive.google.com/uc?export=view&id=1NmThtVbH0oCzKqh4TubWXUQIZQ9g5594", #kak novelia dn1
            "https://drive.google.com/uc?export=view&id=1OcpKQziE2cDVgOvLDSZRunHIfK0xbHvv", #kak jasmine dn1
            "https://drive.google.com/uc?export=view&id=1Ne_YKKiaChfpMpt6w75O9jXfF_ybS_W4", #bang tobias dn1
            "https://drive.google.com/uc?export=view&id=1OZgcohUpmlfcnliWLp5YoOw2H9WH_6I6", #kak yohana dn1
            "https://drive.google.com/uc?export=view&id=1PKuhxcxPy_TfQJmT5iISHRKktnqKxCx8", #bang rizki dn1
            "https://drive.google.com/uc?export=view&id=1MUHgePoav5npMCNBAHTP_15YU8nLdab3", #bang arafi dn1
            "https://drive.google.com/uc?export=view&id=1P6JB27F1yeaLp1HXjDnLxMoqRT6RaanV", #kak uyi dn1
            "https://drive.google.com/uc?export=view&id=1ILdHALKB_KU_rl1I8iK4uTwKT3tk8DOU", #kak chalifia dn1
            "https://drive.google.com/uc?export=view&id=1NUtjz0C5hGd3LXqEHoerFGyjtoKOKNPf", #bang irvan dn1
            "https://drive.google.com/uc?export=view&id=1MIOtduUnqVm8rIdxL0t3oLajtNhrVS-C", #kak izza dn1
            "https://drive.google.com/uc?export=view&id=1N2iRRLQRDoNPKlqQOVFoJ6VsH4ZzeiCb", #kak zuhrah dn1
            "https://drive.google.com/uc?export=view&id=1MZqNa-8nHmVv2fbXFuXql-3bd5lh0WmK", #bang raid dn1
            "https://drive.google.com/uc?export=view&id=1NJ-0t3RtXyxms667D1yqiNBp7e_OMws_", #kak tria dn1
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
                "kesan" : "Penjelasannya ringkas tetapi informatif",  
                "pesan" : "Semangat terus mengejar mimpinya"
            },
            {
                "nama"  : "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan" : "Ramah dan mudah diajak bicara",  
                "pesan" : "Semoga hari-harinya berjalan dengan baik"
            },
            {
                "nama"  : "Nazwa Nabilla",
                "nim": "121450122",
                "umur": "21 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Way kandis",
                "hobbi": "Belajar",
                "sosmed": "@nazwanbilla",
                "kesan" : "Penyampaiannya mudah dipahami",  
                "pesan" : "Jangan lupa untuk semangat menjalani hari-harinya"
            },
            {
                "nama"  : "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21 Tahun",
                "asal": "Batam, Kepulauan Riau",
                "alamat": "Belwis",
                "hobbi": "Main game",
                "sosmed": "@bastiansilaban_",
                "kesan" : "Tenang dan penyampaiannya jelas",  
                "pesan" : "Semangat terus bang menggapai cita-citanya"
            },
            {
                "nama"  : "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20 Tahun",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Dengerin musik",
                "sosmed": "@deaa.rsn",
                "kesan" : "Sabar dan informatif dalam menjelaskan",  
                "pesan" : "Semoga dipenuhi dengan keberkahan"
            },
            {
                "nama"  : "Esteria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "19 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Belwis",
                "hobbi": "Main golf bareng kadiv",
                "sosmed": "@esteriars",
                "kesan" : "Baik dalam menjelaskan informasi",  
                "pesan" : "Semangat kuliahnya dan semoga diberi kelancaran"
            },
            {
                "nama"  : "Natasya Ega Lina",
                "nim": "122450024",
                "umur": "19 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Belwis",
                "hobbi": "Jadi humas",
                "sosmed": "@nateee__15",
                "kesan" : "Santai tapi tetap profesional",  
                "pesan" : "Semangat terus menjalani setiap kegiatan"
            },
            {
                "nama"  : "Novelia Adinda",
                "nim": "122450104",
                "umur": "21 Tahun",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan" : "Baik dan ramah",  
                "pesan" : "Semoga selalu diberikan ketenangan dalam menjalani kegiatan"
            },
            {
                "nama"  : "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Main sepak takraw",
                "sosmed": "@jasminednva",
                "kesan" : "Sikapnya positif, membawa kesan yang baik",  
                "pesan" : "Jangan lupa untuk terus semangat"
            },
            {
                "nama"  : "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20 Tahun",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Jogging",
                "sosmed": "@tobiassiagian",
                "kesan" : "Penjelasannya mudah dipahami dan informatif",  
                "pesan" : "Semangat terus mengejar cita-citanya"
            },
             {
                "nama"  : "Yohana Manik",
                "nim": "122450126",
                "umur": "19 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi": "Main Bowling",
                "sosmed": "@yo_annamnk",
                "kesan" : "Cara berbicaranya santai tapi tetap tegas",  
                "pesan" : "Semoga dikelilingi oleh orang-orang yang baik"
            },
            {
                "nama"  : "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21 Tahun",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobbi": "Bikin portofolio",
                "sosmed": "@rzkdrnnn",
                "kesan" : "Sabar dan baik dalam menjelaskan",  
                "pesan" : "Semangat terus bang bikin portofolionya"
            },
            {
                "nama"  : "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20 Tahun",
                "asal": "Bandung",
                "alamat": "Way Huwi",
                "hobbi": "Bertani",
                "sosmed": "@rafiramadhanmaulana",
                "kesan" : "Terbuka dalam mendengarkan pendapat",  
                "pesan" : "Semoga sukses terus ya bang"
            },
            {
                "nama"  : "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20 Tahun",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobbi": "Tepuk Semangat",
                "sosmed": "@u_yippy",
                "kesan" : "Pekerja keras dan dapat diandalkan",  
                "pesan" : "Semangat terus kak, jangan lupa untuk istirahat"
            },
            {
                "nama"  : "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20 Tahun",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Q Time",
                "sosmed": "@chlfawww",
                "kesan" : "Menunjukkan sikap yang positif",  
                "pesan" : "Semoga diberikan selalu diberikan kesehatan"
            },
            {
                "nama"  : "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21 Tahun",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton youtube, main game",
                "sosmed": "@alfaritziirvan",
                "kesan" : "Penjelasannya mudah untuk dipahami dan baik dalam menjelaskan",  
                "pesan" : "Semoga hari-harinya selalu dipenuhi hal positif"
            },
            {
                "nama"  : "Izza Lutfia",
                "nim": "122450090",
                "umur": "20 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Main Rubik",
                "sosmed": "@izzalutfia",
                "kesan" : "Semangat dan ramah dalam menjelaskan",  
                "pesan" : "Semoga segala yang Kakak lakukan berbalik menjadi kebaikan"
            },
            {
                "nama"  : "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@alyaavanevi",
                "kesan" : "Memberikan arahan dengan cara yang enak dan jelas",  
                "pesan" : "Semangat terus kak mengajinya"
            },
            {
                "nama"  : "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20 Tahun",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "telat",
                "sosmed": "@rayths_",
                "kesan" : "Menyampaikan dengan penuh perhatian",  
                "pesan" : "Jangan lupa untuk istirahat dan berdoa"
            },
            {
                "nama"  : "Tria Yunanni",
                "nim": "122450062",
                "umur": "20 Tahun",
                "asal": "Way Kanan",
                "alamat": "Sukarame",
                "hobbi": "Baca Buku",
                "sosmed": "@tria_y062",
                "kesan" : "Penyampaiannya jelas dan murah senyum",  
                "pesan" : "Semoga apa yang sedang dijalani dapat dilalui dengan baik "
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()  

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=15EFttnnvXS-7Sm7QXh_y8lFgEINciNbX", #bang dimas dn1
            "https://drive.google.com/uc?export=view&id=1YOLB2M107IzbQUrFVsE6WwGM6qMana0j", #kak catherine dn1
            "https://drive.google.com/uc?export=view&id=1bstxQLaGEDwZ3N8WdwfySvZXu5zhsdXW", #bang akbar dn1
            "https://drive.google.com/uc?export=view&id=1QhqR1shEaS4yX4PCtbpgpdfHTLAyjGTf", #kak rani dn1
            "https://drive.google.com/uc?export=view&id=177R0HOJELiV7C8JDNdcHdIWDQxy2LCY5", #bang rendra dn1
            "https://drive.google.com/uc?export=view&id=1MfxXK7gIaOrrzLt_X-G7LKkWfF4_FO_v", #kak salwa dn1
            "https://drive.google.com/uc?export=view&id=1Dc6cEIigpcTRpYxg2QVb2dQSJhmBjS-a", #bang yosia dn1
            "https://drive.google.com/uc?export=view&id=1aMX5e8uTAgtKO8yfGENnuWX4b6aWkEr9", #bang ari dn1
            "https://drive.google.com/uc?export=view&id=1JphnAYCdOaVlRRTr1rq2dPZIGY4wuLCg", #kak azizah dn1
            "https://drive.google.com/uc?export=view&id=1jtTUSdZvngujnOow_-2u7MJWLsdh-9gx", #kak meira dn1
            "https://drive.google.com/uc?export=view&id=1FQ-dgjgOB2rbmIpOFd8eTfbC1oOn_GQn", #bang rendi dn1
            "https://drive.google.com/uc?export=view&id=1HVcwvlZKRiOz1Jzj1cb_Et2SEyNMVmf0", #kak renta dn1
            "https://drive.google.com/uc?export=view&id=1Vc2-b-NGIRgjvyLBtH-BzFUT0gInX84p", #bang josua dn1

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
                "kesan" : "Pekerja keras dan sangat peduli terhadap himpunan",  
                "pesan" : "Semangat terus bang menjalankan tugasnya, jangan lupa untuk istirahat"
            },
            {
                "nama"  : "Catherine Firdhasari Maulina Sinaga",
                "nim"   : "121450072",
                "umur"  : "20",
                "asal"  : "Sumatera Utara",
                "alamat": "Airan",
                "hobbi" : "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan" : "Tenang dan penuh perhatian",  
                "pesan" : "Semoga apa yang hari-harinya dipenuhi kebahagiaan"
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
                "kesan" : "Membantu menjelaskan terkait himpunan",  
                "pesan" : "Semangat bang kuliahnya semoga dilancarkan urusannya"
            },
            {
                "nama"  : "Rani Puspita sari",
                "nim"   : "122450030",
                "umur"  : "20",
                "asal"  : "Kota Metro",
                "alamat": "Rajabasa",
                "hobbi" : "Dengar musik",
                "sosmed": "@ranniu",
                "kesan" : "Penjelasannya mudah dipahami dan informatif",  
                "pesan" : "Semoga terus hari-harinya terus bahagia"
            },
            {
                "nama"  : "Rendra Eka Prayoga",
                "nim"   : "122450112",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Belwis",
                "hobbi" : "Mancing Ikan Mas",
                "sosmed": "@rendraepr",
                "kesan" : "Dapat membuat suasana menjadi menyenangkand dan santai",  
                "pesan" : "Semangat terus bang mancing ikan masnya"
            },
            {
                "nama"  : "Salwa Farhanatussaidah",
                "nim"   : "122450055",
                "umur"  : "20",
                "asal"  : "Pesawaran",
                "alamat": "Airan",
                "hobbi" : "Nonton",
                "sosmed": "@slwfhn_694",
                "kesan" : "Pendengar yang baik dan perhatian",  
                "pesan" : "Semoga dapat terus menjadi orang yang perhatian"
            },
            {
                "nama"  : "Yosia Letare Banurea",
                "nim"   : "121450149",
                "umur"  : "20",
                "asal"  : "Dairi, Sumatera Utara",
                "alamat": "Perum Griya Indah",
                "hobbi" : "Tidur",
                "sosmed": "@yosiabanurea",
                "kesan" : "Santai tapi jelas dalam menyampaikan arahannya",  
                "pesan" : "Semoga dapat terus bersemangat dalam menjalai hari-harinya"
            },
            {
                "nama"  : "Ari Sigit",
                "nim"   : "121450069",
                "umur"  : "23",
                "asal"  : "Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobbi" : "Futsal",
                "sosmed": "@ari_sigit17",
                "kesan" : "Santai,ramah, mudah bergaul",  
                "pesan" : "Semoga apa yang diinginkan dapat segera tercapai"
            },
            {
                "nama"  : "Azizah Kusumah Putri",
                "nim"   : "122450068",
                "umur"  : "21",
                "asal"  : "Lampung Selatan",
                "alamat": "Natar",
                "hobbi" : "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan" : "Ramah dan baik dalam menyampaikan informasi",  
                "pesan" : "Semangat berkebunnya kak"
            },
            {
                "nama"  : "Meira Listyaningrum",
                "nim"   : "122450011",
                "umur"  : "20",
                "asal"  : "Pesawaran",
                "alamat": "Airan",
                "hobbi" : "Membaca",
                "sosmed": "@meirasty_",
                "kesan" : "Informatif dan murah senyum dalam menjelaskan",  
                "pesan" : "Jangan lupa untuk memulai hari dengan semangat"
            },
            {
                "nama"  : "Rendi Alexander Hutagalung",
                "nim"   : "122450057",
                "umur"  : "20",
                "asal"  : "Tangerang",
                "alamat": "Kost Benawang",
                "hobbi" : "Menyanyi",
                "sosmed": "@rexander",
                "kesan" : "Friendly, tidak ragu untuk mnenjelaskan sesuatu",  
                "pesan" : "Semangat nyanyinya kak, semoga terus berkembang"
            },
            {
                "nama"  : "Renta Siahaan",
                "nim"   : "122450070",
                "umur"  : "21",
                "asal"  : "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi" : "Membaca dan Memancing",
                "sosmed": "@renta.shn",
                "kesan" : "Detail dalam menjelaskan",  
                "pesan" : "Semoga kegiatannya selalu dilancarkan dan dipenuhi dengan hal-hal positif"
            },
            {
                "nama"  : "Josua Panggabean",
                "nim"   : "122450061",
                "umur"  : "21",
                "asal"  : "Pematang Siantar",
                "alamat": "Gerbang Barat",
                "hobbi" : "Menonton",
                "sosmed": "@josuapanggabean_",
                "kesan" : "Mudah bergaul, baik, dan ramah",  
                "pesan" : "Semoga selalu sukses dan tetap semangat"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()   

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1LtywQ9qgVgmaD6OPCJYrGL89QR1nXtVO", #bang andrian dn1
            "https://drive.google.com/uc?export=view&id=1LAv7XVfdw3TwR626deCiJSXSbLpemRCk", #kak adisty dn1
            "https://drive.google.com/uc?export=view&id=1LHTZeil281-_PxDlxUPo4vDfQDBmGhIC", #kak nabilla dn1
            "https://drive.google.com/uc?export=view&id=1LmyuAx683K7_HAtSdntdFRwuM_pzJMcI", #bang danang dn1
            "https://drive.google.com/uc?export=view&id=1KhDjfsBJSV-rHq7lOlfFwVMWAOa5_We4", #bang farrel dn1
            "https://drive.google.com/uc?export=view&id=1LfJ2rX0AGjmPmuRrSfGO9pt0bRzUj_3R", #kak nabilah dn1
            "https://drive.google.com/uc?export=view&id=1L0uo639Do7Z66AwJQ1RwxuSl6e_z3i42", #kak alvia dn1
            "https://drive.google.com/uc?export=view&id=1Ks9I3-O771sW1GK3eX_A9KIOR1Xx_5wb", #bang dhafin dn1
            "https://drive.google.com/uc?export=view&id=1KqdRaY4iUrG2fmBedSCtJ-qxMtXbJqxw", #kak elia dn1


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
                "kesan" : "Informatif dalam menjelaskan dan dapat mencairkan suasana",  
                "pesan" : "Semangat menjalani kegiatannya, semoga dilancarkan"
            },
            {
                "nama"  : "Adisty Syawalda Ariyanto",
                "nim"   : "121450136",
                "umur"  : "22",
                "asal"  : "Metro",
                "alamat": "Sukarame ",
                "hobbi" : "Nonton Film",
                "sosmed": "@adistysa_",
                "kesan" : "Profesional dalam menjalani tugas",  
                "pesan" : "Semoga apa selalu dikelilingi oleh orang-orang baik"
            },
            {
                "nama"  : "Nabila Azhari",
                "nim"   : "121450029",
                "umur"  : "21",
                "asal"  : "Simalungun",
                "alamat": "Airan ",
                "hobbi" : "Menghitung Uang",
                "sosmed": "@zhjung",
                "kesan" : "Mendetail dalam menjelaskan sesuatu",  
                "pesan" : "Semangat terus kerjain tugas-tugasnya"
            },
            {
                "nama"  : "Danang Hilal Kurniawan",
                "nim"   : "122450085",
                "umur"  : "21",
                "asal"  : "Bandar Lampung",
                "alamat": "Airan",
                "hobbi" : "Belajar",
                "sosmed": "@dananghk_",
                "kesan" : "Memberikan penjelasan yang rapi dan santai",  
                "pesan" : "Semangat belajarnya, semoga sukses"
            },
            {
                "nama"  : "Farrel Julio Akbar",
                "nim"   : "122450110",
                "umur"  : "20",
                "asal"  : "Bogor",
                "alamat": "Lapas",
                "hobbi" : "Kayang",
                "sosmed": "@farel_julio",
                "kesan" : "Baik dan profesional tapi tetap santai",  
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
                "kesan" : "Pembawaanya tenang bikin suasana jadi santai",  
                "pesan" : "Dilancarkan terus segalam urusannya baik akademik maupun non-akademik"
            },
            {
                "nama"  : "Alvia Asrinda Br.Gintng",
                "nim"   : "122450077",
                "umur"  : "20",
                "asal"  : "Binjai",
                "alamat": "Korpri",
                "hobbi" : "Nonton Winda",
                "sosmed": "@alviagnting",
                "kesan" : "Pendengar yang baik ",  
                "pesan" : "Semoga hari-harinya dilalui dengan baik"
            },
            {
                "nama"  : "Dhafin Razaqa Luthfi",
                "nim"   : "122450133",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi" : "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan" : "Memancarkan energi yang postifi",  
                "pesan" : "Semangat terus olahraganya"
            },
            {
                "nama"  : "Elia Meylani Simanjuntak",
                "nim"   : "122450026",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Korpri",
                "hobbi" : "Main Alat Musik",
                "sosmed": "@meylanielia",
                "kesan" : "Menjalankan tugas dengan profesional",  
                "pesan" : "Semangat terus menggapai cita-citanya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()    
# Tambahkan menu lainnya sesuai kebutuhan