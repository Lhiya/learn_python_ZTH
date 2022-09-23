
#password = ['kopinikmatnyamandilambung', 'asikasikjos']
permintaan_security1 = "kopinikmatnyamandilambung"
permintaan_security2 = 'asikasikjos'

password = str(input("Silahkan Masukkan Password : " ))


for x in range(len(password)):
        if permintaan_security1 == password:
                print(f"--Silahkan masuk ke kost sultan--")
                break
        elif permintaan_security2 == password:
                print(f"--Silahkan masuk ke kost sultan--")
                break
        else:
                print(f"Anda Tidak diperbolehkan masuk")
                break


