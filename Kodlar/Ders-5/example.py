"""
1’den 10’a kadar konsola yazdırsın,
5 sayısı geldiğinde 5 sayısı 
bulundu yazsın.
#1
x = 1

while x<10:
  if(x == 5):
    print("5 sayisi bulundu!")
  print(x)
  x +=1
"""



"""
0’dan 10’a kadar olan 
çift sayıların toplamını
 yazdıran program

toplam = 0
x = 0 

while x<11:
  # sayi 2ye bölümünden kalan 0 ise çifttir.
  if(x % 2 == 0):
    print(x)
    toplam += x
  x = x+1

print("toplam : ",toplam)
"""


"""
Sıfırdan 100’e kadar olan sayıların
3 katlarını yazdıran kod.
#1.
x=0
while x<100:
  print(x*3)
  x= x+1
#2
x=0
while True:
  if( x==100):
    break
  print(x*3)
  x= x+1
"""



"""
x = 0
while x<10:
  x = x+1
  if(x == 5):
    continue
    break
  print(x)  
"""

"""
x = 1
while x<10:
  print("ilk",x)
  if(x == 5):
    break
  x = x+1
  print("son",x)
"""

"""
x = 10

while x>0:
  print(x)
  x +=1
  if(x == 100):
    break

print("Bittii :)")
"""
