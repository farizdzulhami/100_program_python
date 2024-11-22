print('='*30)
print('PROGRAM KONVERSI KILOGRAM')
print('='*30)

kg = float(input('Masukkan Massa Kilogram: '))
g = kg * 1000
t = kg / 1000
lb = kg * 2.20462
oz = kg * 35.274

print('Hasil Konversi:')
print(g, 'Gram')
print(t, 'Ton')
print(lb, 'Pound')
print(oz, 'Ounce')