nama = input("masukan nama siswa : ")
kehadiran = input("masukan jumlah kehadiran siswa : ") 
kehadiran = int(kehadiran)

if kehadiran >= 10:
    print("lulus")
elif kehadiran >= 8:
    print("peringatan")
else:
    print("Gagal")
