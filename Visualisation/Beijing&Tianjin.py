from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
y = [51, 53, 52, 48, 37, 39, 37, 23, 36, 40, 44, 44]
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
z = [81, 78, 54, 49, 41, 42, 41, 26, 41, 50, 51, 61]
xd = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
zd = [114, 110, 85, 90, 103, 127, 121, 79, 103, 88, 86, 95]
yd = [81, 80, 85, 84, 93, 121, 108, 72, 97, 68, 76, 73]
fig = plt.figure()
ax = Axes3D(fig)
ax.plot(x, y, z, c='r', label='PM2.5')
ax.plot(xd, yd, zd, c='g', label='AQI')
ax.legend(loc='best')
ax.set_xlabel('Month',fontdict={'size': 15, 'color': 'red'})
ax.set_ylabel('Beijing',fontdict={'size': 15, 'color': 'red'})
ax.set_zlabel('Tianjin',fontdict={'size': 15, 'color': 'red'})
plt.show()

           
