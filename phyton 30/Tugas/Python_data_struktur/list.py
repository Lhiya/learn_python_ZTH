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
kaset_paling_baru = "Percy Jackson"
anime[0] = kaset_paling_baru
print(f"Jadwal Movie Terbaru 2 : {anime}")

