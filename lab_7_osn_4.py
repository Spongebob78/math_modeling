from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ball, = plt.plot([], [], '.', color='b')

plt.axis('equal')

x = []
y = []

y0=0.1
x0=0.1
C=0.3
D=0.33
frames = 100
edge = 1

for n in range(100):
    xn = x0**2 - y0 ** 2+ C 
    yn = 2 * x0 * y0 + D 


    x.append(xn)
    y.append(yn)

    x0 = xn
    y0 = yn

ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
def animate(i):
    ball.set_data(x[:i], y[:i])
    
ani = FuncAnimation(fig, animate, frames=frames, interval=30)
ani.save('lab_7_osn_4.gif')
