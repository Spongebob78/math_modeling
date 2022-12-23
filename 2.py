import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='b')
trajectory, = plt.plot([], [], '-', color='g')
weels, = plt.plot([], [], '-', color='r')

frames = np.arange(0, 4.85 * np.pi, 0.06)
plt.axis('equal')
ax.set_xlim(-1, 13)
ax.set_ylim(0, 10)


def circle_move(R, t):
    x = R * (t - np.sin(t)) 
    y = R * (1 - np.cos(t))
    return x, y

def weels_fanc(R, x0, y0, vx0, vy0, t):
    x0 = x0 + vx0 * t
    y0 = y0 + vy0 * t

    alpha = np.arange(0, 2*np.pi, 0.1)

    x = x0 + R * np.cos(alpha)
    y = y0 + R * np.sin(alpha)
    return x, y

X, Y = [], []
R = 1

def animate(i):
    X.append(circle_move(R=R, t=i)[0])
    Y.append(circle_move(R=R, t = i)[1])
    ball.set_data(circle_move(R=R, t=i))
    trajectory.set_data(X, Y)
    weels.set_data(weels_fanc(R, 0, R, 1, 0, t=i))

ani = animation.FuncAnimation(fig, animate, frames=frames, interval=30)
ani.save('lab_7_dop_1.gif')