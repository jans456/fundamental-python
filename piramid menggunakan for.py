
#tinggi = 5
tinggi = int(input('mau berapa tinggi : '))

#piramid
print()
for a in range(tinggi):
    for b in range(tinggi-a):
        print(' ',end='')

    for c in range(a+1):
       print('- ',end='')
    print()

#piramid terbalik
print()
for d in range(tinggi):
    for e in range(d+1):
        print(' ',end= '')
    for f in range(tinggi-d):
        print('* ', end= '')
    print()
 

#keluar menurun 5
# tinggi_l = 5
# print()
# for a in range(tinggi_l):
#     for b in range(a):
#         print(' -',end= '')




    
    
  