import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()
ball, = plt.plot([], [], '-', color='r', label='Ball')
 
def butterfly():
    t = np.arange(-100, 100, 0.1)
    x = np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4*t) + (np.sin(t/12) ** 5))
    y = np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4*t) + (np.sin(t/12) ** 5))
    return x, y
	
edge = 1000
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
    ball.set_data(butterfly())

ani = animation.FuncAnimation(fig,
                              animate,
                              frames=300,
                              interval=30
                             )
 
ani.save('lec_7_osn_3.gif')