campur = ["pisang goreng", True, 3.14, "maslia Qomar", 10]
print(f"contoh list : {campur}")

anime = ["Naruto", "Moana", "How to train your dragon", "bos baby", "coco"]
print(f"List Movie : {anime} \n")
print(f"Mengakses data anime pada index ke 2 : {anime[2]}")
print(f"Mengakses data anime pada index ke 2-4 : {anime[2:5]}")
#menampilkan item dari index awal sampai range tertentu
print(f"mengakases item dariindex pertama sampai index ke 3 : {anime[:4]}")
print(f"mengakses item dari index ke 3 sampai index terakhir : {anime[3:]}")
#panjang array / List
print(f"Panjang List : {len(anime)}")

#mengecek apakah sebuah item tersedia dalam sebuah list

if "Moana" in anime:
    print("Tersedia")
else:
    print("Tidak Tersedia")

#Menambah item pada list
new_movie = "avatar 2"
anime.append(new_movie) #method append
print(f"List Movie Terkini : {anime}")

#menambah data dengan menggunakan method insert ()
new_movie2 = "Big Foot"
anime.insert(3,new_movie2)
print(f"Jadwal Movie Terbaru : {anime}")

#Update
#Mengubah item dalam sebuah array
kaset_paling_baru = "Percy Jackson"
anime[0] = kaset_paling_baru
print(f"Jadwal Movie Terbaru 2 : {anime}")

matrik = [[8, 4, 3], [-5, 6, 2], [7, 9, -8]]
print(f"Matrix : {matrik}")
print(f"{matrik[1][2]}")
matrik[1][2] = 1
print(f"Matrix : {matrik}")

#Delete
#Methods --> pop(), remove(), clear()
#1. Menghapus data pada ururtan terakhir --> pop()
anime.pop()
print(f"List movie setelah dihapus menggunakan method pop : {anime}")

#2. Menghapus data pada spesifik item menggunakan methode remove()
anime.remove("bos baby")
print(f"List movie setelah dihapus menggunakan method remove : {anime}")

#anime.clear()
#print(f"List movie setelah dihapus menggunakan method clear : {anime}")

"Method tambahan"
#sort() mengurutkan item
angka = [2, 5, 3, 4, 6, 7, 1, 9]
buah = ['ceri', 'nanas', 'anggur', 'jeruk']
print(f"List Angka : {angka}")
print(f"List Buah : {buah}")
angka.sort()
buah.sort()
print(f"List Angka : {angka} ")
print(f"List Buah : {buah}")

#reverse( )--> membalikkan ururtan item
buah.reverse()
angka.reverse()
print(f"Reverse Buah : {buah}")
print(f"Reverse Angka : {angka}")

#Count() --> Menghitung jumlahitem dalam sebuah array
angka2 = [1, 3, 4, 3, 5, 2, 6]
print(f"Jumlah angka 3 dalam variable Angka : {angka2.count(3)}")

#copy()

angka_copy = angka2.copy()
print(f"angka2 : {angka2}")
print(f"angka_copy : {angka_copy}")

#looping
ii = 0
for ii in range(10):
    print(ii)

for i in range(len(anime)):
    print(anime[i])

for x in range(2):
    print(f"saya tidak akan mengulangi lagi ke {x}")



permintaan_bocil = "Moana"
for i in range(len(anime)):
    if permintaan_bocil == anime[i]:
        print(f"Memberikan Kaset {permintaan_bocil}")
        print(f"Menagih uang 10.000")
        break
    else:
        print("Bukan ini")

#pass and continue --> melewatkan item yang dimaksud
print ()

for x in range(10):
    if x == 3:
        pass
    else:
        print(x)

for x in range(10):
    if x == 3:
        continue
    else:
        print(x)


#setiap kali anak sultan keluar kost2an dan masuk gerbang, satpam meminta password
#passsword yang diperbolehkan
#1 "kopi nikmat nyaman di lambung"
#2. asikasikjos
#maka:
#"pintu dibuka"
#"dipersilahkan masuk"
#jika password salah "anda tidak diperbolehkan masuk"

#mas2 dapat kiriman kaset terbaru
#baru mikir apa kaset yang tidak laku, dicek 
#kalau ada kaset yg tdk laku akan diganti
#kalau tidak ada, oo ternyata sudah ga ada kasetnya


