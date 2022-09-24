kputra = []
kputri = []

cek = True
while cek:
    print("-- Formulir Pendaftaran Kos-kosan pak erte--")
    nama = input("Masukkan nama : ")
    gender = input("jenis kelamin p/l : ")
    print("")
    tanya = input("isi formulir lagi? ya/tidak : ")

    if gender == 'l':
        kputra.append(nama)
    else:
        kputri.append(nama)
    if tanya == 'ya':
        cek = True
    else:
        cek = False

    print()
    print(f"List Kost Putra {kputra} ")
    print(f"List Kost Putri {kputri} ")


