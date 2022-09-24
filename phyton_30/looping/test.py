pasword_kartu_atm = 123456
cek = 0
while cek<3:
    pin = int(input("Masukkan Pin KArtu ATM anda"))
    if pasword_kartu_atm == pin:
        print("Silahkan masuk ke menu selanjutnya")
        break
    else:
        ("Password yang anda masukkan salah")

print(" Total ulang : {cek}")