pegawai = input("Masukkan status pegawai (Tetap/Kontrak): ")
anak = int(input("Masukkan jumlah anak: "))

gaji = 0
tunjangan = 0
if pegawai == "Tetap":
    gaji += 6000000
    if anak <= 3:
        tunjangan = anak * 220000
    else:
        tunjangan = anak * 200000
elif pegawai == "Kontrak":
    gaji += 4000000
else:
    print("Anda salah memasukan input")
print("Gaji anda adalah Rp{:,}".format(tunjangan + gaji))


# true / false | 1 / 0 | benar / salah
# if(False):
#     print("ucup")
# elif(False):
#     print("sapat")
# else:
#     print("ga milih")

# if True:
#     if(False):
#         print("ucup")
#     elif True:


#     else:
#         print('Sapat')
# elif True:
#     print('sien')
# else:
#     print("pedil")
