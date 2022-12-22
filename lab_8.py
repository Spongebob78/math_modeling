import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='b')
trajectory, = plt.plot([], [], '-', color='g')

frames = np.arange(0, np.pi * 8, 0.01)
plt.axis('equal')
ax.set_xlim(-1, 2)
ax.set_ylim(0, 1)


def ellips_fanc(r, frames): 
    
    x = r * np.cos(frames)
    y = r * np.sin(frames)
    return x, y

X, Y = [], []
r = 0.1

def animate(i):
    X.append(ellips_fanc(r=r, frames=i)[0])
    Y.append(ellips_fanc(r=r, frames=i)[1])
    ball.set_data(ellips_fanc(r=r, frames=i))
    trajectory.set_data(X, Y)

ani = animation.FuncAnimation(fig, animate, frames=frames, interval=30)
ani.save('lab_8.png')