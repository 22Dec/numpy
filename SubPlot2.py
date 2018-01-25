import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

plt.figure()
gs=gridspec.GridSpec(3,3)
ax1=plt.subplot(gs[0,:])
ax2=plt.subplot(gs[1,:2])
ax3=plt.subplot(gs[1:,2])
ax4=plt.subplot(gs[-1,0])
ax5=plt.subplot(gs[-1,1])
ax1.plot([0,3],[1,2],linestyle='--')
ax1.set_title('yang')
plt.show()