import matplotlib.pyplot as plt
import numpy as np
n=12
x=np.arange(n)
y1=(1-x/float(n))*np.random.uniform(.5,1,n)

y2=(1-x/float(n))*np.random.uniform(.5,1,n)

plt.bar(x,y1, facecolor='#9999ff', edgecolor='white')
plt.bar(x,-y2, facecolor='#ff9999', edgecolor='white')

for i,j in zip(x,y1):
    plt.text(i+0.1,j+0.03,'%.2f'%j,ha='center',va='bottom')
for i,j in zip(x,y2):
    plt.text(i+0.1,-j-0.1,'%.2f'%j,ha='center',va='bottom')
plt.xlim(-1,n)
plt.ylim(-1,1)
plt.xticks(())
plt.yticks(())
plt.show()
