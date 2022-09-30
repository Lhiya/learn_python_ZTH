def penjumlahan(x, y):
    total = x+y
    if total > 100:
        print("benar")
    else:
        print("kurang banyak")
    return total

def coba(*args):
    print(type(args))
    print(args[-1])
    total= 2 + args[-1][-1]
    print(total)

coba("hallo", 1.3, 2, 14, [1, 2, 3, 4])


def coba2(**kwargs):
    print(kwargs)
    print(kwargs['nama3'])

coba2(nama="afif", nama2="Desi", nama3="lia")

