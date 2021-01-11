from pyecharts import Map
region_distribution = {'密云县': 59, '怀柔区': 34, '门头沟区': 36, '延庆县': 36, '昌平区': 37, '平谷区': 39, '海淀区': 40, '顺义区': 40 ,'房山区': 41, '丰台区': 41,'石景山区': 42, '朝阳区': 43, '大兴区': 44, '西城区': 44, '东城区': 44, '通州区': 45}
region=list(region_distribution.keys())
values=list(region_distribution.values())
map = Map("北京地图",'PM25浓度分布（微克/立方米）', width=1200, height=600)
map.add('北京', region, values, visual_range=[30, 45], maptype='北京', is_visualmap=True, visual_text_color='#000', is_map_symbol_show=False, is_label_show=True)
map.show_config()
map.render(path="北京地图.html")
