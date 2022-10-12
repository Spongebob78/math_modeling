n = int(input())
b1 = int(input())
q = int(input())

for i in range(1, n):
  num = b1 * q ** (n - 1)
  print(num)
