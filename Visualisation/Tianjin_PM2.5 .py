import matplotlib
import matplotlib.pyplot as plt
num = [81, 78, 54, 49, 41, 42, 41, 26, 41, 50, 51, 61]
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
plt.bar(x, num,  label='Tianjin',color='steelblue', alpha=0.8)
plt.title("The Concentration of PM2.5 in Tianjin, 2019")
plt.xlabel("Month")
plt.ylabel("PM2.5 Concentration")
plt.legend()
plt.plot(x, num, "indianred", marker='*', ms=10)
plt.xticks(rotation=45)
plt.legend(loc="upper right")
plt.show()  
