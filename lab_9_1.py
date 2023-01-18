import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 3, 0.1)
 
def radio_function(n, t):
    dmdt = n * k 
    return dmdt
 
n_0 = 10
k = 1

n_t = odeint(radio_function, n_0, t)
 
plt.plot(t, n_t[:,0])
plt.grid()
plt.savefig('lab_9.png')