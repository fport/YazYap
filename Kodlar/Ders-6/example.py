"""
#Girilen kelimenin Türkçe karakter içerip içermediğini kontrol eden program. ğ ü ş ö ç İ ı 

türkce = "ğüşöçİı"
girdi = input("Bir kelime giriniz : ") # abcd
sayac = 0

# harf -> a
# sesliharf -> ğ

for harf in girdi:
  for sesliharf in türkce:
    if harf == sesliharf:
      sayac += 1  

if(sayac == 0):
  print("Türkce karakter icermiyor!")
elif(sayac != 0):
  print("Türkçe karakter içeriyor")
"""

"""
#Kullanıcının girdiği iki sayı arasındaki sayıları listeleyen program - range

x = int(input("Birinci sayiyi giriniz : "))
y = int(input("İkinci sayiyi giriniz : "))

for i in range(x,y):
  print(i)
"""

"""
1’den 10’a kadar konsola yazdırsın, 5 sayısı geldiğinde 5 sayısı bulundu yazsın.
for x in range(1,10):
  if x == 5:
    print("5 sayisi bulundu")
    continue
  print(x)
"""


"""
#Girilen kelimenin Türkçe karakter içerip içermediğini kontrol eden program. ğ ü ş ö ç İ ı 

girdi = input("Bir kelime giriniz : ")

for i in girdi:
  if(i == "ğ" or i=="ü" or i=="ç" or i=="ş" or i=="ö" or i=="İ" or i=="ı"):
    print("Türkçe karakter içeriyor")
    break
  else:
    print("Türkce karakter yok")
"""


#range(3) -> sıfırdan 3'e kadar 0 1 2
#range(1,3) -> 1den 3'e kadar 1 2 
#range(2,11,4) -> 2den 11'e kadar 4er  4er -> 2 6 10


"""
for i in range(5):
  print(i)
"""

"""
sayilar = 123456
for x in str(sayilar):
  print(int(x)*3)
"""

"""
for x in "furkan":
  print(x)
"""


"""
#5.Haftanın çözümleri
#1.soru
toplam = 0
x = 1
while x < 150:
  # 7'ye bolunebılıyor demek
  if(x%7 == 0):
    toplam += x
  x += 1
print("toplam :",toplam)

#2.soru
y = int(input("Faktöriyel almak istediğiniz sayiyi girin! ->"))
faktoriyel = 1

while y > 0:
  faktoriyel *= y
  y -= 1

print("sonuc :",faktoriyel)
"""
