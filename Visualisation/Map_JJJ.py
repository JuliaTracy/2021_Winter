from pyecharts import Map
city1=['北京']
values1=[42]
city2=['天津']
values2=[51]
region_distribution = {'保定市': 59, '唐山市': 54, '廊坊市': 46, '石家庄市': 63, '秦皇岛市': 41, '邯郸市': 66, '邢台市': 65, '张家口市': 26 ,'承德市': 29, '沧州市': 50,'衡水市': 56}
region=list(region_distribution.keys())
values=list(region_distribution.values())
map = Map("京津冀地图",'京津冀', width=1200, height=600)
map.add('北京', city1, values1, visual_range=[1, 10], maptype='北京', is_visualmap=True, visual_text_color='#000', is_label_show=True)
map.add('天津', city2, values2, visual_range=[1, 10], maptype='天津', is_visualmap=True, visual_text_color='#000', is_label_show=True)
map.add('河北', region, values, visual_range=[20, 70], maptype='河北', is_visualmap=True, visual_text_color='#000')
map.show_config()
map.render(path="京津冀地图.html")
