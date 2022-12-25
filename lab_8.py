import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='b')
trajectory, = plt.plot([], [], '-', color='black')

frames = np.arange(0, 4.85 * np.pi, 0.06)
plt.axis('equal')
ax.set_xlim(-1, 13)
ax.set_ylim(0, 10)


def circle_move(R, alpha):
    x = R * np.cos(alpha)
    y = R * np.sin(alpha)
    return x, y

X, Y = [], []
R = 0.3
alpha = np.arange(-2*np.pi, 2*np.pi, 0.1)


def animate(i):
    X.append(circle_move(R=R, alpha=i)[0])
    Y.append(circle_move(R=R, alpha= i)[1])
    ball.set_data(circle_move(R=R, alpha=i))
    trajectory.set_data(X, Y)

ani = animation.FuncAnimation(fig, animate, frames=frames, interval=30)
ani.save('lab_7_dop_1.gif')