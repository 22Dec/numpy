import matplotlib.pyplot as plt

plt.figure()
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 3, 4, 2, 5, 8, 6]
left,bottom,width,height=.1,.1,.8,.8
ax1=plt.axes([left,bottom,width,height])
ax1.plot(x,y,'b')
ax1.set_title("title")
ax2=plt.axes([.2,.6,.25,.25])
ax2.plot(x,y)

ax3=plt.axes([.6,.2,.25,.25])
ax3.plot(y[::-1],x)

plt.show()