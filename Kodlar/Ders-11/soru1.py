def Toplama(x,y):
  return x+y

def Cikarma(x,y):
  return x-y

def Carpma(x,y):
  return x*y

def Bolme(x,y):
  return x/y

while True:
  print("""
    Yapmak istediğiniz işlemi seciniz.
    ***********
    1- Toplama
    2- Çıkarma
    3- Çarpma
    4- Bölme
    ***********
  """)
  secim = int(input("Secim yapınız 1/2/3/4\n"))

  sayi1 = int(input("1.Sayiyi seciniz\n"))
  sayi2 = int(input("2.Sayiyi seciniz\n"))


  if secim == 1:
    print(sayi1, " + ", sayi2, " = ", Toplama(sayi1,sayi2))
  elif secim == 2:
    print(sayi1, " - ", sayi2, " = ", Cikarma(sayi1,sayi2))
  elif secim == 3:
    print(sayi1, " * ", sayi2, " = ", Carpma(sayi1,sayi2))
  elif secim == 4:
    print(sayi1, " / ", sayi2, " = ", Bolme(sayi1,sayi2))
  else:
    print("Gecersiz giriş yapıldı")
