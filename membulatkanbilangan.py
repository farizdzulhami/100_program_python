print(30*"\033[92m=")
print("PROGRAM MEMBULATKAN BILANGAN".center(35))
print(30*"\033[92m=")
KELIPATAN = 25
total_belanja = float(input("masukan total belanja = "))
sisa = total_belanja % KELIPATAN
hasil = total_belanja - sisa
print(f"total belanja anda adalah = {hasil}")