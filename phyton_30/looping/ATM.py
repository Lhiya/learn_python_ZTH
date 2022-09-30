

pasword_kartu_atm = 123456
cek = 0
loop = True
while loop:
    if cek < 3:
        pin = int(input("Masukkan Pin Kartu ATM anda "))
        if pasword_kartu_atm == pin:
             print("Silahkan masuk ke menu selanjutnya")
             break
        else:
             print("Password yang anda masukkan salah")
             coba_lagi=input("Coba lagi? ya/tidak ")
             if coba_lagi == "ya":
                cek+=1
             else:
                 print("Terima Kasih")
                 loop=False
    else:
        print("Kartu anda tertelan")
        loop=False
            
        
        
    
    
