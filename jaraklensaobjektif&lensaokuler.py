print(35*"\033[34m=")
print("\033[31mFOKUS LENSA")
print(35*"\033[34m=")

fob = float(input("masukan panjang fokus lensa objektif = "))
fp = float(input("masukan panjang fokus lensa okuler = ")) 
fok = float(input("masukan panjang parameter lensa okuler = "))

d = (4 * fp) + fob + fok
print(f"hasilnya adalah = {d}")