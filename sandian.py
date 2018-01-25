import numpy as np
import matplotlib.pyplot as plt
n=1024
x=np.random.normal(0,1,n)
y=np.random.normal(0,1,n)
t=np.arctan2(x,y)
plt.figure(num='1')
plt.scatter(x,y,s=60,c=t,alpha=70)
plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)
plt.xticks(())
plt.yticks(())

plt.figure(num=2)
plt.scatter(np.arange(20),np.linspace(-5,5,20),s=60)
plt.show()
