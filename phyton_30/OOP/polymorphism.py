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

    def luas(self):
        luas = 1/2*self.alas*self.tinggi
        return luas

class Persegipanjang():
    panjang =None
    lebar = None

    def luas(self):
        luas = self.panjang*self.lebar
        return luas
