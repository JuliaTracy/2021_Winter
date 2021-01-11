from pyecharts import Map
region_distribution = {'蓟县': 45, '宝坻区': 51, '武清区': 52, '南开区': 50, '滨海新区': 50, '西青区': 51, '静海县': 52, '和平区': 53 ,'红桥区': 55, '河东区': 51,'津南区': 52, '北辰区': 53, '东丽区': 51, '河北区': 50, '河西区': 51, '宁河县': 53}
region=list(region_distribution.keys())
values=list(region_distribution.values())
map = Map("天津地图",'天津市', width=1200, height=600)
map.add('天津', region, values, visual_range=[45, 55], maptype='天津', is_visualmap=True, visual_text_color='#000')
map.show_config()
map.render(path="天津地图.html")
