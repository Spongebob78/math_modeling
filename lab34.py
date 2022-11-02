import numpy as np
N = 5 
M = 6

A = np.zeros((N,M))

for n in range(N):
  for m in range(M):
    x1 = np.sin(N * (n + 1) + M * (m + 1))
    if x1 < 0:
        A[n,m] = 0 
    else:
      A[n,m] = x1

print(A)
print()

new_A = np.zeros((N, M))
for i in range(N):
  for j in range(M):
    new_A[i, j] = A[i, j]


new_A[::, 0], new_A[::, 1] = new_A[::, 1], new_A[::, 0]
print(A)
print()
print(new_A)



      
