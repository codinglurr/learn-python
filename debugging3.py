try:
    bil1 = int(input("Masukkan bilangan bulat pertama: "))
except ValueError:
    print("Input bukan bilangan bulat, diganti menjadi nilai default 1")
    bil1 = 1

try:
    bil2 = int(input("Masukkan bilangan bulat kedua: "))
except ValueError:
    print("Input bukan bilangan bulat, diganti menjadi nilai default 1")
    bil2 = 1

try:
    print(bil1/bil2)
except ZeroDivisionError:
    print("division by zero")