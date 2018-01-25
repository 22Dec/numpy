import matplotlib.pyplot as plt
import numpy as np
n=256
x=np.linspace(-3,3,n)
y=np.linspace(-3,3,n)
def f(x,y):
    return (1 - x / 2 + x**5 + y**3) * np.exp(-x**2 -y**2)


X,Y=np.meshgrid(x,y)
plt.contourf(X,Y,f(X,Y),10,alpha=0.7,cmap=plt.cm.hot)
C=plt.contour(X,Y,f(X,Y),10,colors='black',linwidth=0.5)

plt.clabel(C,inline=True,fontsize=10)













plt.xticks(())
plt.yticks(())
plt.show()