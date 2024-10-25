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
                "kesan": "pengalaman yang abang ceritakan sangat menginspirasi",  
                "pesan": "Selalu dimudahkan segala sesuatu"
            },
            {
                "nama": "Meliza Wulandari",
                "nim": "121450065",
                "umur": "20",
                "asal": "Pagar Alam (Sumatera Selatan)",
                "alamat": "Kota baru",
                "hobbi": "Nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan": "pengalaman yag kakak ceritakan sangat menginspirasi",  
                "pesan": "Semoga dimudahkan dan dilancarkan apa yang disemogakan"
            },
            {
                "nama": "Putri Maulida Chairani",
                "nim": "121450050",
                "umur": "21",
                "asal": "Payakumbuh (Sumatera Barat)",
                "alamat": "Nangka 4",
                "hobbi": "Dengerin bang pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan": "pengalaman yang kakak ceritakan sangat menginspirasi",  
                "pesan": "Semoga dimudahkan dan dilancarkan apa yang disemogakan"
            },
            {
                "nama": "Hartiti Fadilah",
                "nim": "121450031",
                "umur": "21",
                "asal": "Palembang",
                "alamat": "Pemda",
                "hobbi": "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan": "pengalaman yang kakak ceritakan sangat menginspirasi",  
                "pesan": "Semoga dimudahkan dan dilancarkan apa yang disemogakan "
            },
            {
                "nama": "Nadilla Andara Putri",
                "nim": "121450003",
                "umur": "21",
                "asal": "Metro",
                "alamat": "Kota Baru",
                "hobbi": "Membaca",
                "sosmed": "@ndillaandr26",
                "kesan": "pengalaman yang kakak ceritakan sangat menginspirasi",  
                "pesan": "Semoga dimudahkan dan dilancarkan apa yang disemogakan"
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
                "pesan" : "Semoga dimudahkan dan dilancarkan apa yang disemogakan"
            },
            {
                "nama"  : "Annisa Cahyani Surya",
                "nim"   : "121450114",
                "umur"  : "21",
                "asal"  : "Tanggerang Selatan",
                "alamat": "Way Huwi",
                "hobbi" : "Membaca, Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
                "pesan" : "Semoga dimudahkan dan dilancarkan apa yang disemogakan"
            },
            {
                "nama"  : "Wulan Sabina",
                "nim"   : "121450150",
                "umur"  : "21",
                "asal"  : "Medan",
                "alamat": "Raden Saleh",
                "hobbi" : "Nonton Drakor",
                "sosmed": "@wlnsbn0",
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
                "pesan" : "Semoga dimudahkan dan dilancarkan apa yang disemogakan"
            },
            {
                "nama"  : "Annisa Dini Amaliya",
                "nim"   : "121450081",
                "umur"  : "21",
                "asal"  : "Tanggerang",
                "alamat": "Jati Agung",
                "hobbi" : "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
                "pesan" : "Semoga dimudahkan dan dilancarkan apa yang disemogakan"
            },
            {
                "nama"  : "Anisa Fitriyani",
                "nim"   : "121450150",
                "umur"  : "21",
                "asal"  : "Medan",
                "alamat": "Raden Saleh",
                "hobbi" : "Nonton Drakor",
                "sosmed": "@wlnsbn0",
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
                "pesan" : "Semoga dimudahkan dan dilancarkan apa yang disemogakan"
            },
            {
                "nama"  : "Mirzan Yusuf Rabbani",
                "nim"   : "122450118",
                "umur"  : "20",
                "asal"  : "Jakarta",
                "alamat": "Korpri",
                "hobbi" : "Main Kucing",
                "sosmed": "@myrrinn",
                "kesan" : "pengalaman yang abang ceritakan sangat menginspirasi",  
                "pesan" : "Semoga dimudahkan dan dilancarkan apa yang disemogakan"
            },
            {
                "nama"  : "Dhea Amelia Putri",
                "nim"   : "122450004",
                "umur"  : "20",
                "asal"  : "Sukabumi, Jawa Barat",
                "alamat": "Natar",
                "hobbi" : "Suka Ikut Tes SKD",
                "sosmed": "@dhea_wedding",
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
                "pesan" : "Semoga dimudahkan dan dilancarkan apa yang disemogakan"
            },
            {
                "nama"  : "Muhammad Fahrul Aditya",
                "nim"   : "121450156",
                "umur"  : "22",
                "asal"  : "Surakarta, Jawa Tengah",
                "alamat": "Pahoman",
                "hobbi" : "Melukis, badminton, hiking, ngopi, dengerin music, nonton film dan ngoding",
                "sosmed": "@fhrul.pdf",
                "kesan" : "pengalaman yang abang ceritakan sangat menginspirasi",  
                "pesan" : "Semoga dimudahkan dan dilancarkan apa yang disemogakan"
            },
            {
                "nama"  : "Berlianda Enda Putri",
                "nim"   : "122450065",
                "umur"  : "21",
                "asal"  : "Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi" : "Main Game",
                "sosmed": "@berlyyanda",
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
                "pesan" : "Semoga dimudahkan dan dilancarkan apa yang disemogakan"
            },
            {
                "nama"  : "Jeremia Susanto",
                "nim"   : "122450022",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi" : "Marah-marah",
                "sosmed": "@jeremia_s_",
                "kesan" : "pengalaman yang abang ceritakan sangat menginspirasi",  
                "pesan" : "Semoga dimudahkan dan dilancarkan apa yang disemogakan"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1GqJ_6TFrHfqplxpOdVE_aoj_HZUXfbpg", #kak lutfi
            "https://drive.google.com/uc?export=view&id=1GbioT1naHmK-sAiXrS7zn5uNNAFBb0y7", #bang bintang
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
                "pesan" : "Tetap semangat kak dalam menjalani hari-harinya, semoga diperlancar dalam menyelesaikan tugas dan tanggung jawab yang sedang di emban"
            },
            {
                "nama"  : "Rian Bintang Wijaya",
                "nim"   : "122450094",
                "umur"  : "20",
                "asal"  : "Palembang, Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi" : "Mendengar Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan" : "pengalaman yang abang ceritakan sangat menginspirasi",  
                "pesan" : "Semoga kegiatannya di dalam maupun di luar perkuliahan tetap lancar dan tetap semangat kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1RWgqyusXGPJClnVVjn_s3MCSm63iQ-Fy", #bang erickson dn 
            "https://drive.google.com/uc?export=view&id=1Q1dMAamIvkG3oXI5nB-6V2EHzmyorTT2", #kak abeth dn
            "https://drive.google.com/uc?export=view&id=19JjlQtmiZ-1WvgpdvA8P1Xd2Kb_dbyOE", #kak afifah dn s
            "https://drive.google.com/uc?export=view&id=1GB7cGU1BeN9orY_y4VH41T40soab7nte", #kak allya dn s
            "https://drive.google.com/uc?export=view&id=1gnMsLqa1EMqPUGlY9DRtMM8yDSRW0ahV", #kak hanum dn s
            "https://drive.google.com/uc?export=view&id=1BHdS3-OKOrWmlSZO7ATf_GCMfNT2yx1V", #bang ferdy dn s
            "https://drive.google.com/uc?export=view&id=1WPGXifHQ5eb4F-GvghQAVGBFdSUMsZnY", #bang deri dn s
            "https://drive.google.com/uc?export=view&id=1yaAofgqhaSNEePpBd6Oh0hqmrE5P0KGD", #kak oktavia dn s
            "https://drive.google.com/uc?export=view&id=18BpvVqXnB3h8RSPN2Vh3QvRfbp4nPoaw", #bang deyvan dn
            "https://drive.google.com/uc?export=view&id=1XLcy62n3HK9frz97BQCJf34hQZtblx0f", #bang ibnu dn
            "https://drive.google.com/uc?export=view&id=1b4XGem3phWmN0gsSME4_hSKPPNkZyjry", #bang jo dn
            "https://drive.google.com/uc?export=view&id=1PK3QE7FBMwJs1VgrIDPrA5LLypXGMWRm", #bang kemas dn
            "https://drive.google.com/uc?export=view&id=1bcMsgifyFq8WSFzUkRZ3VZ2HBD-KO_zt", #bang leonard dn
            "https://drive.google.com/uc?export=view&id=1vYFGbQj_W0rj4eO4X6dllnkkQzkIxmN4", #kak presilia dn
            "https://drive.google.com/uc?export=view&id=1wj6rscJxqPlzNaRXmMSqUIHU9dUvTWut", #kak rafa dn
            "https://drive.google.com/uc?export=view&id=1WdYZpDI9qwAJYrp70ZS3CY8BKXclLHJh", #bang sahid dn s
            "https://drive.google.com/uc?export=view&id=1milred8s9zpeSu3hVZWcGxdKbU3CoiGv", #kak vanes dn
            "https://drive.google.com/uc?export=view&id=151nlaE_-CU-_DSePFKXXuLRvikeFn3Ah", #bang ateng dn s
            "https://drive.google.com/uc?export=view&id=1in5H609G7RZ8htW0aBePB1hltrMrNwDy", #bang gede dn s
            "https://drive.google.com/uc?export=view&id=1p2e6X0AbZ2DDvvsL1kYr6kgU7R8leIJd", #kak jaclin dn s
            "https://drive.google.com/uc?export=view&id=1ClRuZzmVlNQHPfX6oKdJt-1X4l1gzAJK", #bang rafly dn s
            "https://drive.google.com/uc?export=view&id=1peUDX5MK8Hmy0ZCJY8-vMGDUu3YrN6tl", #kak dini dn s

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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
                "pesan" : "Semangat terus kak dalam menjalani hari-harinya, semoga semua tugas dan tanggung jawab yang diemban dapat diselesaikan dengan lancar"
            },
            {
                "nama"  : "Syalaisha Andini Putriansyah",
                "nim"   : "122450022",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi" : "Marah-marah",
                "sosmed": "@jeremia_s_",
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
                "pesan" : "Semangat kak dalam menjalani hari-harinya, semoga urusannya dalam dunia perkuliahan dapat diselesaikan dengan mudah"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1H2u71MT9pnWkuLZcovctHTEMHc8Tq4MH", #bang rafi dn s
            "https://drive.google.com/uc?export=view&id=1Hb3I2xJ_SIMTFTk97j4a0ZIPwgVWjUtU", #kak okta dn s
            "https://drive.google.com/uc?export=view&id=1HG__86bGzPwGpMtx77-AKtAHb_QGxHSq", #bang ahmad dn s
            "https://drive.google.com/uc?export=view&id=1HYl7-3ylnSmkRgDaS9zRkuObesugjKTO", #kak fadhil dn s
            "https://drive.google.com/uc?export=view&id=1HS1xzs4OUCKYuMDcCOAUgC92bFJ9Cyar", #kak syalaisha dn s
            "https://drive.google.com/uc?export=view&id=1H_-QKrFcZIvvs0hR_zngPc2qeGUM8rs1", #kak dinda dn s
            "https://drive.google.com/uc?export=view&id=1HUpA4eNdLqQk5uK7oKeO_QQVgw739e6a", #kak marleta dn s
            "https://drive.google.com/uc?export=view&id=1Hk-4IMGGQnZXQBqj42EdBpbovo8J-9Ex", #kak rut junita dn s
            "https://drive.google.com/uc?export=view&id=1HakAaJGccfqwmyQZG7ofNTFtos54mvYf", #kak syadza dn s
            "https://drive.google.com/uc?export=view&id=1H9MeCzL9N4ODgAslrKS-3Dj-CCkqlCAF", #bang eggi dn s
            "https://drive.google.com/uc?export=view&id=1HspJcvrDjnVCzlESaKP8vPikA-OC1TFa", #kak febiya dn s
            "https://drive.google.com/uc?export=view&id=1HQpDeadQ5q_Wi2qsQIYw5x0hnWksrOSb", #kak happy syahrul dn s
            "https://drive.google.com/uc?export=view&id=1HZIzXu9YUxfiBL1QwRo51piheouiV4tg", #bang randa dn s
            "https://drive.google.com/uc?export=view&id=1YybaYByUKEuuUL_oYi4AUrDb3UgzXwRt", #kak vita dn
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
                "kesan" : "pengalaman yang abang ceritakan sangat menginspirasi",  
                "pesan" : "Tetap semangat kak dalam menjalani hari-harinya, semoga diperlancar dalam menyelesaikan tugas dan tanggung jawab yang sedang di emban"
            },
            {
                "nama"  : "Annisa Novantika",
                "nim"   : "121450005",
                "umur"  : "21",
                "asal"  : "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi" : "Memasak",
                "sosmed": "@anovavona",
                "kesan" : "kakaknya ramah",  
                "pesan" : "semoga kuliahnya lancar"
            },
            {
                "nama"  : "Ahmad Sahidin Akbar",
                "nim"   : "121450114",
                "umur"  : "21",
                "asal"  : "Tanggerang Selatan",
                "alamat": "Way Huwi",
                "hobbi" : "Membaca, Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan" : "pengalaman yang abang ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang abang ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang abang ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang abang ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang abang ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang abang ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang abang ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang abang ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang abang ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang abang ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
                "pesan" : "Semangat terus kak dalam menjalani perkuliahannya serta jangan lupa untuk jaga kesehatan"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1KRJnBqOrpDGUgbJjFBgl53l6N7hjTt_a", #bang yogy dn s
            "https://drive.google.com/uc?export=view&id=1JxoAydMaakJxWJYy43aOstZB3aKoHeNr", #kak ramadhita dn s
            "https://drive.google.com/uc?export=view&id=1LaJStnx96SeihXcW9gIwaN94GlSRCea5", #kak nazwa dn s
            "https://drive.google.com/uc?export=view&id=1LdZDWHzjGdYy327Zg8XBa1wdHNNllA-Q", #bang bastian dn s
            "https://drive.google.com/uc?export=view&id=1LMkJa2SmuB4n3tsiPWG3KyJ1ill6MZjl", #kak dea dn s
            "https://drive.google.com/uc?export=view&id=1LVQuMnFmdbeB6cBRr44Kh5_K4papgozh", #kak esteria dn s
            "https://drive.google.com/uc?export=view&id=1LPH6QWdTjAKtVwVB327DwctNT9HI4p8v", #kak natasya ega dn s
            "https://drive.google.com/uc?export=view&id=1KxKT0xmHTqUuiu6w8y2qSCWiv3YiK7j0", #kak novelia dn s
            "https://drive.google.com/uc?export=view&id=1LGmFrZdfQfRMwh-Lr90TtdJVNH6uiUui", #kak jasmine dn s
            "https://drive.google.com/uc?export=view&id=1LmXY0D2ra6W25v-htcFXFMy76oO7bbCc", #bang tobias dn s
            "https://drive.google.com/uc?export=view&id=1L582x1ZkcRH7kCnF15067kqqBpvbebth", #kak yohana dn s
            "https://drive.google.com/uc?export=view&id=1LyxkXLGIpFeDvq_DNBrGWoX5joV96DKB", #bang rizki dn s
            "https://drive.google.com/uc?export=view&id=1JumBzSBB7HrzKjOfeNLQQIaSf-BURYmE", #bang arafi dn s
            "https://drive.google.com/uc?export=view&id=1Lw9ct7Wp3amZqHxFPTV9AjB3QKWJp0q3", #kak uyi dn s
            "https://drive.google.com/uc?export=view&id=1M0fgPiUHRHDp3Qfs6cd3zxlpCE94F4nJ", #kak chalifia dn s
            "https://drive.google.com/uc?export=view&id=1KwYWpyCIPSagtW3_555ZdFNLQZXmoDhs", #bang irvan dn s
            "https://drive.google.com/uc?export=view&id=1KsGU2uDIlaXYRaGHffgzT_bpDN-pqwQd", #kak izza dn s
            "https://drive.google.com/uc?export=view&id=1KbarKt6nz5LPM3KB-ipZLMORiBd5XQub", #kak zuhrah dn s
            "https://drive.google.com/uc?export=view&id=1Kqay263YzMPdQfDeRZD129l9up1wWLpL", #bang raid dn s
            "https://drive.google.com/uc?export=view&id=1slu-o22MSwKg_BP5JDOUdvjbzAyaWNS7", #kak tria dn
        ]
        data_list = [
            {
                "nama"  : "Yogy Sae Tama",
                "nim": "121450041",
                "umur": "21 Tahun",
                "asal": "Tangerang",
                "alamat": "Jatimulyo",
                "hobi": "Bangun pagi",
                "sosmed": "@yogyyyyyy",
                "kesan" : "pengalaman yang abang ceritakan sangat menginspirasi",  
                "pesan" : "Tetap semangat kak dalam menjalani hari-harinya, semoga diperlancar dalam menyelesaikan tugas dan tanggung jawab yang sedang di emban"
            },
            {
                "nama"  : "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobi": "Jalan - Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
                "pesan" : "Semoga kegiatannya di dalam maupun di luar perkuliahan tetap lancar dan tetap semangat kak"
            },
            {
                "nama"  : "Nazwa Nabilla",
                "nim": "121450122",
                "umur": "21 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Way kandis",
                "hobi": "belajar",
                "sosmed": "@nazwanbilla",
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
                "pesan" : "Tetap semangat kak dalam menjalani harinya, semoga urusannya baik di akademik maupun non akademik dapat berjalan dengan lancar"
            },
            {
                "nama"  : "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21 Tahun",
                "asal": "Batam, Kep. Riau",
                "alamat": "Belwis",
                "hobi": "main game",
                "sosmed": "@bastiansilaban_",
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
                "pesan" : "Semoga selalu dilancarkan semua urusannya kak, jangan lupa untuk tetap semangat kak dalam menjalani kehidupan"
            },
            {
                "nama"  : "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20 Tahun",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobi": "dengerin musik",
                "sosmed": "@deaa.rsn",
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
                "pesan" : "Tetap semangat dalam menjalani perkuliahannya kak dan jangan lupa jaga kesehatan"
            },
            {
                "nama"  : "Esteria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "19 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Belwis",
                "hobi": "Main golf bareng kadiv",
                "sosmed": "@esteriars",
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
                "pesan" : "Tetap semangat kak dalam menjalani dunia perkuliahan"
            },
            {
                "nama"  : "Natasya Ega Lina",
                "nim": "122450024",
                "umur": "19 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobi": "jadi humas",
                "sosmed": "@nateee__15",
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
                "pesan" : "Semangat terus kak dalam menjalani perkuliahannya serta jangan lupa untuk jaga kesehatan"
            },
            {
                "nama"  : "Novelia Adinda",
                "nim": "122450104",
                "umur": "21 Tahun",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
                "pesan" : "Jangan lupa untuk tetap semangat dalam menjalani dunia perkuliahan kak, semoga urusannya selalu dilancarkan"
            },
            {
                "nama"  : "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Way Kandis",
                "hobi": "Main sepak takraw",
                "sosmed": "@jasminednva",
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
                "pesan" : "Semangat terus kak dalam menjalani hari-harinya, semoga semua tugas dan tanggung jawab yang diemban dapat diselesaikan dengan lancar"
            },
            {
                "nama"  : "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20 Tahun",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobi": "Jogging",
                "sosmed": "@tobiassiagian",
                "kesan" : "pengalaman yang abang ceritakan sangat menginspirasi",  
                "pesan" : "Semangat kak dalam menjalani hari-harinya, semoga urusannya dalam dunia perkuliahan dapat diselesaikan dengan mudah"
            },
             {
                "nama"  : "Yohana Manik",
                "nim": "122450126",
                "umur": "19 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobi": "Main Bowling",
                "sosmed": "@yo_annamnk",
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
                "pesan" : "Tetap semangat kak dalam menjalani hari-harinya, semoga diperlancar dalam menyelesaikan tugas dan tanggung jawab yang sedang di emban"
            },
            {
                "nama"  : "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21 Tahun",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobi": "Bikin portofolio",
                "sosmed": "@rzkdrnnn",
                "kesan" : "pengalaman yang abang ceritakan sangat menginspirasi",  
                "pesan" : "Semoga kegiatannya di dalam maupun di luar perkuliahan tetap lancar dan tetap semangat kak"
            },
            {
                "nama"  : "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20 Tahun",
                "asal": "Bandung",
                "alamat": "Way Huwi",
                "hobi": "Bertani",
                "sosmed": "@rafiramadhanmaulana",
                "kesan" : "pengalaman yang abang ceritakan sangat menginspirasi",  
                "pesan" : "Tetap semangat kak dalam menjalani harinya, semoga urusannya baik di akademik maupun non akademik dapat berjalan dengan lancar"
            },
            {
                "nama"  : "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20 Tahun",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobi": "Tepuk Semangat",
                "sosmed": "@u_yippy",
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
                "pesan" : "Semoga selalu dilancarkan semua urusannya kak, jangan lupa untuk tetap semangat kak dalam menjalani kehidupan"
            },
            {
                "nama"  : "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20 Tahun",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobi": "Q Time",
                "sosmed": "@chlfawww",
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
                "pesan" : "Tetap semangat dalam menjalani perkuliahannya kak dan jangan lupa jaga kesehatan"
            },
            {
                "nama"  : "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21 Tahun",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobi": "Nonton youtube, main game",
                "sosmed": "@alfaritziirvan",
                "kesan" : "pengalaman yang abang ceritakan sangat menginspirasi",  
                "pesan" : "Tetap semangat kak dalam menjalani dunia perkuliahan"
            },
            {
                "nama"  : "Izza Lutfia",
                "nim": "122450090",
                "umur": "20 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobi": "Main Rubik",
                "sosmed": "@izzalutfia",
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
                "pesan" : "Semangat terus kak dalam menjalani perkuliahannya serta jangan lupa untuk jaga kesehatan"
            },
            {
                "nama"  : "Khaalishah Zuhrah Alyaa Vanefi",
                "nim": "122450034",
                "umur": "20 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobi": "Mengaji",
                "sosmed": "@alyaavanevi",
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
                "pesan" : "Jangan lupa untuk tetap semangat dalam menjalani dunia perkuliahan kak, semoga urusannya selalu dilancarkan"
            },
            {
                "nama"  : "Raid Muhammad Naufal",
                "nim": "122450027",
                "umur": "20 Tahun",
                "asal": "Lampung Tengah",
                "alamat": "Sukarame",
                "hobi": "telat",
                "sosmed": "@rayths_",
                "kesan" : "pengalaman yang abang ceritakan sangat menginspirasi",  
                "pesan" : "Semangat terus kak dalam menjalani hari-harinya, semoga semua tugas dan tanggung jawab yang diemban dapat diselesaikan dengan lancar"
            },
            {
                "nama"  : "Tria Yunanni",
                "nim": "122450062",
                "umur": "20 Tahun",
                "asal": "Way Kanan",
                "alamat": "Sukarame",
                "hobi": "Baca Buku",
                "sosmed": "@tria_y062",
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
                "pesan" : "Semangat kak dalam menjalani hari-harinya, semoga urusannya dalam dunia perkuliahan dapat diselesaikan dengan mudah"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()  

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1EeVG7gClrdJi4MCq_CpfQd480uw1p5dw", #bang dimas dn s
            "https://drive.google.com/uc?export=view&id=1iYWuL5DV8E-dINZXRAF2qVaO070tHMdi", #kak catherine dn s
            "https://drive.google.com/uc?export=view&id=1X4xkhwXl1SGQpLCRBQVxBa1RHnSRvvk0", #bang akbar dn s
            "https://drive.google.com/uc?export=view&id=1bbO-Ld98EkvOiXuev4nBYcTSc8lNbk9X", #kak rani dn s
            "https://drive.google.com/uc?export=view&id=1_m6gCZpn32Rg2pc0wyW-UOL1TaaeXKcl", #bang rendra dn s
            "https://drive.google.com/uc?export=view&id=1wABUc8w7sb2v-hBj8VdEir7ukNMJPwG9", #kak salwa dn s
            "https://drive.google.com/uc?export=view&id=1dV29MMU89WLIV7RCo07KJ47O8QWeQ1tn", #bang yosia dn  s
            "https://drive.google.com/uc?export=view&id=1p40VrYL9jw59ewSi_214B3-BVjKMyNIg", #bang ari dn s
            "https://drive.google.com/uc?export=view&id=1VSWoTQcZZhR3SmY-WAAeWfwcgiOZKMu1", #kak azizah dn s
            "https://drive.google.com/uc?export=view&id=1iJ8iUfwGD5nwBHyxBjiS5FQmBNdP9aYG", #kak meira dn s
            "https://drive.google.com/uc?export=view&id=1RNXXnTMV-RXGD-TYs7dC6iUDm84J_e2X", #bang rendi dn s
            "https://drive.google.com/uc?export=view&id=17EOxwfebAx-ohTFM-fPYbeGx9RZ5TMC4", #kak renta dn s
            "https://drive.google.com/uc?export=view&id=1kAc7X5QFIX0lRmHrDIalsF5qpxucBQJ7", #bang josua dn s

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
                "kesan" : "pengalaman yang abang ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang abang ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang abang ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang abang ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang abang ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang abang ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang abang ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang abang ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang abang ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang abang ceritakan sangat menginspirasi",  
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
                "kesan" : "pengalaman yang kakak ceritakan sangat menginspirasi",  
                "pesan" : "Semangat terus kak dalam menjalani hari-harinya, semoga semua tugas dan tanggung jawab yang diemban dapat diselesaikan dengan lancar"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()    
# Tambahkan menu lainnya sesuai kebutuhan
