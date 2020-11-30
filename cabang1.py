voucher = int(input("jika mempunyai voucher diskon, berapa besar diskonnya? (terdapat 3 macam: 50.000, 100.000, 150.000) "))
belanja = input("sudah pernah berbelanja di toko ini? (ya/belum) ")
kartu = input("apakah punya kartu anggota? (ya/tidak) ")
total = int(input("total belanja? "))

diskon = 0

if belanja == "belum":
  diskon += 50000
else:
  diskon += voucher

if total > 500000:
  diskon += 50000

print("total potongan harga:",diskon)