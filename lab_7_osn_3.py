import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()
figure = plt.plot([], [], '-', color='r', label='Ball')

plt.axis('equal')


def butterfly():
    t = np.arange(0, 12 * np.pi, 0.01)
    x = np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4*t) + (np.sin(t/12) ** 5))
    y = np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4*t) + (np.sin(t/12) ** 5))
    ax.set_xlim(-5.5, 5,5)
    ax.set_ylim(-5.5, 5,5)
    return x, y
	
def heart():
    t = np.arange(0, 12 * np.pi, 0.01)
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(3 * t)
    ax.set_xlim(-20, 20)
    ax.set_ylim(-20, 20)
    return x, y

def animate(i):
    figure.set_data(butterfly())
    return figure,

def animate1(i):
    figure.set_data(heart())
    return figure, 

ani = animation.FuncAnimation(fig,
                              animate,
                              interval=30
                             )
ani.save('lec_7_osn_3_butterfly.gif')

ani = animation.FuncAnimation(fig,
                              animate1,
                              interval=30
                             )
ani.save('lec_7_osn_3_heart.gif')