print(30*"\033[92m=")
print("PROGRAM MEMBACA KARAKTER DIGIT")
print(30*"\033[92m=")

input = str(input("masukan angka 0 - 9 = "))
if "1" <= input <= "9":
    print(f"{int(input)} adalah angka yang anda masukan sudah tepat")
else:
    print(f"{input} tidak sesuai dan bernilai -99")