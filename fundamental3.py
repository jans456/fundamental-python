print('Tipe data skalar => tipe data sederhana')
anak1='janji'
anak2='fita'
anak3='uler'
anak4='tikus'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

print('\ntipe data list/daftar/array')
anak = ['janji', 'fita', 'uler', 'tikus']
print(anak)
anak.append('Limo')
print(anak)

print('\nsapa anak ke 2')
print(f"{anak[1]}")

print('\nsapa semua anak')
for a in anak:
    print(f'hai {a}!')

print ('\nsapa semua anak: cara ribet' )
for a in range(0, len(anak)):   
    print(f'{a+1}. hai {anak[a]}')






