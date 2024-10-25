
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
            "Departemen MEDKRAf",
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
            "https://drive.google.com/uc?export=view&id=1ZlQjABG1Xr8MLxG-lEa3lJUC5R0Fjp9S", #Bang Kharisma
            "https://drive.google.com/uc?export=view&id=1fHsCUH0lw_4B7dCl9BvDGWCGfq1vylHq", #Bang Pandra
            "https://drive.google.com/uc?export=view&id=1GWVkqfKujDPW4wrzhmQg8w8e9uslCGic", #Kak Meliza
            "https://drive.google.com/uc?export=view&id=1ye2Fu7cxo7NPDKLpKFEXXWZ2xMRlZKxA", #Kak putri
            "https://drive.google.com/uc?export=view&id=1BDU2eFVWzUQWtBgQSN5xxAv7rP_uwerS", #Kak Hartiti
            "https://drive.google.com/uc?export=view&id=1C_CykRvfMhaB28Nje_IJhMCCcQ-6Or_l", #Kak Nadila


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
                "kesan" : "Memiliki pembawaan yang beriwibawa dan menujukkan semangat kepemimpinan yang tinggi sangat menginspirasi kami. Pembawaan yang tenang namun tegas membuat kami merasa termotivasi untuk terus berkembang",  
                "pesan" : "Semoga tetap menjadi teladan yang menginspirasi, mendorong kami untuk terus maju dan berkontribusi lebih baik dalam himpunan. Teruslah memimpin dengan semangat membawa himpunan kita menuju kesuksesan yang lebih besar dan semoga himpunan semakin berkembang dan sukses dalam menjalankan peran"
            },
            {
                "nama"  : "Pandra Insani Putra Azwan",
                "nim"   : "121450137",
                "umur"  : "21",
                "asal"  : "Bukit Kemuning, Lampung Utara",
                "alamat": "Bawen 2",
                "hobbi" : "Bermain gitar dan menyanyi",
                "sosmed": "@pandrainsni27",
                "kesan" : "Seru dan memiliki kepribadian yang humoris, sehingga percakapan menjadi lebih menyenangkan. Mampu mengarahkan pembicaraan dengan jelas dan efektif. Cara komunikasinya santai namun fokus nmemberikan wawasan yang bermakna",  
                "pesan" : "Semoga tetap membawa semangat positif dan profesionalisme dalam setiap langkah, semoga terus sukses dalam menjalankan peran"
            },
            {
                "nama"  : "Meliza Wulandari",
                "nim"   : "121450065",
                "umur"  : "20",
                "asal"  : "Pagar Alam, Sumatera Selatan",
                "alamat": "Kotabaru",
                "hobbi" : "Nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan" : "Menjelaskan setiap informasi yang disampaikan mudah dipahami, terasa terorganisir dan jelas, membuat suasana menjadi lebih tenang dan kondusif untuk memahami berbagai aspek penting, memberikan pemahaman yang mendalam tentang organisasi dan tugas-tugas di dalamnya",  
                "pesan" : "Tetaplah menjadi sosok yang terorganisir dan terus ciptakan suasana yang membuat orang lain merasa nyaman dalam belajar dan berkembang, semoga sukses selalu dalam menjalankan peran"
            },
            {
                "nama"  : "Putri Maulida Chairani",
                "nim"   : "121450050",
                "umur"  : "21",
                "asal"  : "Payakumbuh, Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi" : "Dengerin bang pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan" : "Dalam menyampaikan penjelasan, membuat setiap informasi yang diberikan menjadi mudah dimengerti. Dengan cara penyampaiannya yang jelas dan runtut, setiap penjelasan yang disampaikan mendukung diskusi yang lebih produktif",  
                "pesan" : "Semoga terus mempertahankan keteraturan dalam menyampaikan setiap hal apapun dan sukses selalu dalam menjalankan peran"
            },
            {
                "nama"  : "Hartiti Fadilah",
                "nim"   : "121450031",
                "umur"  : "21",
                "asal"  : "Palembang",
                "alamat": "Pemda",
                "hobbi" : "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan" : "Memberikan pemahaman yang jelas dan baik tentang peran dan tanggung jawabnya dalam mengelola keuangan. Menyampaikan informasi secara sistematis dan jelas, yang memudahkan untuk memahami setiap aspek terkait",  
                "pesan" : "Semoga terus mengembangkan kemampuan dalam mengelola tanggung jawab keuangan, tetap semangat dalam menjalankan peran sebagai bendahara"
            },
            {
                "nama"  : "Nadilla Andara Putri",
                "nim"   : "121450003",
                "umur"  : "21",
                "asal"  : "Metro",
                "alamat": "KotaBaru",
                "hobbi" : "Membaca",
                "sosmed": "@ndillaandr26",
                "kesan" : "Memiliki kemampuan yang baik dalam menjelaskan pengelolaan keuangan dengan cara yang menyenangkan dan mampu menyampaikan informasi dengan jelas, sehingga mudah memahami setiqp detail dan memiliki cara yang mudah dipahami dalam menyampaikannya",  
                "pesan" : "Terus semangat dan sukses selalu dalam menjalankan tugas dan peran sebagai bendahara."
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1_mdNF1SpMg29xJFiwGyiXKyeQvlaqCmG",
            "https://drive.google.com/uc?export=view&id=1MgehzNtmsUJNeebolQmZGDrtWfdlYeeQ",
            "https://drive.google.com/uc?export=view&id=1sYY0pATziru0ZkdUpDU8pyTaYoHhdFGg",
            "https://drive.google.com/uc?export=view&id=1ujAwGUTf_BNIxr5NTVEtnQnk2vZRWfhE",
            "https://drive.google.com/uc?export=view&id=1F8AULbROOjD2Y3dGiUhQekViGku_bQbU",
            "https://drive.google.com/uc?export=view&id=1AtbcFNxPURITtS9-44HOWxPa__6zLKNw",
            "https://drive.google.com/uc?export=view&id=1-Z9IN0RcbgrQE8fc9CwLg4oXvukK2Z0u",
            "https://drive.google.com/uc?export=view&id=16SK3SFoGfobggD6AY7OGrTB5jpq13B-4",
            "https://drive.google.com/uc?export=view&id=1SfRFO2iBTp59L_bJTtbh6865mR--d5hM",
            "https://drive.google.com/uc?export=view&id=1XLn43dhEr1arVpFlRs3_9_zUdnBYiCCH",
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
                "kesan" : "Selalu tampil humble dan ceria serta menunjukkan pembawaan yang positif. Menjelaskan wawasannya yang mendalam tentang peran badan legislasi benar-benar menginspirasi kami untuk lebih memahami pentingnya peran dalam himpunan",  
                "pesan" : "Semoga terus menjadi teladan dengan pembawaanya yang positif, membuat suasana diskusi semakin menarik dan bermanfaat dan semangat dan sukses selalu dalam menjalankan peran dan tanggung jawabnya"
            },
            {
                "nama"  : "Annisa Cahyani Surya",
                "nim"   : "121450114",
                "umur"  : "21",
                "asal"  : "Tanggerang Selatan",
                "alamat": "Way Huwi",
                "hobbi" : "Membaca, Nonton",
                "sosmed": "@annisacahyanisurya",
                "kesan" : "Selalu komunikatif dan informatif dalam menjelaskan perannya. Penjelasannya yang jelas membantu saya memahami tugas dan tanggung jawab yang ada di badan ini",  
                "pesan" : "Teruslah semangat dalam menjalankan tugas dan perannya, semoga terus informatif dan komunikatif selalu dalam memberikan penjelasan"
            },
            {
                "nama"  : "Wulan Sabina",
                "nim"   : "121450150",
                "umur"  : "21",
                "asal"  : "Medan",
                "alamat": "Raden Saleh",
                "hobbi" : "Nonton Drakor",
                "sosmed": "@wlnsbn0",
                "kesan" : "Memberikan pemahaman yang baik mengenai proses pengelolaan keuangan dengan lebih baik, dengan sikap terbuka dan komunikatifnya membuat diskusi menjadi lebih efektif dan menyenangkan",  
                "pesan" : "Teruslah menunjukkan kepedulian dan komitmen dalam menjalankan peran dan tugas, semangat dan sukses selalu untuk kedepannya"
            },
            {
                "nama"  : "Annisa Dini Amaliya",
                "nim"   : "121450081",
                "umur"  : "21",
                "asal"  : "Tanggerang",
                "alamat": "Jati Agung",
                "hobbi" : "Nonton Dracin",
                "sosmed": "@anisadini10",
                "kesan" : "Memiliki kepribadian yang menarik dan inspiratif, cara menjelaskan dan memberikan wawasan mengenai pentingnya partisipasi aktif dalam setiap langkah pengambilan keputusan mudah dipahami",  
                "pesan" : "Terus mendorong keterlibatan anggota dalam proses pengambilan keputusan dan terus berbagi insight dan pengalamannya, semangat selalu dalam menjalankan peran di himpunan ini"
            },
            {
                "nama"  : "Anisa Fitriyani",
                "nim"   : "121450150",
                "umur"  : "21",
                "asal"  : "Medan",
                "alamat": "Raden Saleh",
                "hobbi" : "Nonton Drakor",
                "sosmed": "@wlnsbn0",
                "kesan" : "Informatif dalam menjelaskan tentang berbagai aspek tugas dan tanggung jawab di komisi ini, sehingga dapat memahami dengan jelas peran penting yang dimiliki oleh komisi ini dalam pengambilan keputusan di himpunan",  
                "pesan" : "Terus menjalankan upaya untuk menyebarluaskan informasi yang mendalam tentang peran dan fungsi di komisi ini, agar lebih banyak anggota himpunan dapat memahami pentingnya keterlibatan dalam setiap proses yang ada, semangat teru kak untuk kedepannya"
            },
            {
                "nama"  : "Mirzan Yusuf Rabbani",
                "nim"   : "122450118",
                "umur"  : "20",
                "asal"  : "Jakarta",
                "alamat": "Korpri",
                "hobbi" : "Main Kucing",
                "sosmed": "@myrrinn",
                "kesan" : "Sosok yang tenang tidak begitu banyak bicara tetapi memiliki cara tersendiri dalam meninggalkan kesan mendalam ke kami. Dengan sikap humblenya, meski jarang berbicara namun setiap interaksinya selalu positif",  
                "pesan" : "Semangat menjalani perkuliahannya kak dan semangat untuk menjalani peran di himpunan ini"
            },
            {
                "nama"  : "Dhea Amelia Putri",
                "nim"   : "122450004",
                "umur"  : "20",
                "asal"  : "Sukabumi, Jawa Barat",
                "alamat": "Natar",
                "hobbi" : "Suka Ikut Tes SKD",
                "sosmed": "@dhea_wedding",
                "kesan" : "Sosok yang menarik dan memberikan penjelasan yang jelas dan membantu saya memahami peran dan juga tanggung jawabnya di komisi ini. Selain itu sosok yang mengasyikkan membuat setiap diskusi terasa menyenangkan dan mudah dipahami",  
                "pesan" : "Teruslah menjadi pribadi yang menyenangkan, dan tetap semangat kak dalam menjalankan tugas"
            },
            {
                "nama"  : "Muhammad Fahrul Aditya",
                "nim"   : "121450156",
                "umur"  : "22",
                "asal"  : "Surakarta, Jawa Tengah",
                "alamat": "Pahoman",
                "hobbi" : "Melukis, badminton, hiking, ngopi, dengerin music, nonton film dan ngoding",
                "sosmed": "@fhrul.pdf",
                "kesan" : "Sangat menarik, seru, mengasyikkan, dan selalu berhasil menciptakan suasana yang penuh tawa dengan humorisnya. Dibalik kesan seru itu, selalu memberikan penjelasan yang jelas serta mudah dipahami. Setiap interaksi dengannya selalu meninggalkan kesan yang positif",  
                "pesan" : "Semoga terus sukses dalam memimpin komisi ini dengan baik dan semangat dalan menjalankan peran dan tugasnya"
            },
            {
                "nama"  : "Berlianda Enda Putri",
                "nim"   : "122450065",
                "umur"  : "21",
                "asal"  : "Sumatera Barat",
                "alamat": "Way Huwi",
                "hobbi" : "Main Game",
                "sosmed": "@berlyyanda",
                "kesan" : "Sosok yang baik, dan menarik. Bisa menciptakan suasana yang terbuka dan mendukung dalam setiap diskusi atau menjelaskan sesuatu",  
                "pesan" : "Terus menjadi pribadi yang hangat dan baik. Semoga sukses selalu dalam setiap langkah kak dan semnagat menjalani perkuliahannya dan peran di komisi ini"
            },
            {
                "nama"  : "Jeremia Susanto",
                "nim"   : "122450022",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Kemiling",
                "hobbi" : "Marah-marah",
                "sosmed": "@jeremia_s_",
                "kesan" : "Sosok yang baik dan mengasyikkan, setiap kali berbicara suasana terasa menyenangkan karena bisa mengikuti pembicaraan dengan baik, dan membuat diskusi menjadi seru",  
                "pesan" : "Terus menjadi pribadi yang ramah dan menyenangkan, dan semangat menjalani peran dan tugas di komisi ini"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1k7SJ9vN2S6WRrebi6r1coI-3zptWRKck", #kak lutfi
            "https://drive.google.com/uc?export=view&id=1VSt3oJQXZocC86aA478eQX3ohPK57XYx", #bang bintang
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
                "kesan" : "Sangat informatif dalam menjelaskan sesuatu dan menjadi sosok yang memberikan banyak masukan serta motivasi melalui pengalaman yang telah dilakukan",  
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
                "kesan" : "Sangat informatif dalam menjelaskan sesuatu dan banyak memberikan motivasi",  
                "pesan" : "Semoga kegiatannya di dalam maupun di luar perkuliahan tetap lancar dan tetap semangat kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1-Y1hNCg0GaXJCHzT24EyrWg7jqMxut8z", #bang ericson
            "https://drive.google.com/uc?export=view&id=1cgo9kWg-l8VEJfb3Ahwne8Z_nG8vmQnv", #kak abeth 
            "https://drive.google.com/uc?export=view&id=1Xx9iDAJ6gQtkAcy-InAETkbvETQJl4iu", #kak afifah
            "https://drive.google.com/uc?export=view&id=1l_q0WVqbXurzslSCuWLCR3iN_WXzisIM", #kak allya
            "https://drive.google.com/uc?export=view&id=1sL7Nmap38LCt4oLWKLMpXLFzaZGDBljr", #kak hanum 
            "https://drive.google.com/uc?export=view&id=196yik6r5aGJXHL1iKM3aln0ztHMu910R", #bang ferdy
            "https://drive.google.com/uc?export=view&id=1PSTejoSWTnqEZY1zNozwNV1GuYjfqKeq", #bang deri
            "https://drive.google.com/uc?export=view&id=1ZHR-QLRA6IXvs4xT9m5w1-h82AR4flUA", #kak oktavia
            "https://drive.google.com/uc?export=view&id=1NvkwjMuynuLrQGMTRvB90iusdqpUU7GH", #bang deyvan
            "https://drive.google.com/uc?export=view&id=1ymPQ5XLmZP9GxQD8qzCBD_IZXGR_1Gb8", #bang ibnu
            "https://drive.google.com/uc?export=view&id=1iij1TxZUUgnvWyTnTgSSzHEewCpKiPVa", #bang jo
            "https://drive.google.com/uc?export=view&id=1KDGjiVv84_ESBZs7_ZU-QKKYr5AZkfx4", #bang kemas
            "https://drive.google.com/uc?export=view&id=1AjubfB6DqSwN1Oi0dUhTMrJED_NxPO5s", #bang leonard
            "https://drive.google.com/uc?export=view&id=13-Q2N0CCKaGK1di_IQkK4E5was3Ddlem", #kak presilia
            "https://drive.google.com/uc?export=view&id=1R_rYLBJJo5k32wQM0sEu3tXdgEztTvU8", #kak rafa
            "https://drive.google.com/uc?export=view&id=1YiOXXAE7NCGqDOxmYr7vHQo0rCbgsAWK", #bang sahid
            "https://drive.google.com/uc?export=view&id=17yx2wp2qS27Y9p4G3ZMtMBEHd9g7p9v_", #kak vanes
            "https://drive.google.com/uc?export=view&id=1CDqbIufKbN8A9LYeFU_0yZ5xePCeRSkm", #bang ateng
            "https://drive.google.com/uc?export=view&id=1ZBLk-KUwU0D6HFATjcJKUH3xKZtM9TjZ", #bang gede
            "https://drive.google.com/uc?export=view&id=1d89JGXTTdBWd_RFuaLzBgCPcwPvJ_SwT", #kak jaclin
            "https://drive.google.com/uc?export=view&id=1EzGbpL9efqTz7_P719FBOhLBNHlDnl9T", #bang rafly
            "https://drive.google.com/uc?export=view&id=1nt1iqZByM-I2T3HE9gOnBGO3Y7MJgAAO", #kak dini

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
            "https://drive.google.com/uc?export=view&id=1ZnPN8dgLh9u7yoWQFph5GoRxPngoVyhT",#Bang Dimas
            "https://drive.google.com/uc?export=view&id=1_BrK6VWxKNWGDEgGsiQtOdyd1WvQDfUT",#Kak Chatrine
            "https://drive.google.com/uc?export=view&id=1UAHn6bgensloOoF5_Aav1UTTTDU6r6FC",#Bang Akbar
            "https://drive.google.com/uc?export=view&id=1ovuJm3HX87U_7vBETs75zNrQRi4YGCgs",#Kak Rani
            "https://drive.google.com/uc?export=view&id=1SBO5CUHFqxI-B3XfOOq7P6VTH-8OAo7A",#Bang Rendra
            "https://drive.google.com/uc?export=view&id=1eltlWLFfwnfsX5KwOLym8VoRrC2587tP",#Kak Salwa
            "https://drive.google.com/uc?export=view&id=1Jtdv16ycllpr37-CQ7mpW3zvRZvWbPBa",#Kak Yosia
            "https://drive.google.com/uc?export=view&id=1YQ2NES9fNinRPlYMig_K5YfvPXYKNje_",#Bang Ari
            "https://drive.google.com/uc?export=view&id=1aUVUKFmmevADrmmcIVgGSrHj51SrB5TW",#Kak Azizah
            "https://drive.google.com/uc?export=view&id=1U7Jgh96g0iAYaEHMjDJkoth2kBtBj3CG",#Kak Meira
            "https://drive.google.com/uc?export=view&id=167VrEs09hb6pfmwJnh9XAEtJB4SBTJjj",#Bang Rendi
            "https://drive.google.com/uc?export=view&id=1p-q18hkB6x1pFI1VG3TcvHga-xPGZKk6",#Kak Renta
            "https://drive.google.com/uc?export=view&id=1vWwF4sZh64O90lC7PcDx9qvkZqzkgqOo",#Bang Josua

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
                "nama"  : "Rani Puspita Sari",
                "nim"   : "122450033",
                "umur"  : "20",
                "asal"  : "Sumatera Barat",
                "alamat": "Gang Perwira, Belwis",
                "hobbi" : "Nonton Dracin",
                "sosmed": "@rannipu",
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
                "nama"  : "Yosia Letare Banurea",
                "nim"   : "121450149",
                "umur"  : "20",
                "asal"  : "Sumatera Utara",
                "alamat": "Perumahan Griya Indah",
                "hobbi" : "Tidur",
                "sosmed": "@yosiabanurea",
                "kesan" : "Selalu komunikatif dan informatif dalam menjelaskan perannya. Penjelasannya yang jelas membantu saya memahami tugas dan tanggung jawab yang ada di badan ini",  
                "pesan" : "Teruslah semangat dalam menjalankan tugas dan perannya, semoga terus informatif dan komunikatif selalu dalam memberikan penjelasan"
            },
            {
                "nama"  : "Ari Sigit",
                "nim"   : "121450069",
                "umur"  : "23",
                "asal"  : "Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobbi" : "Futsal",
                "sosmed": "@ari_sigit17",
                "kesan" : "Selalu komunikatif dan informatif dalam menjelaskan perannya. Penjelasannya yang jelas membantu saya memahami tugas dan tanggung jawab yang ada di badan ini",  
                "pesan" : "Teruslah semangat dalam menjalankan tugas dan perannya, semoga terus informatif dan komunikatif selalu dalam memberikan penjelasan"
            },
            {
                "nama"  : "Azizah Kusumah Putri",
                "nim"   : "122450068",
                "umur"  : "21",
                "asal"  : "Lampung Selatan",
                "alamat": "Natar",
                "hobbi" : "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan" : "Selalu komunikatif dan informatif dalam menjelaskan perannya. Penjelasannya yang jelas membantu saya memahami tugas dan tanggung jawab yang ada di badan ini",  
                "pesan" : "Teruslah semangat dalam menjalankan tugas dan perannya, semoga terus informatif dan komunikatif selalu dalam memberikan penjelasan"
            },
            {
                "nama"  : "Meira listyaningrum",
                "nim"   : "122450011",
                "umur"  : "20",
                "asal"  : "Pesawaran",
                "alamat": "Airan",
                "hobbi" : "Membaca",
                "sosmed": "@meirasty_",
                "kesan" : "Selalu komunikatif dan informatif dalam menjelaskan perannya. Penjelasannya yang jelas membantu saya memahami tugas dan tanggung jawab yang ada di badan ini",  
                "pesan" : "Teruslah semangat dalam menjalankan tugas dan perannya, semoga terus informatif dan komunikatif selalu dalam memberikan penjelasan"
            },
            {
                "nama"  : "Rendi Alexander Hutagalung",
                "nim"   : "122450057",
                "umur"  : "20",
                "asal"  : "Tanggerang ",
                "alamat": "Kost Benawang",
                "hobbi" : "Menyanyi",
                "sosmed": "@rexanders",
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
                "nama"  : "Josua Panggabean",
                "nim"   : "122450061",
                "umur"  : "21",
                "asal"  : "Sumatera Utara (Pematang Siantar)",
                "alamat": "Gya Kost",
                "hobbi" : "Menonton dan Menari",
                "sosmed": "@josuapanggabean_",
                "kesan" : "Selalu komunikatif dan informatif dalam menjelaskan perannya. Penjelasannya yang jelas membantu saya memahami tugas dan tanggung jawab yang ada di badan ini",  
                "pesan" : "Teruslah semangat dalam menjalankan tugas dan perannya, semoga terus informatif dan komunikatif selalu dalam memberikan penjelasan"
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
