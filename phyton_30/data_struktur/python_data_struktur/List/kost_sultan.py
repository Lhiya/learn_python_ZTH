
kuncai = ['kopinikmatnyamandilambung', 'asikasikjos']

print("---- Selamat Datang Di Kost Sultan -----")

password = str(input("Silahkan Masukkan Password : " ))

lock = True

for k in kuncai:
        if k == password:
                lock = False
        else:
                lock = True

if lock == False:
        print("password yang anda masukkan benar")
        print("Silahkan Masuk")
else:
        print("Password yang anda masukkan salah")
        print("Anda tidak diperbolehkan masuk")



