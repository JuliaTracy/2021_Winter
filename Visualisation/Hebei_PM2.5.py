import matplotlib
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif']=['SimHei']
num = np.array([59, 54, 46, 63, 41, 66, 65, 26, 29, 50, 56])
x = ['保定', '唐山', '廊坊', '石家庄', '秦皇岛', '邯郸', '邢台', '张家口', '承德', '沧州', '衡水']
width = 0.8
plt.bar(x, num, width=width, label='PM2.5 Concentration',color='steelblue', alpha=0.8)
plt.title("The Concentration of PM2.5 of Cities in Hebei Province, 2019")
plt.xlabel("City in Hebei Province")
plt.ylabel("PM2.5 Concentration(ug/m^3)")
plt.legend()  
plt.show()  
