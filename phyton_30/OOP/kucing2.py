class Kucing:
    nama = None
    ekor = None
    warna_bulu = None
    suara = None
    warna_mata = None
    umur = None
    self_umur = 'u'
    total_makan = 0

    def __init__(self, nma, ekr, w_mata, w_bulu, umur):
        self.nama = nma
        self.ekor = ekr
        self.warna_bulu = w_bulu
        self.warna_mata = w_mata
        self.umur = umur

    def get_nama(self):
        print(self.nama)

    def deskripsi(self):
        print(f"Kucing bernama {self.nama} dengan warna mata {self.warna_mata} berumur {self.umur}")

    def bersuara(self):#method/berhaviour
        print("meoww")

    def makan(self):
        print(f"{self.nama} sedang makan")
        self.total_makan+=1
    
    def bermain(self):
        print("Kucing sedang bermain")

    def tidur(self):
        print("Kucing sedang tidur")

    def tambah_umur(self):
        self_umur = self.umur+1
        print("umur Omar bertambah 1 tahun")
    
    def makan_perhari(self):
        print(f"hari ini {self.nama} makan sebanyak {self.total_makan} kali")
    
#instanciate/mencetak
k1 = Kucing("eko", "panjang", "biru", "putih", "1 tahun")
k1.deskripsi()
k1.get_nama()
k1.makan()
k1.bermain()
k1.makan_perhari()
k1.makan()
k1.bermain()
k1.makan_perhari()


