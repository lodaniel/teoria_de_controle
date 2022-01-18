import numpy as np
import matplotlib.pyplot as plt
tfinal = 10
T = 0.1
N = int(tfinal/T)
t = np.linspace(0,tfinal,N)
t[1] = T
t[2] = 2*T
y = np.linspace(0,tfinal,N)
y[1] = 0
y[2] = 0
u = np.linspace(0,tfinal,N)
u[1] = 0
u[2] = 0
r = np.linspace(0,tfinal,N)
r[1] = 1
r[2] = 1
e = np.linspace(0,tfinal,N)
e[1] = r[1] - y[1]
e[2] = r[2] - y[2]
kp = 5.0
Ti = 2.3
Td = 0.6
C1 = kp*(1+Td/T)
C2 = kp*(-1-2*Td/T+T/Ti)
C3 = kp*Td/T
for k in range(3,N):
    t[k] = k*T
    r[k] = 1
    y[k] = 2*y[k-1]-y[k-2]+.005*u[k-1]+.005*u[k-2]
    e[k] = r[k] - y[k]
    u[k] = u[k-1] + C1*e[k] + C2*e[k-1] + C3*e[k-2]
plt.stem(t,r,linefmt='blue')
plt.stem(t,y,linefmt='green',markerfmt='D')
plt.show()
