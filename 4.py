import matplotlib.pyplot as plt
import numpy as np

R1=1.496*10**8
T1=3.156*10**7
R2=3.844*10**7
T2=2.36*10**6
N=1000.0

def X(t):
         return R1*np.cos(2*np.pi*t/T1)
def Y(t):
         return R1*np.sin(2*np.pi*t/T1)
def x(t):
         return R2*np.cos(2*np.pi*t/T2)
def y(t):
         return R2*np.sin(2*np.pi*t/T2)

t=[T1*i/N for i in np.arange(0,N,1)]

X=np.array([X(a) for a in t])
Y=np.array([Y(a) for a in t])
x=np.array([x(a) for a in t])
y=np.array([y(a) for a in t])

XG=X+x
YG=Y+y
plt.plot(X, Y)
plt.plot(XG,YG)
plt.savefig('4.png')
