from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
figure, = plt.plot([], [], '-', color='b')

plt.axis('equal')


def fraktal(y0, x0, C, D):
    n = np.arange(x0, y0, 0.01)
    x = (x0(n-1)**2) - (y0(n-1)**2) + C
    y = 2 * x0(n-1) * y0(n-1) + D
    return x, y

x1 = []
y1 = []

def animate(t):
    x1.append(fraktal(t)[0])
    y1.append(fraktal(t)[1])
    figure.set_data(fraktal(y0=0.1, x0=0.1, C=0.3, D=0.33))
    
ani = FuncAnimation(fig, animate, frames=100, interval=30)
ani.save('lec_7_osn_4_fraktal.gif')