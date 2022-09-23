
permintaan_security1 = "kopinikmatnyamandilambung"
permintaan_security2 = 'asikasikjos'

password = str(input("Silahkan Masukkan Password : " ))



if permintaan_security1 == password:
    print(f"--Selamat Datang di Kost Sultan--")
elif permintaan_security2 == password:
    print(f"--Selamat Datang di Kost Sultan--")
else:
    print(f"Anda Tidak diperbolehkan masuk")

print("\n")


print("--- Selamat datang di disc rental WAKANDA ---")
movie = ['the internship', 'salt', 'pride and prejudice', 'transformer 2', 'kungfu panda 1']
print(f"Daftar Disk film yang tersedia : {movie} \n ")
if "salt" in movie:
    print("Ternyata masih ada dan perlu diganti")
else:
    print("Ooooo....Ternyata Kasetnya Udah Enggak Ada")
print("\n")

movie1 = "Black Panther"
movie.append(movie1)
print(f"Daftar Disc Movie Terbaru : {movie} \n")
movie.remove("salt")
print(f"Daftar Disk movie Terkini : {movie} \n")
  