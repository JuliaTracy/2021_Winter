import matplotlib
import matplotlib.pyplot as plt
import numpy as np
num = np.array([51, 53, 52, 48, 37, 39, 37, 23, 36, 40, 44, 44])
num1 = np.array([81, 78, 54, 49, 41, 42, 41, 26, 41, 50, 51, 61])
num2 = np.array([145, 121, 62, 52, 34, 39, 37, 27, 35, 51, 72, 83])
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
total_width, n = 0.8, 3
width = total_width / n
plt.bar(x, num, width=width, label='Beijing',color='steelblue', alpha=0.8)
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, num1, width=width, label='Tianjin', color='indianred', alpha=0.8)
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, num2, width=width, label='Shijiazhuang', color='yellow', alpha=0.8)
plt.title("The Concentration of PM2.5 in 2019")
plt.xlabel("Month")
plt.ylabel("PM2.5 Concentration(ug/m^3)")
plt.legend()  
plt.show()  
