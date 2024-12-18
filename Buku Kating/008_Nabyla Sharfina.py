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
            "https://drive.google.com/uc?export=view&id=1BPQhRXxpa-CnuFpI5cloVJWiFyeDK5E4", #bang kharisma
            "https://drive.google.com/uc?export=view&id=1YT_MPGMhzpA2QqjpRL92xf3Wjtgl39gA", #bang pandra
            "https://drive.google.com/uc?export=view&id=1CxyB1IrUtH1Z7XTCeAmjWTlkNqbwAXRv", #kak meliza
            "https://drive.google.com/uc?export=view&id=1kxXgGra4FqZ1ZxisD4gFq2l5pEP68Vma", #kak putri
            "https://drive.google.com/uc?export=view&id=1HfsZTVQDr7t5Xu2Av68SbZdhBbiXH4jV", #kak hartiti
            "https://drive.google.com/uc?export=view&id=14bp6YfgEGNGO6_45rcpWwdy-YrdzlvVM", #kak nadilla
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
                "kesan" : "Sangat inspiratif dan menjadi sosok yang memberikan banyak masukan melalui pengalaman yang telah dilakukan",  
                "pesan" : "Semangat terus buat kedepannya, semoga proses dalam menyelesaikan kegiatannya dapat berjalan dengan lancar! "
            },
            {
                "nama"  : "Pandra Insani Putra Azwan",
                "nim"   : "121450137",
                "umur"  : "21",
                "asal"  : "Bukit Kemuning, Lampung Utara",
                "alamat": "Bawen 2",
                "hobbi" : "Bermain gitar dan menyanyi",
                "sosmed": "@pandrainsni27",
                "kesan" : "Sangat inspiratif dan menjadi sosok yang dapat memberikan banyak masukan melalui pengalaman yang telah dilakukan ",  
                "pesan" : "Semangat dalam menjalani hari-harinya"
            },
            {
                "nama"  : "Meliza Wulandari",
                "nim"   : "121450065",
                "umur"  : "20",
                "asal"  : "Pagar Alam, Sumatera Selatan",
                "alamat": "Kotabaru",
                "hobbi" : "Nonton drakor",
                "sosmed": "@wulandarimeliza",
                "kesan" : "Sangat baik dan selalu memberikan semangat dan inspirasi",  
                "pesan" : "Semoga dilancarkan semua urusannya dalam dunia perkuliahan"
            },
            {
                "nama"  : "Putri Maulida Chairani",
                "nim"   : "121450050",
                "umur"  : "21",
                "asal"  : "Payakumbuh, Sumatera Barat",
                "alamat": "Nangka 4",
                "hobbi" : "Dengerin bang pandra gitaran",
                "sosmed": "@ptrimaulidaaa_",
                "kesan" : "Sangat baik dan selalu memberikan semangat dan inspirasi",  
                "pesan" : "Semoga kegiatannya di dunia perkuliahan maupun di luar perkuliahan selalu dimudahkan"
            },
            {
                "nama"  : "Hartiti Fadilah",
                "nim"   : "121450031",
                "umur"  : "21",
                "asal"  : "Palembang",
                "alamat": "Pemda",
                "hobbi" : "Nyanyi",
                "sosmed": "@hrtfdlh",
                "kesan" : "Sangat baik dan selalu memberikan semangat dan inspirasi",  
                "pesan" : "Tetap semangat kak dalam menjalani hari-harinya"
            },
            {
                "nama"  : "Nadilla Andara Putri",
                "nim"   : "121450003",
                "umur"  : "21",
                "asal"  : "Metro",
                "alamat": "KotaBaru",
                "hobbi" : "Membaca",
                "sosmed": "@ndillaandr26",
                "kesan" : "Sangat baik dan selalu memberikan semangat dan inspirasi",  
                "pesan" : "Semangat dalam menjalani tugas, tanggung jawab yang diemban, dan semoga lancar kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    kesekjenan()

elif menu == "Baleg":
    def baleg():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1juF4DIWryeLBRt44cGpRsvbNsVpaZojS", #kak tri
            "https://drive.google.com/uc?export=view&id=1LRl8KHE2tA0cAkaLsGhAtYUoxIunWuwe", #kak anissa cahyani surya
            "https://drive.google.com/uc?export=view&id=1uAEV7ih9YUW0IvvwKvMfscvMrIN2xLjY", #kak wulan sabina
            "https://drive.google.com/uc?export=view&id=1lr8pdc79Wy6MWI9B3ib4LbPb2uZp1Nvw", #kak anisa dini amalia
            "https://drive.google.com/uc?export=view&id=1SANy73pBawz7WyFGxhknICHdcOmE-ow8", #kak anisa fitriyani
            "https://drive.google.com/uc?export=view&id=1UgDySMjgkxLZOKR_Up0G0E1Tv3It6gyT", #bang mirzan
            "https://drive.google.com/uc?export=view&id=1xTI2kd7LoMRln24YiWQorBIrKnPifUEc", #kak dhea
            "https://drive.google.com/uc?export=view&id=1OZMMC5ZHpvGrcYkusKT03Zmz6Aiz9o5U", #bang fahrul
            "https://drive.google.com/uc?export=view&id=1_vJjP3GqUMXVkGWw4aJaT7p8PNtQiwCj", #bang berliana
            "https://drive.google.com/uc?export=view&id=1ISjrxlQzfg37DC98e6ipQSr1bophWHtO", #bang jeremi
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
                "kesan" : "Sangat informatif dalam menjelaskan sesuatu dan menjadi sosok yang memberikan banyak masukan serta motivasi melalui pengalaman yang telah dilakukan",  
                "pesan" : "Tetap semangat kak dalam menjalani hari-harinya, semoga diperlancar dalam menyelesaikan tugas dan tanggung jawab yang sedang di emban"
            },
            {
                "nama"  : "Annisa Cahyani Surya",
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
                "nama"  : "Wulan Sabina",
                "nim"   : "121450150",
                "umur"  : "21",
                "asal"  : "Medan",
                "alamat": "Raden Saleh",
                "hobbi" : "Nonton Drakor",
                "sosmed": "@wlnsbn0",
                "kesan" : "Sangat baik, informatif dalam menerangkan suatu permasalahan dan sangat menginspirasi",  
                "pesan" : "Tetap semangat kak dalam menjalani harinya, semoga urusannya baik di akademik maupun non akademik dapat berjalan dengan lancar"
            },
            {
                "nama"  : "Anisa Dini Amaliya",
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
                "nama"  : "Anisa Fitriyani",
                "nim"   : "122450019",
                "umur"  : "20",
                "asal"  : "Batam",
                "alamat": "Kalianda",
                "hobbi" : "Membaca Al-Waqiah setiap maghrib",
                "sosmed": "@ansftynn_",
                "kesan" : "Sangat baik dan sangat menginspirasi dalam kehidupan",  
                "pesan" : "Tetap semangat dalam menjalani perkuliahannya kak dan jangan lupa jaga kesehatan"
            },
            {
                "nama"  : "Mirzan Yusuf Rabbani",
                "nim"   : "122450118",
                "umur"  : "20",
                "asal"  : "Jakarta",
                "alamat": "Korpri",
                "hobbi" : "Main Kucing",
                "sosmed": "@myrrinn",
                "kesan" : "Sangat menginspirasi dalam kehidupan ",  
                "pesan" : "Tetap semangat kak dalam menjalani dunia perkuliahan"
            },
            {
                "nama"  : "Dhea Amelia Putri",
                "nim"   : "122450004",
                "umur"  : "20",
                "asal"  : "Sukabumi, Jawa Barat",
                "alamat": "Natar",
                "hobbi" : "Suka Ikut Tes SKD",
                "sosmed": "@dhea_wedding",
                "kesan" : "Sangat baik dan sangat mengasyikkan ",  
                "pesan" : "Semangat terus kak dalam menjalani perkuliahannya serta jangan lupa untuk jaga kesehatan"
            },
            {
                "nama"  : "Muhammad Fahrul Aditya",
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
                "nama"  : "Berliana Enda Putri",
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
                "nama"  : "Jeremia Susanto",
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
    baleg()

elif menu == "Senator":
    def senator():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1lJSsyKQlAd7JC-D6gUtJx6jgT5JpxUdR", #kak lutfi
            "https://drive.google.com/uc?export=view&id=1-IgZEwoHqxGgG325qtEEzBCu8w_UeWql", #bang bintang
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
                "kesan" : "Sangat informatif dalam menjelaskan mengenai senator dan banyak memberikan masukan serta motivasi melalui pengalaman yang telah dilakukan",  
                "pesan" : "Semangat terus kak dalam menjalani dunia perkuliahan semoga tetap diberi kelancaran dalam melakukan tugas yang diemban"
            },
            {
                "nama"  : "Rian Bintang Wijaya",
                "nim"   : "122450094",
                "umur"  : "20",
                "asal"  : "Palembang, Sumatera Selatan",
                "alamat": "Kota Baru",
                "hobbi" : "Mendengar Lagu",
                "sosmed": "@bintangtwinkle",
                "kesan" : "Sangat informatif dalam menerangkan sesuatu dan mampu memberikan motivasi yang sangat berarti",  
                "pesan" : "Semoga kegiatan di dalam maupun di luar perkuliahan diperlancar, tetap semangat bang"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    senator()

elif menu == "Departemen PSDA":
    def psda():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1yOcOXYBbPPD0fKDDbN43Z_a_v-56czsn", #bang erickson dn
            "https://drive.google.com/uc?export=view&id=1SWM9hyINWMnEkvl-N0Tf0Hni8w3DAui2", #kak abeth dn
            "https://drive.google.com/uc?export=view&id=1dqPFTSiurwiljpnBuqMw0qsGTG30_pAh", #kak afifah dn
            "https://drive.google.com/uc?export=view&id=1tV9AxJEbVlXx5lCcsKQvU0gMG8WhtBu_", #kak allya dn
            "https://drive.google.com/uc?export=view&id=1z6Nf_pGRwr3YHl5jZmtN9xDqtHoSo7U0", #kak hanum dn
            "https://drive.google.com/uc?export=view&id=1_BLhVq-u3otlQEoSOysl2Vu6W1sifgFd", #bang ferdy dn
            "https://drive.google.com/uc?export=view&id=1XaF3VJMyoqaqqZbs-feCa9WtxG_Tr-k7", #bang deri dn
            "https://drive.google.com/uc?export=view&id=1UUEr1gdGPs-t7v2CZsv2hk3L0RpkO-nd", #kak oktavia dn
            "https://drive.google.com/uc?export=view&id=1uN-yF4xkPuAZa-OGkIgLJPfQDlCtzbUU", #bang deyvan dn
            "https://drive.google.com/uc?export=view&id=1_QmWY3uSgcxW5s1sRAGSIMt9qLPmm49f", #bang ibnu dn
            "https://drive.google.com/uc?export=view&id=1mSpgiOk8OkwmlY5It2DrafcQiW4cL7UB", #bang jo dn
            "https://drive.google.com/uc?export=view&id=1ZIzpLl3E6eeM2F1pCOE59aWMxrmsmuD2", #bang kemas dn
            "https://drive.google.com/uc?export=view&id=1pOlz7rWyLs7CI1TSOxvNYrjVKUbttKNm", #bang leonard dn
            "https://drive.google.com/uc?export=view&id=1lZmI37RTz5_ZcGbe4AlIxOxK1BZn-n3v", #kak presilia dn
            "https://drive.google.com/uc?export=view&id=1PzbkPhAfMpOqJPMMOSjZ_TgEtyxugXky", #kak rafa dn
            "https://drive.google.com/uc?export=view&id=1RzeQIfZzlYNL4THMLdBbVOGW2xC8sF_e", #bang sahid dn
            "https://drive.google.com/uc?export=view&id=1wRI1AcIN7hHi8Kw7dQg2-CmbVnyuV7qm", #kak vanes dn
            "https://drive.google.com/uc?export=view&id=1vzJq0Dr_lcwNLBtE44ceqcL7yDefn0pP", #bang ateng dn
            "https://drive.google.com/uc?export=view&id=1KMx27KU6gYRH2SxQZHh9MGMgxiHpWm9q", #bang gede dn
            "https://drive.google.com/uc?export=view&id=1CxDELCaWXdsX1B7axA7xsL0ACCkzyjUr", #kak jaclin dn
            "https://drive.google.com/uc?export=view&id=13ZC4S6I2Rhukg8iT37fST7jvgn-SdvLy", #bang rafly dn
            "https://drive.google.com/uc?export=view&id=1ZYzuVrKw3G_Aar9z-u-ZU5XgJMudQqcr", #kak dini dn

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
                "kesan" : "Menerangkan informasi dengan sangat jelas dan mampu memberikan banyak masukan dan motivasi",  
                "pesan" : "Tetap semangat bang dalam mengikuti kegiatan baik di dalam maupun di luar perkuliahan dan semoga diperlancar bang segala urusannya"
            },
            {
                "nama"  : "Elisabeth Claudia Simanjuntak",
                "nim"   : "122450123",
                "umur"  : "18",
                "asal"  : "Pekanbaru",
                "alamat": "Sukarame",
                "hobbi" : "Memancing keributan",
                "sosmed": "@celisabethh_",
                "kesan" : "Sangat ramah dan baik hati",  
                "pesan" : "Tetap semangat kak dalam menjalani hari-harinya, semoga diperlancar semua urusan kedepannya"
            },
            {
                "nama"  : "Nisrina Nur Afifah",
                "nim"   : "122450052",
                "umur"  : "19",
                "asal"  : "Bekasi",
                "alamat": "Sukarame",
                "hobbi" : "Nabok orang",
                "sosmed": "@afifahhnsrn",
                "kesan" : "Sangat baik dan informatif dalam menerangkan suatu permasalahan",  
                "pesan" : "Semangat terus kak, semoga kegiatan maupun tanggung jawab yang sedang diemban dapat berjalan dengan lancar"
            },
            {
                "nama"  : "Allya Nurul Islami Pasha",
                "nim"   : "122450033",
                "umur"  : "20",
                "asal"  : "Sumatera Barat",
                "alamat": "Gang Perwira, Belwis",
                "hobbi" : "Nonton Dracin",
                "sosmed": "@allyaislami_",
                "kesan" : "Sangat informatif dalam menerangkan sesuatu",  
                "pesan" : "Tetap semangat kak dalam melakukan tanggung jawab yang sedang diemban, semoga dipermudah semua urusannya"
            },
            {
                "nama"  : "Farahanum Afifah Ardiansyah",
                "nim"   : "122450056",
                "umur"  : "20",
                "asal"  : "Padang, Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi" : "Tidur",
                "sosmed": "@farahanumafifahh",
                "kesan" : "Sangat baik dan informatif dalam menerangkan sesuatu",  
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
                "kesan" : "Sangat baik dan ramah",  
                "pesan" : "Tetap semangat bang dalam menjalani dunia perkuliahan, semoga diperlancar kegiatan kedepannya"
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
                "pesan" : "Semangat terus bang dalam menjalani perkuliahannya serta jangan lupa untuk jaga kesehatan"
            },
            {
                "nama"  : "Oktavia Nurwinda Puspita Sari",
                "nim"   : "122450041",
                "umur"  : "20",
                "asal"  : "Lampung Timur",
                "alamat": "Way Hui",
                "hobbi" : "Memasak",
                "sosmed": "@_oktavianrwnda_",
                "kesan" : "Sangat ramah dan baik hati",  
                "pesan" : "Tetap semangat kak dalam menjalani hari-harinya, semoga diperlancar segala urusan kedepannya"
            },
            {
                "nama"  : "Deyvan Loxefal",
                "nim"   : "121450148",
                "umur"  : "21",
                "asal"  : "Riau",
                "alamat": "Pulau Damar",
                "hobbi" : "Belajar",
                "sosmed": "@depanloo",
                "kesan" : "Sangat informatif dalam menjelaskan divisi Manajemen Minat dan Bakat dan memberikan banyak masukan melalui pengalaman yang telah dilakukan ",  
                "pesan" : "Tetap semangat bang dalam menjalankan semua kegiatan yang sedang diemban, semoga diperlancar bang segala urusannya"
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
                "pesan" : "Semangat bang dalam menjalani perkuliahannya, semoga diperlancar segala urusan kedepannya"
            },
             {
                "nama"  : "Johannes Krisjon Silitonga",
                "nim"   : "122450043",
                "umur"  : "19",
                "asal"  : "Tanggerang",
                "alamat": "Jalan Lapas",
                "hobbi" : "Ngasprak",
                "sosmed": "@johanneskrisjnnn",
                "kesan" : "Sangat informatif dalam menjelaskan sesuatu dan banyak memberi masukan melalui pengalaman yang telah dilakukan",  
                "pesan" : "Semangat bang dalam menjalani dunia perkuliahan dan tetap jaga kesehatan bang"
            },
            {
                "nama"  : "Kemas Veriandra Ramadhan",
                "nim"   : "122450016",
                "umur"  : "19",
                "asal"  : "Bekasi",
                "alamat": "Golf Asri",
                "hobbi" : "Bermain ular python digital",
                "sosmed": "@kemasverii",
                "kesan" : "Sangat informatif dalam menjelaskan sesuatu dan sangat ramah",  
                "pesan" : "Semangat bang dalam menjalani kegiatannya dan semoga diperlancar segala urusan kedepannya"
            },
            {
                "nama"  : "Leonard Andreas Napitupulu",
                "nim"   : "121450153",
                "umur"  : "21",
                "asal"  : "Sumatera Utara",
                "alamat": "Kobam",
                "hobbi" : "Belajar",
                "sosmed": "@lnrd.__",
                "kesan" : "Sangat baik dan ramah ",  
                "pesan" : "Tetap jaga kesehatan bang dan semangat dalam menjalani dunia perkuliahan"
            },
            {
                "nama"  : "Presilia",
                "nim"   : "122450081",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Kota Baru",
                "hobbi" : "Tidur",
                "sosmed": "@presiliamg",
                "kesan" : "Sangat baik hati dan ramah",  
                "pesan" : "Semoga dilancarkan semua urusannya kak, jangan lupa untuk tetap semangat kak dalam menjalani kehidupan"
            },
            {
                "nama"  : "Rafa Aqilla Jungjunan",
                "nim"   : "122450142",
                "umur"  : "20",
                "asal"  : "Riau",
                "alamat": "Belwis",
                "hobbi" : "Membaca webtoon",
                "sosmed": "@rafaaqilla",
                "kesan" : "Sangat baik dan sangat ramah",  
                "pesan" : "Tetap semangat dalam menjalani perkuliahannya kak dan tetap jaga kesehatan"
            },
            {
                "nama"  : "Sahid Maulana",
                "nim"   : "122450109",
                "umur"  : "21",
                "asal"  : "Depok, Jawa Barat",
                "alamat": "Airan Raya",
                "hobbi" : "Bermain Game",
                "sosmed": "@sahid_maul19",
                "kesan" : "Baik hati dan ramah",  
                "pesan" : "Tetap semangat kak dalam menjalani dunia perkuliahan"
            },
            {
                "nama"  : "Vanessa Olivia Rose",
                "nim"   : "121450108",
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
                "nim"   : "121450117",
                "umur"  : "21",
                "asal"  : "Bandar Lampung",
                "alamat": "Kota Baru",
                "hobbi" : "Menolong",
                "sosmed": "@mfarhan.ath",
                "kesan" : "Sangat informatif dalam menjelaskan sesuatu dan banyak memberi masukan",  
                "pesan" : "Semangat bang dalam menjalani kegiatan di dalam maupun di luar perkuliahan, semoga segala urusan kedepannya diperlancar"
            },
            {
                "nama"  : "Gede Moena",
                "nim"   : "121450014",
                "umur"  : "21",
                "asal"  : "Bekasi",
                "alamat": "Korpri Raya",
                "hobbi" : "Belajar dan main game",
                "sosmed": "@gedemoenaa",
                "kesan" : "Sangat baik dan ramah",  
                "pesan" : "Tetap semangat bang dalam menjalani dunia perkuliahan dan semoga semuanya diperlancar"
            },
            {
                "nama"  : "Jaclin Alcavella",
                "nim"   : "122450015",
                "umur"  : "19",
                "asal"  : "Sumatera Selatan",
                "alamat": "Korpri",
                "hobbi" : "Berenang",
                "sosmed": "@jaclinalcv_",
                "kesan" : "Sangat baik dan informatif dalam menjelaskan sesuatu",  
                "pesan" : "Tetap semangat kak dalam menjalani hari-harinya dan jangan lupa untuk jaga kesehatan kak"
            },
            {
                "nama"  : "Rafly Prabu Darmawan",
                "nim"   : "122450140",
                "umur"  : "20",
                "asal"  : "Bangka Belitung",
                "alamat": "Sukarame",
                "hobbi" : "Main Game",
                "sosmed": "@raflyy_pd2684",
                "kesan" : "Sangat baik dan ramah",  
                "pesan" : "Jangan lupa jaga kesehatan bang dan tetap semangat dalam menjalani hari-harinya"
            },
            {
                "nama"  : "Syalaisha Andini Putriansyah",
                "nim"   : "122450111",
                "umur"  : "21",
                "asal"  : "Tanggerang",
                "alamat": "Sukarame",
                "hobbi" : "Membaca",
                "sosmed": "@syalaisha.i__",
                "kesan" : "Sangat baik dan ramah",  
                "pesan" : "Semangat kak dalam menjalani hari-harinya, semoga urusannya dalam dunia perkuliahan dapat diselesaikan dengan mudah"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    psda()

elif menu == "Departemen MIKFES":
    def mikfes():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1qTlCByOTepmYAmHMNqSTOiiNzInqlgZG", #bang rafi dn
            "https://drive.google.com/uc?export=view&id=1YybaYByUKEuuUL_oYi4AUrDb3UgzXwRt", #kak anisa dn
            "https://drive.google.com/uc?export=view&id=1fgEAzLWz2mySdrV73UxJP7JLRgogS-Um", #bang ahmad dn
            "https://drive.google.com/uc?export=view&id=1TUSHT9s2WGO50TIBbfHAJzenaFyo5w8N", #bang fadhil dn
            "https://drive.google.com/uc?export=view&id=1ZTHuRKoMclZ3oHGd9Jm1mzWPIPnnQfME", #kak dina dn
            "https://drive.google.com/uc?export=view&id=1Wnqx5QeUR2XaCIxnYZi36fbBp81__GNm", #kak dinda dn
            "https://drive.google.com/uc?export=view&id=16JS_tzUVR4mOdPsPPhO09WCuppomxex5", #kak marleta dn
            "https://drive.google.com/uc?export=view&id=1zqlMDd3VWPHESPFwO_Xwhv7n9V6dxtl5", #kak rut junita dn
            "https://drive.google.com/uc?export=view&id=1GK9egTOkasL0t5yz6jDBPY4tFq9SgKSU", #kak syadza dn
            "https://drive.google.com/uc?export=view&id=1AF1AE_DpTLkT992P8_S4_ycXikNO_zUy", #bang eggi dn
            "https://drive.google.com/uc?export=view&id=1Rb2r7WJRdXMV5jhgNsZukQlrDr7EiXhR", #kak febiya dn
            "https://drive.google.com/uc?export=view&id=1W7paDYSuMDswqUl2Fk0CY0yxYW4nc64S", #kak happy syahrul dn
            "https://drive.google.com/uc?export=view&id=1gIWl2NPjh-QMHNNKYBRFb36y1U431kG5", #bang randa dn

        ]
        data_list = [
            {
                "nama"  : "Rafi Fadhlillah",
                "nim"   : "121450143",
                "umur"  : "21",
                "asal"  : "Lubuk Linggau",
                "alamat": "Jalan Nangka 4",
                "hobbi" : "Olahraga",
                "sosmed": "@rafadhilillah",
                "kesan" : "Sangat informatif dalam menjelaskan departemen MIKFES dan banyak memberikan tips serta masukan melalui pengalaman yang telah dilakukan",  
                "pesan" : "Semangat terus bang dalam mengikuti kegiatan di dalam dan di luar perkuliahan, semoga segala urusannya diperlancar"
            },
            {
                "nama"  : "Annisa Novantika",
                "nim"   : "121450005",
                "umur"  : "21",
                "asal"  : "Lampung Utara",
                "alamat": "Jl. Pulau Sebesi, Sukarame",
                "hobbi" : "Memasak",
                "sosmed": "@anovavona",
                "kesan" : "Sangat baik dan informatif dalam menerangkan suatu permasalahan",  
                "pesan" : "Tetap semangat kak dalam menjalani kegiatan perkuliahan, semoga urusannya dipermudah "
            },
            {
                "nama"  : "Ahmad Sahidin Akbar",
                "nim"   : "122450044",
                "umur"  : "20",
                "asal"  : "Tulang Bawang",
                "alamat": "Sukarame",
                "hobbi" : "Olahraga",
                "sosmed": "@sahid22__",
                "kesan" : "Informatif dalam menjelaskan sesuatu",  
                "pesan" : "Semoga kegiatannya di dalam maupun di luar perkuliahan tetap lancar bang"
            },
            {
                "nama"  : "Fadhil Fitra Wijaya",
                "nim"   : "122450082",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Teluk Betung",
                "hobbi" : "Main game",
                "sosmed": "@fadhilfwee",
                "kesan" : "Banyak memberikan informasi dalam menerangkan suatu permasalahan",  
                "pesan" : "Tetap jaga kesehatan kak dan jangan lupa untuk tetap semangat kak dalam mengikuti dunia perkuliahan"
            },
            {
                "nama"  : "Syalaisha Andina Putriansyah",
                "nim"   : "122450121",
                "umur"  : "21",
                "asal"  : "Tangerang",
                "alamat": "Gang Yudhistira",
                "hobbi" : "Baca jurnal",
                "sosmed": "@dkselsd_31",
                "kesan" : "Sangat baik hati dan ramah",  
                "pesan" : "Semoga dipermudah segala urusannya kak, jangan lupa untuk tetap semangat dalam menjalani perkuliahan"
            },
            {
                "nama"  : "Dinda Nababan",
                "nim"   : "122450120",
                "umur"  : "20",
                "asal"  : "Medan, Sumatera Utara",
                "alamat": "Jalan Lapas",
                "hobbi" : "Belajar",
                "sosmed": "@dindanababan_",
                "kesan" : "Menginspirasi dalam kehidupan melalui pengalaman yang telah diraih",  
                "pesan" : "Tetap semangat kak dalam menjalani perkuliahannya kak dan jangan lupa untuk tetap jaga kesehatan"
            },
            {
                "nama"  : "Marleta Cornelia Leander",
                "nim"   : "122450092",
                "umur"  : "20",
                "asal"  : "Depok, Jawa Barat",
                "alamat": "Gang Nangka 3",
                "hobbi" : "Review Jurnal",
                "sosmed": "@marletacornelia",
                "kesan" : "Baik hati dan banyak memberikan informasi",  
                "pesan" : "Semangat kak dalam menjalani dunia perkuliahan dan semoga dipermudah segala urusannya"
            },
            {
                "nama"  : "Rut Junita Sari Siburian",
                "nim"   : "122450103",
                "umur"  : "20",
                "asal"  : "Batam, Kepulauan Riau",
                "alamat": "Gang Nangka 3",
                "hobbi" : "Review Jurnal",
                "sosmed": "@junitaa_0406",
                "kesan" : "Sangat baik dan ramah",  
                "pesan" : "Semangat kak dalam mengikuti dunia perkuliahan serta jangan lupa untuk jaga kesehatan"
            },
            {
                "nama"  : "Syadza Puspadari Azhar",
                "nim"   : "122450072",
                "umur"  : "20",
                "asal"  : "Palembang",
                "alamat": "Belwis",
                "hobbi" : "Resume SG",
                "sosmed": "@puspadrr",
                "kesan" : "Sangat seru dan baik hati",  
                "pesan" : "Jangan lupa untuk tetap semangat dalam menjalani dunia perkuliahan kak, semoga urusannya selalu dilancarkan"
            },
            {
                "nama"  : "Eggi satria",
                "nim"   : "122450032",
                "umur"  : "20",
                "asal"  : "Sukabumi",
                "alamat": "Korpri",
                "hobbi" : "Ngoding WISATA",
                "sosmed": "@egistr",
                "kesan" : "Sangat informatif dalam menjelaskan banyak informasi",  
                "pesan" : "Semangat bang dalam menjalani dunia perkuliahan, semoga semua tanggung jawab yang diemban dapat diselesaikan dengan lancar"
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
                "pesan" : "Tetap semangat kak dalam mengikuti dunia perkuliahan dan semoga diperlancar segala urusannya"
            },
             {
                "nama"  : "Happy Syahrul Ramadhan",
                "nim"   : "122450013",
                "umur"  : "20",
                "asal"  : "Lampung Timur",
                "alamat": "Karang Anyar",
                "hobbi" : "Main game",
                "sosmed": "@sudo.syahrulramadhannn",
                "kesan" : "Baik dan ramah",  
                "pesan" : "Tetap semangat bang dalam menjalani hari-harinya dan jangan lupa jaga kesehatan bang"
            },
            {
                "nama"  : "Randa Andriana Putra",
                "nim"   : "122450083",
                "umur"  : "21",
                "asal"  : "Banten",
                "alamat": "Sukarame",
                "hobbi" : "Tidur dan berkembang",
                "sosmed": "@randaandriana_",
                "kesan" : "Banyak memberikan informasi serta motivasi melalui pengalaman yang telah dilakukan",  
                "pesan" : "Semoga segala urusan di dalam maupun di luar perkuliahan tetap lancar dan jangan lupa tetap semangat bang"
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
                "kesan" : "Sangat informatif dalam menjelaskan departemen MEDKRAF dan banyak memberikan masukan ",  
                "pesan" : "Semangat bang dalam mengikuti segala kegiatan di dalam maupun di luar perkuliahan dan semoga segala urusannya diperlancar bang "
            },
            {
                "nama"  : "Elok Fiola",
                "nim"   : "122450051",
                "umur"  : "19",
                "asal"  : "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi" : "Editing",
                "sosmed": "@elokfiola",
                "kesan" : "Sangat informatif dalam menjelaskan dan banyak memberikan motivasi",  
                "pesan" : "Tetap semangat dan semoga kegiatannya di dalam maupun di luar perkuliahan tetap lancar"
            },
            {
                "nama"  : "Arsyiah Azahra",
                "nim"   : "121450035",
                "umur"  : "21",
                "asal"  : "Bandar Lampung",
                "alamat": "Tanjung Senang",
                "hobbi" : "Nugas",
                "sosmed": "@arsyiah.__",
                "kesan" : "Sangat baik, informatif dalam menerangkan suatu permasalahan",  
                "pesan" : "Jangan lupa jaga kesehatan kak dan tetap semangat kak dalam menjalani harinya"
            },
            {
                "nama"  : "Cintya Bella",
                "nim"   : "122450066",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Teluk",
                "hobbi" : "Ngegym",
                "sosmed": "@cintyabella28",
                "kesan" : "Baik hati dan ramah sekali",  
                "pesan" : "Semoga diperlancar kak segala kegiatan kedepannya"
            },
            {
                "nama"  : "Najla Juwairia",
                "nim"   : "122450037",
                "umur"  : "19",
                "asal"  : "Sumatera Utara",
                "alamat": "Airan",
                "hobbi" : "Menulis, Membaca, Fangirling",
                "sosmed": "@nanana_minjoo",
                "kesan" : "Sangat baik dan ramah",  
                "pesan" : "Jangan lupa jaga kesehatan dan tetap semangat dalam menjalani perkuliahannya kak"
            },
            {
                "nama"  : "Rahma Neliyana",
                "nim"   : "122450036",
                "umur"  : "20",
                "asal"  : "Lampung",
                "alamat": "Sukarame",
                "hobbi" : "Baca Coding",
                "sosmed": "@rahmanellyana",
                "kesan" : "Baik hati dan banyak memberikan motivasi serta masukan melalui kegiatan yang telah dilakukan",  
                "pesan" : "Tetap semangat kak dalam mengikuti segala kegiatan dan semoga semuanya dipermudah urusannya"
            },
            {
                "nama"  : "Try Yani Rizki Nur Rohmah",
                "nim"   : "122450020",
                "umur"  : "20",
                "asal"  : "Lampung Barat",
                "alamat": "Korpri",
                "hobbi" : "Bernyanyi dan Menonton",
                "sosmed": "@tryyaniciaaa",
                "kesan" : "Sangat baik dan sangat mengasyikkan",  
                "pesan" : "Tetap semangat kak dalam menjalani perkuliahannya serta jangan lupa untuk jaga kesehatan"
            },
            {
                "nama"  : "Muhammad Kaisar Firdaus",
                "nim"   : "121450135",
                "umur"  : "21",
                "asal"  : "Pesawaran",
                "alamat": "Pulau Damar",
                "hobbi" : "Lagi nyari",
                "sosmed": "@dino_lapet",
                "kesan" : "Sangat seru, mengasyikkan, dan informatif dalam menjelaskan sesuatu",  
                "pesan" : "Jangan lupa untuk tetap semangat bang dalam menjalani segala kegiatannya"
            },
            {
                "nama"  : "Dwi Ratna Anggraeni",
                "nim"   : "122450008",
                "umur"  : "20",
                "asal"  : "Jambi",
                "alamat": "Jalan Durian 5 Pemda",
                "hobbi" : "Membaca",
                "sosmed": "@dwiratnn_",
                "kesan" : "Sangat baik dan ramah",  
                "pesan" : "Semangat kak dalam menjalani perkuliahannya dan semoga diperlancar"
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
                "pesan" : "Tetap semangat bang dalam menjalani dunia perkuliahan "
            },
             {
                "nama"  : "Nasywa Nur Afifah",
                "nim"   : "122450125",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Jalan Durian 1 Pemda",
                "hobbi" : "Nonton drakor",
                "sosmed": "@nsywanaf",
                "kesan" : "Sangat ramah dan mengasyikkan",  
                "pesan" : "Tetap semangat kak dalam mengikuti dunia perkuliahan, semoga diperlancar dalam menyelesaikan semua tugasnya"
            },
            {
                "nama"  : "Priska Silvia Ferantiana",
                "nim"   : "122450053",
                "umur"  : "19",
                "asal"  : "Palembang",
                "alamat": "Jalan Nangka 2",
                "hobbi" : "Baca novel yang bikin nangis",
                "sosmed": "@prskslv",
                "kesan" : "Baik hati dan ramah",  
                "pesan" : "Semoga kegiatan baik di dalam maupun di luar perkuliahan tetap lancar dan tetap semangat kak"
            },
            {
                "nama"  : "Muhammad Arsal Ranjana Utama",
                "nim"   : "121450111",
                "umur"  : "21",
                "asal"  : "Depok",
                "alamat": "Jalan Nangka 4",
                "hobbi" : "Ngoding",
                "sosmed": "@arsal.utama",
                "kesan" : "Sangat baik dan ramah",  
                "pesan" : "Semangat bang dalam menjalani harinya dan tetap jaga kesehatan"
            },
            {
                "nama"  : "Abit Ahmad Oktarian",
                "nim"   : "122450042",
                "umur"  : "19",
                "asal"  : "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi" : "Ngoding, Gaming",
                "sosmed": "@abitahmad",
                "kesan" : "Sangat seru dan mengasyikkan",  
                "pesan" : "Semoga selalu dilancarkan segala urusannya bang dan semoga tugas yang sedang diemban dapat diselesaikan dengan baik "
            },
            {
                "nama"  : "Akmal Faiz Abdillah",
                "nim"   : "122450114",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Perumahan Griya Sukarame",
                "hobbi" : "Main HP",
                "sosmed": "@_akmal.faiz",
                "kesan" : "Sangat baik dan banyak memberikan informasi",  
                "pesan" : "Tetap semangat bang dalam menjalani perkuliahannya kak"
            },
            {
                "nama"  : "Hermawan Manurung",
                "nim"   : "122450069",
                "umur"  : "20",
                "asal"  : "Bogor",
                "alamat": "Dekat jalan tol, Wisma Hana Hani",
                "hobbi" : "Bengong dan membaca buku",
                "sosmed": "@hermawan.mnrng",
                "kesan" : "Sangat menginspirasi dalam kehidupan melalui pengalaman yang telah dilakukan dan sangat seru",  
                "pesan" : "Semangat bang dalam menjalani dunia perkuliahan semoga segala urusannya dipermudah"
            },
            {
                "nama"  : "Khusnun Nisa",
                "nim"   : "122450078",
                "umur"  : "20",
                "asal"  : "Lampung Selatan",
                "alamat": "Belwis",
                "hobbi" : "Mengerjakan tugas",
                "sosmed": "@khusnun_nisa335",
                "kesan" : "Sangat baik, mengasyikkan, dan seru ",  
                "pesan" : "Semangat terus kak dalam menjalani perkuliahannya serta jangan lupa untuk tetap jaga kesehatan"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    medkraf()

elif menu == "Departemen Eksternal":
    def eksternal():
        gambar_urls = [
            "https://drive.google.com/uc?export=view&id=1sWOBFSt1-F1zoryil5Fx3MVQ4ISFFQbJ", #bang yogy dn
            "https://drive.google.com/uc?export=view&id=1oOIMQ0G-VwkwZ__1bC9Xeo2DH5uh3EMH", #kak ramadhita dn
            "https://drive.google.com/uc?export=view&id=1F8VYxAHFNITiGD9Ombbdd6dVpAghVG75", #kak nazwa dn
            "https://drive.google.com/uc?export=view&id=1yo8Y_EeHC8G9r-FeV55-9960M8VY7vVA", #bang bastian dn
            "https://drive.google.com/uc?export=view&id=1IRloQPTpKQ0zqdYOH0RrXFgxeQ7MlkU8", #kak dea dn
            "https://drive.google.com/uc?export=view&id=1wd9pPTXFBx7EFKeEWuQ_LICOp1waDYpe", #kak esteria dn
            "https://drive.google.com/uc?export=view&id=19PFCwdrENV4r_lKjj1gbg7uN6SQVLv0v", #kak natasya ega dn
            "https://drive.google.com/uc?export=view&id=1tcJ9ylebQVAtHJfka1aoYdmf91hRs5Mj", #kak novelia dn
            "https://drive.google.com/uc?export=view&id=15hDSaPPfJpbErrvlASkZLaKI-D8MpUHR", #kak jasmine dn
            "https://drive.google.com/uc?export=view&id=1RiVFJJA5Rp-BK9pQW57qzpvgnJxm8PCz", #bang tobias dn
            "https://drive.google.com/uc?export=view&id=1QSt1-YwV664MAtOfVkvYBsEXDJ1JGGr-", #kak yohana dn
            "https://drive.google.com/uc?export=view&id=14PsVGxbFgzivV34_5h5zasCsWy5PHVk5", #bang rizki dn
            "https://drive.google.com/uc?export=view&id=1_jhcd9O11tq7Qj-SuLbyZ9kVuFbmmY7z", #bang arafi dn
            "https://drive.google.com/uc?export=view&id=12WU7Pg9za_lrxhxNmBEG53Ea411MkJfu", #kak uyi dn
            "https://drive.google.com/uc?export=view&id=1cOrwwVrrwtXhEuNBoc8GMsio0RrGDja0", #kak chalifia dn
            "https://drive.google.com/uc?export=view&id=1E6GXxvBauz1qyPwN48S9-uJXwczBa-JK", #bang irvan dn
            "https://drive.google.com/uc?export=view&id=1vQxJkLeFBN8PwwSBAdvZ9YdYlV51f34F", #kak izza dn
            "https://drive.google.com/uc?export=view&id=1E85NscnViNz3uH-MIRtgUDSUHyjcGNJ1", #kak zuhrah dn
            "https://drive.google.com/uc?export=view&id=1BaPPwXFONK7OyxP7Ur6YmWc7sNdjVO_9", #bang raid dn
            "https://drive.google.com/uc?export=view&id=1slu-o22MSwKg_BP5JDOUdvjbzAyaWNS7", #kak tria dn
        ]
        data_list = [
            {
                "nama"  : "Yogy Sae Tama",
                "nim"   : "121450041",
                "umur"  : "21 Tahun",
                "asal"  : "Tangerang",
                "alamat": "Jatimulyo",
                "hobbi" : "Bangun pagi",
                "sosmed": "@yogyyyyyy",
                "kesan" : "Sangat informatif dalam menerangkan departemen Eksternal dan banyak memberikan motivasi ",  
                "pesan" : "Tetap semangat bang dalam mengikuti segala kegiatan, semoga segala urusannya dipermudah"
            },
                        {
                "nama"  : "Ramadhita Atifa Hendri",
                "nim"   : "121450131",
                "umur"  : "21 Tahun",
                "asal"  : "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi" : "Jalan - Jalan",
                "sosmed": "@ramadhitaatifa",
                "kesan" : "Sangat informatif dalam menerangkan suatu permasalahan",  
                "pesan" : "Semoga kegiatannya baik di dalam maupun di luar perkuliahan tetap lancar kak"
            },
                        {
                "nama"  : "Nazwa Nabilla",
                "nim"   : "121450122",
                "umur"  : "21 Tahun",
                "asal"  : "Jakarta Selatan",
                "alamat": "Way kandis",
                "hobbi" : "Belajar",
                "sosmed": "@nazwanbilla",
                "kesan" : "Sangat baik, ramah, dan, informatif dalam menjelaskan sesuatu",  
                "pesan" : "Tetap semangat kak dalam menjalani segala kegiatannya dan semoga diperlancar"
            },
            {
                "nama"  : "Bastian Heskia Silaban",
                "nim"   : "122450130",
                "umur"  : "21 Tahun",
                "asal"  : "Batam, Kepulauan Riau",
                "alamat": "Belwis",
                "hobbi" : "Main game",
                "sosmed": "@bastiansilaban_",
                "kesan" : "Tegas, namun sangat informatif dalam menerangkan sesuatu",  
                "pesan" : "Semoga selalu dilancarkan semua urusannya bang, jangan lupa untuk tetap semangat dalam menjalani perkuliahan"
            },
             {
                "nama"  : "Dea Mutia Risani",
                "nim"   : "122450099",
                "umur"  : "20 Tahun",
                "asal"  : "Sumatera Barat",
                "alamat": "Korpri",
                "hobbi" : "Dengerin musik",
                "sosmed": "@deaa.rsn",
                "kesan" : "Sangat baik dan ramah",  
                "pesan" : "Tetap semangat dalam menjalani perkuliahannya kak dan jangan lupa jaga kesehatan"
            },
            {
                "nama"  : "Esteria Rohanauli Sidauruk",
                "nim"   : "122450025",
                "umur"  : "19 Tahun",
                "asal"  : "Jakarta Selatan",
                "alamat": "Belwis",
                "hobbi" : "Main golf bareng kadiv",
                "sosmed": "@esteriars",
                "kesan" : "Banyak memberi masukan dan sangat menginspirasi dalam kehidupan",  
                "pesan" : "Tetap semangat kak dalam menjalani dunia perkuliahan"
            },
                        {
                "nama"  : "Natasya Ega Lina",
                "nim"   : "122450024",
                "umur"  : "19 Tahun",
                "asal"  : "Jakarta Selatan",
                "alamat": "Belwis",
                "hobbi" : "Jadi humas",
                "sosmed": "@nateee__15",
                "kesan" : "Sangat baik dan sangat mengasyikkan ",  
                "pesan" : "Semangat terus kak dan sukses terus untuk kedepannya"
            },
            {
                "nama"  : "Novelia Adinda",
                "nim"   : "122450104",
                "umur"  : "21 Tahun",
                "asal"  : "Jakarta Timur",
                "alamat": "Belwis",
                "hobbi" : "Tidur",
                "sosmed": "@nvliaadinda",
                "kesan" : "Sangat seru, ramah, dan  baik hati",  
                "pesan" : "Jangan lupa untuk tetap semangat dalam menjalani dunia perkuliahan kak, semoga urusannya selalu dilancarkan"
            },
            {
                "nama"  : "Ratu Keisha Jasmine Deanova",
                "nim"   : "122450106",
                "umur"  : "20 Tahun",
                "asal"  : "Jakarta Selatan",
                "alamat": "Way Kandis",
                "hobbi" : "Main sepak takraw",
                "sosmed": "@jasminednva",
                "kesan" : "Informatif dalam menjelaskan sesuatu, baik hati, dan banyak memberi masukan serta motivasi",  
                "pesan" : "Tetap semangat kak dalam menjalani hari-harinya, semoga semua tugas dan tanggung jawab dapat diselesaikan dengan baik"
            },
                        {
                "nama"  : "Tobias David Manogari",
                "nim"   : "122450091",
                "umur"  : "20 Tahun",
                "asal"  : "Sumatera Utara",
                "alamat": "Pemda",
                "hobbi" : "Jogging",
                "sosmed": "@tobiassiagian",
                "kesan" : "Sangat baik dan sangat mengasyikkan",  
                "pesan" : "Jangan lupa untuk tetap jaga kesehatan kak dan tetap semangat kak dalam menjalani hari-harinya"
            },
             {
                "nama"  : "Yohana Manik",
                "nim"   : "122450126",
                "umur"  : "19 Tahun",
                "asal"  : "Jakarta Selatan",
                "alamat": "Belwais",
                "hobbi" : "Main Bowling",
                "sosmed": "@yo_annamnk",
                "kesan" : "Sangat baik dan banyak memberi masukan serta semangat",  
                "pesan" : "Tetap semangat kak dalam menjalani hari-harinya"
            },
            {
                "nama"  : "Rizki Adrian Bennovry",
                "nim"   : "121450073",
                "umur"  : "21 Tahun",
                "asal"  : "Bekasi",
                "alamat": "TVRI",
                "hobbi" : "Bikin portofolio",
                "sosmed": "@rzkdrnnn",
                "kesan" : "Sangat seru dan mengasyikkan",  
                "pesan" : "Semoga kegiatannya di dalam maupun di luar perkuliahan tetap lancar dan tetap semangat kak"
            },
            {
                "nama"  : "Arafi Ramadhan Maulana",
                "nim"   : "122450002",
                "umur"  : "20 Tahun",
                "asal"  : "Bandung",
                "alamat": "Way Huwi",
                "hobbi" : "Bertani",
                "sosmed": "@rafiramadhanmaulana",
                "kesan" : "Sangat baik dan ramah",  
                "pesan" : "Tetap semangat kak dalam menjalani harinya"
            },
            {
                "nama"  : "Asa Do'a Uyi",
                "nim"   : "122450005",
                "umur"  : "20 Tahun",
                "asal"  : "Muara Enim",
                "alamat": "Korpri",
                "hobbi" : "Tepuk Semangat",
                "sosmed": "@u_yippy",
                "kesan" : "Sangat ramah dan baik hati",  
                "pesan" : "Semoga selalu dilancarkan semua urusannya kak, jangan lupa untuk tetap semangat kak"
            },
            {
                "nama"  : "Chalifia Wananda",
                "nim"   : "122450076",
                "umur"  : "20 Tahun",
                "asal"  : "Padang",
                "alamat": "Sukarame",
                "hobbi" : "Q Time",
                "sosmed": "@chlfawww",
                "kesan" : "Sangat baik dan ramah",  
                "pesan" : "Tetap semangat dalam menjalani perkuliahannya kak dan jangan lupa jaga kesehatan"
            },
            {
                "nama"  : "Irvan Alfaritzi",
                "nim"   : "122450093",
                "umur"  : "21 Tahun",
                "asal"  : "Sumatera Barat",
                "alamat": "Sukarame",
                "hobbi" : "Nonton youtube, main game",
                "sosmed": "@alfaritziirvan",
                "kesan" : "Sangat ramah",  
                "pesan" : "Tetap semangat bang dalam menjalani dunia perkuliahan"
            },
            {
                "nama"  : "Izza Lutfia",
                "nim"   : "122450090",
                "umur"  : "20 Tahun",
                "asal"  : "Bandar Lampung",
                "alamat": "Teluk Betung",
                "hobbi" : "Main Rubik",
                "sosmed": "@izzalutfia",
                "kesan" : "Sangat baik, banyak memberi masukan serta semangat melalui pengalaman yang telah dilakukan ",  
                "pesan" : "Semangat terus kak dalam menjalani perkuliahannya serta jangan lupa untuk jaga kesehatan"
            },
            {
                "nama"  : "Khaalishah Zuhrah Alyaa Vanefi",
                "nim"   : "122450034",
                "umur"  : "20 Tahun",
                "asal"  : "Bandar Lampung",
                "alamat": "Rajabasa",
                "hobbi" : "Mengaji",
                "sosmed": "@alyaavanevi",
                "kesan" : "Sangat seru dan mengasyikan",  
                "pesan" : "Tetap semangat kak dan semoga urusannya selalu dilancarkan"
            },
            {
                "nama"  : "Raid Muhammad Naufal",
                "nim"   : "122450027",
                "umur"  : "20 Tahun",
                "asal"  : "Lampung Tengah",
                "alamat": "Sukarame",
                "hobbi" : "telat",
                "sosmed": "@rayths_",
                "kesan" : "Sangat baik dan sangat informatif dalam menjelaskan sesuatu",  
                "pesan" : "Tetap semangat kak dalam menjalani hari-harinya"
            },
            {
                "nama"  : "Tria Yunanni",
                "nim"   : "122450062",
                "umur"  : "20 Tahun",
                "asal"  : "Way Kanan",
                "alamat": "Sukarame",
                "hobbi" : "Baca Buku",
                "sosmed": "@tria_y062",
                "kesan" : "Sangat baik dan sangat mengasyikkan",  
                "pesan" : "Semangat kak dan semoga urusannya dalam dunia perkuliahan dapat diselesaikan dengan mudah"
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
                "kesan" : "Sangat informatif dalam menjelaskan mengenai departemen Internal dan menjadi sosok inspiratif melalui pengalaman yang telah dilakukan",  
                "pesan" : "Tetap semangat kak dan semoga dipermudah segala urusannya"
            },
            {
                "nama"  : "Catherine Firdhasari Maulina Sinaga",
                "nim"   : "121450072",
                "umur"  : "20",
                "asal"  : "Sumatera Utara",
                "alamat": "Airan",
                "hobbi" : "Baca Novel",
                "sosmed": "@cathrine.sinaga",
                "kesan" : "Sangat informatif dalam menerangkan sesuatu",  
                "pesan" : "Semoga kegiatannya di dalam maupun di luar perkuliahan tetap dipermudah dan sukses kak"
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
                "kesan" : "Sangat informatif dalam menerangkan permasalahan dan menginspirasi dalam kehidupan",  
                "pesan" : "Semangat bang dalam menjalani dunia perkuliahan dan semoga diperlancar segala urusannya"
            },
            {
                "nama"  : "Rani Puspita sari",
                "nim"   : "122450030",
                "umur"  : "20",
                "asal"  : "Kota Metro",
                "alamat": "Rajabasa",
                "hobbi" : "Dengar musik",
                "sosmed": "@rannipu",
                "kesan" : "Sangat ramah dan baik hati",  
                "pesan" : "Semoga selalu dipermudah segala urusannya kak dan tetap semangat kak"
            },
            {
                "nama"  : "Rendra Eka Prayoga",
                "nim"   : "122450112",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Belwis",
                "hobbi" : "Mancing Ikan Mas",
                "sosmed": "@rendraepr",
                "kesan" : "Sangat baik dan banyak memberikan motivasi melalui pengalaman yang telah dilakukan",  
                "pesan" : "Tetap semangat bang dalam menjalani dunia perkuliahannya"
            },
            {
                "nama"  : "Salwa Farhanatussaidah",
                "nim"   : "122450055",
                "umur"  : "20",
                "asal"  : "Pesawaran",
                "alamat": "Airan",
                "hobbi" : "Nonton",
                "sosmed": "@slwfhn_694",
                "kesan" : "Sangat ramah dan baik hati",  
                "pesan" : "Tetap jaga kesehatan kak dan tetap semangat kak dalam menjalani dunia perkuliahan"
            },
            {
                "nama"  : "Yosia Letare Banurea",
                "nim"   : "121450149",
                "umur"  : "20",
                "asal"  : "Dairi, Sumatera Utara",
                "alamat": "Perum Griya Indah",
                "hobbi" : "Tidur",
                "sosmed": "@yosiabanurea",
                "kesan" : "Sangat baik dan informatif",  
                "pesan" : "Semangat terus bang dalam menjalani perkuliahan dan semoga diperlancar segala urusannya"
            },
            {
                "nama"  : "Ari Sigit",
                "nim"   : "121450069",
                "umur"  : "23",
                "asal"  : "Lampung Barat",
                "alamat": "Labuhan Ratu",
                "hobbi" : "Futsal",
                "sosmed": "@ari_sigit17",
                "kesan" : "Sangat baik dan sangat informatif dalam menerangkan divisi kerohanian",  
                "pesan" : "Jangan lupa tetap semangat bang dalam menjalani perkuliahan kak dan tetap jaga kesehatan bang"
            },
            {
                "nama"  : "Azizah Kusumah Putri",
                "nim"   : "122450068",
                "umur"  : "21",
                "asal"  : "Lampung Selatan",
                "alamat": "Natar",
                "hobbi" : "Berkebun",
                "sosmed": "@azizahksma15",
                "kesan" : "Sangat baik dan ramah",  
                "pesan" : "Semangat kak dalam menjalani hari-harinya"
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
                "pesan" : "Semangat kak dan semoga urusannya dalam dunia perkuliahan dapat diselesaikan dengan mudah"
            },
            {
                "nama"  : "Rendi Alexander Hutagalung",
                "nim"   : "122450057",
                "umur"  : "20",
                "asal"  : "Tangerang",
                "alamat": "Kost Benawang",
                "hobbi" : "Menyanyi",
                "sosmed": "@rexander",
                "kesan" : "Sangat baik dan banyak memberi masukan",  
                "pesan" : "Semangat bang dan semoga diperlancar dalam menyelesaikan tugas dan tanggung jawab yang sedang di emban"
            },
            {
                "nama"  : "Renta Siahaan",
                "nim"   : "122450070",
                "umur"  : "21",
                "asal"  : "Sumatera Utara",
                "alamat": "Gerbang Barat",
                "hobbi" : "Membaca dan Memancing",
                "sosmed": "@renta.shn",
                "kesan" : "Baik hati dan ramah",  
                "pesan" : "Semoga kegiatannya di dalam maupun di luar perkuliahan tetap lancar kak"
            },
            {
                "nama"  : "Josua Panggabean",
                "nim"   : "122450061",
                "umur"  : "21",
                "asal"  : "Pematang Siantar",
                "alamat": "Gerbang Barat",
                "hobbi" : "Menonton",
                "sosmed": "@josuapanggabean_",
                "kesan" : "Sangat baik, informatif dalam menerangkan suatu permasalahan",  
                "pesan" : "Tetap jaga kesehatan bang dan semoga urusannya baik di akademik maupun non akademik dapat berjalan dengan lancar"
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
                "kesan" : "Sangat informatif dalam menjelaskan departemen SSD dan banyak memberi motivasi melalui kegiatan yang telah dilakukan ",  
                "pesan" : "Semangat bang dalam menjalani perkuliahan dan jangan lupa jaga kesehatan bang "
            },
            {
                "nama"  : "Adisty Syawalda Ariyanto",
                "nim"   : "121450136",
                "umur"  : "22",
                "asal"  : "Metro",
                "alamat": "Sukarame ",
                "hobbi" : "Nonton Film",
                "sosmed": "@adistysa_",
                "kesan" : "Informatif dalam menjelaskan sesuatu",  
                "pesan" : "Semoga segala urusannya baik di dalam maupun di luar perkuliahan tetap lancar kak"
            },
            {
                "nama"  : "Nabila Azhari",
                "nim"   : "121450029",
                "umur"  : "21",
                "asal"  : "Simalungun",
                "alamat": "Airan ",
                "hobbi" : "Menghitung Uang",
                "sosmed": "@zhjung",
                "kesan" : "Sangat baik dan ramah",  
                "pesan" : "Semangat kak dalam menjalani harinya, semoga segala urusannya diperlancar"
            },
            {
                "nama"  : "Danang Hilal Kurniawan",
                "nim"   : "122450085",
                "umur"  : "21",
                "asal"  : "Bandar Lampung",
                "alamat": "Airan",
                "hobbi" : "Belajar",
                "sosmed": "@dananghk_",
                "kesan" : "Sangat informatif dalam menerangkan dan menginspirasi melalui pengalaman yang telah dilakukan",  
                "pesan" : "Tetap semangat dan semoga selalu dilancarkan semua urusannya bang"
            },
            {
                "nama"  : "Farrel Julio Akbar",
                "nim"   : "122450110",
                "umur"  : "20",
                "asal"  : "Bogor",
                "alamat": "Lapas",
                "hobbi" : "Kayang",
                "sosmed": "@farel_julio",
                "kesan" : "Sangat baik dan informatif ketika menjelaskan sesuatu",  
                "pesan" : "Tetap semangat bang dalam menjalani perkuliahannya dan semoga dipermudah"
            },
            {
                "nama"  : "Nabilah Andika Fitriati",
                "nim"   : "121450139",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Kedaton",
                "hobbi" : "Tidur",
                "sosmed": "@nabilahanftr",
                "kesan" : "Sangat baik hati dan ramah",  
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
                "pesan" : "Tetap jaga kesehatan dan semangat terus kak dalam menjalani perkuliahannya"
            },
            {
                "nama"  : "Dhafin Razaqa Luthfi",
                "nim"   : "122450133",
                "umur"  : "20",
                "asal"  : "Bandar Lampung",
                "alamat": "Bandar Lampung",
                "hobbi" : "Olahraga",
                "sosmed": "@dhafinrzqa13",
                "kesan" : "Baik hati",  
                "pesan" : "Jangan lupa untuk tetap semangat dalam menjalani dunia perkuliahan bang, semoga segala kegiatannya diperlancar"
            },
            {
                "nama"  : "Elia Meylani Simanjuntak",
                "nim"   : "122450026",
                "umur"  : "20",
                "asal"  : "Bekasi",
                "alamat": "Korpri",
                "hobbi" : "Main Alat Musik",
                "sosmed": "@meylanielia",
                "kesan" : "Sangat baik dan ramah",  
                "pesan" : "Semangat kak dalam menjalani hari-harinya dan jangan lupa jaga kesehatan kak"
            },
        ]
        display_images_with_data(gambar_urls, data_list)
    ssd()    
# Tambahkan menu lainnya sesuai kebutuhan
