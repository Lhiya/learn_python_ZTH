#overriding class mamalia
class Mamalia():
    def deskripsi(self):
        print("ini adalah hewan mamalia")

class Sapi(Mamalia):
    def deskripsi(self):
        print("ini adalah hewan sapi")

#m1 = Mamalia()
#m1.deskripsi()

s1 = Sapi()
s1.deskripsi()


