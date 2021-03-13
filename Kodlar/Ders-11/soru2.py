print("YazYap Bank'a Hoşgeldin\n İşlem Yapmak İçin Kartınızı takınız.\n")
secim = input("Kartınızı  takmak için t, bankamatikten çıkmak için 1 yazınız.")

bakiye = 1500

if(secim == "t"):
  print("Kartiniz okunuyor ...")
  while True:
    secenek = int(input("""
      *******************
      -> Yapmak istediğiniz işlemi seciniz.
      1- Karta Para Yükle
      2- Karttan Para Çek
      3- Hesap Özeti
      4- Çıkış
      *******************
    """))
    while secenek<1 or secenek>4:
      secenek = int(input("Lütfen 1-4 arasında bir secenek giriniz\n"))
    if(secenek == 1):
      miktar = int(input("Miktarınızı giriniz : "))
      bakiye += miktar
    elif(secenek == 2):
      miktar = int(input("Miktarınızı giriniz : "))
      bakiye -= miktar
    elif(secenek==3):
      print("""
        ISIM : İdris
        SOYISIM : Altan
        IBAN : XXXXX
        BAKIYE : {}
        """.format(bakiye))
    elif(secenek == 4):
      print("Güle Güle YazYap:)")
      break
          
