class Kucing:
    nama = None
    ekor = None
    warna_bulu = None
    suara = None
    warna_mata = None
    umur = None

    def get_nama(self):
        print(self.nama)

    def deskripsi(self):
        print(f"Kucing bernama {self.nama} dengan warna mata {self.warna_mata} berumur {self.umur}")
    def bersuara(self):#method/berhaviour
        print("meoww")

    def makan(self):
        print("Kucing sedang makan")
    
    def bermain(self):
        print("Kucing sedang bermain")

    def tidur(self):
        print("Kucing sedang tidur")

    def tambah_umur(self):
        self_umur = self.umur+1
        print("umur Omar bertambah 1 tahun")

#instanciate/mencetak
k1 = Kucing()
k2 = Kucing()

print(type(k1))

#memberikan atribut / properti
k1.nama = "Kitty"
k1. warna_mata = "biru"
k1.warna_bulu = "putih"
k1.ekor ="panjang"
k1.umur= 5
k2.nama = "Omaar"
k2.warna_bulu = "Hitam"
k2.warna_mata = "hijau"
k2.ekor="pendek"
k2.umur = 6 

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

#k2.get_nama()
k2.deskripsi()
k2.tambah_umur()
k2.deskripsi()


