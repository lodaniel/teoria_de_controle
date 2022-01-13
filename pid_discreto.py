import numpy as np
import matplotlib.pyplot as plt
tfinal=10
T=0.1
N=int(tfinal/T)
t=np.linspace(0,tfinal,N)
t[1]=T
t[2]=2*T
y=np.linspace(0,tfinal,N)
y[1]=0
y[2]=0
u=np.linspace(0,tfinal,N)
u[1]=0
u[2]=0
r0=1
r=np.linspace(0,tfinal,N)
r[1]=1
r[2]=1
e=np.linspace(0,tfinal,N)
e[1]=r[1]-y[1]
e[2]=r[2]-y[2]
Kp=2
Ti=2
Td=.3
C0=Kp*(1+Td/T)
C1=-Kp*(1+2*Td/T-T/Ti)
C2=Kp*Td/T
for k in range(3,N):
    t[k]=k*T
    r[k]=1
    y[k]=1.905*y[k-1]-0.9048*y[k-2]+0.004837*u[k-1]+0.004679*u[k-2]
    e[k]=r[k]-y[k]
    u[k]=u[k-1]+C0*e[k]+C1*e[k-1]+C2*e[k-2]
plt.stem(t,r,linefmt='blue',markerfmt='D')
plt.stem(t,y,linefmt='green')
plt.show()

