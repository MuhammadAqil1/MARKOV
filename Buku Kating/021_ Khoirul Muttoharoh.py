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
                "pesan" : "terus pertahankan profesionalisme dan cara kerja yang terorganisir ya kak"
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
                "pesan" : "Terus pertahankan keterampilan komunikasi yang baik ya kaka"
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
                "kesan" : "sangat informatif dan menyenangkan tentang pengelolaan keuangan",  
                "pesan" : "Terus jaga transparansi dan komunikasi yang baik dalam pengelolaan anggaran kak"
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
                "pesan" : "teruslah menjadi pemimpin yang visioner dan dorong kami untuk lebih aktif untuk berkontribusi dalam himpunan ya kak."
            },
            {
                "nama"  : "Annisa Cahyani Surya",
                "nim"   : "121450114",
                "umur"  : "21",
                "asal"  : "Tanggerang Selatan",
                "alamat": "Way Huwi",
                "hobbi" : "Membaca, Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan" : "sangat informatif. Pendekatannya yang sistematis dan jelas.",  
                "pesan" : "Terus berkomitmen dalam memperjuangkan kepentingan anggota himpunan. "
            },
            {
                "nama"  : "Wulan Sabina",
                "nim"   : "121450150",
                "umur"  : "21",
                "asal"  : "Medan",
                "alamat": "Raden Saleh",
                "hobbi" : "Nonton Drakor",
                "sosmed": "@wlnsbn0",
                "kesan" : "sangat informatif dalam pentingnya transparansi pengelolaan keuangan.",  
                "pesan" : " Terus bekerja dengan teliti dan terbuka ya kak."
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
                "pesan" : "Teruslah mengedepankan transparansi dan partisipasi dalam setiap kebijakan yang diambil ya kak."
            },
            {
                "nama"  : "Anisa Fitriyani",
                "nim"   : "121450150",
                "umur"  : "21",
                "asal"  : "Medan",
                "alamat": "Raden Saleh",
                "hobbi" : "Nonton Drakor",
                "sosmed": "@wlnsbn0",
                "kesan" : "sangat informatif dan membuat saya lebih memahami peran penting komisi ini dalam himpunan.",  
                "pesan" : " Semoga komisi ini terus berinovasi dan memberikan kontribusi nyata bagi perkembangan himpunan"
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
                "pesan" : "Semoga Komisi 2 terus menjaga transparansi dan komunikasi yang baik ya kak"
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
                "pesan" : " Terus berinovasi dan menjaga komunikasi yang baik"
            },
            {
                "nama"  : "Berlianda Enda Putri",
                "nim"   : "122450065",
                "umur"  : "21",
                "asal"  : "Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi" : "Main Game",
                "sosmed": "@berlyyanda",
                "kesan" : "sangat informatif dan menarik",  
                "pesan" : "terus berinovasi dan berkolaborasi dalam menciptakan regulasi yang bermanfaat bagi himpunan."
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
                "pesan" : "Terus berinovasi dalam merumuskan kebijakan yang bermanfaat bagi anggota himpunan"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=16mxlsEJGzu2yeLfMce8NM9dDrcM3TTA0", #kak lutfi
            "https://drive.google.com/uc?export=view&id=15vA3yIh7K_L2C7Fwmhen49TT1FfofkfN", #bang bintang
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
                "kesan" : "menunjukkan tanggung jawab besar dan mampu menciptakan lingkungan yang inklusif, sangat menginspirasi!",  
                "pesan" : "Semoga terus konsisten dalam mengemban amanah dan memberikan yang terbaik bagi himpunan"
            },
            {
                "nama"  : "Rian Bintang Wijaya",
                "nim"   : "122450094",
                "umur"  : "20",
                "asal"  : "Palembang, Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi" : "Mendengar Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan" : "menunjukkan dedikasi luar biasa dalam mendampingi senator, selalu siap bekerja sama dan menjalankan tugas dengan penuh tanggung jawab.",  
                "pesan" : " Semoga terus menjadi inspirasi dan memberikan kontribusi terbaik ya bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=17knRcfMgnccG5WAY0JQnzKAo23V8z1GS", #bang erickson dn
            "https://drive.google.com/uc?export=view&id=1kN9Y4E2Hk0Jx0La-Pylgv7r23SAAZcv0", #kak abeth dn
            "https://drive.google.com/uc?export=view&id=1-96TJaz4Joe1RoD54b-PQ1Y7QERpCHSI", #kak afifah dn
            "https://drive.google.com/uc?export=view&id=1UVBzCijvrYUYZRGy-Z-imOr9LGGdVYWI", #kak allya dn
            "https://drive.google.com/uc?export=view&id=1ndhByE0NevjpyAHjpfY-LJoR0rvO1h9Z", #kak hanum dn
            "https://drive.google.com/uc?export=view&id=1GKSGCPF1-e2zT0nEOKjJO_T6-kriHnJt", #bang ferdy dn
            "https://drive.google.com/uc?export=view&id=1wn6sGaB2DOXpmWk1iV7Feur7t8pA4xEh", #bang deri dn
            "https://drive.google.com/uc?export=view&id=1VfbiWTKvSXPEx1-z9GRw8BlXTwY3YZv7", #kak oktavia dn
            "https://drive.google.com/uc?export=view&id=1pPcrp1sXTsZ3Aw0e939CszslDi95VmW_", #bang deyvan dn
            "https://drive.google.com/uc?export=view&id=1sjMUIiKbAy44sIG-Z-RJh0SpYZCLcMhe", #bang ibnu dn
            "https://drive.google.com/uc?export=view&id=1tjaS90B1NKR8aVNElSOJiWX_DX6wj0BG", #bang jo dn
            "https://drive.google.com/uc?export=view&id=1DjpYmpgCv2XJFEZ26m4Oontk5pjcahI8", #bang kemas dn
            "https://drive.google.com/uc?export=view&id=1ghTkV5tZAk5igWLUHtVkoSVePPx-L242", #bang leonard dn
            "https://drive.google.com/uc?export=view&id=1EDmWXCguBcBzniwdK2c4cf_RWIm7iyC7", #kak presilia dn
            "https://drive.google.com/uc?export=view&id=18T8gVZHdynnMr1-8OPLiOvRTW0GFCsBW", #kak rafa dn
            "https://drive.google.com/uc?export=view&id=1sjMUIiKbAy44sIG-Z-RJh0SpYZCLcMhe", #bang sahid dn
            "https://drive.google.com/uc?export=view&id=1K81woh4uOlMh6RN0lFukU_qGMpcQBIrv", #kak vanes dn
            "https://drive.google.com/uc?export=view&id=1G4mR0n6l8e2--3cRIyCJBP52zL8IHI-s", #bang ateng dn
            "https://drive.google.com/uc?export=view&id=1HEbXiyv70UJypIXulPNRBem7fUltwjbr", #bang gede dn
            "https://drive.google.com/uc?export=view&id=1sdB8ea_Pjl_6wz2MHSYJj6ZiSaq-YuMU", #kak jaclin dn
            "https://drive.google.com/uc?export=view&id=1Bhy3FH7h0iiy51ncyVgeIdqqcPCtgnyq", #bang rafly dn
            "https://drive.google.com/uc?export=view&id=17yA_vrQG3ptjV5vLNWi5z19bDp2LtY5h", #kak dini dn

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
                "kesan" : "komitmen tinggi dalam memajukan kualitas anggota dan menginspirasi",  
                "pesan" : "Semoga terus berinovasi dan menciptakan program yang bermanfaat bagi kemajuan himpunan"
            },
            {
                "nama"  : "Elisabeth Claudia Simanjuntak",
                "nim"   : "122450123",
                "umur"  : "18",
                "asal"  : "Pekanbaru",
                "alamat": "Sukarame",
                "hobbi" : "Memancing keributan",
                "sosmed": "@celisabethh_",
                "kesan" : "sangat teliti dan cekatan dalam mengelola segala kebutuhan administratif, membuat kegiatan PSDA berjalan lebih rapi dan efektif",  
                "pesan" : "Semoga terus konsisten dan semakin bersemangat dalam mengurus administrasi PSDA"
            },
            {
                "nama"  : "Nisrina Nur Afifah",
                "nim"   : "122450052",
                "umur"  : "19",
                "asal"  : "Bekasi",
                "alamat": "Sukarame",
                "hobbi" : "Nabok orang",
                "sosmed": "@afifahhnsrn",
                "kesan" : "menunjukkan dedikasi tinggi dan komitmen kuat dalam menjalankan proses kaderisasi.",  
                "pesan" : "Semoga selalu diberi semangat dan kreativitas untuk terus membimbing calon anggota dengan baik"
            },
            {
                "nama"  : "Allya Nurul Islami Pasha",
                "nim"   : "122450033",
                "umur"  : "20",
                "asal"  : "Sumatera Barat",
                "alamat": "Gang Perwira, Belwis",
                "hobbi" : "Nonton Dracin",
                "sosmed": "@allyaislami_",
                "kesan" : "sangat cekatan dan profesionalitas dalam setiap kegiatan,",  
                "pesan" : "Semoga terus bersemangat dalam membimbing dan menjadi contoh bagi para calon anggota"
            },
            {
                "nama"  : "Farahanum Afifah Ardiansyah",
                "nim"   : "122450056",
                "umur"  : "20",
                "asal"  : "Padang, Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi" : "Tidur",
                "sosmed": "@farahanumafifahh",
                "kesan" : "sangat berdedikasi dan selalu siap membantu ",  
                "pesan" : "Tetaplah konsisten dan berikan yang terbaik dalam membimbing calon anggota ya kak"
            },
            {
                "nama"  : "Ferdy Kevin Naibaho",
                "nim"   : "122450107",
                "umur"  : "19",
                "asal"  : "Medan, Sumatera Utara",
                "alamat": "Jalan Senopati Raya 18",
                "hobbi" : "Dengerin Rocky Gerung",
                "sosmed": "@ferdy_kevin",
                "kesan" : "menunjukkan dedikasi dan profesionalitas yang luar biasa",  
                "pesan" : "Semoga terus memberikan inspirasi dan semangat bagi para calon anggota ya bang"
            },
            {
                "nama"  : "M. Deriansyah Okutra",
                "nim"   : "122450101",
                "umur"  : "19",
                "asal"  : "Kayu Agung",
                "alamat": "Jalan Pagar Alam",
                "hobbi" : "Bercerita horror",
                "sosmed": "@dransyh_",
                "kesan" : "sangat antusias dan siap membantu",  
                "pesan" : "Terima kasih atas dedikasi dan semangatnya dalam mendukung proses kaderisasi. "
            },
            {
                "nama"  : "Oktavia Nurwenda Puspita Sari",
                "nim"   : "122450041",
                "umur"  : "20",
                "asal"  : "Lampung Timur",
                "alamat": "Way Hui",
                "hobbi" : "Memasak",
                "sosmed": "@_oktavianrwnda_",
                "kesan" : "menunjukkan kerja sama yang solid dan antusiasme tinggi",  
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
                "kesan" : "membantu anggota menemukan dan mengembangkan potensi mereka",  
                "pesan" : "emoga terus menciptakan peluang yang bermanfaat bagi anggota"
            },
            {
                "nama"  : "Ibnu Farhan Al-Ghifari",
                "nim"   : "121450121",
                "umur"  : "21",
                "asal"  : "Jambi",
                "alamat": "Pulau Damar, Kobam",
                "hobbi" : "Bermain Game Online",
                "sosmed": "@al_ghifari032",
                "kesan" : "menunjukkan antusiasme dan dedikasi yang luar biasa",  
                "pesan" : "Semoga terus berkontribusi dalam membantu anggota menemukan dan mengembangkan potensi"
            },
             {
                "nama"  : "Johannes Krisjon Silitonga",
                "nim"   : "122450043",
                "umur"  : "19",
                "asal"  : "Tanggerang",
                "alamat": "Jalan Lapas",
                "hobbi" : "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan" : "sangat aktif dan responsif, menciptakan atmosfer yang mendukung bagi anggota untuk mengeksplorasi dan mengembangkan potensi",  
                "pesan" : "Semoga terus bersemangat dan memberikan kontribusi yang berarti bagi perkembangan anggota"
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
                "pesan" : "Semoga kegiatannya di dalam maupun di luar perkuliahan tetap lancar dan tetap semangat bang"
            },
            {
                "nama"  : "Leonard Andreas Napitupulu",
                "nim"   : "121450153",
                "umur"  : "21",
                "asal"  : "Sumatera Utara",
                "alamat": "Kobam",
                "hobbi" : "Belajar",
                "sosmed": "@lnrd.__",
                "kesan" : "menunjukkan antusiasme dan kreativitas dalam setiap kegiatan",  
                "pesan" : "Semoga terus bersemangat dalam membantu anggota menemukan potensi terbaiknya"
            },
            {
                "nama"  : "Presilia",
                "nim"   : "122450081",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Kota Baru",
                "hobbi" : "Tidur",
                "sosmed": "@presiliamg",
                "kesan" : "antusias dan kreatif dalam menjalankan tugas",  
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
                "kesan" : "menunjukkan semangat yang tinggi dan kerja sama yang baik",  
                "pesan" : "Tetap semangat dalam menjalani perkuliahannya kak"
            },
            {
                "nama"  : "Sahid Maulana",
                "nim"   : "122450109",
                "umur"  : "21",
                "asal"  : "Depok, Jawa Barat",
                "alamat": "Airan Raya",
                "hobbi" : "Bermain Game",
                "sosmed": "@sahid_maul19",
                "kesan" : "sangat aktif dan kreatif, membantu menciptakan lingkungan yang positif untuk pengembangan potensi",  
                "pesan" : "Semoga terus bersemangat dan terus memberikan inspirasi bagi anggota"
            },
            {
                "nama"  : "Vanessa Olivia Rose",
                "nim"   : "121450068",
                "umur"  : "20",
                "asal"  : "Jakarta",
                "alamat": "Perumahan Korpri",
                "hobbi" : "Belajar",
                "sosmed": "@roselivnes__",
                "kesan" : "berhasil menciptakan suasana yang ceria dan menyenangkan. Energi positif dan ide-ide kreatif membuat setiap kegiatan menjadi lebih hidup dan menginspirasi",  
                "pesan" : "Semoga terus berinovasi dan memberikan pengalaman berharga bagi semua anggota, jangan lupa jaga kedehatan ya kak"
            },
            {
                "nama"  : "M. Farhan Athaulloh",
                "nim"   : "121450156",
                "umur"  : "22",
                "asal"  : "Surakarta, Jawa Tengah",
                "alamat": "Pahoman",
                "hobbi" : "Melukis, badminton, hiking, ngopi, dengerin music, nonton film dan ngoding",
                "sosmed": "@fhrul.pdf",
                "kesan" : "menunjukkan komitmen tinggi dan kemampuan yang sangat baik dalam menjalankan tugas",  
                "pesan" : "Semoga terus menciptakan program yang inovatif dan bermanfaat bagi semua anggota"
            },
            {
                "nama"  : "Gede Moana",
                "nim"   : "121450014",
                "umur"  : "21",
                "asal"  : "Bekasi",
                "alamat": "Korpri Raya",
                "hobbi" : "Belajar dan main game",
                "sosmed": "@gedemoenaa",
                "kesan" : "sangat antusias dan responsif",  
                "pesan" : "sangat kompak dan antusias"
            },
            {
                "nama"  : "Jaclin Alcavella",
                "nim"   : "122450015",
                "umur"  : "19",
                "asal"  : "Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi" : "Berenang",
                "sosmed": "@jaclinalcv_",
                "kesan" : "menunjukkan dedikasi yang luar biasa dan selalu siap membantu serta responsif",  
                "pesan" : "Semangat kak dalam menjalani hari-harinya dan memberikan kontribusi yang berarti bagi semua program yang dijalankan"
            },
            {
                "nama"  : "Rafly Prabu Darmawan",
               "nim"   : "122450140",
                "umur"  : "20",
                "asal"  : "Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi" : "Main Game",
                "sosmed": "@raflyy_pd2684",
                "kesan" : "menunjukkan semangat dan antusiasme tinggi",  
                "pesan" : "Semoga terus berinovasi dan memberikan kontribusi positif bagi kemajuan tim"
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
                "pesan" : "Semangat kak dalam menjalani hari-harinya, semoga urusannya dalam dunia perkuliahan dapat diselesaikan dengan mudah"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1YKNiWbwY3jOh067vCxdZ55iN8UvONyYc", #bang rafi dn
            "https://drive.google.com/uc?export=view&id=1rSsgJzVgIl9tojFQXiAUYyBekeu35eIh", #bang ahmad dn
            "https://drive.google.com/uc?export=view&id=17L5MxcMeTgt2OrTcdCWaSFz0LnTnoW_0", #bang fadhil dn
            "https://drive.google.com/uc?export=view&id=15-2mowlQGOVigpobCwIgppi-v0jJTCqr", #kak dina dn
            "https://drive.google.com/uc?export=view&id=1VYMGVGniHryN2JYUCn7CZX4yB1hp4i97", #kak dinda dn
            "https://drive.google.com/uc?export=view&id=16o6A78JqBqY9RZVu1y-GGJFmwsK_6hme", #kak marleta dn
            "https://drive.google.com/uc?export=view&id=1yFliisqkaoG-XeNPZSEqin2w_D-VRYvV", #kak rut junita dn
            "https://drive.google.com/uc?export=view&id=191w61QSLwW8rjjP_axR5Cix4O32OTmUR", #kak syadza dn
            "https://drive.google.com/uc?export=view&id=1mjaWvNJiyweO9V1Ay6igR89nVQ_5hake", #bang eggi dn
            "https://drive.google.com/uc?export=view&id=1ayloSGzrze9b7lmPysAh09vluY5P-7PM", #kak febiya dn
            "https://drive.google.com/uc?export=view&id=1pooIAy5oDPDFSg8weh1KUQvA_WTcIBHu", #kak happy syahrul dn
            "https://drive.google.com/uc?export=view&id=16ZuYQpxNLfLUCy7wOTWMzgRh5bnLz4NE", #bang randa dn
            "https://drive.google.com/uc?export=view&id=1DHYoiOXbDJYRkNwdmmvvIAxx3c8NR4Lg", #kak vita dn
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
                "kesan" : "menunjukkan komitmen tinggi dan selalu membawa ide-ide segar",  
                "pesan" : "Semoga terus menghadirkan program-program inspiratif yang membantu anggota dalam mengembangkan diri dan potensi mereka"
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
                "pesan" : "Semoga terus bersemangat dan memberikan yang terbaik untuk menciptakan acara yang berkesan"
            },
            {
                "nama"  : "Fadhil Fitra Wijaya",
                "nim"   : "122450082",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Teluk Betung",
                "hobbi" : "Main game",
                "sosmed": "@fadhilfwee",
                "kesan" : "sangat antusias dan cekatan",  
                "pesan" : "semangat dalam mendukung suksesnya Mikfes"
            },
            {
                "nama"  : "Syalaisha Andina Putriansyah",
                "nim"   : "122450121",
                "umur"  : "21",
                "asal"  : "Tangerang",
                "alamat": "Gang Yudhistira",
                "hobbi" : "Baca jurnal",
                "sosmed": "@dkselsd_31",
                "kesan" : "pendiam tetapi penuh komitmen",  
                "pesan" : "Semoga terus memberikan kontribusi yang berarti dan inspiratif meskipun tanpa banyak kata"
            },
            {
                "nama"  : "Dinda Nababan",
                 "nim"   : "122450120",
                "umur"  : "20",
                "asal"  : "Medan, Sumatera Utara",
                "alamat": "Jalan Lapas",
                "hobbi" : "Belajar",
                "sosmed": "@dindanababan_",
                "kesan" : "pendiam tapi selalu sigap dan teliti",  
                "pesan" : "Tetap semangat dan teruslah memberikan yang terbaik"
            },
            {
                "nama"  : "Marleta Cornelia Leander",
                "nim"   : "122450092",
                "umur"  : "20",
                "asal"  : "Depok, Jawa Barat",
                "alamat": "Gang Nangka 3",
                "hobbi" : "Review Jurnal",
                "sosmed": "@marletacornelia",
                "kesan" : "pendiam tapi penuh dedikasi",  
                "pesan" : "Semoga terus semangat dan memberikan kontribusi yang berarti"
            },
            {
                "nama"  : "Rut Junita Sari Siburian",
               "nim"   : "122450103",
                "umur"  : "20",
                "asal"  : "Batam, Kepulauan Riau",
                "alamat": "Gang Nangka 3",
                "hobbi" : "Review Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan" : "menunjukkan ketelitian dan kemampuan dalam menyampaikan informasi dengan jelas, meskipun dengan cara yang tenang",  
                "pesan" : "Semoga terus berkontribusi dengan cara yang tepat dan efektif"
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
                "pesan" : "semagat untuk terus membantu dan selalu membawa informasi yang berguna "
            },
            {
                "nama"  : "Eggi satria",
                 "nim"   : "122450032",
                "umur"  : "20",
                "asal"  : "Sukabumi",
                "alamat": "Korpri",
                "hobbi" : "Ngoding WISATA",
                "sosmed": "@egistr",
                "kesan" : "seorang daplok yang baik, selalu siap membantu dan memberikan dukungan",  
                "pesan" : "Semangat terus bang eggi dalam menjalani hari-harinya, semoga semua tugas dan tanggung jawab yang diemban dapat diselesaikan dengan lancar"
            },
            {
                "nama"  : "Febiya Jomy Pratiwi",
               "nim"   : "122450074",
                "umur"  : "20",
                "asal"  : "Tulang Bawang",
                "alamat": "Jalan Kelengkeng Raya",
                "hobbi" : "Review jurnal",
                "sosmed": "@pratiwifebiya",
                "kesan" : "sangat informatif meskipun dengan sikap yang tenang",  
                "pesan" : "Semoga terus memberikan kontribusi positif dan ide-ide kreatif untuk kesuksesan Mikfes"
            },
             {
                "nama"  : "Happy Syahrul Ramadhan",
                "nim"   : "122450013",
                "umur"  : "20",
                "asal"  : "Lampung Timur",
                "alamat": "Karang Anyar",
                "hobbi" : "Main game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan" : "komitmen yang luar biasa dan menciptakan suasana yang positif",  
                "pesan" : "komitmen yang luar biasa dan selalu siap membantu, menciptakan suasana kerja yang positif"
            },
            {
                "nama"  : "Randa Andriana Putra",
                "nim"   : "122450083",
                "umur"  : "21",
                "asal"  : "Banten",
                "alamat": "Sukarame",
                "hobbi" : "Tidur dan berkembang",
                "sosmed": "@randaandriana_",
                "kesan" : "sosok yang informatif dan selalu siap membantu",  
                "pesan" : "Terima kasih atas dedikasi dan informasi yang selalu di berikan "
            },
            {
                "nama"  : "Vita Anggraini",
                "nim"   : "121450005",
                "umur"  : "21",
                "asal"  : "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi" : "Memasak",
                "sosmed": "@anovavona",
                "kesan" : "menunjukkan dedikasi yang tinggi dan mampu memberikan informasi yang jelas",  
                "pesan" : "Semoga terus bersemangat dan memberikan kontribusi positif untuk setiap kegiatan"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    mikfes()

elif menu == "Departemen MEDKRAF":
    def medkraf():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=13Lw9sR96zh1VZLJejCYzqTG3AEAZ8zus", #bang wahyu dn
            "https://drive.google.com/uc?export=view&id=1o80ZLdlBhQT_9fMbz7h4o8hpt1sMMDY0", #kak elok dn
            "https://drive.google.com/uc?export=view&id=1ADuweM2TxszSD_I6o5IXGhJov083KQXr", #kak arsyiah dn
            "https://drive.google.com/uc?export=view&id=1nfRuCR51mnWWZ3fLs5bY0y50Ri_nBrk5", #kak cintya dn
            "https://drive.google.com/uc?export=view&id=1PNiZhnUvCQsZp7BhE3QpTp0czRNGYNJl", #kak najla dn
            "https://drive.google.com/uc?export=view&id=1Z-7-eYoVSdfknByQE8lhC5vt8MPoWmOd", #kak rahma dn
            "https://drive.google.com/uc?export=view&id=1lq1O8GMpQ0ugluy8yhiB3ZChuBrHWC8B", #kak try yani dn
            "https://drive.google.com/uc?export=view&id=1E9hNxa0KFUyRa-2_tP2TKlpl_yBzPRJn", #bang kaisar dn
            "https://drive.google.com/uc?export=view&id=1_1aGgJrGmb8R6eBFWqhRXUdoMctDLFSA", #kak dwi dn
            "https://drive.google.com/uc?export=view&id=1rHz-JXKjg1l_8zUHaJXUcgudVl2Nfeuk", #bang gym dn
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
                "kesan" : "membuat divisi ini semakin hidup dan menarik, memberikan dampak positif bagi semua anggota",  
                "pesan" : "Semoga terus berinovasi dan menghasilkan karya-karya yang menginspirasi bagi semuanya"
            },
            {
                "nama"  : "Elok Fiola",
                "nim"   : "122450051",
                "umur"  : "19",
                "asal"  : "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi" : "Editing",
                "sosmed": "@elokfiola",
                "kesan" : "sangat teliti dan responsif",  
                "pesan" : "Semoga terus bersemangat dalam membantu tim dan berkontribusi dengan ide-ide kreatif"
            },
            {
                "nama"  : "Arsyiah Azahra",
                "nim"   : "121450035",
                "umur"  : "21",
                "asal"  : "Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi" : "Nugas",
                "sosmed": "@arsyiah.__",
                "kesan" : "menunjukkan semangat dan antusiasme tinggi, membantu menciptakan konten yang menarik dan berdampak",  
                "pesan" : "Semoga terus berkontribusi dengan ide-ide segar yang menginspirasi"
            },
            {
                "nama"  : "Cintya Bella",
                "nim"   : "122450066",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Teluk",
                "hobbi" : "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan" : "menunjukkan semangat dan komitmen tinggi, menciptakan karya-karya yang menarik dan inspiratif.",  
                "pesan" : "Semoga terus berinovasi dan memberikan kontribusi yang berarti bagi setiap proyek"
            },
            {
                "nama"  : "Najla Juwairia",
                "nim"   : "122450037",
                "umur"  : "19",
                "asal"  : "Sumatera Utara",
                "alamat": "Airan",
                "hobbi" : "Menulis, Membaca, Fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan" : "menunjukkan semangat yang tinggi dan kemampuan luar biasa dalam menciptakan konten yang menarik",  
                "pesan" : "Semoga terus berinovasi dan memberikan kontribusi positif bagi setiap proyek"
            },
            {
                "nama"  : "Rahma Neliyana",
                "nim"   : "122450036",
                "umur"  : "20",
                "asal"  : "Lampung",
                "alamat": "Sukarame",
                "hobbi" : "Baca Coding",
                "sosmed": "@rahmanellyana",
                "kesan" : " sosok daplok yang baik, selalu siap membantu, memberikan dukungan kepada adik-adiknya dan membawa energi positif",  
                "pesan" : "Terima kasih atas dedikasi dan sikap baik serta Kebaikan dan ketulusan hati dalam membantu kami"
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
                "kesan" : "Sangat seru dan menunjukkan kreativitas dan semangat tinggi",  
                "pesan" : "Semoga terus menciptakan hasil dokumentasi yang berkualitas dan menjadi kenangan berharga bagi setiap kegiatan"
            },
            {
                "nama"  : "Dwi Ratna Anggraeni",
                "nim"   : "122450008",
                "umur"  : "20",
                "asal"  : "Jambi",
                "alamat": "Jalan Durian 5 Pemda",
                "hobbi" : "Membaca",
                "sosmed": "@dwiratnn_",
                "kesan" : " sangat detail dan berdedikasi, memastikan setiap kegiatan terekam dengan baik dan rapi",  
                "pesan" : " Semoga terus bersemangat dalam mengabadikan setiap momen berharga dengan kualitas yang terbaik"
            },
            {
                "nama"  : "Gymnastiar Al Khoarizmy",
                "nim"   : "122450096",
                "umur"  : "20",
                "asal"  : "Serang",
                "alamat": "Lapangan Golf UIN",
                "hobbi" : "Baca komik",
                "sosmed": "@jimnn.as",
                "kesan" : "sangat teliti dan profesional, memastikan setiap detail terekam dengan baik",  
                "pesan" : "SSemoga terus menghasilkan dokumentasi yang berkualitas dan berkesan"
            },
             {
                "nama"  : "Nasywa Nur Afifah",
                "nim"   : "122450125",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Jalan Durian 1 Pemda",
                "hobbi" : "Nonton drakor",
                "sosmed": "@nsywanaf",
                "kesan" : " semangat menciptakan konten yang menarik dan berkualitas",  
                "pesan" : " Semoga terus semangat berinovasi dan menghasilkan karya yang inspiratif"
            },
            {
                "nama"  : "Priska Silvia Ferantiana",
                "nim"   : "122450053",
                "umur"  : "19",
                "asal"  : "Palembang",
                "alamat": "Jalan Nangka 2",
                "hobbi" : "Baca novel yang bikin nangis",
                "sosmed": "@prskslv",
                "kesan" : "menjadikan setiap konten lebih menarik dan berkesan",  
                "pesan" : " Teruslah berkarya dan menciptakan konten yang menginspirasi"
            },
            {
                "nama"  : "Muhammad Arsal Ranjana Utama",
                "nim"   : "121450111",
                "umur"  : "21",
                "asal"  : "Depok",
                "alamat": "Jalan Nangka 4",
                "hobbi" : "Ngoding",
                "sosmed": "@arsal.utama",
                "kesan" : "sangat inovatif dan antusias",  
                "pesan" : "Semoga terus bersemangat menghasilkan konten yang menarik dan inspiratif"
            },
            {
                "nama"  : "Abit Ahmad Oktarian",
                "nim"   : "122450042",
                "umur"  : "19",
                "asal"  : "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi" : "Ngoding, Gaming",
                "sosmed": "@abitahmad",
                "kesan" : "antusiasme menjadikan setiap proyek lebih menarik dan bermakna",  
                "pesan" : " Semoga terus berkontribusi dengan ide-ide segar dan menghasilkan karya yang menginspirasi"
            },
            {
                "nama"  : "Akmal Faiz Abdillah",
                "nim"   : "122450114",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi" : "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan" : "menunjukkan semangat dan antusiasme yang tinggi walau pendiam",  
                "pesan" : "Semoga terus berinovasi dan menghasilkan karya yang menginspirasi"
            },
            {
                "nama"  : "Hermawan Manurung",
                "nim"   : "122450069",
                "umur"  : "20",
                "asal"  : "Bogor",
                "alamat": "Dekat jalan tol, Wisma Hana Hani",
                "hobbi" : "Bengong dan membaca buku",
                "sosmed": "@hermawan.mnrng",
                "kesan" : "sangat asik dan penuh energi, selalu membawa suasana positif ke dalam setiap kegiatan",  
                "pesan" : "Terima kasih atas semangat dan kreativitas yang membuat divisi Media Kreatif jadi begitu asik"
            },
            {
                "nama"  : "Khusnun Nisa",
                "nim"   : "122450078",
                "umur"  : "20",
                "asal"  : "Lampung Selatan",
                "alamat": "Belwis",
                "hobbi" : "Mengerjakan tugas",
                "sosmed": "@khusnun_nisa335",
                "kesan" : "pandai membagi waktu selalu dapat diandalkan, memastikan setiap tugas terselesaikan dengan efisien",  
                "pesan" : "Semoga terus bersemangat dan memberikan yang terbaik di setiap proyek walaupun dengan banyaknya kegiatan"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1piFwLTBFsYa3DoQYBl-5z73OtOPgur43", #bang yogy dn
            "https://drive.google.com/uc?export=view&id=1NAJt7fktPIaQz8uHs3HVb6yFM_zdanWH", #kak ramadhita dn
            "https://drive.google.com/uc?export=view&id=17BPDH9ooMTIIQw-an_gRr5-N6YKKlho2", #kak nazwa dn
            "https://drive.google.com/uc?export=view&id=1GZBicPj-vl3Wtg3iAbiswiStPWN9O5ky", #bang bastian dn
            "https://drive.google.com/uc?export=view&id=1kDReyk5ZorVEJEoqQ-DUk7EatAXBniC3", #kak dea dn
            "https://drive.google.com/uc?export=view&id=1o5a2B9JQLJAAh2wvXYrfT2OCiSmDiukJ", #kak esteria dn
            "https://drive.google.com/uc?export=view&id=1IuEhH1juOg_5CAKKJ9NqbiJLQh4xB92n", #kak natasya ega dn
            "https://drive.google.com/uc?export=view&id=1VH-zv8Cl-JNkX5p_cPmSOm5k-1B3iulc", #kak novelia dn
            "https://drive.google.com/uc?export=view&id=1foqTWKaOtKJQJQUd4MaU4vVrnHwmossg", #kak jasmine dn
            "https://drive.google.com/uc?export=view&id=1RCUrJspGuvVVQjCgC5jUn5Pn5adMwCFd", #bang tobias dn
            "https://drive.google.com/uc?export=view&id=1Ibeu7KuAKm36zC229GWpYc0-YYnJ1_nY", #kak yohana dn
            "https://drive.google.com/uc?export=view&id=19lKvfPuLMH6pXqCWTd67Z6xYNF7N93sr", #bang rizki dn
            "https://drive.google.com/uc?export=view&id=1kPe90soDBKZx0uyPd-Lp7kERpYzlm7KK", #bang arafi dn
            "https://drive.google.com/uc?export=view&id=1XKFwAB8xOVgLDUqRzzL7XULOkruomtBq", #kak uyi dn
            "https://drive.google.com/uc?export=view&id=1vvPtmQMCWEbdGUMrkK0yNgT49IKTaQgg", #kak chalifia dn
            "https://drive.google.com/uc?export=view&id=1xp4KHkunxARMiDcSNY28Q--rBWt3wjtA", #bang irvan dn
            "https://drive.google.com/uc?export=view&id=1wZnwJtLv_rwKwOa3Aj9DqQYSN0HPBc52", #kak izza dn
            "https://drive.google.com/uc?export=view&id=1RpE2YQJ33x1LILaCUBhRCBLFTuCges0H", #kak zuhrah dn
            "https://drive.google.com/uc?export=view&id=1OqYEXyzz6zUBOnHVF6nWrnGUYf0iYEUp", #bang raid dn
            "https://drive.google.com/uc?export=view&id=1eJUSbwaGbz95ZoztrjW3MOzj-GUML5_0", #kak tria dn
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
                "kesan" : "menunjukkan komitmen tinggi dan kemampuan komunikasi yang sangat baik",  
                "pesan" : "Semoga terus memperkuat hubungan dan menciptakan peluang baru yang bermanfaat bagi himpunan"
            },
            {
                "nama"  : "Ramadhita Atifa Hendri",
                "nim": "121450131",
                "umur": "21 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi": "Jalan - Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan" : "selalu menunjukkan dedikasi dan ketelitian dalam setiap tugas",  
                "pesan" : "Semoga terus berkontribusi dengan semangat dan membantu memperkuat hubungan"
            },
            {
                "nama"  : "Nazwa Nabilla",
                "nim": "121450122",
                "umur": "21 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Way kandis",
                "hobbi": "belajar",
                "sosmed": "@nazwanbilla",
                "kesan" : "menunjukkan komitmen yang tinggi dan kemampuan komunikasi yang baik serta asik",  
                "pesan" : "Semoga terus menciptakan kerjasama yang bermanfaat dan memperkuat jaringan dengan berbagai pihak"
            },
            {
                "nama"  : "Bastian Heskia Silaban",
                "nim": "122450130",
                "umur": "21 Tahun",
                "asal": "Batam, Kep. Riau",
                "alamat": "Belwis",
                "hobbi": "main game",
                "sosmed": "@bastiansilaban_",
                "kesan" : "Sangat berdedikasi serta menunjukkan antusiasme dan kemampuan komunikasi yang baik",  
                "pesan" : "Semoga terus berkontribusi dengan semangat dan menjaga hubungan baik"
            },
            {
                "nama"  : "Dea Mutia Risani",
                "nim": "122450099",
                "umur": "20 Tahun",
                "asal": "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi": "dengerin musik",
                "sosmed": "@deaa.rsn",
                "kesan" : "memiliki kemampuan luar biasa dalam membangun relasi yang berdampak postif",  
                "pesan" : "Semoga terus berinovasi dan menciptakan peluang kerjasama yang bermanfaat"
            },
            {
                "nama"  : "Esteria Rohanauli Sidauruk",
                "nim": "122450025",
                "umur": "19 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Belwis",
                "hobbi": "Main golf bareng kadiv",
                "sosmed": "@esteriars",
                "kesan" : " sangat baik dan selalu peduli, siap membantu rekan-rekan dengan sepenuh hati",  
                "pesan" : " Semoga terus bersemangat dan memberikan kontribusi yang berarti bagi setiap kegiatan ya kak"
            },
            {
                "nama"  : "Natasya Ega Lina",
                "nim": "122450024",
                "umur": "19 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi": "jadi humas",
                "sosmed": "@nateee__15",
                "kesan" : "menunjukkan profesionalisme dan kreativitas yang tinggi, selalu siap menyampaikan pesan dengan jelas",  
                "pesan" : "Semoga terus berinovasi dalam menyampaikan informasi dan membangun citra positif"
            },
            {
                "nama"  : "Novelia Adinda",
                "nim": "122450104",
                "umur": "21 Tahun",
                "asal": "Jakarta Timur",
                "alamat": "Belwis",
                "hobbi": "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan" : "pendiam menunjukkan ketelitian dan komitmen dalam setiap tugas",  
                "pesan" : "Terima kasih atas dedikasi dan kerja keras dalam mendukung divisi Hubungan Luar."
            },
            {
                "nama"  : "Ratu Keisha Jasmine Deanova",
                "nim": "122450106",
                "umur": "20 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Way Kandis",
                "hobbi": "Main sepak takraw",
                "sosmed": "@jasminednva",
                "kesan" : "sangat aktif dan energik, selalu siap terlibat dalam berbagai aktivitas",  
                "pesan" : "Semoga terus berkontribusi dengan energi positif dan ide-ide kreatif"
            },
            {
                "nama"  : "Tobias David Manogari",
                "nim": "122450091",
                "umur": "20 Tahun",
                "asal": "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi": "Jogging",
                "sosmed": "@tobiassiagian",
                "kesan" : " sangat asik dan penuh energi, selalu membawa suasana positif dan keceriaan ke dalam setiap program",  
                "pesan" : "Semoga terus membawa semangat positif yang membuat setiap kegiatan semakin menarik"
            },
             {
                "nama"  : "Yohana Manik",
                "nim": "122450126",
                "umur": "19 Tahun",
                "asal": "Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi": "Main Bowling",
                "sosmed": "@yo_annamnk",
                "kesan" : "menunjukkan sikap profesional yang luar biasa",  
                "pesan" : "Semoga terus menjaga standar tinggi dalam setiap tugas yang diemban"
            },
            {
                "nama"  : "Rizki Adrian Bennovry",
                "nim": "121450073",
                "umur": "21 Tahun",
                "asal": "Bekasi",
                "alamat": "TVRI",
                "hobbi": "Bikin portofolio",
                "sosmed": "@rzkdrnnn",
                "kesan" : "menunjukkan komitmen yang tinggi dan kepedulian terhadap isu-isu sosial",  
                "pesan" : " Semoga terus berkontribusi dalam memberikan dampak positif bagi masyarakat"
            },
            {
                "nama"  : "Arafi Ramadhan Maulana",
                "nim": "122450002",
                "umur": "20 Tahun",
                "asal": "Bandung",
                "alamat": "Way Huwi",
                "hobbi": "Bertani",
                "sosmed": "@rafiramadhanmaulana",
                "kesan" : "menunjukkan komitmen dan kepedulian yang tinggi",  
                "pesan" : " Semoga terus bersemangat dalam memberikan dampak positif bagi masyarakat sekitar"
            },
            {
                "nama"  : "Asa Do'a Uyi",
                "nim": "122450005",
                "umur": "20 Tahun",
                "asal": "Muara Enim",
                "alamat": "Korpri",
                "hobbi": "Tepuk Semangat",
                "sosmed": "@u_yippy",
                "kesan" : "menunjukkan komitmen yang tinggi dan empati yang besar",  
                "pesan" : "Semoga terus bersemangat dalam memberikan kontribusi positif bagi masyarakat"
            },
            {
                "nama"  : "Chalifia Wananda",
                "nim": "122450076",
                "umur": "20 Tahun",
                "asal": "Padang",
                "alamat": "Sukarame",
                "hobbi": "Q Time",
                "sosmed": "@chlfawww",
                "kesan" : "komitmen yang tinggi dan kepedulian yang mendalam terhadap isu-isu sosial",  
                "pesan" : "eruslah berinovasi dan membawa perubahan yang nyata bagi masyarakat"
            },
            {
                "nama"  : "Irvan Alfaritzi",
                "nim": "122450093",
                "umur": "21 Tahun",
                "asal": "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi": "Nonton youtube, main game",
                "sosmed": "@alfaritziirvan",
                "kesan" : "antusias dan penuh inisiatif",  
                "pesan" : "Semoga terus menjadi agen perubahan dan memberikan inspirasi bagi orang lain"
            },
            {
                "nama"  : "Izza Lutfia",
                "nim": "122450090",
                "umur": "20 Tahun",
                "asal": "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi": "Main Rubik",
                "sosmed": "@izzalutfia",
                "kesan" : "sangat aktif dan antusias, siap mengambil inisiatif dalam setiap kegiatan",  
                "pesan" : "Semoga terus berkontribusi dengan energi positif dan ide-ide kreatif"
            },
            {
                "nama"  : "Khaalishah Zuhrah Alyaa Vanefi",
                "nim"   : "122450034",
                "umur": "20 Tahun",
                "asal"  : "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi" : "Mengaji",
                "sosmed": "@alyaavanevi",
                "kesan" : "Siap membantu, menciptakan dampak yang signifikan bagi masyarakat",  
                "pesan" : "Semoga terus bersemangat dalam memberikan manfaat dan kontribusi positif bagi masyarakat"
            },
            {
                "nama"  : "Raid Muhammad Naufal",
                "nim"   : "122450027",
                "umur"  : "20 Tahun",
                "asal"  : "Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi" : "telat",
                "sosmed": "@rayths_",
                "kesan" : "menunjukkan kepedulian yang tinggi",  
                "pesan" : "Semoga terus bersemangat dalam memberikan manfaat bagi masyarakat dan menjadikan setiap program lebih berdampak"
            },
            {
                "nama"  : "Tria Yunanni",
                "nim": "122450062",
                "umur": "20 Tahun",
                "asal": "Way Kanan",
                "alamat": "Sukarame",
                "hobbi": "Baca Buku",
                "sosmed": "@tria_y062",
                "kesan" : "antusias dan berkomitmen, menciptakan dampak yang berarti dalam setiap program",  
                "pesan" : "Semoga terus bersemangat dalam memberikan kontribusi positif kepada masyarakat"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    eksternal()  

elif menu == "Departemen Internal":
    def internal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1QkhuR2IxcC7GbQthks3-J-YfHQX4eetm", #bang dimas dn
            "https://drive.google.com/uc?export=view&id=1JCY6HArbhz9u7v2QlI9NeuIuSCUQDPFz", #kak catherine dn
            "https://drive.google.com/uc?export=view&id=1GnDInfe3VIifpZLH6SSy26ydb2lG-IJ5", #bang akbar dn
            "https://drive.google.com/uc?export=view&id=1THK-fSYhBBEIimD9O6SpZfXeOZ29HTgi", #kak rani dn
            "https://drive.google.com/uc?export=view&id=10P5g1-DJjdfj2l7Q3bqf3D50CZbySADx", #bang rendra dn
            "https://drive.google.com/uc?export=view&id=1y-kwMCksjUU-x6CsG0oxoOCAe3Wuwhir", #kak salwa dn
            "https://drive.google.com/uc?export=view&id=1Mzlnd4BBl5VEheCXax2JXj9gONl7lMTW", #bang yosia dn
            "https://drive.google.com/uc?export=view&id=16wVWs0ec_Tc7QWDWotojdppXYyI_-tXm", #bang ari dn
            "https://drive.google.com/uc?export=view&id=1ApUCbTkBlXsO14U4Xqaq_tLk95W8vgIe", #kak azizah dn
            "https://drive.google.com/uc?export=view&id=1LDmOgEZoMGphDekRp_gMc8G2ZE9TktMi", #kak meira dn
            "https://drive.google.com/uc?export=view&id=17oSlHjc7ncXBldbdkUm8RG9qVclMJsd1", #bang rendi dn
            "https://drive.google.com/uc?export=view&id=1XpHIAOg6AmsGSQXycZEm4HpBKi7uZ42Y", #kak renta dn
            "https://drive.google.com/uc?export=view&id=1f3iMXa9zbZcGXjdxzuuFmMpqcvwxhP8S", #bang josua dn

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
                "kesan" : "menunjukkan dedikasi yang tinggi dan kemampuan untuk membangun komunikasi yang baik",  
                "pesan" : "Semoga terus menciptakan lingkungan yang harmonis dan mendukung pengembangan anggota"
            },
            {
                "nama"  : "Catherine Firdhasari Maulina Sinaga",
                "nim"   : "121450071",
                "umur"  : "20",
                "asal"  : "Sumatera Utara",
                "alamat": "Airan",
                "hobbi" : "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan" : "teliti dan responsif, memastikan semua komunikasi berjalan lancar",  
                "pesan" : "Semoga terus berkontribusi dengan semangat dan membantu menjaga hubungan baik"
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
                "kesan" : "menunjukkan perhatian dan kepedulian yang tinggi",  
                "pesan" : "Semoga terus bersemangat dalam menciptakan hubungan yang baik antar anggota"
            },
            {
                "nama"  : "Rani Puspita sari",
                 "nim"  : "122450030",
                "umur"  : "20",
                "asal"  : "Kota Metro",
                "alamat": "Rajabasa",
                "hobbi" : "Dengar musik",
                "sosmed": "@ranniu",
                "kesan" : "pendiam namun penuh perhatian",  
                "pesan" : "Teruslah bersinar dengan cara nya sendiri"
            },
            {
                "nama"  : "Rendra Eka Prayoga",
                "nim"   : "122450112",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Belwis",
                "hobbi" : "Mancing Ikan Mas",
                "sosmed": "@rendraepr",
                "kesan" : " sangat asik selalu mampu menciptakan atmosfer kerja yang ceria dan kolaboratif",  
                "pesan" : "Semoga terus menciptakan suasana yang menyenangkan dan positif untuk semua anggota"
            },
            {
                "nama"  : "Salwa Farhanatussaidah",
                "nim"   : "122450055",
                "umur"  : "20",
                "asal"  : "Pesawaran",
                "alamat": "Airan",
                "hobbi" : "Nonton",
                "sosmed": "@slwfhn_694",
                "kesan" : "menunjukkan komitmen yang tinggi dan kemampuan untuk menjaga hubungan baik antar anggota",  
                "pesan" : "Semoga terus berkontribusi untuk menciptakan suasana yang harmonis dan positif "
            },
            {
                "nama"  : "Yosia Letare Banurea",
                "nim"   : "121450149",
                "umur"  : "20",
                "asal"  : "Dairi, Sumatera Utara",
                "alamat": "Perum Griya Indah",
                "hobbi" : "Tidur",
                "sosmed": "@yosiabanurea",
                "kesan" : "kemampuan luar biasa dalam menjaga suasana yang menyenangkan dan inklusif",  
                "pesan" : " Semoga terus menciptakan momen-momen yang memperkuat kebersamaan"
            },
            {
                "nama"  : "Ari Sigit",
                "nim"   : "121450069",
                "umur"  : "23",
                "asal"  : "Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobbi" : "Futsal",
                "sosmed": "@ari_sigit17",
                "kesan" : "menunjukkan dedikasi yang luar biasa dalam menciptakan program yang mendukung pertumbuhan spiritual anggota",  
                "pesan" : "Semoga terus memberikan inspirasi dan memperkuat nilai-nilai spiritual"
            },
            {
                "nama"  : "Azizah Kusumah Putri",
                "nim"   : "122450068",
                "umur"  : "21",
                "asal"  : "Lampung Selatan",
                "alamat": "Natar",
                "hobbi" : "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan" : "pendiam memiliki kedalaman pemikiran dan kemampuan mendengarkan yang luar biasa",  
                "pesan" : "Semangat terus untuk edikasi dan ketenangan dalam divisi Kerohanian"
            },
            {
                "nama"  : "Meira Listyaningrum",
                "nim"   : "122450011",
                "umur"  : "20",
                "asal"  : "Pesawaran",
                "alamat": "Airan",
                "hobbi" : "Membaca",
                "sosmed": "@meirasty_",
                "kesan" : "pendiam memiliki kebijaksanaan",  
                "pesan" : "Tetap semangat dalam setiap langkah di divisi Kerohanian"
            },
            {
                "nama"  : "Rendi Alexander Hutagalung",
                "nim"   : "122450057",
                "umur"  : "20",
                "asal"  : "Tangerang",
                "alamat": "Kost Benawang",
                "hobbi" : "Menyanyi",
                "sosmed": "@rexander",
                "kesan" : "pendiam mampu memberikan inspirasi melalui ketulusan",  
                "pesan" : "semangat untuk menciptakan suasana yang positif "
            },
            {
                "nama"  : "Renta Siahaan",
                "nim"   : "122450070",
                "umur"  : "21",
                "asal"  : "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi" : "Membaca dan Memancing",
                "sosmed": "@renta.shn",
                "kesan" : "pendiam namun penuh semangat selalu menunjukkan ketenangan dan kebijaksanaan",  
                "pesan" : "semangat untuk berdedikasi dan memberikan inspirasi bagi anggota lainnya"
            },
            {
                "nama"  : "Josua Panggabean",
                "nim"   : "122450061",
                "umur"  : "21",
                "asal"  : "Pematang Siantar",
                "alamat": "Gerbang Barat",
                "hobbi" : "Menonton",
                "sosmed": "@josuapanggabean_",
                "kesan" : "pendiam memiliki cara yang unik dalam menyampaikan dukungan",  
                "pesan" : "Semoga terus semangat dan memberikan inspirasi melalui kehadiran yang tenang dan penuh makna"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    internal()   

elif menu == "Departemen SSD":
    def ssd():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=19-K7Vr4jojSLWfLaZK9m_Ui08gMlaWli", #bang andrian dn
            "https://drive.google.com/uc?export=view&id=18BZoto8kIi9Ue3musgu4aP8sLdo-VP34", #kak adisty dn
            "https://drive.google.com/uc?export=view&id=1tuspXPp-6MV3o0GKc2qtxv7woBvenSa0", #kak nabilla dn
            "https://drive.google.com/uc?export=view&id=1HRK-KfNkNOWlSlpXR47YA6K3IZNlaGAM", #bang danang dn
            "https://drive.google.com/uc?export=view&id=1XFw2fLG6OU7q97s-fPSQYhOOGWG4zRkl", #bang farrel dn
            "https://drive.google.com/uc?export=view&id=1nnhPbI3rrusrzTIt9uqJfyOqvEndaqLm", #kak nabilah dn
            "https://drive.google.com/uc?export=view&id=17x6mFsakdLMWSVrEch1fQijW9RAqW7Ag", #kak alvia dn
            "https://drive.google.com/uc?export=view&id=1Mi_yJuQo0NLnLsu6tbTvDKhHjLAvn5d8", #bang dhafin dn
            "https://drive.google.com/uc?export=view&id=1V7Rz_HiHLUcdEN-EuL_gy00GK7fgV_6U", #kak elia dn


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
                "kesan" : "menunjukkan dedikasi yang luar biasa dalam menciptakan program-program yang mendukung kewirausahaan",  
                "pesan" : "Semoga terus berkontribusi dalam mengembangkan potensi kewirausahaan mahasiswa dan menciptakan usaha-usaha kreatif yang berdampak positif"
            },
            {
                "nama"  : "Adisty Syawaida Ariyanto",
                "nim"   : "121450136",
                "umur"  : "22",
                "asal"  : "Metro",
                "alamat": "Sukarame ",
                "hobbi" : "Nonton Film",
                "sosmed": "@adistysa_",
                "kesan" : "menunjukkan semangat yang tinggi dan selalu siap membantu",  
                "pesan" : "Semoga terus berinovasi dan berkontribusi untuk menciptakan peluang kewirausahaan yang menarik"
            },
            {
                "nama"  : "Nabila Azhari",
                "nim"   : "121450029",
                "umur"  : "21",
                "asal"  : "Simalungun",
                "alamat": "Airan ",
                "hobbi" : "Menghitung Uang",
                "sosmed": "@zhjung",
                "kesan" : "memberikan dukungan dan inovasi",  
                "pesan" : "Semoga terus bersemangat dalam mengembangkan ide-ide baru dan menciptakan usaha yang bermanfaat"
            },
            {
                "nama"  : "Danang Hilal Kurniawan",
                "nim"   : "122450085",
                "umur"  : "21",
                "asal"  : "Bandar Lampung",
                "alamat": "Airan",
                "hobbi" : "Belajar",
                "sosmed": "@dananghk_",
                "kesan" : "Sangat informatif dan menciptakan suasana positif yang mendorong kolaborasi dan inovasi",  
                "pesan" : "Semoga terus bersemangat dan menjadi sumber inspirasi"
            },
            {
                "nama"  : "Farrel Julio Akbar",
                "nim"   : "122450110",
                "umur"  : "20",
                "asal"  : "Bogor",
                "alamat": "Lapas",
                "hobbi" : "Kayang",
                "sosmed": "@farel_julio",
                "kesan" : "menunjukkan sikap profesional dan etos kerja yang tinggi",  
                "pesan" : "Tetap semangat dalam terus berkolaborasi dan berinovasi untuk mengembangkan potensi kewirausahaan yang ada"
            },
            {
                "nama"  : "Nabilah Andika Fitriati",
                "nim"   : "121450139",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi" : "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan" : "pendiam menunjukkan ketelitian dan kepekaan",  
                "pesan" : "Tetap semangat kontribusi dalam menciptakan lingkungan yang positif dan produktif"
            },
            {
                "nama"  : "Alvia Asrinda Br.Gintng",
                "nim"   : "122450077",
                "umur"  : "20",
                "asal"  : "Binjai",
                "alamat": "Korpri",
                "hobbi" : "Nonton Winda",
                "sosmed": "@alviagnting",
                "kesan" : "pendiam memiliki cara unik",  
                "pesan" : "semangat dalam setiap pekerjaan yang dilakukan"
            },
            {
                "nama"  : "Dhafin Razaqa Luthfi",
                "nim"   : "122450133",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi" : "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan" : "memiliki cara yang unik dalam menyampaikan dukungan",  
                "pesan" : "Jangan lupa untuk tetap semangat terus berkontribusi dan berinovasi"
            },
            {
                "nama"  : "Elia Meylani Simanjuntak",
                "nim"   : "122450026",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Korpri",
                "hobbi" : "Main Alat Musik",
                "sosmed": "@meylanielia",
                "kesan" : "ramah menciptakan lingkungan kerja yang nyaman",  
                "pesan" : "Semangat terus kak dalam mengembangkan potensi kewirausahaan mahasiswa"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()    
# Tambahkan menu lainnya sesuai kebutuhan

# Tambahkan menu lainnya sesuai kebutuhan
