#chaining (rantai)
class Warteg():
    def __init__(self) -> None:
        self.total = 0
        self.item = []

    def nasi(self):
        self.item.append("Nasi 1 Porsi")
        self.total = self.total+1000
        return self
    
    def bakwan(self):
        self.item.append("Bakwan 1 Biji")
        self.total = self.total+2500
        return self

    def kangkung(self):
        self.item.append("Sayur Kangkung")
        self.total = self.total+2500
        return self

    def ayam_krispi(self):
        self.item.append("Ayam krispi")
        self.total = self.total+8500
        return self

    def krupuk_udang(self):
        self.item.append("Krupuk Udang")
        self.total = self.total+2500
        return self

    def bayar(self):
        print(f"item : {self.item}")
        print(f"tagihan : {self.total}")
        return self

#cara normal
#mas_mas = Warteg() #instance
#mas_mas.nasi()
#mas_mas.ayam_krispi()
#mas_mas.bayar()

mas_mas1 = Warteg().nasi().bakwan().kangkung().ayam_krispi().krupuk_udang().bayar()
