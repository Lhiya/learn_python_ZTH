#lakukan looping untuk mengetahui total pada variable harga
harga =[3000, 400, 34500, 10000]
r = 0

for i in harga:
    r += i
    
print(r)
("\n")

print("-- Selamat Datang di Supermarket La Tansa Lillah --")
barang = {
        "item":{
            "nama1": "Tomat 1 bungkus",
            "nama2": " Ayam 1 kg",
            "nama3": "Kentang 1 kg",
            "nama4": "Cabai 1/4 kg",
            "nama5": "Wortel 1 bungkus"
        }
        }

list_belanja = []
list_harga = []
i = 0

cek = True
while cek:
    print(" ---- Pilih Barang ----")
    print()
    print("1. Tomat 1 bungkus : Rp. 5000")
    print("2. Ayam 1 kg : Rp. 45000")
    print("3. Kentang 1 kg : Rp. 35000")
    print("4. Cabai 1/4 kg : Rp. 25000")
    print("5. Wortel 1 bungkus : Rp. 7000")
    print()

    print("Mau beli apa? ")
    angka = int(input("masukkan angka : "))
    tanya = str(input("ada lagi? ya/tidak : "))
    print()

    if angka == 1:
        list_belanja.append('Tomat 1 kg')
    elif angka == 2:
        list_belanja.append('Ayam 1 kg')
    elif angka == 3:
        list_belanja.append('Kentang 1 kg')
    elif angka == 4:
        list_belanja.append('Cabai 1/4 kg')
    elif angka == 5:
        list_belanja.append('Wortel 1 bungkus')
    else:
        False

    if angka == 1:
        list_harga.append(5000)
    elif angka == 2:
        list_harga.append(45000)
    elif angka == 3:
        list_harga.append(35000)
    elif angka == 4:
        list_harga.append(25000)
    elif angka == 5:
        list_harga.append(7000)
    else:
        False


    if tanya == 'ya':
        cek = True
    else:
        cek = False


for r in list_harga:
    i += r

print()
print(f"List Belanja :  {list_belanja} ")
print(f"list harga : {list_harga}")
print(f"Total Tagihan : {i}")



