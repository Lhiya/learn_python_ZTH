print(" ----- Selamat Datang Di Kei Laundry -----")
print("Daftar Harga per Kilogram")
print("1. Cuci Lipat : Rp. 4000")
print('2. Setrika : Rp. 4000')
print("3. Cuci Setrika : Rp. 8000")
print("Pilih Jenis Laundry")

angka = int(input("Masukkan pilihan angka  : "))
berat_kilo = float(input("masukkan berat/kilo : "))

if angka == 1:
    harga = 4000
elif angka == 2:
    harga = 4000
elif angka == 3:
    harga = 8000


total_harga = harga*berat_kilo
print(f"Total Tagihan {total_harga}")