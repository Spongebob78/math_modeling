import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

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


X=np.array([X(w) for w in t])
Y=np.array([Y(w) for w in t])
x=np.array([x(w) for w in t])
y=np.array([y(w) for w in t])
XG=X+x
YG=Y+y
plt.figure()
plt.axis([-2.0*10**8,2.0*10**8,-2.0*10**8,2.0*10**8])
plt.plot(X,Y)
plt.plot(XG,YG)

