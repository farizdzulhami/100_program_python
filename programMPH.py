print('='*25)
print('PROGRAM KONVERSI MPH')
print('='*25)

mph = float(input('Masukkan Kecepatan Mil Per Jam: '))
ms = mph / 2.23694
kmj = mph * 1.60934
fts = mph * 1.46667
kt = mph * 0.868976

print('Hasil Konversi:')
print(ms, 'm/s')
print(kmj, 'km/jam')
print(fts, 'ft/s')
print(kt, 'kt')