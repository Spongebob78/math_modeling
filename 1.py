import matplotlib.pyplot as plt
import numpy as np

R1=1.496*10**8
T1=3.156*10**7
R2=3.844*10**7
T2=2.36*10**6
N=1000.0

def XY(t):
    X1 = R1*np.cos(2*np.pi*t/T1)
    Y1 = R1*np.sin(2*np.pi*t/T1)
    return X1, Y1 
def xy(t):
    x1 = R2*np.cos(2*np.pi*t/T2)
    y1 = R2*np.sin(2*np.pi*t/T2)
    return x1, y1

XX1, YY1 = [], []
xx1, yy1 = [], []

t=[T1*i/N for i in np.arange(0,N,1)]

XX1=np.array([XY(w) for w in t])
YY1=np.array([XY(w) for w in t])
xx1=np.array([xy(w) for w in t])
yy1=np.array([xy(w) for w in t])

XG=XX1+xx1
YG=YY1+yy1

plt.plot(XX1, YY1)
plt.plot(XG, YG)
plt.savefig('1.png')
