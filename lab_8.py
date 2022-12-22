import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='b')
trajectory, = plt.plot([], [], '-', color='g')

frames = np.arange(0, 4.85 * np.pi, 0.06)
plt.axis('equal')
ax.set_xlim(-1, 13)
ax.set_ylim(0, 10)


def ellips_fanc(p, ee): 
    fi = np.arange(0, np.pi * 8, 0.01)
    r = 10 / (1 + (0.9 * np.cos(fi)))
    x = r * np.cos(fi)
    y = r * np.sin(fi)
    return x, y

X, Y = [], []

def animate(i):
    X.append(ellips_fanc(p = 10, ee = 0.9)[0])
    Y.append(ellips_fanc()[1])
    ball.set_data(ellips_fanc())
    trajectory.set_data(X, Y)

ani = animation.FuncAnimation(fig, animate, frames=frames, interval=30)
ani.save('.gif')