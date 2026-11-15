
print('===== Simulasi Tabungan Liburan =====')

lama_menabung = int(input('Berapa hari anda menabung?: '))
berapa_uang = int(input('Berapa uang yang ingin anda tabung per sesinya?: '))
total_uang = 0

print('\n===== Mulai menabung =====')

for hari in range(1, lama_menabung + 1):
    print('\n[ Hari ke-', hari, ']')
    if hari == 3:
        print('Hari ke', hari, 'di skip dulu buat bensin')
        continue
    for sesi in range(1,4):
        if sesi == 3:
            print('Anda terlalu banyak menabung dihari ini')
            break
        print('Sesi ke-', sesi, 'Anda menabung sebanyak', berapa_uang)
        total_uang += berapa_uang


else:
    print('\nStatus: Misi menabung selama', lama_menabung, 'hari telah tuntas')

print('\n===== Hasil tabungan =====')

if total_uang >= 200000:
    print('Uang anda Rp', total_uang, '-Keren! bisa dipakai liburan keluar kota.')
elif total_uang >= 50000:
    print('Uang anda Rp', total_uang, '-Lumayan! bisa dipakai jalan jalan didalam kota..')
else:
    print('Uang anda Rp', total_uang, '-Uang belum banyak, jajan disekitar rumah saja.')
