import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-5, 5, 50)
y = np.sin(x) + np.random.rand(50)
plt.scatter(x, y)
params = np.polyfit(x, y, 3)
param_func = np.poly1d(params)
y_predict = param_func(x)
plt.scatter(x,y)
plt.plot(x, y_predict)
plt.show()

