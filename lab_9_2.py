import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 10, 0.1)
 
def radio_function(m, t):
    dmdt = m * -k * t
    return dmdt
 
m = 1000
k = 0.08

m_t = odeint(radio_function, m, t)
 
plt.plot(t, m_t[:,0])
plt.grid()
plt.savefig('lab_9_2.png')