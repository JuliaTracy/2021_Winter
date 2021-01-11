import matplotlib
import matplotlib.pyplot as plt
num = [51, 53, 52, 48, 37, 39, 37, 23, 36, 40, 44, 44]
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
plt.bar(x, num,  label='Beijing',color='steelblue', alpha=0.8)
plt.title("The Concentration of PM2.5 in Beijing, 2019")
plt.xlabel("Month")
plt.ylabel("PM2.5 Concentration")
plt.legend()
plt.plot(x, num, "indianred", marker='*', ms=10)
plt.xticks(rotation=45)
plt.legend(loc="upper right")
plt.show()  
