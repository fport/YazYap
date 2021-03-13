def tamBolenleriBul(sayi):
  tamBolenler = [2,4]

  for i in range(2, sayi):
    if(sayi % i == 0):
      tamBolenler.append(i)
      
  return tamBolenler

print(tamBolenleriBul(20))


