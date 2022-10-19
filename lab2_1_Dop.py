x1 = int(input())
x2 = int(input())
x3 = int(input())

D = (x2 ** 2) - (4 * x1 * x3)
print(D)
if D < 0: 
  print("Нет решения")
else:
  if x2 > 0:
    x3 = x2 - x2 - x2
    xf1 = ((x3) + (D ** 0.5)) / (2 * x1)
    xf2 = ((x3) - (D ** 0.5)) / (2 * x1)
  elif x2 < 0:
    xf1 = ((x2) + (D ** 0.5)) / (2 * x1)
    xf2 = ((x2) - (D ** 0.5)) / (2 * x1)
print(f"Ответ х1 и х2 {xf1}, {xf2}")