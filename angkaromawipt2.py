print('\n')
print('='*25)
print('Angka romawi 2')
print('='*25)

romawi = int(input("\nMasukkan bilangan bulat untuk menentukan angka romawi: "))

angka_romawi = ""
nilai_romawi = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I")
]

for nilai, simbol in nilai_romawi:
    while romawi >= nilai:
        angka_romawi += simbol
        romawi -= nilai

print("Angka Romawinya adalah :", angka_romawi, '\n')