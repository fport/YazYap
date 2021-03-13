sayilar = [18,22,15,85,65,30,10,20,32,34,28,101,5,4,32]
sayac = 0

for sayi in sayilar:
  if sayi%5 == 0:
    print(str(sayi)+ "-> 5in katıdır")
    sayac +=1
  
print("5'in katı olan sayiların adeti ->",sayac)  
