class Mamalia:
    alat_pernafasan = "paru-paru"
    bertulang_belakang = True
    melahirkan = True

    def menyusui(self):
        print("Hewan ini bisa menyusui")
    
    def melahirkan(self):
        print("Hewan ini bisa melahirkan")

class Sapi(Mamalia):
    ekor = None
    kelenjar_susu = True
    jenis_makanan = 'rumput'
    warna_kulit = None
    jenis_sapi = None
    berat = 0

    #def __init__(self, ekr, kjr_susu, J_makan, W_klt, j_sapi) 
        
    def memproduksi(self):
        print("Hewan ini memproduksi susu")

    def makan(self):
        print("Hewan ini makan setiap hari")

    def tidur(self):
        print("Hewan ini tidur dikandang")

class Kuda(Mamalia):
    jenis_kuda = None
    kelenjar_susu = True
    jenis_makan = 'rumput'
    warna_kulit = None
    berat = 0

    def berlari(self):
        print("Kuda berlari sangat kencang")

    def melahirkan(self):
        print("Hewan ini melahirkan anak")
    
    s1 = Sapi()
    s1.jenis_sapi = "limosin"
    s1.warna_kulit = "coklat"

    print(s1.jenis_sapi)
    s1.menyusui()


class Mobil:
    bahan_bakar = None
    kecepatan = None
    merk = None
    jenis = None
    
    def berlari(self):
        print("Mobil ini berlari dengan kecepatan sekian km")

    def model(self):
        print("Mobil mempunyai banyak model")

class Hatch(Mobil):
    model = "mini"
    tempat_duduk = "2 kursi"
    bahan_bakar = None
    warna = None

    def lari(self):
        print("Mobil Hatch berlari dengan kecepatan normal")

    def tampilan(self):
        print("mobil ini tampilannya mini and simple")

    def kegunaan(self):
        print("Mobil ini sangat bagus digunakan untuk tempat parkir yang tidak luas")

h1 = Hatch()
h1.warna = "merah"
h1.bahan_bakar="Pertamax"
print(h1.warna)
h1.berlari()
