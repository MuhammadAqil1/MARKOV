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
            "https://drive.google.com/uc?export=view&id=1Y2sGes6Cahv2coEcBLUdBOv6gM-7LeHO", #kak meliza
            "https://drive.google.com/uc?export=view&id=1ChgSlBK3RjOOtxKpp4E61Z2M4a7k3QPN", #kak putri
            "https://drive.google.com/uc?export=view&id=1JoBaabzUvaTqL6TDK_qR_np_ymesoGF1", #kak hartiti
            "https://drive.google.com/uc?export=view&id=1WaqGwL2JR2C6jSVn0Ep1BGeYXoaW_-qR", #kak nadilla


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
                "kesan": "seru diajak ngobrol",  
                "pesan":"tetap seseru ini terus bang"
            },
            {
                "nama": "Pandra Insani Putra Azwan",
                "nim": "121450137",
                "umur": "21",
                "asal":"Bukitr Kemuning(Lampung Utara)",
                "alamat": "Bawen 2",
                "hobbi": "Bermain gitar dan menyanyi",
                "sosmed": "@pandrainsni27",
                "kesan": "asik orangnya",  
                "pesan":"tetap seasik ini terus bang"
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal":"Pagar Alam(Sumatera Selatan)",
                "alamat": "Kota baru",
                "hobbi": "Nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "baik cara ngomongnya",  
                "pesan":"tetap baik terus gitu ya kak cara ngomongnya, enak didengar"
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal":"Payakumbuh(Sumatera Selatan)",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin bang pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "pendiam kakaknya",  
                "pesan":"semoga kita bisa ngobrol lebih banyak kak"
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal":"Palembang",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "ramah kakanya",  
                "pesan":"tetap senantiasa ramah seperti itu kak"
            },
            {
                "nama": "Nadilla Andara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal":"Metro",
                "alamat": "Kota Baru",
                "hobbi": "Membaca",
                "sosmed": "@ndillaandr26",
                "kesan": "murah senyum kakaknya",  
                "pesan":"tetap sering-sering senyum kak, manis soalnya"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=10qo2JDOdtccDrcF2LoZZPr91FEB3sQOW", #kak tri
            "https://drive.google.com/uc?export=view&id=113xDgOL542OFGWTsAvlpXmQSJdp4QLHK", #kak anissa cahyani surya
            "https://drive.google.com/uc?export=view&id=10r5W-KQFmnY8mZd8LQ17olVN4wHUV01l", #kak wulan sabina
            "https://drive.google.com/uc?export=view&id=10dgu-tiCoMsUctMxVsiQeoRAJ_qDsfQp", #kak anisa dini amalia
            "https://drive.google.com/uc?export=view&id=11DzIT1wjdlWxBiLsvEEsqUdf9jptj7cM", #kak anisa fitriyani
            "https://drive.google.com/uc?export=view&id=10jzbVwW2tW3RMN-myDsy4VuIXcWlwfy-", #bang mirzan
            "https://drive.google.com/uc?export=view&id=10im39fqQu5jKoB1La9w9mZknFp6kDSOn", #kak dhea
            "https://drive.google.com/uc?export=view&id=1Et7AXjaJ1xUsX9Uw5V90wTrSPzpKZRKT", #bang fahrul
            "https://drive.google.com/uc?export=view&id=10Tza6KPQnuXH_ue5lSQviU3ePIdmV7xc", #kak berliana
            "https://drive.google.com/uc?export=view&id=116zSZ548YgMwjXAoyimgoulvFkzTWHlW", #bang jeremi
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
                "kesan" : "Kakak baik banget, bikin suasana jadi santai dan nyaman.",  
                "pesan" : "Makasih ya, Kak, atas semangatnya, semoga bisa sering ketemu lagi."
            },
            {
                "nama"  : "Annisa Cahyani Surya",
                "nim"   : "121450114",
                "umur"  : "21",
                "asal"  : "Tanggerang Selatan",
                "alamat": "Way Huwi",
                "hobbi" : "Membaca, Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan" : "Kakak sangat ramah dan bijaksana, memberi motivasi buat terus berkembang.",  
                "pesan" : "Terima kasih atas inspirasinya, semoga bisa sering diskusi lagi."
            },
            {
                "nama"  : "Wulan Sabina",
                "nim"   : "121450150",
                "umur"  : "21",
                "asal"  : "Medan",
                "alamat": "Raden Saleh",
                "hobbi" : "Nonton Drakor",
                "sosmed": "@wlnsbn0",
                "kesan" : "Seru dan asyik diajak ngobrol, sangat terbuka.",  
                "pesan" : " Terima kasih sudah membagi pengalaman ya kak, sangat membantu kami."
            },
            {
                "nama"  : "Annisa Dini Amaliya",
                "nim"   : "121450081",
                "umur"  : "21",
                "asal"  : "Tanggerang",
                "alamat": "Jati Agung",
                "hobbi" : "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan" : "Kakak menyenangkan dan penuh energi positif.",  
                "pesan" : "Terima kasih untuk inspirasinya Kak, sukses selalu!"
            },
            {
                "nama"  : "Anisa Fitriyani",
                "nim"   : "121450150",
                "umur"  : "21",
                "asal"  : "Medan",
                "alamat": "Raden Saleh",
                "hobbi" : "Nonton Drakor",
                "sosmed": "@wlnsbn0",
                "kesan" : "Kakak sangat perhatian dan sabar dalam menjawab pertanyaan.",  
                "pesan" : "Makasih Kak, saya jadi lebih yakin. Semoga bisa belajar lebih banyakdari kakak."
            },
            {
                "nama"  : "Mirzan Yusuf Rabbani",
                "nim"   : "122450118",
                "umur"  : "20",
                "asal"  : "Jakarta",
                "alamat": "Korpri",
                "hobbi" : "Main Kucing",
                "sosmed": "@myrrinn",
                "kesan" : "Kakak humble dan rendah hati, bikin nyaman.",  
                "pesan" : "Terima kasih sudah mendengarkan, Kak, semoga bisa sering ngobrol."
            },
            {
                "nama"  : "Dhea Amelia Putri",
                "nim"   : "122450004",
                "umur"  : "20",
                "asal"  : "Sukabumi, Jawa Barat",
                "alamat": "Natar",
                "hobbi" : "Suka Ikut Tes SKD",
                "sosmed": "@dhea_wedding",
                "kesan" : "Kakak pintar dan komunikatif, memberi wawasan baru.",  
                "pesan" : "Makasih Kak, obrolan kita sangat menginspirasi!"
            },
            {
                "nama"  : "Muhammad Fahrul Aditya",
                "nim"   : "121450156",
                "umur"  : "22",
                "asal"  : "Surakarta, Jawa Tengah",
                "alamat": "Pahoman",
                "hobbi" : "Melukis, badminton, hiking, ngopi, dengerin music, nonton film dan ngoding",
                "sosmed": "@fhrul.pdf",
                "kesan" : "Kakak sangat peduli dan memberi motivasi.",  
                "pesan" : "Terima kasih atas semangatnya, saya jadi lebih optimis."
            },
            {
                "nama"  : "Berlianda Enda Putri",
                "nim"   : "122450065",
                "umur"  : "21",
                "asal"  : "Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi" : "Main Game",
                "sosmed": "@berlyyanda",
                "kesan" : "Kakak ramah dan penuh semangat, bikin termotivasi.",  
                "pesan" : "Makasih, Kak, semoga bisa ketemu dan ngobrol lagi!"
            },
            {
                "nama"  : "Jeremia Susanto",
                "nim"   : "122450022",
                "umur"  : "20",
                "asal"  : " Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi" : "Marah-marah",
                "sosmed": "@jeremia_s_",
                "kesan" : "Kakak humble banget dan enak diajak cerita.",  
                "pesan" : "Terima kasih, Kak, atas semangat dan inspirasi yang diberi."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()
elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=122sr7a2T3imcdHbTSlySQFzriYEfPmUE", #kak lutfi
            "https://drive.google.com/uc?export=view&id=124Mg4Posk8afHHw3-9CLQ6CRuA7INVg2", #bang bintang
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
                "kesan" : "Kakak asyik dan ramah, mudah diajak diskusi.",  
                "pesan" : "Terima kasih sudah meluangkan waktu Kak, semoga bisa sering ngobrol dengan kakak."
            },
            {
                "nama"  : "Rian Bintang Wijaya",
                "nim"   : "122450094",
                "umur"  : "20",
                "asal"  : "Palembang, Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi" : "Mendengar Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan" : "Positif dan sangat menghargai pendapat.",  
                "pesan" : "Terima kasih bang, semoga bisa ngobrol lagi di lain waktu."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1IRbxjqzBpGdx5VqteIRSYxR39u1jFBJB",#bang erickson
            "https://drive.google.com/uc?export=view&id=1Ybg-EZY8Yluu2wiIJDHjYyT3_0l5mm21",#kak abeth
            "https://drive.google.com/uc?export=view&id=16jQU_xkzKibwqwgBhPl6iu6ohs2-CEM7",#kak afifah
            "https://drive.google.com/uc?export=view&id=1-bpdl6LPhmpAOV0O-X3ojiEVKKD_zv35",#kak allya
            "https://drive.google.com/uc?export=view&id=1MSRhojFfHNmNySda96s1tvma4tbnyvO-",#kak hanum
            "https://drive.google.com/uc?export=view&id=1SWv6LoSJGV-YSZRhexpMaGyevLY3UnDc",#bang ferdy
            "https://drive.google.com/uc?export=view&id=1jZ9__yb4dgFhsawDcoh9oW8zpQgt5QMq",#bang deri
            "https://drive.google.com/uc?export=view&id=1KAXtCp3BOHBlHpHsXDyxjyx1dtboscBe",#kak oktavia
            "https://drive.google.com/uc?export=view&id=1BMi4U-nNqXk43OEEEA5VsjgpkWX-3raF",#bang deyvan 
            "https://drive.google.com/uc?export=view&id=1GEtoUmMBE2TdZiL0RT_LjpJ6RSFVqUL-",#bang ibnu
            "https://drive.google.com/uc?export=view&id=14i7r2s7XS9kDwzZK3THoSpxeCUzeAdlh",#bang jo
            "https://drive.google.com/uc?export=view&id=1iOIa65FglTVBLv9toMuTIvyL9soFQUyN",#bang kemas
            "https://drive.google.com/uc?export=view&id=1NeGxkwre_DiWPNq-HxJ_3NbMHXAlvxsY",#bang leonard
            "https://drive.google.com/uc?export=view&id=1vRPFGUK59Jt4SmRS_q8Zalff2Uo9t46h",#kak presilia
            "https://drive.google.com/uc?export=view&id=1_G-M52IvIPnC4wE-vDEB5wE3rOgNne6Z",#kak rafa
            "https://drive.google.com/uc?export=view&id=1SR94zByoS8M3q0k41DlRl2KU9T7CeouP",#bang sahid 
            "https://drive.google.com/uc?export=view&id=1ukYx733u8hC-pxQIG97zeDND9ahvsMpw",#kak vanes 
            "https://drive.google.com/uc?export=view&id=1LLx2uY6EHxYZ_ADa9aJ7T8qVAVF87xv-",#bang ateng
            "https://drive.google.com/uc?export=view&id=1N2Qry9XzJHVxeVQ3O2HV6ehu-ZmKk9PQ",#bang gede
            "https://drive.google.com/uc?export=view&id=1_PWoq16CIPh2gk1w8MZZna6YoHElYGwx",#kak jaclin
            "https://drive.google.com/uc?export=view&id=1Y6-Ysu--xdlSJqB_uqJZNpInrTY3pFsC",#bang rafly
            "https://drive.google.com/uc?export=view&id=1QqOkliy-pPYPmhDYXvDonh3NhB7qSH1D",#kak dini
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
                "kesan" : "Sangat suportif dan terbuka.",  
                "pesan" : "Makasih bang, jadi tambah semangat setelah obrolan ini."
            },
            {
                "nama"  : "Elisabeth Claudia Simanjuntak",
                "nim"   : "122450123",
                "umur"  : "18",
                "asal"  : "Pekanbaru",
                "alamat": "Sukarame",
                "hobbi" : "Memancing keributan",
                "sosmed": "@celisabethh_",
                "kesan" : "Kakak menginspirasi dan sabar, bikin nyaman.",  
                "pesan" : "Makasih Kak, obrolan kemarin memberi banyak pelajaran."
            },
            {
                "nama"  : "Nisrina Nur Afifah",
                "nim"   : "122450052",
                "umur"  : "19",
                "asal"  : "Bekasi",
                "alamat": "Sukarame",
                "hobbi" : "Nabok orang",
                "sosmed": "@afifahhnsrn",
                "kesan" : "Kakak rendah hati dan memberikan arahan yang bagus.",  
                "pesan" : "Terima kasih atas bimbingannya Kak, sukses terus ya."
            },
            {
                "nama"  : "Allya Nurul Islami Pasha",
                "nim"   : "122450033",
                "umur"  : "20",
                "asal"  : "Sumatera Barat",
                "alamat": "Gang Perwira, Belwis",
                "hobbi" : "Nonton Dracin",
                "sosmed": "@allyaislami_",
                "kesan" : "Kakak menyenangkan dan terbuka dalam sharing.",  
                "pesan" : "Makasih Kak, saya jadi lebih paham berkat sharing-nya."
            },
            {
                "nama"  : "Farahanum Afifah Ardiansyah",
                "nim"   : "122450056",
                "umur"  : "20",
                "asal"  : "Padang, Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi" : "Tidur",
                "sosmed": "@farahanumafifahh",
                "kesan" : "Kakak sabar dan komunikatif, memberikan banyak tips.",  
                "pesan" : "Terima kasih banyak atas arahannya, sangat bermanfaat."
            },
            {
                "nama"  : "Ferdy Kevin Naibaho",
                "nim"   : "122450107",
                "umur"  : "19",
                "asal"  : "Medan, Sumatera Utara",
                "alamat": "Jalan Senopati Raya 18",
                "hobbi" : "Dengerin Rocky Gerung",
                "sosmed": "@ferdy_kevin",
                "kesan" : "santai dan ramah, bikin ngobrolnya asik.",  
                "pesan" : "Makasih bang, untuk waktunya. Semoga kita bisa belajar bersama."
            },
            {
                "nama"  : "M. Deriansyah Okutra",
                "nim"   : "122450101",
                "umur"  : "19",
                "asal"  : "Kayu Agung",
                "alamat": "Jalan Pagar Alam",
                "hobbi" : "Bercerita horror",
                "sosmed": "@dransyh_",
                "kesan" : "Sangat memberi motivasi dan inspirasi.",  
                "pesan" : "Terima kasih banyak bang, obrolan kemarin jadi penyemangat!"
            },
            {
                "nama"  : "Oktavia Nurwenda Puspita Sari",
                "nim"   : "122450041",
                "umur"  : "20",
                "asal"  : "Lampung Timur",
                "alamat": "Way Hui",
                "hobbi" : "Memasak",
                "sosmed": "@_oktavianrwnda_",
                "kesan" : "Kakak perhatian dan peduli pada perkembangan kita.",  
                "pesan" : "Makasih Kak, semoga bisa terus berhubungan."
            },
            {
                "nama"  : "Deyvan Loxefal",
                "nim"   : "121450148",
                "umur"  : "21",
                "asal"  : "Riau",
                "alamat": "Pulau Damar",
                "hobbi" : "Belajar",
                "sosmed": "@depanloo",
                "kesan" : " Kakak humoris, bikin suasana obrolan lebih santai.",  
                "pesan" : "Terima kasih ya bang, sharing-nya sangat membantu."
            },
            {
                "nama"  : "Ibnu Farhan Al-Ghifari",
                "nim"   : "121450121",
                "umur"  : "21",
                "asal"  : "Jambi",
                "alamat": "Pulau Damar, Kobam",
                "hobbi" : "Bermain Game Online",
                "sosmed": "@al_ghifari032",
                "kesan" : "abang komunikatif ",  
                "pesan" : "sukses terus bang"
            },
             {
                "nama"  : "Johannes Krisjon Silitonga",
                "nim"   : "122450043",
                "umur"  : "19",
                "asal"  : "Tanggerang",
                "alamat": "Jalan Lapas",
                "hobbi" : "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan" : "Sangat humble dan rendah hati.",  
                "pesan" : "Terima kasih sudah meluangkan waktu dan semangat, bang."
            },
            {
                "nama"  : "Kemas Veriandra Ramadhan",
                "nim"   : "122450016",
                "umur"  : "19",
                "asal"  : "Bekasi",
                "alamat": "Golf Asri",
                "hobbi" : "Bermain ular python digital",
                "sosmed": "@kemasverii",
                "kesan" : "Ramah dan sangat menyenangkan.",  
                "pesan" : "Makasih banyak bang, tetap tambah semangat!"
            },
            {
                "nama"  : "Leonard Andreas Napitupulu",
                "nim"   : "121450153",
                "umur"  : "21",
                "asal"  : "Sumatera Utara",
                "alamat": "Kobam",
                "hobbi" : "Belajar",
                "sosmed": "@lnrd.__",
                "kesan" : "Inspiratif dan motivasional.",  
                "pesan" : "Terima kasih bang, semoga bisa ngobrol lebih banyak."
            },
            {
                "nama"  : "Presilia",
                "nim"   : "122450081",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Kota Baru",
                "hobbi" : "Tidur",
                "sosmed": "@presiliamg",
                "kesan" : " Kakak suportif dan penuh semangat.",  
                "pesan" : "Terima kasih, Kak, semoga bisa terus belajar dari kakak."
            },
            {
                "nama"  : "Rafa Aqilla Jungjunan",
                "nim"   : "122450148",
                "umur"  : "20",
                "asal"  : "Riau",
                "alamat": "Belwis",
                "hobbi" : "Membaca webtoon",
                "sosmed": "@rafaaqilla",
                "kesan" : "Bijak dalam memberi nasihat.",  
                "pesan" : "Makasih Kak, semua nasihatnya sangat bermanfaat."
            },
            {
                "nama"  : "Sahid Maulana",
                "nim"   : "122450109",
                "umur"  : "21",
                "asal"  : "Depok, Jawa Barat",
                "alamat": "Airan Raya",
                "hobbi" : "Bermain Game",
                "sosmed": "@sahid_maul19",
                "kesan" : "Kakak baik hati dan sangat suportif.",  
                "pesan" : "Terima kasih, Kak, untuk motivasi yang sangat berarti."
            },
            {
                "nama"  : "Vanessa Olivia Rose",
                "nim"   : "121450068",
                "umur"  : "20",
                "asal"  : "Jakarta",
                "alamat": "Perumahan Korpri",
                "hobbi" : "Belajar",
                "sosmed": "@roselivnes__",
                "kesan" : "Kakak punya banyak ide kreatif dan inspiratif.",  
                "pesan" : "Makasih banyak, Kak, semoga bisa sering berdiskusi."
            },
            {
                "nama"  : "M. Farhan Athaulloh",
                "nim"   : "121450117",
                "umur"  : "21",
                "asal"  : "Bandar Lampung",
                "alamat": "Kota Baru",
                "hobbi" : "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan" : " Kakak ramah dan sabar mendengarkan cerita.",  
                "pesan" : " Terima kasih, Kak, untuk motivasinya yang sangat berharga."
            },
            {
                "nama"  : "Gede Moena",
                "nim"   : "121450014",
                "umur"  : "21",
                "asal"  : "Bekasi",
                "alamat": "Korpri Raya",
                "hobbi" : "Belajar dan main game",
                "sosmed": "@gedemoenaa",
                "kesan" : "Kakak baik dan supportive banget.",  
                "pesan" : "Terima kasih banyak, Kak. wawancara kemarin sangat berarti."
            },
            {
                "nama"  : "Jaclin Alcavella",
                "nim"   : "122450015",
                "umur"  : "19",
                "asal"  : "Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi" : "Berenang",
                "sosmed": "@jaclinalcv_",
                "kesan" : "Kakak menginspirasi dan bikin termotivasi.",  
                "pesan" : "Makasih ya, Kak, semoga bisa belajar lebih banyak."
            },
            {
                "nama"  : "Rafly Prabu Darmawan",
                "nim"   : "122450140",
                "umur"  : "20",
                "asal"  : "Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi" : "Main Game",
                "sosmed": "@raflyy_pd2684",
                "kesan" : "Kakak punya energi positif dan selalu terbuka.",  
                "pesan" : "Terima kasih banyak, Kak, inspirasi yang sangat berharga."
            },
            {
                "nama"  : "Syalaisha Andini Putriansyah",
                "nim"   : "122450111",
                "umur"  : "21",
                "asal"  : "Tanggerang",
                "alamat": "Sukarame",
                "hobbi" : "Membaca",
                "sosmed": "@syalaisha.i__",
                "kesan" : "Kakak penuh semangat dan memberi motivasi tinggi.",  
                "pesan" : "Terima kasih, Kak. Tetap semangat."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1-Yrvu8ctNNjIG44tlpx2z_ZgeonjvryU",  #bang rafi
            "https://drive.google.com/uc?export=view&id=1-LXNEgZEqFSoDEwVKVLXavB9hzxvAtKJ",  #kak anisa
            "https://drive.google.com/uc?export=view&id=1-kmANQ4JJ5GH63u-8JwLodgyPmY18Otw",  #bang ahmad
            "https://drive.google.com/uc?export=view&id=1-si2W39FibzvjWh67bmh70mQV148PDSu",  #bang fadhil
            "https://drive.google.com/uc?export=view&id=1-JXdCuYh3Ddnwrf1iGusiiQUWVrO-1Kd",  #kak dina
            "https://drive.google.com/uc?export=view&id=1-KBUT4DZAqYw__Kxvjao0qLAAAAXJUm0",  #kak dinda
            "https://drive.google.com/uc?export=view&id=1-DEQ8sCO63sj8WfJ04AoMCPcYoUUKnFV",  #kak marleta
            "https://drive.google.com/uc?export=view&id=1-V3our7rB0zXqsmGfRXxP2uPCkNpbdKQ",  #kak rut junita
            "https://drive.google.com/uc?export=view&id=1-RMZN31OHOU4sZ5JosBzx9SPZVbN4sd9",  #kak syadza 
            "https://drive.google.com/uc?export=view&id=1-kcGX5KYFL5PK3yfS5yR25LXzwiKxR_c",  #bang eggi
            "https://drive.google.com/uc?export=view&id=1-U4WVBHrdvQQ36-gxwtY5WzxVdA2jh0V",  #kak febiya
            "https://drive.google.com/uc?export=view&id=1-roN89i7kDz7A0dhXh6HoltmOYiCdoAm",  #kak happy syahrul
            "https://drive.google.com/uc?export=view&id=1-6vrOJtK3JCLNklNBblYx42pz0vxxeeA",  #bang randa
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
                "kesan" : "Kakak punya wawasan luas dan cara pandang yang bijaksana.",  
                "pesan" : "Makasih, Kak, semoga bisa sering berdiskusi lagi."
            },
            {
                "nama"  : "Annisa Novantika",
                "nim"   : "121450005",
                "umur"  : "21",
                "asal"  : "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi" : "Memasak",
                "sosmed": "@anovavona",
                "kesan" : "Kakak penuh semangat dan bijak dalam memberi saran.",  
                "pesan" : "Terima kasih Kak, semoga bisa belajar lebih banyak dari kakak."
            },
            {
                "nama"  : "Ahmad Sahidin Akbar",
                "nim"   : "122450044",
                "umur"  : "20",
                "asal"  : "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi" : "Olahraga",
                "sosmed": "@sahid22__",
                "kesan" : "Kakak positif dan selalu memberi semangat.",  
                "pesan" : "Terima kasih banyak Kak, semoga lancar kuliahnya"
            },
            {
                "nama"  : "Fadhil Fitra Wijaya",
                "nim"   : "122450082",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Teluk Betung",
                "hobbi" : "Main game",
                "sosmed": "@fadhilfwee",
                "kesan" : "Kakak sangat mendukung dan penuh ide baru.",  
                "pesan" : "Makasih, Kak. Semoga bisa sering ngobrol sama kakak."
            },
            {
                "nama"  : "Syalaisha Andina Putriansyah",
                "nim"   : "122450121",
                "umur"  : "21",
                "asal"  : "Tangerang",
                "alamat": "Gang Yudhistira",
                "hobbi" : "Baca jurnal",
                "sosmed": "@dkselsd_31",
                "kesan" : "Kakak humoris dan sabar dalam berdiskusi.",  
                "pesan" : "Terima kasih Kak, semoga bisa belajar lebih banyak."
            },
            {
                "nama"  : "Dinda Nababan",
                "nim"   : "122450120",
                "umur"  : "20",
                "asal"  : "Medan, Sumatera Utara",
                "alamat": "Jalan Lapas",
                "hobbi" : "Belajar",
                "sosmed": "@dindanababan_",
                "kesan" : "Kakak sangat inspiratif dan memberi semangat.",  
                "pesan" : "Terima kasih, Kak! Semoga saya bisa belajar lebih banyak dari pengalaman Kakak."
            },
            {
                "nama"  : "Marleta Cornelia Leander",
                "nim"   : "122450092",
                "umur"  : "20",
                "asal"  : "Depok, Jawa Barat",
                "alamat": "Gang Nangka 3",
                "hobbi" : "Review Jurnal",
                "sosmed": "@marletacornelia",
                "kesan" : "Kakak ramah dan mudah diajak ngobrol.",  
                "pesan" : "Makasih banyak, Kak! Semoga kita bisa berdiskusi lagi di lain waktu."
            },
            {
                "nama"  : "Rut Junita Sari Siburian",
                "nim"   : "122450103",
                "umur"  : "20",
                "asal"  : "Batam, Kepulauan Riau",
                "alamat": "Gang Nangka 3",
                "hobbi" : "Review Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan" : "Kakak punya wawasan luas dan berbagi dengan tulus.",  
                "pesan" : "Terima kasih, Kak! Semoga nasihat Kakak terus menginspirasi saya."
            },
            {
                "nama"  : "Syadza Puspadari Azhar",
                "nim"   : "122450072",
                "umur"  : "20",
                "asal"  : "Palembang",
                "alamat": "Belwis",
                "hobbi" : "Resume SG",
                "sosmed": "@puspadrr",
                "kesan" : "Profesional dan berpengalaman.",  
                "pesan" : "Semoga saya bisa mengikuti jejak Kakak yang sukses."
            },
            {
                "nama"  : "Eggi satria",
                "nim"   : "122450032",
                "umur"  : "20",
                "asal"  : "Sukabumi",
                "alamat": "Korpri",
                "hobbi" : "Ngoding WISATA",
                "sosmed": "@egistr",
                "kesan" : "Sangat peduli dan mendengarkan dengan baik.",  
                "pesan" : "Semoga saya bisa mendapatkan bimbingan lebih lanjut dari Kakak."
            },
            {
                "nama"  : "Febiya Jomy Pratiwi",
                "nim"   : "122450074",
                "umur"  : "20",
                "asal"  : "Tulang Bawang",
                "alamat": "Jalan Kelengkeng Raya",
                "hobbi" : "Review jurnal",
                "sosmed": "@pratiwifebiya",
                "kesan" : "Kakak punya aura positif yang menular.",  
                "pesan" : "Makasih, Kak! Semoga saya bisa terus belajar dari Kakak."
            },
             {
                "nama"  : "Happy Syahrul Ramadhan",
                "nim"   : "122450013",
                "umur"  : "20",
                "asal"  : "Lampung Timur",
                "alamat": "Karang Anyar",
                "hobbi" : "Main game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan" : "Kakak sangat sabar dan memberi arahan yang jelas.",  
                "pesan" : " Terima kasih, Kak! Semoga bisa berbagi pengalaman lagi."
            },
            {
                "nama"  : "Randa Andriana Putra",
                "nim"   : "122450083",
                "umur"  : "21",
                "asal"  : "Banten",
                "alamat": "Sukarame",
                "hobbi" : "Tidur dan berkembang",
                "sosmed": "@randaandriana_",
                "kesan" : "Kakak bijak dan memberikan perspektif yang menarik.",  
                "pesan" : "Terima kasih, Kak! Semoga saran Kakak bisa saya terapkan dengan baik."
            },

        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=16KsQ4L3xVqcHcPxuaHhao9gqMXN2J0Nz",#bang yogy
            "https://drive.google.com/uc?export=view&id=16p9LSgZnD-vUu6Ybqs9X1kRSF_BrPoVh",#kak ramadhita
            "https://drive.google.com/uc?export=view&id=1QV39x2LFMPNo4qO8i1eFIV2hUvh8H2cq",#kak nazwa
            "https://drive.google.com/uc?export=view&id=167KhVnyzak4c17BnqC4qfiR7ma6wRv_a",#bang bastian
            "https://drive.google.com/uc?export=view&id=10iOOFQoh0u9k26yFSwnCfKvZs-Gxv0ib",#kak dea
            "https://drive.google.com/uc?export=view&id=1ysRElWKXYB0gc7afFIW1tFhVBLGyFnHy",#kak esteria
            "https://drive.google.com/uc?export=view&id=1C2DMmklWy5w-fgD3wpyoqqH9vL7ZNac0",#kak natasya ega
            "https://drive.google.com/uc?export=view&id=1UjkUwwHXSoWnkRFf06zyA9tZIywfYlag",#kak novelia
            "https://drive.google.com/uc?export=view&id=1a3XiEuUuwvHq-zLPnaShB6CLeRcOuRVC",#kak jasmine
            "https://drive.google.com/uc?export=view&id=1pJf3X37qQ2wDoVKay4eVNVYfO3K7Sxvt",#bang tobias 
            "https://drive.google.com/uc?export=view&id=1Qp7Anlgu5OcrPKtuOm9lTe8IARdmyKSw",#kak yohana 
            "https://drive.google.com/uc?export=view&id=19FDvK8z7FOWPsPKUMpN8jwUnNJ8dyC0O",#bang arafi 
            "https://drive.google.com/uc?export=view&id=17P30HEMETmCIojJkWQYN0CgAVv78SKwA",#kak uyi 
            "https://drive.google.com/uc?export=view&id=1XNejdBKttbvqXkT-Mz0Px50Z43fneEgG",#kak chalifia
            "https://drive.google.com/uc?export=view&id=1iSnTFw5REPd8wRpeamYMdm6FqUs6diKp",#bang irvan
            "https://drive.google.com/uc?export=view&id=1ikMD1QGI6JdjtWM53ZwEgTmci5M36czM",#kak izza
            "https://drive.google.com/uc?export=view&id=1HZgsdYRJikZax-FxYpWuwZZpHUBIrP-S",#kak zuhrah 
            "https://drive.google.com/uc?export=view&id=1iXPYBnBifxJmYNP5dcRiDhAZvpTHN5-c",#bang raid
            "https://drive.google.com/uc?export=view&id=1_GHxurXRvfo5SUpZBWYZ5LSOuC0e9SB7",#kak tria 
            
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
                "kesan" : "Kakak open-minded dan terbuka dengan ide-ide baru.",  
                "pesan" : "Makasih, Kak! Semoga diskusi kita membuat saya lebih kreatif."
            },
            {
                "nama"  : "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan" : " Kakak punya passion yang menular dan bikin semangat.",  
                "pesan" : "Semoga Kakak terus membagikan ilmu dan pengalaman kepada kami semua!"
            },
            {
                "nama"  : "Nazwa Nabilla",
                "nim": "121450122",
                "umur": "21 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Way kandis",
                "hobbi": "Belajar",
                "sosmed": "@nazwanbilla",
                "kesan" : "Kakak ramah dan mudah didekati.",  
                "pesan" : "Semoga Kakak selalu terbuka untuk membantu dan berbagi lagi di lain waktu."
            },
            {
                "nama"  : "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21 Tahun",
                "asal": "Batam, Kepulauan Riau",
                "alamat": "Belwis",
                "hobbi": "Main game",
                "sosmed": "@bastiansilaban_",
                "kesan" : " Wawasan Kakak sangat luas dan bermanfaat.",  
                "pesan" : "Semoga Kakak terus menjadi sumber inspirasi bagi mahasiswa lainnya!"
            },
            {
                "nama"  : "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20 Tahun",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "Dengerin musik",
                "sosmed": "@deaa.rsn",
                "kesan" : "Kakak terlihat sangat profesional dalam menjelaskan hal-hal.",  
                "pesan" : "Semoga Kakak selalu sukses dan membagikan tips berharga kepada kami."
            },
            {
                "nama"  : "Esteria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "19 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Belwis",
                "hobbi": "Main golf bareng kadiv",
                "sosmed": "@esteriars",
                "kesan" : "Kakak sangat peduli dan mendengarkan dengan baik.",  
                "pesan" : "Semoga Kakak terus memberikan dukungan kepada junior seperti kami."
            },
            {
                "nama"  : "Natasya Ega Lina",
                "nim": "122450024",
                "umur": "19 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Belwis",
                "hobbi": "Jadi humas",
                "sosmed": "@nateee__15",
                "kesan" : "Kakak punya aura positif yang membuat nyaman.",  
                "pesan" : "Semoga energi positif Kakak selalu menyebar ke lingkungan sekitar."
            },
            {
                "nama"  : "Novelia Adinda",
                "nim": "122450104",
                "umur": "21 Tahun",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan" : "Kakak sabar dalam menjelaskan setiap pertanyaan.",  
                "pesan" : "Semoga Kakak selalu diingat sebagai mentor yang baik bagi kami."
            },
            {
                "nama"  : "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Main sepak takraw",
                "sosmed": "@jasminednva",
                "kesan" : "Komunikasi Kakak sangat jelas dan mudah dipahami.",  
                "pesan" : "Semoga Kakak terus menyebarkan ilmu dan pengalaman kepada yang lain."
            },
            {
                "nama"  : "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20 Tahun",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Jogging",
                "sosmed": "@tobiassiagian",
                "kesan" : "Kakak bijaksana dan memiliki pandangan yang menarik.",  
                "pesan" : "Semoga Kakak selalu memberikan perspektif baru yang menginspirasi."
            },
             {
                "nama"  : "Yohana Manik",
                "nim": "122450126",
                "umur": "19 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi": "Main Bowling",
                "sosmed": "@yo_annamnk",
                "kesan" : "Kakak humoris dan membuat suasana menjadi lebih hidup.",  
                "pesan" : "Semoga kita bisa berbagi tawa dan cerita lagi di lain kesempatan."
            },
            {
                "nama"  : "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20 Tahun",
                "asal": "Bandung",
                "alamat": "Way Huwi",
                "hobbi": "Bertani",
                "sosmed": "@rafiramadhanmaulana",
                "kesan" : "Kakak disiplin dan fokus saat menjelaskan.",  
                "pesan" : "Semoga Kakak terus menjadi contoh yang baik untuk kami semua."
            },
            {
                "nama"  : "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20 Tahun",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobbi": "Tepuk Semangat",
                "sosmed": "@u_yippy",
                "kesan" : "Kakak sangat mendukung dan memberi motivasi.",  
                "pesan" : "Semoga Kakak selalu mendapatkan dukungan yang sama dari orang lain."
            },
            {
                "nama"  : "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20 Tahun",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Q Time",
                "sosmed": "@chlfawww",
                "kesan" : "Kakak memiliki karakter yang kuat dan inspiratif.",  
                "pesan" : "Semoga Kakak terus menjadi panutan bagi mahasiswa lainnya."
            },
            {
                "nama"  : "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21 Tahun",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton youtube, main game",
                "sosmed": "@alfaritziirvan",
                "kesan" : "Kakak terbuka terhadap ide-ide baru.",  
                "pesan" : "Semoga Kakak selalu siap untuk berbagi pikiran dan inovasi dengan kami."
            },
            {
                "nama"  : "Izza Lutfia",
                "nim": "122450090",
                "umur": "20 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Main Rubik",
                "sosmed": "@izzalutfia",
                "kesan" : "Kakak penuh semangat dan memberi inspirasi.",  
                "pesan" : "Semoga semangat Kakak menular kepada lebih banyak teman-teman."
            },
            {
                "nama"  : "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Mengaji",
                "sosmed": "@alyaavanevi",
                "kesan" : "Kakak memberi perhatian lebih kepada junior.",  
                "pesan" : "Semoga Kakak selalu mendapatkan apresiasi atas dedikasinya."
            },
            {
                "nama"  : "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20 Tahun",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi": "telat",
                "sosmed": "@rayths_",
                "kesan" : "Kakak mampu menjelaskan dengan cara yang menarik.",  
                "pesan" : "Semoga Kakak terus berinovasi dalam cara penyampaian ilmu."
            },
            {
                "nama"  : "Tria Yunanni",
                "nim": "122450062",
                "umur": "20 Tahun",
                "asal": "Way Kanan",
                "alamat": "Sukarame",
                "hobbi": "Baca Buku",
                "sosmed": "@tria_y062",
                "kesan" : "Kakak percaya diri dan memotivasi kami.",  
                "pesan" : "Semoga Kakak selalu berani mengejar impian dan cita-cita."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1oazl6KMeY7imwjbdFPvpiEH_lCwl0bEg",#Bg Dimas
            "https://drive.google.com/uc?export=view&id=1C6iN29lItROYFJCBgvghM7vhrM2ccMNV",#kak catherine
            "https://drive.google.com/uc?export=view&id=1CjhqJoT2nbFqhQo9S45Su426_ME8zL_A",#bg akbar
            "https://drive.google.com/uc?export=view&id=1HxolchitsWLU3AbfQ_GfmpsuJ4f2dtoj",#kak renta
            "https://drive.google.com/uc?export=view&id=1ux60W_h9QUeLf4eJgkZNQxafyMUDagTp",#kak salwa
            "https://drive.google.com/uc?export=view&id=1-zp_245Jq-PPe3lGGQegZw14x7VG5e4p",#bg rendra
            "https://drive.google.com/uc?export=view&id=17oyFZTGE5C4L2PsW8IArq4ZOI1iakWIv",#bg yosia
            "https://drive.google.com/uc?export=view&id=1fH3oX_3KdyzmRMMaAsPm-GmrWNKVzrES",#bg ari 
            "https://drive.google.com/uc?export=view&id=1aACo1KT7nQscwi3Zf07YNlvkm79mR4ej",#bg josua
            "https://drive.google.com/uc?export=view&id=1hyS4ljEYn-tMzD1cJha3rBkzD1BYThYw",#kak azizah
            "https://drive.google.com/uc?export=view&id=13RbrKTVXW-gCAWnvssXSfBa4r6IzaBZh",#kak meira
            "https://drive.google.com/uc?export=view&id=18UQvAqduxYCWqDKuQIs9KIJNljYSkEcU",#bg rendi
            
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
                "kesan" : "kakaknya baik dan seru",  
                "pesan" : "semoga sukses kuliahnya"
            },
            {
                "nama"  : "Catherine Firdhasari Maulina Sinaga",
                "nim"   : "121450071",
                "umur"  : "20",
                "asal"  : "Sumatera Utara",
                "alamat": "Airan",
                "hobbi" : "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan" : "kakaknya ramah banget",  
                "pesan" : "semoga sukses selalu"
            },
            {
                "nama"  : "M.Akbar Resdika",
                "nim"   : "121450066",
                "umur"  : "20",
                "asal"  : "Lampung Barat (Way Tenun)",
                "alamat": "Labuhan Dalam (Untung)",
                "hobbi" : "Suka kucing tapi gak suka ngurusnya",
                "sosmed": "@akbar_restika",
                "kesan" : "ramah dan seru",  
                "pesan" : "tetap semangat dan jangan menyerah"
            },
            {
                "nama"  : "Renta Siahaan",
                "nim"   : "122450070",
                "umur"  : "21",
                "asal"  : "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi" : "Membaca dan Memancing",
                "sosmed": "@renita.shn",
                "kesan" : "murah senyum banget",  
                "pesan" : "bahagia selalu ya kak"
            },
            {
                "nama"  : "Salwa Farhanatussaidah",
                "nim"   : "122450055",
                "umur"  : "20",
                "asal"  : "Pesawaran",
                "alamat": "Airan",
                "hobbi" : "Nonton",
                "sosmed": "@slwfhn_694",
                "kesan" : "seru dan asik banget",  
                "pesan" : "selalu bahagia "
            },
            {
                "nama"  : "Rendra Eka Prayoga",
                "nim"   : "122450112",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Belwis",
                "hobbi" : "Mancing Ikan Mas",
                "sosmed": "@rendraepr",
                "kesan" : "asik dan seru",  
                "pesan" : "sehat selalu dan bahagia"
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
             "https://drive.google.com/uc?export=view&id=10E_iGBjpV4y9ccN6KVdSbanVW_Vd2FQF", #bang andrian 
            "https://drive.google.com/uc?export=view&id=1qybOxlqDsQCb8GMGxvg-ZUujbCwrx602", #kak adisty 
            "https://drive.google.com/uc?export=view&id=1_ntqFsufMAMPaUY7qhWLpxeyhCQsHHZp", #kak nabilla 
            "https://drive.google.com/uc?export=view&id=1U54mQmyzmett7te-x8NzFFbk_r9MVZ60", #bang danang 
            "https://drive.google.com/uc?export=view&id=1dcR6x-SfIw9s4drX_ogHANvVWiUoIMou", #bang farrel 
            "https://drive.google.com/uc?export=view&id=1bQpzYUCUF5_JwQZQ7lyvvGlqzEkUMFUz", #kak nabilah 
            "https://drive.google.com/uc?export=view&id=1tkSOuPysPcFRmAUNLbAnVOAZLS-y9VGb", #kak alvia 
            "https://drive.google.com/uc?export=view&id=11wgQz9EDNuEFJfFQzf8uJNvK7gL19KOK", #bang dhafin 
            "https://drive.google.com/uc?export=view&id=1SU_-sdqhND5fN9IKllP9f85jKETt8QA7", #kak elia 
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
                "kesan" : " Pengalaman Kakak sangat menarik dan bermanfaat.",  
                "pesan" : "Semoga Kakak terus berbagi cerita dan pengalaman kepada kami."
            },
            {
                "nama"  : "Adisty Syawaida Ariyanto",
                "nim"   : "121450136",
                "umur"  : "22",
                "asal"  : "Metro",
                "alamat": "Sukarame ",
                "hobbi" : "Nonton Film",
                "sosmed": "@adistysa_",
                "kesan" : "Kakak sangat hangat dan bersahabat.",  
                "pesan" : "Semoga hubungan kita semakin dekat di masa depan."
            },
            {
                "nama"  : "Nabila Azhari",
                "nim"   : "121450029",
                "umur"  : "21",
                "asal"  : "Simalungun",
                "alamat": "Airan ",
                "hobbi" : "Menghitung Uang",
                "sosmed": "@zhjung",
                "kesan" : "Kakak memiliki perspektif yang unik.",  
                "pesan" : "Semoga Kakak terus berbagi pandangan yang mencerahkan."
            },
            {
                "nama"  : "Danang Hilal Kurniawan",
                "nim"   : "122450085",
                "umur"  : "21",
                "asal"  : "Bandar Lampung",
                "alamat": "Airan",
                "hobbi" : "Belajar",
                "sosmed": "@dananghk_",
                "kesan" : "Kakak mendukung setiap langkah kami.",  
                "pesan" : "Semoga Kakak selalu mendapatkan dukungan yang sama dalam perjalanan Kakak."
            },
            {
                "nama"  : "Farrel Julio Akbar",
                "nim"   : "122450110",
                "umur"  : "20",
                "asal"  : "Bogor",
                "alamat": "Lapas",
                "hobbi" : "Kayang",
                "sosmed": "@farel_julio",
                "kesan" : "Kakak memberi semangat yang berbeda dalam setiap pertemuan.",  
                "pesan" : "Semoga Kakak terus membawa semangat positif ke lingkungan sekitar."
            },
            {
                "nama"  : "Nabilah Andika Fitriati",
                "nim"   : "121450139",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi" : "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan" : "Kakak sangat antusias dalam berbagi pengetahuan.",  
                "pesan" : "Semoga Kakak terus semangat dan menciptakan hal-hal baru yang bermanfaat."
            },
            {
                "nama"  : "Alvia Asrinda Br.Gintng",
                "nim"   : "122450077",
                "umur"  : "20",
                "asal"  : "Binjai",
                "alamat": "Korpri",
                "hobbi" : "Nonton Winda",
                "sosmed": "@alviagnting",
                "kesan" : "Kakak sangat membantu dalam setiap diskusi.",  
                "pesan" : "Semoga Kakak selalu menjadi sumber informasi yang dapat diandalkan."
            },
            {
                "nama"  : "Dhafin Razaqa Luthfi",
                "nim"   : "122450133",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi" : "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan" : " Kakak bisa membuat suasana belajar jadi menyenangkan.",  
                "pesan" : "Semoga Kakak terus membawa keceriaan dalam setiap kegiatan."
            },
            {
                "nama"  : "Elia Meylani Simanjuntak",
                "nim"   : "122450026",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Korpri",
                "hobbi" : "Main Alat Musik",
                "sosmed": "@meylanielia",
                "kesan" : "Kakak sangat memperhatikan kebutuhan kami sebagai junior.",  
                "pesan" : "Semoga Kakak selalu peka terhadap kebutuhan mahasiswa lainnya."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()

elif menu == "Departemen MEDKRAF":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=118LQ8jSPQt8dH1ZKRFIoxPemISw6dQPA", #bang wahyu 
            "https://drive.google.com/uc?export=view&id=16MHXLhHzrMeS8hRShBWeQXk3dS3GRZjJ", #kak elok 
            "https://drive.google.com/uc?export=view&id=1F5goHMKB9Co258eN_6UTtmtnJ0gJsEqi", #kak arsyiah 
            "https://drive.google.com/uc?export=view&id=1EuwgqNZuZpIW8COhAFh32i5XP3KsIACQ", #kak cintya 
            "https://drive.google.com/uc?export=view&id=1GwY6aHU2VnE1PKQZvo8pcvr7ZQQs32Id", #kak najla 
            "https://drive.google.com/uc?export=view&id=1FMpy-b17vkR5J3rtAXZG1dpg5crdnRg3", #kak rahma 
            "https://drive.google.com/uc?export=view&id=1A7g05w4mH3m04M4fs_IoIjWN9xNlZZ10", #kak try yani 
            "https://drive.google.com/uc?export=view&id=1dM8n6qZRiSDrX7iIMtKcxedqiI7Ib-rJ", #bang kaisar 
            "https://drive.google.com/uc?export=view&id=1v3t4oupjjC-pXgR6_1TqVjgtCTOtMfJu", #kak dwi 
            "https://drive.google.com/uc?export=view&id=1Eeo3ZYilUQiyYT9VZ_ibGtc0zdq7lmzw", #bang gym 
            "https://drive.google.com/uc?export=view&id=1fVoEC81UaiGxgnp2XWMLGHj1ctvFDCFb", #kak nasywa 
            "https://drive.google.com/uc?export=view&id=1FTmNdbI8CPO38FEhTpq54pJ_leW8cH7g", #kak priska 
            "https://drive.google.com/uc?export=view&id=1ovrGCUg1JsiaQQxzplcYU0BEd_X4zxdk", #bang arsal 
            "https://drive.google.com/uc?export=view&id=1EipKXcGMBuhYMQj_oMX4r4LWrKpXBAR5", #bang akmal 
            "https://drive.google.com/uc?export=view&id=1Nl-wwnHL3UEmAmAXr4S9u15F9MHbDeOA", #bang hermawan 
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
                "kesan" : "Kakak memiliki wawasan luas dan berwibawa dalam berbicara.",  
                "pesan" : "Semoga Kakak terus menebarkan ilmu dan inspirasi kepada kami semua."
            },
            {
                "nama"  : "Elok Fiola",
                "nim"   : "122450051",
                "umur"  : "19",
                "asal"  : "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi" : "Editing",
                "sosmed": "@elokfiola",
                "kesan" : "Kakak selalu memberi dukungan dan motivasi yang tulus.",  
                "pesan" : "Semoga Kakak selalu mendapatkan dukungan dalam setiap langkah."
            },
            {
                "nama"  : "Arsyiah Azahra",
                "nim"   : "121450035",
                "umur"  : "21",
                "asal"  : "Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi" : "Nugas",
                "sosmed": "@arsyiah.__",
                "kesan" : "Kakak punya kepribadian yang tenang dan menyenangkan.",  
                "pesan" : "Semoga Kakak selalu membawa ketenangan di mana pun berada."
            },
            {
                "nama"  : "Cintya Bella",
                "nim"   : "122450066",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Teluk",
                "hobbi" : "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan" : "Kakak sangat menguasai bidangnya dan membuat kami kagum.",  
                "pesan" : "Semoga Kakak terus menginspirasi banyak orang dengan pengetahuan yang dimiliki."
            },
            {
                "nama"  : "Najla Juwairia",
                "nim"   : "122450037",
                "umur"  : "19",
                "asal"  : "Sumatera Utara",
                "alamat": "Airan",
                "hobbi" : "Menulis, Membaca, Fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan" : "Kakak kreatif dan inovatif dalam memberikan solusi.",  
                "pesan" : "Semoga Kakak terus memberikan kontribusi positif yang membawa perubahan."
            },
            {
                "nama"  : "Rahma Neliyana",
                "nim"   : "122450036",
                "umur"  : "20",
                "asal"  : "Lampung",
                "alamat": "Sukarame",
                "hobbi" : "Baca Coding",
                "sosmed": "@rahmanellyana",
                "kesan" : "Kakak mudah diajak berdiskusi dan memberikan masukan yang berharga.",  
                "pesan" : "Semoga Kakak selalu terbuka dan terus berbagi ide-ide kreatif."
            },
            {
                "nama"  : "Try Yani Rizki Nur Rohmah",
                "nim"   : "122450020",
                "umur"  : "20",
                "asal"  : "Lampung Barat",
                "alamat": "Korpri",
                "hobbi" : "Bernyanyi dan Menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan" : "Kakak sangat menghargai setiap ide dan pendapat yang disampaikan.",  
                "pesan" : "Semoga Kakak selalu mendapatkan penghargaan atas sikap baiknya."
            },
            {
                "nama"  : "Muhammad Kaisar Firdaus",
                "nim"   : "121450135",
                "umur"  : "21",
                "asal"  : "Pesawaran",
                "alamat": "Pulau Damar",
                "hobbi" : "Lagi nyari",
                "sosmed": "@dino_lapet",
                "kesan" : "Kakak punya pembawaan yang tenang dan penuh kedewasaan.",  
                "pesan" : "Semoga Kakak selalu menjadi teladan yang baik bagi kami."
            },
            {
                "nama"  : "Dwi Ratna Anggraeni",
                "nim"   : "122450008",
                "umur"  : "20",
                "asal"  : "Jambi",
                "alamat": "Jalan Durian 5 Pemda",
                "hobbi" : "Membaca",
                "sosmed": "@dwiratnn_",
                "kesan" : "Kakak memberikan kesan nyaman dan membuat kami merasa diterima.",  
                "pesan" : "Semoga Kakak selalu memiliki hubungan yang baik dengan semua orang."
            },
            {
                "nama"  : "Gymnastiar Al Khoarizmy",
                "nim"   : "122450096",
                "umur"  : "20",
                "asal"  : "Serang",
                "alamat": "Lapangan Golf UIN",
                "hobbi" : "Baca komik",
                "sosmed": "@jimnn.as",
                "kesan" : "Kakak punya karakter kuat dan sangat berkarisma.",  
                "pesan" : "Semoga Kakak terus membawa pengaruh positif dalam setiap langkahnya."
            },
             {
                "nama"  : "Nasywa Nur Afifah",
                "nim"   : "122450125",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Jalan Durian 1 Pemda",
                "hobbi" : "Nonton drakor",
                "sosmed": "@nsywanaf",
                "kesan" : "Kakak menunjukkan empati dan perhatian kepada setiap orang.",  
                "pesan" : "Semoga Kakak selalu dihargai atas sikap baiknya yang tulus."
            },
            {
                "nama"  : "Priska Silvia Ferantiana",
                "nim"   : "122450053",
                "umur"  : "19",
                "asal"  : "Palembang",
                "alamat": "Jalan Nangka 2",
                "hobbi" : "Baca novel yang bikin nangis",
                "sosmed": "@prskslv",
                "kesan" : "Kakak memiliki kemampuan komunikasi yang luar biasa.",  
                "pesan" : "Semoga Kakak terus menjadi pembicara hebat yang menginspirasi banyak orang."
            },
            {
                "nama"  : "Muhammad Arsal Ranjana Utama",
                "nim"   : "121450111",
                "umur"  : "21",
                "asal"  : "Depok",
                "alamat": "Jalan Nangka 4",
                "hobbi" : "Ngoding",
                "sosmed": "@arsal.utama",
                "kesan" : "Kakak memberikan banyak pelajaran berharga yang sulit dilupakan.",  
                "pesan" : "Semoga pengalaman dan nasihat Kakak menjadi panduan untuk kita semua."
            },
            {
                "nama"  : "Akmal Faiz Abdillah",
                "nim"   : "122450114",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi" : "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan" : "Kakak sangat menghargai setiap ide dan pendapat yang disampaikan.",  
                "pesan" : "Semoga Kakak selalu menjadi teladan yang baik bagi kami."
            },
            {
                "nama"  : "Hermawan Manurung",
                "nim"   : "122450069",
                "umur"  : "20",
                "asal"  : "Bogor",
                "alamat": "Dekat jalan tol, Wisma Hana Hani",
                "hobbi" : "Bengong dan membaca buku",
                "sosmed": "@hermawan.mnrng",
                "kesan" : "Kakak memberikan kesan nyaman dan membuat kami merasa diterima.",  
                "pesan" : " Semoga Kakak selalu memiliki hubungan yang baik dengan semua orang."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()
# Tambahkan menu lainnya sesuai kebutuhan


# Tambahkan menu lainnya sesuai kebutuhan
