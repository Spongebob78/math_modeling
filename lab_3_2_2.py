from master import e
from master import h
from master import k
import numpy as np

T = 200 
E = 300

N = (2 / (np.pi ** 0.5)) * (h / ((k * T) ** 1.5)) * (e ** (-E / (k * T))) * (E ** (T / 2))

print(N)
              
