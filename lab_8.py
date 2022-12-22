import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='b')
trajectory, = plt.plot([], [], '-', color='g')
weels, = plt.plot([], [], '-', color='r')

frames = np.arange(0, 4.85 * np.pi, 0.06)
plt.axis('equal')
ax.set_xlim(-120, 30)
ax.set_ylim(-120, 90)

def ellips(p, ee, R, t):
    
    t = np.arange(0, np.pi * 8, 0.01)
    
    R = p / (1 + (ee * np.cos(t)))
    
    x = R * np.cos(t)
    y = R * np.sin(t)
    return x, y

def ellips_weels(p, ee, R, t):
    
    t = np.arange(0, np.pi * 8, 0.01)
    
    R = p / (1 + (ee * np.cos(t)))
    
    x = R * np.cos(t)
    y = R * np.sin(t)
    return x, y

X, Y = [], []
R = 1

def animate(i):
    X.append(ellips(p = 1, ee = 0.9, R=R, t=i)[0])
    Y.append(ellips(p = 1, ee = 0.9, R=R, t=i)[1])
    ball.set_data(ellips(p = 1, ee = 0.9, R=R, t=i))
    trajectory.set_data(X, Y)
    weels.set_data(ellips_weels(10, 0.9, R, t=i))

ani = animation.FuncAnimation(fig, animate, frames=frames, interval=30)
ani.save('lab_7_dop_1.gif')