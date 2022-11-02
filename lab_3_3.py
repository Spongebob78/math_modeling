import numpy as np

t = np.arange(0, 5, 0.1)

x0 = 1
y0 = 0
g = 10
v = 5
alpha = 30 * np.pi / 100
vx0 = v * np.cos(alpha)
vy0 = v * np.cos(alpha)

x = x0 + vx0 * t 
y = y0 + vy0 * t - g * t ** 2 / 2

coords = np.zeros((len(t), 3))
for i in range(len(t)):
  coords[i, 0] = t[i]
  coords[i, 1] = x[i]
  coords[i, 2] = y[i]

print(coords)