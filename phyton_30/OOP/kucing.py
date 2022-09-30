class Kucing:
    nama = None
    ekor = None
    warna_bulu = None
    suara = None
    warna_mata = None
    umur = None

    def bersuara(self):#method/berhaviour
        print("meoww")

    def makan(self):
        print("Kucing sedang makan")
    
    def bermain(self):
        print("Kucing sedang bermain")

    def tidur(self):
        print("Kucing sedang tidur")

#instanciate/mencetak
k1 = Kucing()
k2 = Kucing()

print(type(k1))

#memberikan atribut / properti
k1.nama = "Kitty"
k1. warna_mata = "biru"
k1.warna_bulu = "putih"
k1.ekor ="panjang"
k1.umur="Bulan"
k2.nama = "Omaar"
k2.warna_bulu = "Hitam"
k2.warna_mata = "hijau"
k2.ekor="pendek"
k2.umur = "Bulan"

#mengakases atribut
print(k1.nama)
print(k2.nama)
print(k2.warna_bulu)

#mengakses method
k1.bersuara()
k1.makan()
k1.bermain()
k2.bersuara()
k2.makan()
k2.bermain()

#modelkan object lain di dunia nyata
class Tas:
    model = None
    warna = None
    merk = None
    ukuran = None
    jenis_lapisan =None

    def manfaat():
        print("untuk mengbawa barang pribadi")

    def appearance():
        print("Tas terlihat cantik dan lucu")


ts1 = Tas

ts1.model = "Backpack"
ts1.warna = "Pink"
ts1.merk = "Guess"
ts1.ukuran = "sedang"
ts1.jenis_lapisan = "PVC"

print(ts1.model)
print(ts1.warna)
print(ts1.merk)
print(ts1.ukuran)
ts1.manfaat()
ts1.appearance()



