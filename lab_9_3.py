import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 3, 0.1)
 
def radio_function(v, t):
    dmdt = g - k/m * v
    return dmdt
 
v = 10
k = 0.5
m = 1
g = 9.8

n_t = odeint(radio_function, v, t)
 
plt.plot(t, n_t[:,0])
plt.grid()
plt.savefig('lab_9_3.png')