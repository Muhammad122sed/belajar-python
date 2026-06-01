angka1 = float(input("masukan angka pertama anda: "))
angka2 = float(input("masukan angka kedua anda: " ))
operasi = input(" masukan operasi +,*,-,/: ")

if operasi == "+":
        print ( " hasil " , angka1 + angka2)
elif operasi == "-":
        print ( " hasil " , angka1 - angka2)
elif operasi == "*":
        print ( " hasil " , angka1 * angka2)
elif operasi == "/":

        if angka2 != 0 :
                print (" hasil " , angka1 / angka2)
        else:
                print ( " Eror: Tidak bisa dibagi dengan nol! " )
else:
        print (" isi bagian oprasi, angka1 dan angka2 terlebih dahulu")
