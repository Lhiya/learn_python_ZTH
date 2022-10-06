#silahkan membuat objek lain menggunakan init
class Kelinci:
    nama = None
    ekor = None
    warna_bulu = None
    telinga = None
    total_makan = 0

    def __init__(self, nma, ekr, w_bulu, telinga):
        self.nama = nma
        self.ekor = ekr
        self.warna_bulu = w_bulu
        self.telinga = telinga
        

    def get_nama(self):
        print(self.nama)

    def deskripsi(self):
        print(f"Kelinci bernama {self.nama} dengan warna mata {self.warna_mata} berumur {self.umur}")

    def makan(self):
        print(f"{self.nama} sedang makan")
        self.total_makan+=1
    
    def bermain(self):
        print(f"{self.nama} sedang bermain")

    def tidur(self):
        print(f"{self.nama} sedang tidur")
 
    def makan_perhari(self):
        if self.total_makan==0:
            print(f"{self.nama} belum makan sama sekali")
        else:
            print(f"hari ini {self.nama} makan sebanyak {self.total_makan} kali")
        

#instanciate/mencetak
k1 = Kelinci("Omar", "pendek", "putih", "panjang")
k2 = Kelinci("Bulik", "panjang", "coklat", "panjang")


k1.makan()
k1.bermain()
k1.makan_perhari()
k2.makan()
k2.bermain()
k2.makan()
k2.makan_perhari()