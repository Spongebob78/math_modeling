def func(xargs, xkw):
  if xkw['1'] == xargs[0]:
    s = 3,14 * r**2
    
  elif xkw['2'] == xargs[0, 2]:
    s = (1/2) * a * h
     
  elif xkw['3'] == xargs[1, 3]:
    s = a * b 

  print(s)
r = int(input())
a = int(input())
b = int(input())
h = int(input())
  
xargs = [r, a, b, h]
xkw = int(input())
func([r, a, b, h], figure = xkw)
# crug = 1, treug = 2, pram = 3
