from math import sin

N = 5
M = 6

mtx = []
for i in range(N):
  a = []
  for j in range(M):
     a.append(sin(N * (i + 1) + M * (j + 1)))

mtx.append(a)
for i in range(N):
  for j in range(M):
     if mtx[i][j] < 0:
       mtx = 0 
     else:
       print(mtx[i][j])
print()

  