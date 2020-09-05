masa_kerja = int(input("Masa Kerja : "))
umur = int(input("Umur : "))

if masa_kerja >= 5 and umur > 50:
    print("Anda mendapatkan bonus 20%")
elif masa_kerja >= 5:
    print("Anda mendapatkan bonus 10%")
else:
    print("Maaf anda belum mendapatkan bonus")
