def ciftMi(x):
  return x%2==0

toplam = 0 # cift sayiların toplamı
sayac = 0 # kac tane cift sayi var bunu hesap edebilcez
baslangic = int(input("Baslangıc sayisini giriniz"))
bitis = int(input("Bitis sayisini giriniz"))

for sayi in range(baslangic,bitis):
  if(ciftMi(int(sayi))):
    toplam += sayi
    sayac +=1

print("Ortalma",(toplam/sayac))

# baslangıc 10, bitis 20
#10 12 14 16 18 -> 70/5 = 14
