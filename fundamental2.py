# tipe data dictionary sekedar menghubungkan antara KEY dan Value
# KVP = key Value Pair 
# Dictionary = kamus
kamus_ind_eng = {'anak': 'son', 'istri' : 'wive', 'ayah' : 'father', 'ibu' : 'Mother'}

print(kamus_ind_eng)
print(kamus_ind_eng['ayah'])
print(kamus_ind_eng['anak'], kamus_ind_eng['ibu'])


print('\nData ini dikirim oleh server Gojek memberikan info driver si sekolah ')
data_dari_server_gojek ={
    'tanggal' : '2020-06-10',
    'driver_list' : [
        {'nama': 'janji', 'jarak': 10}, #0
        {'nama': 'fita', 'jarak' : 30}, #1
        {'nama': 'uler', 'jarak' : 100}, #2
        {'nama': 'tikus', 'jarak' : 1000} #3
    ]
}
print(data_dari_server_gojek)
print(f"\nDriver sekitar sini{data_dari_server_gojek['driver_list']}")
print(f"Driver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"Driver #4 {data_dari_server_gojek['driver_list'][3]}")
print(f"Driver terdekat berjarak {data_dari_server_gojek['driver_list'][0]['jarak']} meter")