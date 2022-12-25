import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

figur, = plt.plot([], [], 'o', color='brown')
figur1, = plt.plot([], [], 'o', color='red')

R1=1.496*10**8
T1=3.156*10**7
R2=3.844*10**7
T2=2.36*10**6
N=1000.0

def X(R1, T1, t):
         return R1*np.cos(2*np.pi*t/T1)
def Y(R1, T1, t):
         return R1*np.sin(2*np.pi*t/T1)
def x(R2, T2, t):
         return R2*np.cos(2*np.pi*t/T2)
def y(R2, T2, t):
         return R2*np.sin(2*np.pi*t/T2)

t=[T1*i/N for i in np.arange(0,N,1)]

def animate(i):
    
    figur1.set_data(X(R1=R1, T1=T1, t=i))
    XG=X+x
    YG=Y+y
    plt.plot(X, Y)
    plt.plot(XG,YG)
    plt.savefig('4.png')