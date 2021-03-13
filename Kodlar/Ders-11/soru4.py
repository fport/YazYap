def kontrol(metin):
  for karakter in metin:
    if karakter == 'a':
      return True
      break


metin = input("Metin : ")

if(kontrol(metin) == True):
  print("'a' harfi metin içinde bulunuyor.")
else:
  print("'a' harfi metin içinde bulunmuyor.")

