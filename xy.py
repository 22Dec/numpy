import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0, 10, 0.1)
y1 = 0.05 * x**2
y2 = -1 * y1
fig,ax1=plt.subplots()
ax2=ax1.twinx()
ax1.plot(x,y1,'b')
ax2.plot(x,y2,'g--')
ax1.set_xlabel("X Label",color='b')
ax1.set_ylabel("Y1 Label",color='b')
ax2.set_ylabel("Y2 Label",color='g')







plt.show()