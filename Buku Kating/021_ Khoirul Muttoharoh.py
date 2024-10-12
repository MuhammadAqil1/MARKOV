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
            "https://drive.google.com/uc?export=view&id=1UuDll6EvmsLLI6S18guq2qjdrljxNbND", #Bang Kharisma
            "https://drive.google.com/uc?export=view&id=1lOd0lUoe9szDY62I-vUAa4UtXnO-qShl", #Bang Pandra
            "https://drive.google.com/uc?export=view&id=1o1lktcw74fQkhzFVWFxRrzpu3ftN3CnC",
            "https://drive.google.com/uc?export=view&id=1PERkV1lA5FW_wVRTCguamFVuAVSlYSP1",
            "https://drive.google.com/uc?export=view&id=1TH5ShZfH-PGMhK8OWmmk69SGb7T9cloA",
            "https://drive.google.com/uc?export=view&id=1COVpLRyuIaYxsCHDPU0VXS7zY0sWUcrp",


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
                "kesan" : "menginspirasi kami semua untuk terus berkembang dan mendorong kami untuk mencapai yang terbaik",  
                "pesan" :"Teruslah menjadi pemimpin yang inspiratif dan membawa himpunan kita ke pencapaian yang lebih tinggi."
            },
            {
                "nama"  : "Pandra Insani Putra Azwan",
                "nim"   : "121450137",
                "umur"  : "21",
                "asal"  : "Bukit Kemuning, Lampung Utara",
                "alamat": "Bawen 2",
                "hobbi" : "Bermain gitar dan menyanyi",
                "sosmed": "@pandrainsni27",
                "kesan" : "Seru dan terstruktur membantu saya memahami peran lebih dalam.",  
                "pesan" : "Terus jaga profesionalisme dan semangat dalam mengelola himpunan. "
            },
            {
                "nama"  : "Meliza Wulandari",
                "nim"   : "121450065",
                "umur"  : "20",
                "asal"  : "Pagar Alam, Sumatera Selatan",
                "alamat": "Kotabaru",
                "hobbi" : "Nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan" : "Penjelasannya terstruktur membuat suasana jadi lebih memahami dengan baik.",  
                "pesan" : "terus pertahankan profesionalisme dan cara kerja yang terorganisir"
            },
            {
                "nama"  : "Putri Maulida Chairani",
                "nim"   : "121450050",
                "umur"  : "21",
                "asal"  : "Payakumbuh, Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi" : "Dengerin bang pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan" : "sangat teratur dalam menyampaikan penjelasan dan membuat suasana jadi nyaman",  
                "pesan" : "Terus pertahankan keterampilan komunikasimu yang baik"
            },
            {
                "nama"  : "Hartiti Fadilah",
                "nim"   : "121450031",
                "umur"  : "21",
                "asal"  : "Palembang",
                "alamat": "Pemda",
                "hobbi" : "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan" : "menunjukkan pemahaman yang baik tentang peran bendahara dan tanggung jawab keuangan.",  
                "pesan" : "Teruslah berinovasi dalam mengelola keuangan, karena itu sangat penting untuk keberlangsungan himpunan kita"
            },
            {
                "nama"  : "Nadilla Andara Putri",
                "nim"   : "121450003",
                "umur"  : "21",
                "asal"  : "Metro",
                "alamat": "KotaBaru",
                "hobbi" : "Membaca",
                "sosmed": "@ndillaandr26",
                "kesan" : "sangat informatif dan menyenangkan tentang pengelolaan keuangan dan selalu siap membantu tim",  
                "pesan" : "Terus jaga transparansi dan komunikasi yang baik dalam pengelolaan anggaran"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=14cLBaPk-rxKgOGzDEhKFFIUgKby3gkVn",
            "https://drive.google.com/uc?export=view&id=1u_e_7IbkR49xNGpUq0k0dypQ5JLg86MI",
            "https://drive.google.com/uc?export=view&id=1LyOysFPoDo4wx1WFe8A5lCZ3cyE9o_Pl",
            "https://drive.google.com/uc?export=view&id=1FyYUKw6mOeKvSBFolpNVo7Hz_AUP2jAH",
            "https://drive.google.com/uc?export=view&id=1ZXxKC6uWaZk6q8FD9Ne53oEXh-TsolFe",
            "https://drive.google.com/uc?export=view&id=17t4XfB5dODRBv2JKFBUuBnJocJTfbiGZ",
            "https://drive.google.com/uc?export=view&id=1w3z-k4aVl0siron0PKwDLi3zSCsayQ-m",
            "https://drive.google.com/uc?export=view&id=1tvgFgrnnD2Xmhn_8P6Qc2i3ZTD97zWBp",
            "https://drive.google.com/uc?export=view&id=1B2uqKgD9xkijxbyzK-kyyREFwBVv5dwX",
            "https://drive.google.com/uc?export=view&id=1BnraND5nbYfQOw__sW9C1vmvAVoCfZyb",
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
                "kesan" : "sangat menginspirasi dan memberikan wawasan mendalam tentang peran badan legislasi. ",  
                "pesan" : "teruslah menjadi pemimpin yang visioner dan dorong kami untuk lebih aktif berkontribusi."
            },
            {
                "nama"  : "Annisa Cahyani Surya",
                "nim"   : "121450114",
                "umur"  : "21",
                "asal"  : "Tanggerang Selatan",
                "alamat": "Way Huwi",
                "hobbi" : "Membaca, Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan" : "sangat informatif. Pendekatannya yang sistematis dan jelas membantu saya memahami tugas dan tanggung jawab dalam badan ini.",  
                "pesan" : "Teruslah berkomitmen dalam memperjuangkan kepentingan anggota himpunan. "
            },
            {
                "nama"  : "Wulan Sabina",
                "nim"   : "121450150",
                "umur"  : "21",
                "asal"  : "Medan",
                "alamat": "Raden Saleh",
                "hobbi" : "Nonton Drakor",
                "sosmed": "@wlnsbn0",
                "kesan" : "sangat informatifmenunjukkan pemahaman yang baik tentang anggaran dan pentingnya transparansi dalam pengelolaan keuangan.",  
                "pesan" : " Teruslah bekerja dengan teliti dan terbuka, karena itu akan membawa himpunan ke arah yang lebih baik"
            },
            {
                "nama"  : "Annisa Dini Amaliya",
                "nim"   : "121450081",
                "umur"  : "21",
                "asal"  : "Tanggerang",
                "alamat": "Jati Agung",
                "hobbi" : "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan" : "sangat menarik dan membuka wawasan saya tentang proses pengambilan keputusan di himpunan.",  
                "pesan" : "Teruslah mengedepankan transparansi dan partisipasi dalam setiap kebijakan yang diambil."
            },
            {
                "nama"  : "Anisa Fitriyani",
                "nim"   : "121450150",
                "umur"  : "21",
                "asal"  : "Medan",
                "alamat": "Raden Saleh",
                "hobbi" : "Nonton Drakor",
                "sosmed": "@wlnsbn0",
                "kesan" : "sangat informatif dan mendalam relevan dan membuat saya lebih memahami peran penting komisi ini dalam himpunan.",  
                "pesan" : " Semoga komisi terus berinovasi dan memberikan kontribusi nyata bagi perkembangan himpunan"
            },
            {
                "nama"  : "Mirzan Yusuf Rabbani",
                "nim"   : "122450118",
                "umur"  : "20",
                "asal"  : "Jakarta",
                "alamat": "Korpri",
                "hobbi" : "Main Kucing",
                "sosmed": "@myrrinn",
                "kesan" : "sangat informatif mendorong saya untuk berpikir lebih dalam tentang kontribusi yang bisa saya berikan.",  
                "pesan" :"Semoga bisa bersama-sama membangun himpunan yang lebih baik dan lebih inovatif ke depannya."
            },
            {
                "nama"  : "Dhea Amelia Putri",
                "nim"   : "122450004",
                "umur"  : "20",
                "asal"  : "Sukabumi, Jawa Barat",
                "alamat": "Natar",
                "hobbi" : "Suka Ikut Tes SKD",
                "sosmed": "@dhea_wedding",
                "kesan" : "sangat menarik dan informatif yang membantu saya memahami peran dan tanggung jawab yang ada",  
                "pesan" : "Semoga Komisi 2 terus menjaga transparansi dan komunikasi yang baik"
            },
            {
                "nama"  : "Muhammad Fahrul Aditya",
                "nim"   : "121450156",
                "umur"  : "22",
                "asal"  : "Surakarta, Jawa Tengah",
                "alamat": "Pahoman",
                "hobbi" : "Melukis, badminton, hiking, ngopi, dengerin music, nonton film dan ngoding",
                "sosmed": "@fhrul.pdf",
                "kesan" : "sangat informatif dan memberikan perspektif baru tentang proses legislasi",  
                "pesan" : " Teruslah berinovasi dan menjaga komunikasi yang baik"
            },
            {
                "nama"  : "Berlianda Enda Putri",
                "nim"   : "122450065",
                "umur"  : "21",
                "asal"  : "Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi" : "Main Game",
                "sosmed": "@berlyyanda",
                "kesan" : "sangat informatif dan menarik yang membuat saya merasa nyaman untuk berbagi ide dan pendapat.",  
                "pesan" : "teruslah berinovasi dan berkolaborasi dalam menciptakan regulasi yang bermanfaat bagi himpunan."
            },
            {
                "nama"  : "Jeremia Susanto",
                "nim"   : "122450022",
                "umur"  : "20",
                "asal"  : " Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi" : "Marah-marah",
                "sosmed": "@jeremia_s_",
                "kesan" : "sangat informatif dan memberikan perspektif baru tentang peran legislasi dalam himpunan.",  
                "pesan" : "Teruslah berinovasi dalam merumuskan kebijakan yang bermanfaat bagi anggota himpunan"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

# Tambahkan menu lainnya sesuai kebutuhan
