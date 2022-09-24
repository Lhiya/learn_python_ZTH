motor = {
    "merek": "Vario",
    "plat_motor": 39848903,
    "warna": "Hitam",
    "bpkb": {
        "nomor_bpkb":  9732879840,
        "bahan_bakar": "pertalite" 
    }
}

#mengakses data dari variable motor
print(motor)
print(type[motor])
print(motor["merek"])
print(f"Motor mbak lia mereknya adalah : {motor['merek']}")
print(f"plat nomor : {motor['plat_motor']}")
print(f"bpkb : {motor['bpkb']}")
print(f"mengakses bahan bakar dengan menggunakan metod get : {motor.get('bahan_bakar')}")

#update data
motor['warna'] = "merah"
print(f"Data motor : {motor} \n")

#menambah data
motor['pemilik']="maslia qomar"
print(motor)

warna_buah =dict(jeruk="orange", apel="merah", pisang="kuning")
print(warna_buah)

print(f"warna buah apel {warna_buah['apel']}")

#menghapus data pada dictionary
#menggunakan method pop(), popitem(, del
"pop() --> menggunakan data berdasarkan key"
motor.pop('plat_motor')
print(f"Motor : {motor} \n")

"popitem( --> menghapus data pada ururtan terakhir"
motor.popitem()
print(f"data motor terbaru : {motor}")

"del --> sama seperti pop, yaitu menghapus data"
del motor['bpkb']
print(motor)
print()


#looping
for m in motor.values():
    print(m)
print()

for m, n in motor.items():
    print(m, n)


#lakukan looping untuk mengetahui total pada variable harga
harga =[3000, 400, 34500, 10000]
r = 0
#total_harga = + 'harga'
for i in harga:
    r += i 

print(r)


#print(total_harga)

#def sum():
    #L = list(map(int,input().split(" "))) # Membuat list dari input

    #r = 0 # 'r' for result/hasil jumlah seluruh list items

    #for i in L: # Looping ke setiap list item
        #r += i # jumlahkan tiap list item ke variabel 'r'

    #return r # MENGEMBALIKAN HASIL PENJUMLAHAN SELURUH LIST ITEM


# Eksekusi
#print(sum())


