print('='*25)
print('PROGRAM KONVERSI POUND')
print('='*25)

lb = float(input('Masukkan Massa Pound: '))
g = lb * 453.592
kg = lb * 0.453592
t = lb / 2204.62
oz = t * 16

print('Hasil Konversi:')
print(g, 'Gram')
print(kg, 'Kilogram')
print(t, 'Ton')
print(oz, 'Ounce')