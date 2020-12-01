def cariAngka(angka):
    if angka % 3 == 0 and angka % 5 == 0:
        return True
    else:
        return False


b = int(input("Masukan nilai: "))
print(cariAngka(b))
