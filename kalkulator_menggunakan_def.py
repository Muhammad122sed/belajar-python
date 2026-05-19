def tambah(a , b ):
        return a + b
def kurang(a , b ):
        return a - b
def kali(a , b ) :
        return a * b
def bagi(a , b ) :
        return a / b


angka1 = float(input("masukan angka pertama anda: "))
angka2 = float(input("masukan angka kedua anda: " ))
operasi = input(" masukan operasi +,*,-,/: ")

if operasi == "+":
        print ( " hasil " , tambah( angka1, angka2))
elif operasi == "-":
        print ( " hasil " , kurang( angka1, angka2))
elif operasi == "*":
        print ( " hasil " , kali( angka1, angka2))
elif operasi == "/":
        if angka2 != 0 :
                print (" hasil " , bagi( angka1, angka2))
        else:
                print ( " valid pembagian " )
else:
        print (" isi bagian oprasi, angka1 dan angka2 terlebih dahulu")
