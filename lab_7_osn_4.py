from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
figure, = plt.plot([], [], '-', color='b')

plt.axis('equal')


def fraktal(y0, x0, C, D):
    x = (x0**2) - (y0**2) + C
    y = 2 * x0 * y0 + D
    return x, y

x1 = []
y1 = []

def animate(i):
    x1.append(fraktal(i)[])
    y1.append(fraktal(i)[])
    figure.set_data(fraktal(y0=0.1, x0=0.1, C=0.3, D=0.33))
    
ani = FuncAnimation(fig,
                              animate,
                              frames=100,
                              interval=30
                             )
 
ani.save('lec_7_osn_4.gif')