#buat class yang mempunyai chaining method
class Laundry():
    def __init__(self) -> None:
        self.total = 0
        self.item = []

    def cuci(self):
        self.item.append("cuci 1 kilo")
        self.total = self.total+2000
        return self

    def setrika(self):
        self.item.append("Setrika 1 kilo")
        self.total = self.total+2000
        return self

    def cuci_setrika(self):
        self.item.append("Cuci Setrika 1 kilo")
        self.total = self.total+4000
        return self

    def cuci_sepatu(self):
        self.item.append("Sepatu 1 pasang")
        self.total = self.total+25000
        return self

    def bayar(self):
        print(f"Item : {self.item}")
        print(f" Total Tagihan : {self.total}")
        return self


pelanggan = Laundry()
pelanggan.setrika()
pelanggan.cuci()
pelanggan.cuci_setrika()
pelanggan.bayar()

pelanggan1 =Laundry().setrika().cuci().cuci_setrika().cuci_sepatu().bayar()




