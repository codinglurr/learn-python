def hitungGaji(golong, lama):
    if golong == "I":
        return 1000000 + lama * 100000
    elif golong == "II":
        return 3000000 + lama * 150000
    elif golong == "III":
        return 5000000 + lama * 200000


gol = ""
while not(gol == "I" or gol == "II" or gol == "III"):
    gol = input("Masukan golongan: ")

input_ok = False
while not input_ok:
    try:
        lama = int(input("Masukan lama kerja: "))
        input_ok = True
    except ValueError:
        print("Input tidak valid, ulang!")
        continue
    else:
        print("Gaji adalah", hitungGaji(gol, lama))
