import queue

# Inisialisasi antrian
antrian = queue.Queue()

# Fungsi untuk menambah orang ke antrian
def tambah_antrian(nama):
    antrian.put(nama)
    print(f"{nama} telah ditambahkan ke dalam antrian.")

# Fungsi untuk memproses orang dari antrian
def proses_antrian():
    if not antrian.empty():
        nama = antrian.get()
        print(f"{nama} sedang diproses.")
    else:
        print("Tidak ada orang dalam antrian.")

# Fungsi untuk menampilkan orang dalam antrian
def tampilkan_antrian():
    if antrian.empty():
        print("Antrian kosong.")
    else:
        print("Orang-orang yang sedang menunggu dalam antrian:")
        # Menampilkan isi antrian tanpa mengubah urutannya
        for i in list(antrian.queue):
            print(i)

# Menu utama
while True:
    print("\n=== Sistem Antrian Rumah Sakit ===")
    print("1. Tambah orang ke antrian")
    print("2. Proses orang dari antrian")
    print("3. Tampilkan orang yang sedang menunggu")
    print("4. Keluar")
    
    pilihan = input("Masukkan pilihan: ")

    if pilihan == '1':
        nama = input("Masukkan nama pasien: ")
        tambah_antrian(nama)
    elif pilihan == '2':
        proses_antrian()
    elif pilihan == '3':
        tampilkan_antrian()
    elif pilihan == '4':
        print("Terima kasih telah menggunakan sistem antrian!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

    import queue

# Inisialisasi antrian
antrian = queue.Queue()

# Fungsi untuk menambah orang ke antrian (bisa beberapa nama sekaligus)
def tambah_antrian(nama_nama):
    nama_list = [nama.strip() for nama in nama_nama.split(',')]
    for nama in nama_list:
        antrian.put(nama)
        print(f"{nama} telah ditambahkan ke dalam antrian.")

# Fungsi untuk memproses orang dari antrian
def proses_antrian():
    if not antrian.empty():
        nama = antrian.get()
        print(f"{nama} sedang diproses.")
    else:
        print("Tidak ada orang dalam antrian.")

# Fungsi untuk menampilkan orang dalam antrian
def tampilkan_antrian():
    if antrian.empty():
        print("Antrian kosong.")
    else:
        print("Orang-orang yang sedang menunggu dalam antrian:")
        # Menampilkan isi antrian tanpa mengubah urutannya
        for i in list(antrian.queue):
            print(i)

# Menu utama
while True:
    print("\n=== Sistem Antrian Rumah Sakit ===")
    print("1. Tambah orang ke antrian (pisahkan nama dengan koma)")
    print("2. Proses orang dari antrian")
    print("3. Tampilkan orang yang sedang menunggu")
    print("4. Keluar")
    
    pilihan = input("Masukkan pilihan: ")

    if pilihan == '1':
        nama_nama = input("Masukkan nama pasien (pisahkan dengan koma jika lebih dari satu): ")
        tambah_antrian(nama_nama)
    elif pilihan == '2':
        proses_antrian()
    elif pilihan == '3':
        tampilkan_antrian()
    elif pilihan == '4':
        print("Terima kasih telah menggunakan sistem antrian!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")