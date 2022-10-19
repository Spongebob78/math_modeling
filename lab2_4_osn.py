x1 = 1
x2 = 1
 
n = int(input())
 
print(x1)
print(x2)
 
for i in range(2, n): 
  x3 = x1 + x2
  x3 += x2
  x2 = x1
  print(x3)
  
  