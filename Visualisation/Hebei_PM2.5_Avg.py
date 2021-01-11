import matplotlib
import matplotlib.pyplot as plt
num = [95, 90, 51, 45, 33, 35, 33, 24, 34, 43, 54, 68]
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
plt.bar(x, num,  label='Hebei Province',color='steelblue', alpha=0.8)
plt.title("The Concentration of PM2.5 in Hebei Province, 2019")
plt.xlabel("Month")
plt.ylabel("PM2.5 Concentration")
plt.legend()
plt.plot(x, num, "indianred", marker='*', ms=10)
plt.xticks(rotation=45)
plt.legend(loc="upper right")
plt.show()  
