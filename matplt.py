import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-3,3,50)
y1=x**2
y2=2*x+1
plt.figure()
##坐标轴进行备注
plt.xlim((-1,2))
ticks=np.linspace(-1,2,5)
plt.xticks(ticks)
plt.yticks([-6,-4,-1.5,2,8],['really bad','bad','normal','good','really good'])
plt.xlabel('yang')
plt.ylabel('yang2')
##坐标轴调整
ax=plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

plt.plot(x,y1,color='red',linestyle='--',label='yang1')
plt.plot(x,y2,label='yang2')
plt.legend(labels=['quxian','zhixian'],loc='best')##legend线名称
##annotate标注
x0=1.25
y0=2*x0+1
plt.scatter(x0,y0,s=50)
plt.plot([x0,x0],[y0,0],'k--',linewidth=2)
plt.annotate(r'2x+1=%s'%y0,xy=(x0,y0),xycoords='data',xytext=(+30,-30),
             textcoords='offset points',fontsize=10,
             arrowprops=dict(arrowstyle='->',connectionstyle="arc3,rad=.2"))
plt.show()