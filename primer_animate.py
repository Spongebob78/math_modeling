import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='b')
trajectory, = plt.plot([], [], '-', color='g')

frames = np.arange(0, 4.85 * np.pi, 0.06)
plt.axis('equal')

def circle_move(R, t):
    x = R * np.cos(t)
    y = R * np.sin(t)
    return x, y


X, Y = [], []
R = 1 

def animate(i):
    X.append(circle_move(R=R, t=i)[0])
    Y.append(circle_move(R=R, t = i)[1])
    ball.set_data(circle_move(R=R, t=i))
    trajectory.set_data(X, Y)

ani = animation.FuncAnimation(fig, animate, frames=frames, interval=30)
ani.save('lab_7_dop_2.gif')