def persegiPanjang(p, l):
    return p*l, 2*(p+l)


panjang = int(input("Masukkan nilai panjang: "))
lebar = int(input("Masukkan nilai lebar: "))

if panjang > 0 and lebar > 0:
    luas, keliling = persegiPanjang(panjang, lebar)
    print(f"Luas: {luas}")
    print(f"Keliling: {keliling}")
else:
    print("Maaf input nilai tidak valid")
