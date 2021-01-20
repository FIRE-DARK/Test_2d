import numpy as np
import matplotlib.pyplot as plt


plt.axis('on')
plt.grid(True)
plt.axis([-150,150,150,-150])





#Rectangulo
plt.plot([-60,60],[-45,-45],linewidth=2,color='k')
plt.plot([60,60],[-45,45],linewidth=2,color='k')
plt.plot([60,-60],[45,45],linewidth=2,color='k')
plt.plot([-60,-60],[45,-45],linewidth=2,color='k')

#rectangulo 2
plt.plot([-.5,119.5],[-.5,-.5],linewidth=2,color='k')
plt.plot([120,120],[-.5,80],linewidth=2,color='k')
plt.plot([119.5,-.5],[80,80],linewidth=2,color='k')
plt.plot([-.5,-.5],[.5,80],linewidth=2,color='k')

xc=0
yc=0
r=25
p1=0*np.pi/180
p2=360*np.pi/180
dp=(p2-p1)/100

xlast=xc+r*np.cos(p1)
ylast=yc+r*np.sin(p1)
plt.axes().set_aspect('equal')

for p in np.arange(p1,p2+dp,dp):
    xp=xc+r*np.cos(p)
    yp=yc+r*np.sin(p)
    plt.plot([xlast,xp],[ylast,yp],color='y',linewidth=2)
    xlast=xp
    ylast=yp

plt.show()
