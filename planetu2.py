import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
figur, = plt.plot([], [], 'o', color='brown')
figur1, = plt.plot([], [], 'o', color='red')
figur2, = plt.plot([], [], 'o', color='blue')
figur3, = plt.plot([], [], 'o', color='darkred')
trajectory, = plt.plot([], [], '-', color='black')
trajectory1, = plt.plot([], [], '-', color='black')
trajectory2, = plt.plot([], [], '-', color='black')
trajectory3, = plt.plot([], [], '-', color='black')

frames = np.arange(0, np.pi * 2.01, 0.09)

plt.axis('equal')
ax.set_xlim(-13, 10)
ax.set_ylim(-10, 10)

def krug(R, alpha):
    x = R * np.cos(alpha)
    y = R * np.sin(alpha)
    return x, y

def krug1(R1, alpha):
    x1 = R1 * np.cos(alpha)
    y1 = R1 * np.sin(alpha)
    return x1, y1 

def krug2(R2, alpha):
    x2 = R2 * np.cos(alpha)
    y2 = R2 * np.sin(alpha)
    return x2, y2

def krug3(R3, alpha):
    x3 = R3 * np.cos(alpha)
    y3 = R3 * np.sin(alpha)
    return x3, y3    

X1, Y1 = [], []
X2, Y2 = [], []
X3, Y3 = [], []
X4, Y4 = [], []

R = 1
R1 = 2
R2 = 3
R3 = 4
alpha = np.arange(-2*np.pi, 2*np.pi, 0.1)

def animate(i):
    plt.plot([0], [0] , marker='o', color='gold')
    X1.append(krug(R=R, alpha=i)[0])
    X2.append(krug1(R1=R1, alpha=i)[0])
    X3.append(krug2(R2=R2, alpha=i)[0])
    X4.append(krug3(R3=R3, alpha=i)[0])
    Y1.append(krug(R=R, alpha=i)[1])
    Y2.append(krug1(R1=R1, alpha=i)[1])
    Y3.append(krug2(R2=R2, alpha=i)[1])
    Y4.append(krug3(R3=R3, alpha=i)[1])
    figur.set_data(krug(R=R, alpha=i))
    trajectory.set_data(X1, Y1)
    figur1.set_data(krug1(R1=R1, alpha=i))
    trajectory1.set_data(X2, Y2)
    figur2.set_data(krug2(R2=R2, alpha=i))
    trajectory2.set_data(X3, Y3)
    figur3.set_data(krug3(R3=R3, alpha=i))
    trajectory3.set_data(X4, Y4)
    return figur,

ani = animation.FuncAnimation(fig,
                              animate,
                              frames=frames,
                              interval=70,
                              repeat=True
                             )

ani.save('planet2.gif')