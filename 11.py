import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='b')
trajectory, = plt.plot([], [], '-', color='g')

plt.axis('equal')
ax.set_xlim(-5, -13)
ax.set_ylim(-10, 10)


def ellips(R, fi, t):

    x = R * np.cos(fi)
    y = R * np.sin(fi) 
    return x, y

X, Y = [], []
fi = np.arange(0, np.pi * 1, 0.1)
R = 3 / (1 + (0.2 * np.cos(fi)))

def animate(i):
    X.append(ellips(R=R, fi=fi, t=i)[0])
    Y.append(ellips(R=R, fi=fi, t=i)[1])
    ball.set_data(ellips(R=R, fi=fi, t=i))
    trajectory.set_data(X, Y)

ani = animation.FuncAnimation(fig,
                              animate,
                              frames=100,
                              interval=30
                             )
 
ani.save('11.gif')