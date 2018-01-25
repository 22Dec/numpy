import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)

x=np.arange(-3,3,.25)
y=np.arange(-3,3,.25)
X,Y=np.meshgrid(x,y)
r=np.sqrt(X**2+Y**2)
Z=np.sin(r)
ax.plot_surface(X, Y, Z, rstride=2, cstride=2, cmap=plt.get_cmap('rainbow'))
ax.contourf(X,Y,Z,zdir='z',offset=-1,cmap='rainbow')
plt.show()
