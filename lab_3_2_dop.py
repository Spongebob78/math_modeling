from master import e
from master import h
from master import k
import numpy as np
T = 200 
E = 300

number1 = (2 / (np.pi ** 0.5))
number2 = (h / ((k * T) ** (3 / 2)))
number3 = (e ** (-E / (k * T))) # number3 = 0.0 = 
number4 = (E ** (T / 2))
N = number1 * number2 * number3 * number4
print(N)






