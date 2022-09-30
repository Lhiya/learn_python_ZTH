#modelkan object lain di dunia nyata
class Tas:
    model = None
    warna = None
    merk = None
    ukuran = None
    jenis_lapisan =None

    def manfaat(self):
        print("untuk membawa barang pribadi")

    def appearance(self):
        print("Tas terlihat cantik dan lucu")


ts1 = Tas()

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
