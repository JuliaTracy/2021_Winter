import matplotlib
import matplotlib.pyplot as plt
num = [6, 9, 17, 25, 41, 56, 80, 106, 132, 170, 213, 259, 304, 361, 425, 490, 563, 636, 722, 811, 908, 1016]
num1 = [25, 25, 25, 34, 38, 49, 51, 60, 103, 124, 171, 243, 328, 475, 632, 892, 1153, 1540, 2050, 2649, 3281, 3996]
ratio=[0.0]*22
for i in range(len(num)):
    ratio[i]=num[i]/(num[i]+num1[i])
x = list(range(len(num)))
plt.bar(x, ratio,  label='Risk',color='steelblue', alpha=0.8)
plt.title("Hospitalisation Fatality Risk From Jan 20th to Feb 12rd")
plt.xlabel("Days")
plt.ylabel("Risk")
plt.legend()
plt.plot(x, ratio, "indianred", marker='*', ms=10)
plt.xticks(rotation=45)
plt.legend(loc="upper left")
plt.show()  
