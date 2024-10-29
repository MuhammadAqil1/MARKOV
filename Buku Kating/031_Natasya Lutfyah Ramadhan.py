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
            "https://drive.google.com/uc?export=view&id=1Nx--psLqJlgjSl_I2eC2lWOXX1ajWUR2",
            "https://drive.google.com/uc?export=view&id=1NYmVkbSAF0bL0ak1psDs8rXY9rIt8Q0_",
            "https://drive.google.com/uc?export=view&id=1NeufUm5bJQXcc0o20_cDHeo2GWtzNprf",
            "https://drive.google.com/uc?export=view&id=1NnTJWNk33YJPLwuaSsGHEwyb6WTzb8uL",
            "https://drive.google.com/uc?export=view&id=1Ngv8jLz9LRJSlWAAA9IYvzL1hTCQgqGx",
            "https://drive.google.com/uc?export=view&id=1NbcBVdA7x0cEyUmafebvw_eKvMTUcSIy",
            "https://drive.google.com/uc?export=view&id=1O10hHuwPn9KXf9dD-ZnOOH9HEchNeXul",
            "https://drive.google.com/uc?export=view&id=1NtbEzuWdTv6k111aitYEwHJCT69JOWzi",
            "https://drive.google.com/uc?export=view&id=1O6b7JKU8EvnSnUSPviyWQI52bLWcD7gd",
            "https://drive.google.com/uc?export=view&id=1Njf8tb7nFCpd3vGlIb9k7N20r3U1sxJq",
 
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
            "https://drive.google.com/uc?export=view&id=1LTcWdyudTvkSKLB38A8JV0mHArG6lbnK",#lutfi
            "https://drive.google.com/uc?export=view&id=1M_gJ_CtmEvnCFGaYRm9UDZdqZLxqfZhi",#bintang
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
                "kesan" : "kakak selalu jelas banget saat ngejelasin sesuatu, dan motivasinya bikin semangat ngerjain tugas!",  
                "pesan" : "Semoga semua kegiatan kakak, baik di kampus maupun di luar, tetap lancar. Tetap semangat ya, Kak!"
            },
            {
                "nama"  : "Rian Bintang Wijaya",
                "nim"   : "122450094",
                "umur"  : "20",
                "asal"  : "Palembang, Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi" : "Mendengar Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan" : "Abang selalu jelas banget saat ngejelasin sesuatu, dan motivasinya bikin semangat ngerjain tugas!",  
                "pesan" : "Semoga semua kegiatan kakak, baik di kampus maupun di luar, tetap lancar. Tetap semangat ya, Kak!"
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
            "https://drive.google.com/uc?export=view&id=1Rtv8iiKGM7wPCr5UZ3P8fUZNJ5_kkYAV", #kak presilia dn
            "https://drive.google.com/uc?export=view&id=1QSDmFqYWLC8FtbpGrRff-Ngiu3zgHCqw", #kak rafa dn
            "https://drive.google.com/uc?export=view&id=1Qf_GumaM-Pm70t5nnDLPkly7wUYHlyRo", #bang sahid dn
            "https://drive.google.com/uc?export=view&id=1Qds8DrC2q45WGi7kUyMZ0EuhRVLH5rhj", #kak vanes dn
            "https://drive.google.com/uc?export=view&id=1RwrsLq1PUz7KfsxJMMeKcSIkZZVs5Vu4", #bang ateng dn
            "https://drive.google.com/uc?export=view&id=1RJZdutBlpMA_kM7bIUXjGl8rww7DvLrV", #bang gede dn
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
                "kesan" : "Sangat informatif dalam menjelaskan sesuatu dan menjadi sosok yang memberikan banyak masukan serta motivasi melalui pengalaman yang telah dilakukan",  
                "pesan" : "Tetap semangat kak dalam menjalani hari-harinya, semoga diperlancar dalam menyelesaikan tugas dan tanggung jawab yang sedang di emban"
            },
            {
                "nama"  : "Elisabeth Claudia Simanjuntak",
                "nim"   : "121450114",
                "umur"  : "21",
                "asal"  : "Tanggerang Selatan",
                "alamat": "Way Huwi",
                "hobbi" : "Membaca, Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan" : "Sangat informatif dalam menjelaskan sesuatu dan banyak memberikan motivasi",  
                "pesan" : "Semoga kegiatannya di dalam maupun di luar perkuliahan tetap lancar dan tetap semangat kak"
            },
            {
                "nama"  : "Nisrina Nur Afifah",
                "nim"   : "122450052",
                "umur"  : "19",
                "asal"  : "Bekasi",
                "alamat": "Sukarame",
                "hobbi" : "Nabok orang",
                "sosmed": "@afifahhnsrn",
                "kesan" : "Sangat baik, informatif dalam menerangkan suatu permasalahan dan sangat menginspirasi",  
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
                "kesan" : "Sangat informatif dalam menerangkan sesuatu dan sangat menginspirasi",  
                "pesan" : "Semoga selalu dilancarkan semua urusannya kak, jangan lupa untuk tetap semangat kak dalam menjalani kehidupan"
            },
            {
                "nama"  : "Farahanum Afifah Ardiansyah",
                "nim"   : "122450056",
                "umur"  : "20",
                "asal"  : "Padang, Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi" : "Tidur",
                "sosmed": "@farahanumafifahh",
                "kesan" : "Sangat baik dan sangat menginspirasi dalam kehidupan",  
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
                "kesan" : "Sangat baik dan sangat mengasyikkan ",  
                "pesan" : "Semangat terus kak dalam menjalani perkuliahannya serta jangan lupa untuk jaga kesehatan"
            },
            {
                "nama"  : "Oktavia Nurwenda Puspita Sari",
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
                "kesan" : "Sangat baik dan sangat informatif dalam menjelaskan sesuatu",  
                "pesan" : "Semangat terus kak dalam menjalani hari-harinya, semoga semua tugas dan tanggung jawab yang diemban dapat diselesaikan dengan lancar"
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
                "pesan" : "Semangat kak dalam menjalani hari-harinya, semoga urusannya dalam dunia perkuliahan dapat diselesaikan dengan mudah"
            },
             {
                "nama"  : "Johannes Krisjon Silitonga",
                "nim"   : "122450043",
                "umur"  : "19",
                "asal"  : "Tanggerang",
                "alamat": "Jalan Lapas",
                "hobbi" : "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan" : "Sangat informatif dalam menjelaskan sesuatu dan menjadi sosok yang memberikan banyak masukan serta motivasi melalui pengalaman yang telah dilakukan",  
                "pesan" : "Tetap semangat kak dalam menjalani hari-harinya, semoga diperlancar dalam menyelesaikan tugas dan tanggung jawab yang sedang di emban"
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
                "pesan" : "Semoga kegiatannya di dalam maupun di luar perkuliahan tetap lancar dan tetap semangat kak"
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
                "pesan" : "Tetap semangat kak dalam menjalani harinya, semoga urusannya baik di akademik maupun non akademik dapat berjalan dengan lancar"
            },
            {
                "nama"  : "Presilia",
                "nim"   : "121450081",
                "umur"  : "21",
                "asal"  : "Tanggerang",
                "alamat": "Jati Agung",
                "hobbi" : "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan" : "Sangat informatif dalam menerangkan sesuatu dan sangat menginspirasi",  
                "pesan" : "Semoga selalu dilancarkan semua urusannya kak, jangan lupa untuk tetap semangat kak dalam menjalani kehidupan"
            },
            {
                "nama"  : "Rafa Aqilla Jungjunan",
                "nim"   : "122450148",
                "umur"  : "20",
                "asal"  : "Riau",
                "alamat": "Belwis",
                "hobbi" : "Membaca webtoon",
                "sosmed": "@rafaaqilla",
                "kesan" : "Sangat baik dan sangat menginspirasi dalam kehidupan",  
                "pesan" : "Tetap semangat dalam menjalani perkuliahannya kak dan jangan lupa jaga kesehatan"
            },
            {
                "nama"  : "Sahid Maulana",
                "nim"   : "122450109",
                "umur"  : "21",
                "asal"  : "Depok, Jawa Barat",
                "alamat": "Airan Raya",
                "hobbi" : "Bermain Game",
                "sosmed": "@sahid_maul19",
                "kesan" : "Sangat menginspirasi dalam kehidupan ",  
                "pesan" : "Tetap semangat kak dalam menjalani dunia perkuliahan"
            },
            {
                "nama"  : "Vanessa Olivia Rose",
                "nim"   : "121450068",
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
                "nim"   : "121450156",
                "umur"  : "22",
                "asal"  : "Surakarta, Jawa Tengah",
                "alamat": "Pahoman",
                "hobbi" : "Melukis, badminton, hiking, ngopi, dengerin music, nonton film dan ngoding",
                "sosmed": "@fhrul.pdf",
                "kesan" : "Sangat seru dan informatif dalam menjelaskan sesuatu",  
                "pesan" : "Jangan lupa untuk tetap semangat dalam menjalani dunia perkuliahan kak, semoga urusannya selalu dilancarkan"
            },
            {
                "nama"  : "Gede Moana",
                "nim"   : "122450065",
                "umur"  : "21",
                "asal"  : "Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi" : "Main Game",
                "sosmed": "@berlyyanda",
                "kesan" : "Sangat baik dan sangat informatif dalam menjelaskan sesuatu",  
                "pesan" : "Semangat terus kak dalam menjalani hari-harinya, semoga semua tugas dan tanggung jawab yang diemban dapat diselesaikan dengan lancar"
            },
            {
                "nama"  : "Jaclin Alcavella",
                "nim"   : "122450022",
                "umur"  : "20",
                "asal"  : " Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi" : "Marah-marah",
                "sosmed": "@jeremia_s_",
                "kesan" : "Sangat baik dan sangat mengasyikkan",  
                "pesan" : "Semangat kak dalam menjalani hari-harinya, semoga urusannya dalam dunia perkuliahan dapat diselesaikan dengan mudah"
            },
            {
                "nama"  : "Rafly Prabu Darmawan",
                "nim"   : "122450065",
                "umur"  : "21",
                "asal"  : "Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi" : "Main Game",
                "sosmed": "@berlyyanda",
                "kesan" : "Sangat baik dan sangat informatif dalam menjelaskan sesuatu",  
                "pesan" : "Semangat terus kak dalam menjalani hari-harinya, semoga semua tugas dan tanggung jawab yang diemban dapat diselesaikan dengan lancar"
            },
            {
                "nama"  : "Syalaisha Andini Putriansyah",
                "nim"   : "122450022",
                "umur"  : "20",
                "asal"  : " Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi" : "Marah-marah",
                "sosmed": "@jeremia_s_",
                "kesan" : "Sangat baik dan sangat mengasyikkan",  
                "pesan" : "Semangat kak dalam menjalani hari-harinya, semoga urusannya dalam dunia perkuliahan dapat diselesaikan dengan mudah"
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
            "https://drive.google.com/uc?export=view&id=1Sd81E6WhcWbJ077eDxARVlN1j6KW4YO7", #kak vita dn
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
                "kesan" : "Sangat informatif dalam menjelaskan sesuatu dan menjadi sosok yang memberikan banyak masukan serta motivasi melalui pengalaman yang telah dilakukan",  
                "pesan" : "Tetap semangat kak dalam menjalani hari-harinya, semoga diperlancar dalam menyelesaikan tugas dan tanggung jawab yang sedang di emban"
            },
            {
                "nama"  : "Ahmad Sahidin Akbar",
                "nim"   : "121450114",
                "umur"  : "21",
                "asal"  : "Tanggerang Selatan",
                "alamat": "Way Huwi",
                "hobbi" : "Membaca, Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan" : "Sangat informatif dalam menjelaskan sesuatu dan banyak memberikan motivasi",  
                "pesan" : "Semoga kegiatannya di dalam maupun di luar perkuliahan tetap lancar dan tetap semangat kak"
            },
            {
                "nama"  : "Fadhil Fitra Wijaya",
                "nim"   : "122450052",
                "umur"  : "19",
                "asal"  : "Bekasi",
                "alamat": "Sukarame",
                "hobbi" : "Nabok orang",
                "sosmed": "@afifahhnsrn",
                "kesan" : "Sangat baik, informatif dalam menerangkan suatu permasalahan dan sangat menginspirasi",  
                "pesan" : "Tetap semangat kak dalam menjalani harinya, semoga urusannya baik di akademik maupun non akademik dapat berjalan dengan lancar"
            },
            {
                "nama"  : "Syalaisha Andina Putriansyah",
                "nim"   : "122450033",
                "umur"  : "20",
                "asal"  : "Sumatera Barat",
                "alamat": "Gang Perwira, Belwis",
                "hobbi" : "Nonton Dracin",
                "sosmed": "@allyaislami_",
                "kesan" : "Sangat informatif dalam menerangkan sesuatu dan sangat menginspirasi",  
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
                "kesan" : "Sangat baik dan sangat menginspirasi dalam kehidupan",  
                "pesan" : "Tetap semangat dalam menjalani perkuliahannya kak dan jangan lupa jaga kesehatan"
            },
            {
                "nama"  : "Marleta Cornelia Leander",
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
                "nama"  : "Rut Junita Sari Siburian",
                "nim"   : "122450101",
                "umur"  : "19",
                "asal"  : "Kayu Agung",
                "alamat": "Jalan Pagar Alam",
                "hobbi" : "Bercerita horror",
                "sosmed": "@dransyh_",
                "kesan" : "Sangat baik dan sangat mengasyikkan ",  
                "pesan" : "Semangat terus kak dalam menjalani perkuliahannya serta jangan lupa untuk jaga kesehatan"
            },
            {
                "nama"  : "Syadza Puspadari Azhar",
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
                "nama"  : "Eggi satria",
                "nim"   : "121450148",
                "umur"  : "21",
                "asal"  : "Riau",
                "alamat": "Pulau Damar",
                "hobbi" : "Belajar",
                "sosmed": "@depanloo",
                "kesan" : "Sangat baik dan sangat informatif dalam menjelaskan sesuatu",  
                "pesan" : "Semangat terus kak dalam menjalani hari-harinya, semoga semua tugas dan tanggung jawab yang diemban dapat diselesaikan dengan lancar"
            },
            {
                "nama"  : "Febiya Jomy Pratiwi",
                "nim"   : "121450121",
                "umur"  : "21",
                "asal"  : "Jambi",
                "alamat": "Pulau Damar, Kobam",
                "hobbi" : "Bermain Game Online",
                "sosmed": "@al_ghifari032",
                "kesan" : "Sangat baik dan sangat mengasyikkan",  
                "pesan" : "Semangat kak dalam menjalani hari-harinya, semoga urusannya dalam dunia perkuliahan dapat diselesaikan dengan mudah"
            },
             {
                "nama"  : "Happy Syahrul Ramadhan",
                "nim"   : "122450043",
                "umur"  : "19",
                "asal"  : "Tanggerang",
                "alamat": "Jalan Lapas",
                "hobbi" : "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan" : "Sangat informatif dalam menjelaskan sesuatu dan menjadi sosok yang memberikan banyak masukan serta motivasi melalui pengalaman yang telah dilakukan",  
                "pesan" : "Tetap semangat kak dalam menjalani hari-harinya, semoga diperlancar dalam menyelesaikan tugas dan tanggung jawab yang sedang di emban"
            },
            {
                "nama"  : "Randa Andriana Putra",
                "nim"   : "122450016",
                "umur"  : "19",
                "asal"  : "Bekasi",
                "alamat": "Golf Asri",
                "hobbi" : "Bermain ular python digital",
                "sosmed": "@kemasverii",
                "kesan" : "Sangat informatif dalam menjelaskan sesuatu dan banyak memberikan motivasi",  
                "pesan" : "Semoga kegiatannya di dalam maupun di luar perkuliahan tetap lancar dan tetap semangat kak"
            },
            {
                "nama"  : "Vita Anggraini",
                "nim"   : "121450153",
                "umur"  : "21",
                "asal"  : "Sumatera Utara",
                "alamat": "Kobam",
                "hobbi" : "Belajar",
                "sosmed": "@lnrd.__",
                "kesan" : "Sangat baik, informatif dalam menerangkan suatu permasalahan dan sangat menginspirasi",  
                "pesan" : "Tetap semangat kak dalam menjalani harinya, semoga urusannya baik di akademik maupun non akademik dapat berjalan dengan lancar"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen MEDKRAF":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1TdI04z8ERBknrIN_xyC8T1JMUTcB1TfY", #bang wahyu dn
            "https://drive.google.com/uc?export=view&id=1HnVSrDf8aW-bi0onMLRKTyNF13v_zO_d", #kak elok dn
            "https://drive.google.com/uc?export=view&id=1haaJ2sbneWEimh4xrgbfKvBtoc8RNQ6K", #kak arsyiah dn
            "https://drive.google.com/uc?export=view&id=1ICWowaEyRJtCXGcF2LBzT5x32AVrtNiA", #kak cintya dn
            "https://drive.google.com/uc?export=view&id=1Qb-VkdCcYbdG7xBbmhOqupNCLpTl1aBv", #kak najla dn
            "https://drive.google.com/uc?export=view&id=1VvfXCDrkDu8UVoovtGYkUSRLBoYV4Rj4", #kak rahma dn
            "https://drive.google.com/uc?export=view&id=14nu7B-zNP7sY6jXLs0AxzHb6p4n_e1Lo", #kak try yani dn
            "https://drive.google.com/uc?export=view&id=1y3-phk-tdnhw13vysRPvh1SCQb7ldgPc", #bang kaisar dn
            "https://drive.google.com/uc?export=view&id=1SYm0crhDrAvQ66Ucz9J3UIRnZfgw_g7x", #kak dwi dn
            "https://drive.google.com/uc?export=view&id=1YlwJFXiaeBtaNXjt0-RgnxJJuz3ah6t7", #bang gym dn
            "https://drive.google.com/uc?export=view&id=1B13zqETppi_ZwEHiyZ8naXmBh7xI1C09", #kak nasywa dn
            "https://drive.google.com/uc?export=view&id=1nA5rAUgwnpytmU538qbJa2miI66Q0302", #kak priska dn
            "https://drive.google.com/uc?export=view&id=14gAVE2X0A4uyurfLSWzAqqKo-wKUik2v", #bang arsal dn
            "https://drive.google.com/uc?export=view&id=1WWHXrajbhnAG9LQtTYp95QomA7SEEGhP", #bang abit dn
            "https://drive.google.com/uc?export=view&id=1_vkMrZtDAOX3_7QwPTEerQKo6Nm02uDH", #bang akmal dn
            "https://drive.google.com/uc?export=view&id=1SdUhRgE_nhTnJwviIrWbVvjkon9tbyGW", #bang hermawan dn
            "https://drive.google.com/uc?export=view&id=1fq239NPmX37uzdRH_2hRVWC98bQ50eLe", #kak nisa dn
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
                "kesan" : "Sangat informatif dalam menjelaskan sesuatu dan menjadi sosok yang memberikan banyak masukan serta motivasi melalui pengalaman yang telah dilakukan",  
                "pesan" : "Tetap semangat kak dalam menjalani hari-harinya, semoga diperlancar dalam menyelesaikan tugas dan tanggung jawab yang sedang di emban"
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
                "kesan" : "Sangat menginspirasi dalam kehidupan ",  
                "pesan" : "Tetap semangat kak dalam menjalani dunia perkuliahan"
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
                "kesan" : "Sangat informatif dalam menjelaskan sesuatu dan menjadi sosok yang memberikan banyak masukan serta motivasi melalui pengalaman yang telah dilakukan",  
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
                "kesan" : "Sangat informatif dalam menjelaskan sesuatu dan banyak memberikan motivasi",  
                "pesan" : "Semoga kegiatannya di dalam maupun di luar perkuliahan tetap lancar dan tetap semangat kak"
            },
            {
                "nama"  : "Muhammad Arsal Ranjana Utama",
                "nim"   : "121450111",
                "umur"  : "21",
                "asal"  : "Depok",
                "alamat": "Jalan Nangka 4",
                "hobbi" : "Ngoding",
                "sosmed": "@arsal.utama",
                "kesan" : "Sangat baik, informatif dalam menerangkan suatu permasalahan dan sangat menginspirasi",  
                "pesan" : "Tetap semangat kak dalam menjalani harinya, semoga urusannya baik di akademik maupun non akademik dapat berjalan dengan lancar"
            },
            {
                "nama"  : "Abit Ahmad Oktarian",
                "nim"   : "122450042",
                "umur"  : "19",
                "asal"  : "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi" : "Ngoding, Gaming",
                "sosmed": "@abitahmad",
                "kesan" : "Sangat informatif dalam menerangkan sesuatu dan sangat menginspirasi",  
                "pesan" : "Semoga selalu dilancarkan semua urusannya kak, jangan lupa untuk tetap semangat kak dalam menjalani kehidupan"
            },
            {
                "nama"  : "Akmal Faiz Abdillah",
                "nim"   : "122450114",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi" : "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan" : "Sangat baik dan sangat menginspirasi dalam kehidupan",  
                "pesan" : "Tetap semangat dalam menjalani perkuliahannya kak dan jangan lupa jaga kesehatan"
            },
            {
                "nama"  : "Hermawan Manurung",
                "nim"   : "122450069",
                "umur"  : "20",
                "asal"  : "Bogor",
                "alamat": "Dekat jalan tol, Wisma Hana Hani",
                "hobbi" : "Bengong dan membaca buku",
                "sosmed": "@hermawan.mnrng",
                "kesan" : "Sangat menginspirasi dalam kehidupan ",  
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
                "kesan" : "Sangat baik dan sangat mengasyikkan ",  
                "pesan" : "Semangat terus kak dalam menjalani perkuliahannya serta jangan lupa untuk jaga kesehatan"
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
                "hobi": "Bangun pagi",
                "sosmed": "@yogyyyyyy",
                "kesan": "",
                "pesan": "",
            },
            {
                "nama": "Ramadhita Atifa Hendri",#                "jabatan": "Sekretaris Departemen"
                "nim": "121450131",
                "umur": "21 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobi": "Jalan - Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan": "",
                "pesan": "",
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
                "nama": "Esteria Rohanauli Sidauruk",#                "jabatan": "Staff Divisi Hubungan Luar"
                "nim": "122450025",
                "umur": "19 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Belwis",
                "hobi": "kirim bc-an",
                "sosmed": "@esteriars",
                "kesan": "",
                "pesan": "",
            },
            {
                "nama": "Natasya Ega Lina",#                "jabatan": "Staff Divisi Hubungan Luar"
                "nim": "122450024",
                "umur": "19 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobi": "jadi humas",
                "sosmed": "@nateee__15",
                "kesan": "",
                "pesan": "",
            },
            {
                "nama": "Novelia Adinda",#                "jabatan": "Staff Divisi Hubungan Luar"
                "nim": "122450104",
                "umur": "21 Tahun",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan": "",
                "pesan": "",
            },
            {
                "nama": "Ratu Keisha Jasmine Deanova",#                "jabatan": "Staff Divisi Hubungan Luar"
                "nim": "122450106",
                "umur": "20 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Way Kandis",
                "hobi": "Main sepak takraw",
                "sosmed": "@jasminednva",
                "kesan": "",
                "pesan": "",
            },
            {
                "nama": "Tobias David Manogari",#                "jabatan": "Staff Divisi Hubungan Luar"
                "nim": "122450091",
                "umur": "20 Tahun",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobi": "Jogging",
                "sosmed": "@tobiassiagian",
                "kesan": "",
                "pesan": "",
            },
            {
                "nama": "Yohana Manik",#                "jabatan": "Staff Divisi Hubungan Luar"
                "nim": "122450126",
                "umur": "19 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobi": "Main Bowling",
                "sosmed": "@yo_annamnk",
                "kesan": "",
                "pesan": "",
            },
            {
                "nama": "Rizky Adrian Bennovry",#                "jabatan": "Kepala Divisi Pengabdian Masyarakat"
                "nim": "121450073",
                "umur": "21 Tahun",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobi": "Bikin portofolio",
                "sosmed": "@rzkdrnnn",
                "kesan": "",
                "pesan": "",
            },
            {
                "nama": "Arafi Ramadhan Maulana",#                "jabatan": "Staff Divisi Pengabdian Masyarakat"
                "nim": "122450002",
                "umur": "20 Tahun",
                "asal": "Bandung",
                "alamat": "Way Huwi",
                "hobi": "Bertani",
                "sosmed": "@rafiramadhanmaulana",
                "kesan": "",
                "pesan": "",
            },
            {
                "nama": "Asa Do'a Uyi",#                "jabatan": "Staff Divisi Pengabdian Masyarakat"
                "nim": "122450005",
                "umur": "20 Tahun",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobi": "Tepuk Semangat",
                "sosmed": "@u_yippy",
                "kesan": "",
                "pesan": "",
            },
            {
                "nama": "Chalifia Wananda",#                "jabatan": "Staff Divisi Pengabdian Masyarakat"
                "nim": "122450076",
                "umur": "20 Tahun",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobi": "Q Time",
                "sosmed": "@chlfawww",
                "kesan": "",
                "pesan": "",
            },
            {
                "nama": "Irvan Alfaritzi",#                "jabatan": "Staff Divisi Pengabdian Masyarakat"
                "nim": "122450093",
                "umur": "21 Tahun",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobi": "Nonton youtube, main game",
                "sosmed": "@alfaritziirvan",
                "kesan": "",
                "pesan": "",
            },
            {
                "nama": "Izza Lutfia",#                "jabatan": "Staff Divisi Pengabdian Masyarakat"
                "nim": "122450090",
                "umur": "20 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobi": "Main Rubik",
                "sosmed": "@izzalutfia",
                "kesan": "",
                "pesan": "",
            },
            {
                "nama": "Khaalishah Zuhrah Alyaa Vanefi",#                "jabatan": "Staff Divisi Pengabdian Masyarakat"
                "nim": "122450034",
                "umur": "20 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobi": "belajar",
                "sosmed": "@alyaavanevi",
                "kesan": "",
                "pesan": "",
            },
            {
                "nama": "Raid Muhammad Naufal",#                "jabatan": "Staff Divisi Pengabdian Masyarakat"
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
                "nama": "Tria Yunanni",#                "jabatan": "Staff Divisi Pengabdian Masyarakat"
                "nim": "122450062",
                "umur": "20 Tahun",
                "asal": "Way Kanan",
                "alamat": "Sukarame",
                "hobi": "Baca Buku",
                "sosmed": "@tria_y062",
                "kesan": "",
                "pesan": "",
                },
                ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1txdHsmKrEwVGkKJF7DZiTDqQHoRaNPK0", #bang dimas dn
            "https://drive.google.com/uc?export=view&id=1x4IwnZxnwCZkekqXZsHZnDO6pm55S8fr", #kak catherine dn
            "https://drive.google.com/uc?export=view&id=1oLVtYjMqotS-DXtBwiPj1viFBCiE-Jdc", #bang akbar dn
            "https://drive.google.com/uc?export=view&id=1rK8NJtN6iDFdHZRlihDigY5315ZwoQ_3", #kak rani dn
            "https://drive.google.com/uc?export=view&id=1pHuguAttxSiw6Oo7WhSQXeBsvZpEm1Le", #bang rendra dn
            "https://drive.google.com/uc?export=view&id=1KZM9kZbB9MCjxL2ATgrucsp8hvZcJ4wZ", #kak salwa dn
            "https://drive.google.com/uc?export=view&id=1cVzF1zzuyMCqqr049_b_Ii8C90VSzTtU", #bang yosia dn
            "https://drive.google.com/uc?export=view&id=1BNxQt_4lPak5sUXf_EpaJH6SPMfahXBy", #bang ari dn
            "https://drive.google.com/uc?export=view&id=1pTcPeRLCemnj8cQtaJemPaNbOXnhT9A8", #kak azizah dn
            "https://drive.google.com/uc?export=view&id=1JtfQ_TAhrVvbEW9hgy5or0_MRzgpSdyy", #kak meira dn
            "https://drive.google.com/uc?export=view&id=1A_9Hi4pNFXJ7bD5T0RKy0T0gRL9FJX8B", #bang rendi dn
            "https://drive.google.com/uc?export=view&id=1WkkjzRI8PD6T4FAcOKxcpM5RIeoo3cO-", #kak renta dn
            "https://drive.google.com/uc?export=view&id=10n-7tDMCB9Gx5su00unmArqAKb3RydDa", #bang josua dn

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
                "kesan" : "Sangat informatif dalam menjelaskan sesuatu dan menjadi sosok yang memberikan banyak masukan serta motivasi melalui pengalaman yang telah dilakukan",  
                "pesan" : "Tetap semangat kak dalam menjalani hari-harinya, semoga diperlancar dalam menyelesaikan tugas dan tanggung jawab yang sedang di emban"
            },
            {
                "nama"  : "Catherine Firdhasari Maulina Sinaga",
                "nim"   : "121450071",
                "umur"  : "20",
                "asal"  : "Sumatera Utara",
                "alamat": "Airan",
                "hobbi" : "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan" : "Sangat informatif dalam menjelaskan sesuatu dan banyak memberikan motivasi",  
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
                "kesan" : "Sangat baik, informatif dalam menerangkan suatu permasalahan dan sangat menginspirasi",  
                "pesan" : "Tetap semangat kak dalam menjalani harinya, semoga urusannya baik di akademik maupun non akademik dapat berjalan dengan lancar"
            },
            {
                "nama"  : "Rani Puspita sari",
                "nim"   : "122450033",
                "umur"  : "20",
                "asal"  : "Sumatera Barat",
                "alamat": "Gang Perwira, Belwis",
                "hobbi" : "Nonton Dracin",
                "sosmed": "@allyaislami_",
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
                "kesan" : "Sangat baik dan sangat menginspirasi dalam kehidupan",  
                "pesan" : "Tetap semangat dalam menjalani perkuliahannya kak dan jangan lupa jaga kesehatan"
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
                "kesan" : "Sangat seru dan informatif dalam menjelaskan sesuatu",  
                "pesan" : "Jangan lupa untuk tetap semangat dalam menjalani dunia perkuliahan kak, semoga urusannya selalu dilancarkan"
            },
            {
                "nama"  : "Azizah Kusumah Putri",
                "nim"   : "122450068",
                "umur"  : "21",
                "asal"  : "Lampung Selatan",
                "alamat": "Natar",
                "hobbi" : "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan" : "Sangat baik dan sangat informatif dalam menjelaskan sesuatu",  
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
                "pesan" : "Semangat kak dalam menjalani hari-harinya, semoga urusannya dalam dunia perkuliahan dapat diselesaikan dengan mudah"
            },
            {
                "nama"  : "Rendi Alexander Hutagalung",
                "nim"   : "122450057",
                "umur"  : "20",
                "asal"  : "Tangerang",
                "alamat": "Kost Benawang",
                "hobbi" : "Menyanyi",
                "sosmed": "@rexander",
                "kesan" : "Sangat informatif dalam menjelaskan sesuatu dan menjadi sosok yang memberikan banyak masukan serta motivasi melalui pengalaman yang telah dilakukan",  
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
                "kesan" : "Sangat baik, informatif dalam menerangkan suatu permasalahan dan sangat menginspirasi",  
                "pesan" : "Tetap semangat kak dalam menjalani harinya, semoga urusannya baik di akademik maupun non akademik dapat berjalan dengan lancar"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()   

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1gwODKlGn-bWqQ-AfR45fb27S4CHcPnNM", #bang andrian dn
            "https://drive.google.com/uc?export=view&id=1MirF2tx9NssFV1UFa2tNQ2gG9mw4WUOn", #kak adisty dn
            "https://drive.google.com/uc?export=view&id=1CMKEgT0NBXWQdVAeaaQFYCYhc73JcbcX", #kak nabilla dn
            "https://drive.google.com/uc?export=view&id=1IIr-42u5BtuTtt-8JH4IR7ZxQk1zQwPr", #bang danang dn
            "https://drive.google.com/uc?export=view&id=1OJWzKE6lG69lKci3LV7JmBodagbw-bAN", #bang farrel dn
            "https://drive.google.com/uc?export=view&id=1GEDlwY32JX7DCOpbeH8y8w59nt9X2Lbw", #kak nabilah dn
            "https://drive.google.com/uc?export=view&id=19qXG0V2VIiOpsjaD7i-B9bX5uYvWLu6Y", #kak alvia dn
            "https://drive.google.com/uc?export=view&id=1VOs5vQAQmZcmWSwTcNzU4FN5qKLPyFRl", #bang dhafin dn
            "https://drive.google.com/uc?export=view&id=1pmG_A7PQkp8wNFQes-5_FplfMVlGBa8X", #kak elia dn


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
