from pyecharts import Map
region_distribution = {'保定市': 59, '唐山市': 54, '廊坊市': 46, '石家庄市': 63, '秦皇岛市': 41, '邯郸市': 66, '邢台市': 65, '张家口市': 26 ,'承德市': 29, '沧州市': 50,'衡水市': 56}
region=list(region_distribution.keys())
values=list(region_distribution.values())
map = Map("河北地图",'河北', width=1200, height=600)
map.add('河北', region, values, visual_range=[20, 70], maptype='河北', is_visualmap=True, visual_text_color='#000')
map.show_config()
map.render(path="河北地图.html")
