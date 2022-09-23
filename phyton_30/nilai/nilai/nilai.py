nilai = int(input("masukan Nilai : "))

if nilai >=90 and nilai <= 100:
    print("Grade A")
    #jalankan line ini jika line 3 adalah True
elif nilai >= 80 and nilai <= 89:
    print("Grade B")
elif nilai >= 70 and nilai <= 79:
    print("Grade c")
elif nilai >= 60 and nilai <= 69:
    print("Grade D")
elif nilai >= 0 and nilai <= 59:
    print("Grade E")
    print("Gagal")
    print("Ulangi lagi Tahun Depan")
else:
    print("Nilai yang anda masukkan salah")