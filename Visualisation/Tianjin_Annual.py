import numpy as np  
import matplotlib.mlab as mlab  
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
labels=['优良','轻、中度污染','重度污染']
X=[219, 131, 15]  
fig = plt.figure()
plt.pie(X,labels=labels,autopct='%1.2f%%')
plt.title("天津市2019年空气质量情况")
plt.show()
