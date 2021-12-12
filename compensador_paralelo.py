from control import *
import numpy as np
import matplotlib.pyplot as plt
rlocus(tf([1,0],[1, 5, 4, 20]))
x=np.linspace(-3,0, 1000)
a=np.tan(np.pi-np.arccos(0.4))
y=a*x
plt.plot(x,y)
plt.show()    
