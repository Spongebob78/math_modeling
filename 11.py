import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
figur, = plt.plot([], [], 'o', color='b')
trajectory, = plt.plot([], [], '-', color='g')

frames = np.arange(0, np.pi * 2.01, 0.09)

edge = 10
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def ellips(p, e, fi):
    r = p / (1 + (e * np.cos(fi)))
    x = r * np.cos(fi)
    y = r * np.sin(fi)
    return x, y

X, Y = [], []

fi = np.arange(0, np.pi * 8, 0.01)

def animate(i):
    X.append(ellips(p=3, e=0.65, fi=i)[0])
    Y.append(ellips(p=3, e=0.65, fi=i)[1])
    figur.set_data(ellips(p=3, e=0.65, fi=i))
    trajectory.set_data(X, Y)
    return figur,

ani = animation.FuncAnimation(fig,
                              animate,
                              frames=frames,
                              interval=50
                             )
ani.save('11.gif', writer='imagemagick')