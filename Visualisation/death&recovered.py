import matplotlib
import matplotlib.pyplot as plt
import numpy as np
num = np.array([6, 9, 17, 25, 41, 56, 80, 106, 132, 170, 213, 259, 304, 361, 425, 490, 563, 636, 722, 811, 908, 1016])
num1 = np.array([25, 25, 25, 34, 38, 49, 51, 60, 103, 124, 171, 243, 328, 475, 632, 892, 1153, 1540, 2050, 2649, 3281, 3996])
x = list(range(len(num)))
total_width, n = 0.8, 2
width = total_width / n
plt.bar(x, num, width=width, label='Fatal Cases',color='steelblue', alpha=0.8)
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x, num1, width=width, label='Recovered Cases', color='indianred', alpha=0.8)
plt.title("Comparison of Fatal and Recovered Cases From Jan 20th to Feb 12rd")
plt.xlabel("Days")
plt.ylabel("Number")
plt.legend()  
plt.show()  
