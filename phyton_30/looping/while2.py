jawab = "iya"
hitung = 0

while (jawab=="iya"):
    #di dalam while
    hitung+=1
    jawab = input("ulangi lagi ? iya/ tidak : ")

#diluar while
print(f"Total Perulangan : {hitung}")
