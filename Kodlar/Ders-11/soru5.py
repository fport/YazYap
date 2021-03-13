from random import randint

rand = randint(1,100) # 50

while True:
  sayi = int(input("1-100 arası bir sayi seciniz.")) #67

  if(sayi==0 or sayi > 100):
    print("Oyun iptal edildi.")
    break
  elif sayi < rand:
    print("Daha yüksek bir sayi giriniz.")
    continue
  elif sayi > rand:
    print("Daha kücük bir sayi giriniz")
    continue
  else:
    print("Rasgele seciken sayi {0}".format(rand))
    print("Tahmin ettiğiniz sayiniz {0}".format(sayi))
