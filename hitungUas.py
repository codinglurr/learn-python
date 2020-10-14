# def hitung(matkul,nilaiUTS,nilaiUAS):
#    result = (45/100*nilaiUTS)+(55/100*nilaiUAS)
#    return "Mata Kuliah {} adalah {}".format(matkul,result)

# print(hitung("Kalkulus",70,80))

#def tampil_mk():
#   print("MK1: Logmat")
#    print("MK2: Kalkulus")
#    print("MK3: Pengenalan Program")

#tampil_mk()

#22/7 * r * r * t

#jari = int(input("Masukan Jari-jari: "))
#tinggi = int(input("Masukan Tinggi: "))

#def volume_tabung(r,t):
#   result = (3.14 * r**2) * t
#  return "Luas lingkaran adalah {}".format(result)

#print(volume_tabung(jari,tinggi))

#r = int(input())
#R = int(input())
#t = int(input())

#def hitung(r,R,t):
#    result = 1/3*3.14*t * (R**2 + (R*r) + r**2)
#    return "{:.2f}".format(result)

#print(hitung(r,R,t))

#list_bilangan = list(map(int, input().split(" ")))

#def printList(list):
  #lengkapi fungsi berikut
#    for hasil in list:
#        if(hasil % 2 != 0):
#            print(hasil, end=" ")
#    print()
#panggil fungsi printList()
#printList(list_bilangan)
#list_bilangan[0] += 1
#panggil fungsi printList
#printList(list_bilangan)


#def konversiWaktu(detik):
  #lengkapi fungsi berikut
#  jam = detik // 3600
#  sisa_jam = detik% 3600
#  menit = sisa_jam //60
#  sisa_menit = sisa_jam % 60
#  detik = sisa_menit
#  return jam,menit,detik
  
#detik = int(input())

#jam, menit, detik = konversiWaktu(detik)
#print (jam, "jam", menit, "menit", detik, "detik")

#jam = 0
#menit = 0
#detik = int(input())

#def konversiWaktu():
#    global detik,menit,jam
#    jam = detik // 3600
#    sisa_jam = detik % 3600
#    menit = sisa_jam // 60
#    sisa_menit = sisa_jam % 60
#    detik = sisa_menit
#    return jam,menit,detik

#konversiWaktu()
#print (jam, "jam", menit, "menit", detik, "detik")

#saldo = int(input())

#def printMenu():
#  print("1. es teh manis: 50")
#  print("2. es kelapa: 100")
#  print("3. es jeruk: 150")
  
#your code start here

#def membeli():
#    global saldo
#    printMenu()
#    menu = {1:50,2:100,3:150}
#    pilih = int(input("Masukkan angka pesanan anda: "))
#    saldo -= menu[pilih]
#    print("Sisa saldo anda:  {}".format(saldo))
#    print()

#while saldo > 0:
#    membeli()

#key = int(input())
#p = list(map(str, input()))
#def geser(key,p):
#    hasilku = []
#    fix_bener = ""
#    for hasil in range(key,len(p)):
#        hasilku.append(p[hasil])

#    for bener in hasilku:
#        fix_bener += bener
#    return fix_bener

# print (geser(key, p))

def tukar(A):
    return A.reverse()

list_bilangan = list(map(int, input().split()))

tukar(list_bilangan)
print(list_bilangan)
