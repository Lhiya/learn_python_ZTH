print(" ----- Selamat Datang Di SPBU -----")
print("1. Pertamax : Rp. 15000")
print('2. Pertamax Turbo : Rp. 17000')
print("3. Pertamax Plus : Rp. 16000")
print("4. Pertalite : 12000")
print("5. Pertamina Dex : Rp. 13000")
print("6. Dexlite : Rp. 10000")
print("7. Solar : Rp. 8000")
print("Pilih Bahan Bakar")

angka = int(input("masukan angka : "))
total_bahan_bakar = float(input("Masukan total bahan bakar : "))

if angka == 1:
    harga = 15000
elif angka == 2:
    harga = 17000
elif angka == 3:
    harga = 16000
elif angka == 4:
    harga = 12000
elif angka == 5:
    harga = 13000
elif angka == 6:
    harga = 10000
elif angka == 7:
    harga = 8000

total_harga = harga*total_bahan_bakar
print(f"Total Tagihan {total_harga}")