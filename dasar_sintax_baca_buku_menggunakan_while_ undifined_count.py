# perulangan membaca buku dengan while sampai paham

jumlah_baca=0
jumlah_buku = 10
jumlah_paham = 0
print('ibu "berkata baca" bukumu')


print(f"jumlah buku yang sudah dibaca dan dipahami{jumlah_paham}\n")

while jumlah_baca < jumlah_buku * 2:
    jumlah_baca = jumlah_baca+ 1
    if jumlah_paham == 9:
        print(f"Buku ke {jumlah_paham+1} belum paham")
    else:
        jumlah_paham = jumlah_paham + 1
        print(f"buku ke {jumlah_paham} sudah dibaca dan sudah dipahami")
    
print(f'jumlah buku yang sudah dibaca dan dipahami{jumlah_paham}')
if jumlah_paham == jumlah_buku :
    print('"Bu, Semua buku sudah dipahami"\n')
else:
    print(f'\n"Bu tidak semua buku bisa dipahami." budi hanya bisa memahami {jumlah_paham}buku')



