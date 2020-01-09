nilai1 = int(input("Masukan nilai diameter : "))
nilai2 = int(input("Masukan nilai tinggi : "))
volume = ((nilai1/2) * (nilai1/2)) * 3.14*nilai2

print("Maka Hasil Volume tabung adalah = " + str(volume))

print("\n")

sisi = int(input("Masukan panjang Sisi segitiga : "))
keliling = sisi*3

print("Keliling dari segitiga adalah :  " + str(keliling))

print("\n")

angka1 = int(input("Masukan Angka 1 : "))
angka2 = int(input("Masukan Angka 2 : "))

perhitungan = input("Masukan Operator hitung : ")
if (perhitungan == f"+"):
    hasil = angka1 + angka2
    print(hasil)
elif(perhitungan == f"-"):
    hasil = angka1 - angka2
    print(hasil)
elif(perhitungan == f"*"):
    hasil = angka1 * angka2
    print(hasil)
elif(perhitungan == f"/"):
    hasil = angka1 / angka2
    print(hasil)