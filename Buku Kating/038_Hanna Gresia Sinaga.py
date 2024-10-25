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
            "Departemen MEDKRAF",
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
            "https://drive.google.com/uc?export=view&id=1n4DPSHmTzmmZ779mofsn_rCaIf1rZ14p", #Bang Kharisma
            "https://drive.google.com/uc?export=view&id=1ch2uIIgRzInrzsN6gIqWRdFDOmteBpU6", #Bang Pandra
            "https://drive.google.com/uc?export=view&id=1Y2sGes6Cahv2coEcBLUdBOv6gM-7LeHO",
            "https://drive.google.com/uc?export=view&id=1ChgSlBK3RjOOtxKpp4E61Z2M4a7k3QPN",
            "https://drive.google.com/uc?export=view&id=1JoBaabzUvaTqL6TDK_qR_np_ymesoGF1",
            "https://drive.google.com/uc?export=view&id=1WaqGwL2JR2C6jSVn0Ep1BGeYXoaW_-qR",


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
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Pandra Insani Putra Azwan",
                "nim": "121450137",
                "umur": "21",
                "asal":"Bukitr Kemuning(Lampung Utara)",
                "alamat": "Bawen 2",
                "hobbi": "Bermain gitar dan menyanyi",
                "sosmed": "@pandrainsni27",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam(Sumatera Selatan)",
                "alamat": "Kota baru",
                "hobbi": "Nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh(Sumatera Selatan)",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin bang pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "",  
                "pesan":""
            },
            {
                "nama": "Nadilla Andara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kota Baru",
                "hobbi": "Membaca",
                "sosmed": "@ndillaandr26",
                "kesan": "",  
                "pesan":"!"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=10qo2JDOdtccDrcF2LoZZPr91FEB3sQOW",
            "https://drive.google.com/uc?export=view&id=113xDgOL542OFGWTsAvlpXmQSJdp4QLHK",
            "https://drive.google.com/uc?export=view&id=10r5W-KQFmnY8mZd8LQ17olVN4wHUV01l",
            "https://drive.google.com/uc?export=view&id=10dgu-tiCoMsUctMxVsiQeoRAJ_qDsfQp",
            "https://drive.google.com/uc?export=view&id=11DzIT1wjdlWxBiLsvEEsqUdf9jptj7cM",
            "https://drive.google.com/uc?export=view&id=10jzbVwW2tW3RMN-myDsy4VuIXcWlwfy-",
            "https://drive.google.com/uc?export=view&id=10im39fqQu5jKoB1La9w9mZknFp6kDSOn",
            "https://drive.google.com/uc?export=view&id=1tvgFgrnnD2Xmhn_8P6Qc2i3ZTD97zWBp",
            "https://drive.google.com/uc?export=view&id=116zSZ548YgMwjXAoyimgoulvFkzTWHlW",
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
                "kesan" : "",  
                "pesan" : ""
            },
            {
                "nama"  : "Annisa Cahyani Surya",
                "nim"   : "121450114",
                "umur"  : "21",
                "asal"  : "Tanggerang Selatan",
                "alamat": "Way Huwi",
                "hobbi" : "Membaca, Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan" : "",  
                "pesan" : ""
            },
            {
                "nama"  : "Wulan Sabina",
                "nim"   : "121450150",
                "umur"  : "21",
                "asal"  : "Medan",
                "alamat": "Raden Saleh",
                "hobbi" : "Nonton Drakor",
                "sosmed": "@wlnsbn0",
                "kesan" : "",  
                "pesan" : ""
            },
            {
                "nama"  : "Annisa Dini Amaliya",
                "nim"   : "121450081",
                "umur"  : "21",
                "asal"  : "Tanggerang",
                "alamat": "Jati Agung",
                "hobbi" : "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan" : "",  
                "pesan" : ""
            },
            {
                "nama"  : "Anisa Fitriyani",
                "nim"   : "121450150",
                "umur"  : "21",
                "asal"  : "Medan",
                "alamat": "Raden Saleh",
                "hobbi" : "Nonton Drakor",
                "sosmed": "@wlnsbn0",
                "kesan" : "",  
                "pesan" : ""
            },
            {
                "nama"  : "Mirzan Yusuf Rabbani",
                "nim"   : "122450118",
                "umur"  : "20",
                "asal"  : "Jakarta",
                "alamat": "Korpri",
                "hobbi" : "Main Kucing",
                "sosmed": "@myrrinn",
                "kesan" : "",  
                "pesan" :""
            },
            {
                "nama"  : "Dhea Amelia Putri",
                "nim"   : "122450004",
                "umur"  : "20",
                "asal"  : "Sukabumi, Jawa Barat",
                "alamat": "Natar",
                "hobbi" : "Suka Ikut Tes SKD",
                "sosmed": "@dhea_wedding",
                "kesan" : "",  
                "pesan" : ""
            },
            {
                "nama"  : "Berlianda Enda Putri",
                "nim"   : "122450065",
                "umur"  : "21",
                "asal"  : "Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi" : "Main Game",
                "sosmed": "@berlyyanda",
                "kesan" : "",  
                "pesan" : ""
            },
            {
                "nama"  : "Jeremia Susanto",
                "nim"   : "122450022",
                "umur"  : "20",
                "asal"  : " Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi" : "Marah-marah",
                "sosmed": "@jeremia_s_",
                "kesan" : "",  
                "pesan" : ""
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


# Tambahkan menu lainnya sesuai kebutuhan
