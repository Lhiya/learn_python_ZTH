#polimorphism
#method yang samma pada class yang berbeda


class Sapi():
    def makan(self):
        print("SApi makan rumput")

class Ayam():
    def makan(self):
        print("Ayam Makan serangga")


class Segitiga():
    alas = None
    tinggi = None

    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
        
    def luas(self):
        luas = 1/2*self.alas*self.tinggi
        return luas

class Persegipanjang():
    panjang =None
    lebar = None

    def luas(self):
        luas = self.panjang*self.lebar
        return luas

s = Segitiga(2,3)
print(s.luas())

#persegi_panjang = Persegipanjang(2,3)
#print(persegi_panjang.luas())




