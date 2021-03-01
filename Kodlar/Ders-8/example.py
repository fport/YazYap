"""
# liste örneği
sepet = ["elma","armut",3,5.5,["ahmet",12]]

# 0dan 4'e kadar 
print(sepet[0:4])
print(sepet[:-2])

liste = [1,2,3,4]
# len()  lenght
print(len(liste)) # 4
print(len(sepet)) # 5
print(len(sepet[4])) # 2
"""
"""
#örnek çözüm 1
liste = [1,2,3,4]
toplam = 0

for i in liste:
  toplam += i
print(toplam)
"""

"""
#        range(baslangıc, bitis, adım) 
for i in range(1,5,2):
  print(i)
"""
"""
#index-> 0 1 2 3     
liste = [7,8,9,10,11] # len(liste) -> 5
toplam = 0
listeninUzulugu = len(liste) #-> 5

#range(listeninUzulugu) -> 0 1 2 3 4 
# toplam += liste[0] -> 7
# toplam += liste[1] -> 15
# toplam += liste[2] -> 24
# toplam += liste[3] -> 34
# toplam += liste[4] -> 45


for i in range(listeninUzulugu):
  toplam += liste[i]
print(toplam)
"""
"""
#append
liste = [7,3,16,78]
liste.append(10) # liste : [7,3,16,78,10]

print(liste)
"""
"""             -       - -
liste1 = [7,3,16,1,78,16,16,78,6]
liste2 = [21,11,65,7]

#liste1.extend(liste2)
#liste1.insert(1,90)
#liste1.pop()
#liste1.pop(2)
#liste1.sort() # [1,3,7,16,78]
#liste1.remove(16)
#liste1.clear()
#print(liste1.count(16))
#liste1.reverse() # [6,78,16,16,78,1,16,3,7]

print(liste1)
"""
"""
liste = [] # .append ile listeye eleman ekledik
sayi1 = int(input("Birinci sayiyi giriniz -> ")) # 0
sayi2 = int(input("İkinci sayiyi giriniz -> "))  # 5

              # 0   ,  5   -> 0,1,2,3,4
for i in range(sayi1,sayi2):
  liste.append(i)
  
liste.reverse()

print(liste)
"""

# {}-> kümeler  []-> listeler
# listeleri set() ile kümeye cevirebiliyoruz
""""
küme = set([1,2,3,4])
#küme.add(1)

küme.remove(3)
print(küme)
"""
"""
küme = set()

for i in range(50):
  küme.add(i)

print("eklendikten sonra -> ",küme)

for i in range(len(küme)):
  if(i % 2 == 0):
    küme.remove(i)

print("2 bölünenler silindi -> ",küme)
"""
"""
küme = set()

for i in range(len(küme)):
  if(i % 2 != 0):
    küme.add(i)

print(küme)
"""
"""
liste = [1,2,3,3,4,5,6,6,7]
küme = set(liste)

print(küme)
"""
"""
küme1 = set([1,67,12,78,4,23])
küme2 = set([1,2,3,3,4,5,6,6,7])

print("kesişimi",küme1.intersection(küme2)) # kesişimi verir
print("birleşimi",küme1.union(küme2)) # birleşimi
"""
