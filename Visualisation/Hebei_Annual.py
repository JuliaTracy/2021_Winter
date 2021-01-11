import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
x = ('保定', '唐山', '廊坊', '石家庄', '秦皇岛', '邯郸', '邢台', '张家口', '承德', '沧州', '衡水')
number = [194, 221, 235, 174, 274, 165, 175, 308, 308, 234, 200]
plt.barh(x, number)
plt.legend()
plt.xlabel('达标天数')
plt.ylabel('城市')
plt.title('2019年河北省11个城市空气质量达标天数')
plt.show()
