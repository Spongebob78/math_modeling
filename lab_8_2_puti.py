import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
figur, = plt.plot([], [], 'o', color='b')
figur1, = plt.plot([], [], 'o', color='r')
trajectory, = plt.plot([], [], '-', color='g')
trajectory1, = plt.plot([], [], '-', color='g')

frames = np.arange(0, np.pi * 2.01, 0.09)

plt.axis('equal')
ax.set_xlim(-13, 10)
ax.set_ylim(-10, 10)

def ellips1(p, e, fi):
    r = p / (1 + (e * np.cos(fi)))
    x = r * np.cos(fi)
    y = r * np.sin(fi)
    return x, y

def ellips2(p1, e1, fi1):
    r1 = p1 / (0.89 + (e1 * np.cos(fi1)))
    x1 = r1 * np.cos(fi1)
    y2 = r1 * np.sin(fi1)
    return x1, y2    

X1, Y1 = [], []

X2, Y2 = [], []

fi = np.arange(0, np.pi * 8, 0.01)
fi1 = np.arange(0, np.pi * 8, 0.01)

def animate(i):
    plt.plot([-3.2], [0] , marker='.', color='yellow')
    X1.append(ellips1(p=3, e=0.65, fi=i)[0])
    X2.append(ellips2(p1=1.9, e1=0.65, fi1=i)[0])
    Y1.append(ellips1(p=3, e=0.65, fi=i)[1])
    Y2.append(ellips2(p1=1.9, e1=0.65, fi1=i)[1])
    figur.set_data(ellips1(p=3, e=0.65, fi=i))
    trajectory.set_data(X1, Y1)
    figur1.set_data(ellips2(p1=1.9, e1=0.65, fi1=i))
    trajectory1.set_data(X2, Y2)
    return figur,

ani = animation.FuncAnimation(fig,
                              animate,
                              frames=frames,
                              interval=50
                             )
ani.save('planet.gif', writer='imagemagick')