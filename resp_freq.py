!pip install control
from control import *
import matplotlib.pyplot as plt
g=tf([1],[1,0.5,1])
bode_plot(g, dB=True);
g=tf([1],[1,2,1])
nyquist_plot(g),plt.grid()
g=tf(1,[1,2,3,4,0])
nichols_plot(g)
from control.pzmap import pzmap
g=tf([1,1],[1,2,3,4,0])
g.pole()
g.zero()
pzmap(g)
g=tf(1,[1,2,3,0])
rlocus(g);
