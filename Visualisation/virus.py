from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
y = [291, 440, 571, 830, 1287, 1975, 2744, 4535, 5597, 7736, 9720, 11821, 14111, 17238, 20471, 24363, 28060, 31211, 34598, 37251, 40235]
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
yd = [54, 37, 393, 1072, 1965, 2684, 5794, 6973, 9239, 12167, 15238, 17988, 19544, 21558, 23214, 23260, 24702, 26359, 27657, 28942, 23589]
xd = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
zd = [27, 26, 257, 680, 1118, 1309, 3806, 2077, 3248, 4148, 4812, 5019, 4562, 5173, 5072, 3971, 5328, 4833, 4214, 3916, 4008]
z = [77, 149, 131, 259, 444, 688, 776, 1774, 1462, 1739, 1985, 2104, 2591, 2831, 3235, 3893, 3697, 3151, 3401, 2657, 3073]
fig = plt.figure()
ax = Axes3D(fig)
ax.plot(x, y, z, c='r', label='Confirmed')
ax.plot(xd, yd, zd, c='g', label='Suspected')
ax.legend(loc='best')
ax.set_xlabel('Time',fontdict={'size': 15, 'color': 'red'})
ax.set_ylabel('Current',fontdict={'size': 15, 'color': 'red'})
ax.set_zlabel('Increase',fontdict={'size': 15, 'color': 'red'})
plt.show()

           
