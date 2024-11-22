print('='*25)
print('PROGRAM KONVERSI GRAM')
print('='*25)

g = float(input('Masukkan Massa Gram: '))
kg = g / 1000
t = g / 1000000
lb = g / 453.592
oz = g / 28.3495

print('Hasil Konversi:')
print(kg, 'Kilogram')
print(t, 'Ton')
print(lb, 'Pound')
print(oz, 'Ounce')