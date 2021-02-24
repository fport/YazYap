# ödev
"""
kare olusturun
ücgen olusturun
"""

sayi = int(input("bir sayi gir :"))

for i in range(sayi):
  print(i,"🧐  " * (i))

"""
sayi = int(input("bir sayi gir :"))

for i in range(sayi):
  print("🧐  " * (sayi-i))
"""

"""
sayi = int(input("bir sayi gir :"))

for i in range(sayi):
  print("🧐  " * (i))
"""

"""
# 10.soru
#Baslangic kodu 
print("--- Hesap Makinesi -----") 
print("Toplama işlemi̇ yapmak için 1 'e basin. çikarma işlemi yapmak için 2 'e basin. çarpma işlemi  yapmak için 3 'e basin. bölme işlemi yapmak için 4 'e basin.")

islem = input("İslem seciniz : ")

if islem == "1":
  sayi1 = int(input("sayi1 giriniz : "))
  sayi2 = int(input("sayi2 giriniz : "))
  print("Sonuc {}".format(sayi1 + sayi2))
elif islem == "2":
  sayi1 = int(input("sayi1 giriniz : "))
  sayi2 = int(input("sayi2 giriniz : "))
  print("Sonuc {}".format(sayi1 - sayi2))
elif islem == "3":
  sayi1 = int(input("sayi1 giriniz : "))
  sayi2 = int(input("sayi2 giriniz : "))
  print("Sonuc {}".format(sayi1 * sayi2))
elif islem == "4":
  sayi1 = int(input("sayi1 giriniz : "))
  sayi2 = int(input("sayi2 giriniz : "))
  print("Sonuc {}".format(sayi1 / sayi2))
else:
  print("geçersiz işlem girdiniz")
"""

"""
# 9.soru
plaka = input("Plaka giriniz : ")

if plaka == "16":
  print("Bursa")
elif plaka == "34":
  print("İstanbul")
elif plaka == "06":
  print("Ankara")
else:
  print("Turkiye <3")
"""


"""
# 8.soru
firma = input("Firma adı girin : ")
kilo = int(input("Bagajınızın kilosunu giriniz : ")) #22

if kilo < 20:
  print("Hiçbir şey ödemiceksin, devam et!")
else:
  ekKilo = kilo - 20
  ekUcret = ekKilo * 10
  print("{} Fazla bagaj için {} TL ödemelisiniz.".format(firma,ekUcret))
"""

"""
# 7.soru
kisa = int(input("Kısa kenar : "))
uzun = int(input("Uzun kenar : "))

alan = kisa * uzun
cevre = 2 * (kisa + uzun)

print("Alan -> ",alan)
print("Cevre -> ", cevre)
"""


"""
# 6.soru
kare = int(input("Kenar kac cm -> "))

for i in range(kare):
  print("* "*kare)
"""
"""
sayi = int(input("bir sayi gir"))

for i in range(sayi):
  print("x"*sayi)
"""


"""
# 5.soru
sesli_harfler = "aeıioöuü" 
sessiz_harfler = "bcçdfgğhjklmnprsştvyz" 

sessizharf_toplam = 0
sesliharf_toplam = 0

metin = input("Bir metin girer misin dostum :) ")
#metin = "yazyap kursu"
# i =     ^   

for i in metin:
  if i in sesli_harfler:
    sesliharf_toplam += 1
  if i in sessiz_harfler:
    sessizharf_toplam += 1

print("Sessizler -> ",sessizharf_toplam)
print("Sesli harfler -> ",sesliharf_toplam)
"""

"""
# 4.soru
sayi = int(input("Sayi giriniz : ")) # 18

toplam = 0 #1+2+3+6+9
   
# range(1,18) -> 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
# i ->             ^  

for i in range(1, sayi):
  print(i)
  if(sayi % i == 0):
    toplam += i 

if(sayi == toplam):
  print("Mükkemel sayidir.")
else:
  print("Mükkemel sayi değildir.")
"""


"""
# 3.soru
vize1 = int(input("1. Vize puanın : "))
vize2 = int(input("2. Vize puanın : "))
final = int(input("Final puanın : "))

# vizeler %30  final %40
ortalama = vize1 * (3/10) + vize2 * (3/10) + final * (4/10) 

if(ortalama >= 90):
  print("AA")
elif(ortalama >= 85):
  print("BA")
elif(ortalama >= 80):
  print("BB")
elif(ortalama >= 75):
  print("CB")
elif(ortalama >= 70):
  print("CC")
elif(ortalama >= 65):
  print("DC")
elif(ortalama >= 60):
  print("DD")
elif(ortalama >= 55):
  print("FD")
elif(ortalama >= 50):
  print("FF")
else:
  print("K A L D I N")
"""

"""
# 2.soru
yakit = float(input("Km'de aracımız ne kadar yakıyor : "))
km = int(input("Kaç km yol katettiniz: "))

#toplam = yakit * km

print("Toplam tutar : ", yakit * km)
"""


"""
# 1.soru
sayi = int(input("Bir sayi giriniz : "))

if(sayi < 0):
  print("Sayimiz sıfırdan kücüktür.")
elif(sayi > 0):
  print("Sayimiz sıfırdan büyüktür.")
else:
  print("Sayi sıfırdır.")
"""

