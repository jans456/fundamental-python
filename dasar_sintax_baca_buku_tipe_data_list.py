daftar_buku = ['Seven Habits', 'How to Influence People', 'First Thing First', '4XD']
print('tampilkan variable daftar buku')
print(daftar_buku)

print('\nProses Semua Dengan for in')
for a in daftar_buku:
  print(f'buku {a}')

print('\ntampilakan isi daftar_buku pada indeks tertentu\n')
print(daftar_buku[0])
print(f'{daftar_buku[1]}')
print(f'{daftar_buku[0]} dan {daftar_buku[2]}')

print('\nTampilkan dengan for in range')
for i in range(0, len(daftar_buku)):
  print(daftar_buku[i])


daftar_buku = [1, 'Kenji Volume 2', -313,3.14]
print('\nTampilkan dengan for in range, dimana tipe data tiap tipe elemen berbeda')
for i in range(0, len(daftar_buku)):
  print(daftar_buku[i])

print('\nkembali nilai awal daftar_buku')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Thing First', '4XD']
print(daftar_buku)
print('\n tambahkan 1 buku baru')
daftar_buku.append('My heart')
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])


print('\n.clear List')
daftar_buku.clear()
for i in range (0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nmengganti element pertama")
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Thing First', '4XD']
daftar_buku[1]= 'Edight Habits'
for i in range(0, len(daftar_buku)):
   print(daftar_buku[i])

print("\nambil elemen ke 4")
buku =daftar_buku.pop(3)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nBuku yang diambil tadi')
print(buku)

print("\nPOP")
daftar_buku.pop()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])


print("\nPOP -1")
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Thing First', '4XD']
daftar_buku.pop(-4)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Thing First', '4XD']
del daftar_buku[0]
for i in range(0, len(daftar_buku)):
   print(daftar_buku[i])

print("\nPerintah del edngan list Comprehension")
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Thing First', '4XD']
del daftar_buku[0:-1] #fungsi start:END (jumlah) jika diganti petik : hilang semu, 
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nPerintah del edngan list Comprehension")
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Thing First', '4XD']
del daftar_buku[0::2] #fungsi start:end:step
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print("\nmembuat list baru")
daftar_buku = ['Seven Habits', 'How to Influence People', 'First Thing First', '4XD']
daftar_buku_baru = daftar_buku[:]
for i in range(0, len(daftar_buku)):
   print(daftar_buku[i])

print('\nmembuat list baru')
del daftar_buku[:]
for i in range(0, len(daftar_buku_baru)):
   print(daftar_buku_baru[i])

print("\nmembuat list baru dengan comprehension : ganjil")
daftar_buku = ['1 Seven Habits', '2 How to Influence People', '3 First Thing First', '4 4XD']
daftar_buku_baru =daftar_buku[0::2]
for i in range(0, len(daftar_buku_baru)):
   print(daftar_buku_baru[i])

print("\nmembuat list baru dengan comprehension : genap")
daftar_buku = ['1 Seven Habits', '2 How to Influence People', '3 First Thing First', '4 4XD']
daftar_buku_baru =daftar_buku[1::2]
for i in range(0, len(daftar_buku_baru)):
   print(daftar_buku_baru[i])

print("\nmembuat list baru dengan comprehension : buang diujung")
daftar_buku = ['1 Seven Habits', '2 How to Influence People', '3 First Thing First', '4 4XD']
daftar_buku_baru =daftar_buku[0:-1:2]
for i in range(0, len(daftar_buku_baru)):
   print(daftar_buku_baru[i])

print("\nmembuat list baru dengan comprehension : ganjil simpel")
daftar_buku = ['1 Seven Habits', '2 How to Influence People', '3 First Thing First', '4 4XD']
print(daftar_buku[0::2])









