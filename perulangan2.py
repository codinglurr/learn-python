angka = int(input())
nilai = 0
for baris in range(angka):
    for kolom in range(baris):
        print(nilai, end="")
        nilai += 1
        if nilai >= 9:
            nilai = 0
    print()
