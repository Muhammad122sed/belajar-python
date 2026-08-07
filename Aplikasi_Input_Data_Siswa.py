print("aplikasi siswa")

while True:
    try:
         nama = input("masukan nama kamu: ")
         kelas = input("masukan nama kelas kmau: ")
         umur = float(input("masukan umur kamu: "))
         nilai = (float(input("masukan nilai bahasa inggris: ")))


         if nilai >= 90:
            print("nilai A")
         elif nilai >= 68:
            print("nilai B")
         elif nilai >= 60:
            print("nilai C")
         else:
            print("nilai D tolong perbaiki mata kuliah anda")

         print(f"nama kamu adalah {nama} dan kelas {kelas} dan umur kmau {umur} nilai bahasa inggris kamu {nilai}")
    except ValueError:
        print("data eror ulangi lagi")


