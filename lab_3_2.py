from master import G
import numpy as np
a =np.pi / 3
b = 30
h = 100

v = ((G * h * np.tan(b) ** 2)/(2 * np.cos(a) * 2 * (1 - np.tan(b))) ** 0.5)
print(v)

