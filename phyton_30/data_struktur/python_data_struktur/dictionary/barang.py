dc3 = {
    'kode': [1, 2, 3],
    'nama': ['pepsodent', 'sabun', 'sapu'],
    'harga': [10000, 15000, 25000]
}

dc4 = {
    'kode': 5,
    'nama': 'Shampo Panteen',
    'harga': 17500
}
dc5 = {
    'kode': 9,
    'nama': 'sabun cuci rinso',
    'harga': 17500
}

print(f"dic 3 {dc3}")
print(f"dic 4 {dc4}")
print(f"dic 5 {dc5}")
dc3['kode'] = 1, 2, 3, 4
dc3['nama']= 'Pepsodent', 'Sabun', 'Sapu', 'Handyplast'
dc3['harga']= 10000, 15000, 25000, 12500
print(f"dic 3 {dc3}")
dc3['kode'].remove(2)
dc3['nama'].remove('Sabun')
dc3['harga'].remove(15000)

print(dc3)



#buatlah sebuah program
#masukkan kata/kalimat =
#jika kata/kalimat bisa dibaca baik dari depan maupun dari belakang,tampilkan output "ini adalah palindrom"
#jika tidak "ini bukan kata/kalimat palindrom"
#cek materi manipulasi string