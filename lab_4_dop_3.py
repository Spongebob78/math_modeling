linza = input('')
d = int(input("расстояние"))
F = int(input(""))

def func(l, d, f):
  if linza == 'соб' and d < f:
    print("изображение прямое  мниме увел")
  elif linza == 'рас' and d < f:
    print("изображение прямое  мниме умен")
  elif linza == "соб" and d == f:
    print("изоб не даёт изображение ")
  elif linza == 'pac' and d == f:
    print("изображение пряфмое мниме умен")
  elif linza == 'соб' and f < d < 2 * f:
    print('Изображение обратное действ увел')
  elif linza == 'рас' and f < d < 2 * f:
    print("изоб прямое мнимое уменьш")
  else:
    print("")
  