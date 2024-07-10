from collections import deque

# Inisialisasi antrean
antrean = deque()

def tambah_antreanpesanan():
    nama_pesanan = input("Masukkan nama pesanan: ")
    antrean.append(nama_pesanan)
    print(f"Pesanan {nama_pesanan} telah ditambahkan ke antrean.")

def hapus_pesanan_depan():
    antrean.pop()
    print("Antrean telah dihapus.")

while True:
    print("\nMenu:")
    print("1. Tambah Antrean")
    print("2. hapus pesanan")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_antreanpesanan()
    elif pilihan == "2":
        hapus_pesanan_depan()
    elif pilihan == "3":
        break
    