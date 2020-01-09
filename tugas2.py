def hitung(a, b):
        hasil = 3.14 * ((1/2*a)*(1/2*a)) * b
        print(hasil)
    
nilai1 = 20
nilai2 = 28
hitung(nilai1, nilai2)

hitung = lambda nilai: nilai * 3
print(hitung(50))

class Kalkulator:
    def __init__(obj, nilai1, nilai2):
        
        obj.nilai1 = nilai1 
        obj.nilai2 = nilai2

    
    def tambah(tambah):
        hasil = tambah.nilai1 + tambah.nilai2
        print(str(tambah.nilai1) + " + " + str(tambah.nilai2) + " = " + str(hasil))
    def kurang(kurang):
        hasil = kurang.nilai1 - kurang.nilai2
        
        print(hasil)
    def kali(kali):
        hasil = kali.nilai1 * kali.nilai2
        print(hasil)
    def bagi(bagi):
        hasil = bagi.nilai1 / bagi.nilai2
        print(hasil)

p1 = Kalkulator(60, 6)

p1.tambah()
p1.kurang()
p1.kali()
p1.bagi()
       