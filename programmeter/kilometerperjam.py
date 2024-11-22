print('='*25)
print('PROGRAM KONVERSI KM/JAM')
print('='*25)

kmj = float(input('Masukkan Kecepatan Kilometer Per Jam: '))
ms = kmj / 3.6
mph = kmj * 0.621371
fts = kmj * 0.911344
kt = kmj * 0.539957

print('Hasil Konversi:')
print(ms, 'm/s')
print(mph, 'mph')
print(fts, 'ft/s')
print(kt, 'kt')