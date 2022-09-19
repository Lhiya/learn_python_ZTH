#harga_item1 = 15000
#harga_item2 = 20000
#harga_item3 = 30000
#harga_item4 = 40000
#harga_item5 = 14000
#total = harga_item1+harga_item2+harga_item3+harga_item4+harga_item5
#Total_bayar = total - (10/100)

print("------ La Tansa Supermarket _______")
#print("harga total belanja")
harga_total = input("masukan jumlah harga total belanja ")
harga_total = int(harga_total)

print("total belanja:", harga_total)
if harga_total >=100000:
    print(f"Total Belanja:" , harga_total-(10/100*harga_total))
else:
    print(f"Total Belanja:", harga_total)




