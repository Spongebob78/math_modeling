import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
figur, = plt.plot([], [], 'o', color='b')
figur1, = plt.plot([], [], 'o', color='r')
figur2, = plt.plot([], [], 'o', color='g')
figur3, = plt.plot([], [], 'o', color='y')
trajectory, = plt.plot([], [], '-', color='black')
trajectory1, = plt.plot([], [], '-', color='black')
trajectory2, = plt.plot([], [], '-', color='black')
trajectory3, = plt.plot([], [], '-', color='black')

frames = np.arange(0, np.pi * 2.01, 0.09)

plt.axis('equal')
ax.set_xlim(-13, 10)
ax.set_ylim(-10, 10)

def ellips1(p, e, fi):
    r = p / (1 + (e * np.cos(fi)))
    x = r * np.cos(fi)
    y = r * np.sin(fi)
    return x, y

def ellips2(p1, e1, fi):
    r1 = p1 / (0.89 + (e1 * np.cos(fi)))
    x1 = r1 * np.cos(fi)
    y1 = r1 * np.sin(fi)
    return x1, y1    

def ellips3(p2, e2, fi):
    r2 = p2 / (0.678 + (e2 * np.cos(fi)))
    x2 = r2 * np.cos(fi)
    y2 = r2 * np.sin(fi)
    return x2, y2   

def ellips4(p3, e3, fi):
    r3 = p3 / (0.678 + (e3 * np.cos(fi)))
    x3 = r3 * np.cos(fi)
    y3 = r3 * np.sin(fi)
    return x3, y3  

X1, Y1 = [], []
X2, Y2 = [], []
X3, Y3 = [], []
X4, Y4 = [], []

fi = np.arange(0, np.pi * 8, 0.01)

def animate(i):
    plt.plot([-3.2], [0] , marker='.', color='gold')
    X1.append(ellips1(p=3, e=0.65, fi=i)[0])
    X2.append(ellips2(p1=1.9, e1=0.65, fi=i)[0])
    X3.append(ellips3(p2=0.7, e2=0.58, fi=i)[0])
    X4.append(ellips4(p3=0.1, e3=0.51, fi=i)[0])
    Y1.append(ellips1(p=3, e=0.65, fi=i)[1])
    Y2.append(ellips2(p1=1.9, e1=0.65, fi=i)[1])
    Y3.append(ellips3(p2=0.7, e2=0.58, fi=i)[1])
    Y4.append(ellips4(p3=0.1, e3=0.51, fi=i)[1])
    figur.set_data(ellips1(p=3, e=0.65, fi=i))
    trajectory.set_data(X1, Y1)
    figur1.set_data(ellips2(p1=1.9, e1=0.65, fi=i))
    trajectory1.set_data(X2, Y2)
    figur2.set_data(ellips3(p2=0.7, e2=0.58, fi=i))
    trajectory2.set_data(X3, Y3)
    figur3.set_data(ellips4(p3=0.1, e3=0.51, fi=i))
    trajectory3.set_daat(X4, Y4)
    return figur,

ani = animation.FuncAnimation(fig,
                              animate,
                              frames=frames,
                              interval=50
                             )
ani.save('planet.gif')