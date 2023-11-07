# perulangan membaca buku dengan while sampai paham


book_count = 10
print('ibu "berkata baca" bukumu')
read__count=0

understood_count = 0
print(f"jumlah buku yang sudah dibaca dan dipahami{understood_count}\n")

while read__count < book_count * 2:
    read__count = read__count+ 1
    if understood_count == 9:
        print(f"Buku ke {understood_count+1} belum paham")
    else:
        understood_count = understood_count + 1
        print(f"buku ke {understood_count} sudah dibaca dan sudah dipahami")
    
print(f'jumlah buku yang sudah dibaca dan dipahami{understood_count}')
if understood_count == book_count :
    print('"Bu, Semua buku sudah dipahami"\n')
else:
    print(f'\n"Bu tidak semua buku bisa dipahami." budi hanya bisa memahami {understood_count}buku')

book_count = 'banyak'
print(book_count)



