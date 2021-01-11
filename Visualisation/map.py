from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType
c = (
        Geo()
        .add_schema(maptype="china")
        .add(            "",
            [("武汉", 30042), ("深圳", 309), ("郑州", 94), ("杭州", 99), ("湖南", 171), ("合肥", 132),("南昌", 149),("南京",66),("重庆",413),("青岛",39),("成都",88),("哈尔滨",143),("北京",295),("上海",257),("福州",49),("石家庄",23),("西安",99),("南宁",34),("海口",19),("昆明",40),("贵阳",30),("太原",15),("沈阳",21),("天津",99),("兰州",19),("长春",31),("银川",20),("乌鲁木齐",19),("呼和浩特",7),("香港",48),("台湾",17),("西宁",7),("澳门",8),("拉萨",1)],
            type_=ChartType.EFFECT_SCATTER,
            color="green",
        )
        .add(            "geo",
            [("武汉", "上海"), ("武汉", "北京"),("武汉", "杭州"),("武汉", "重庆"),("武汉", "哈尔滨"),("武汉", "成都"),("武汉", "南京"),("武汉","广州"),("武汉","天津"),("武汉","西安")],
            type_=ChartType.LINES,
            effect_opts=opts.EffectOpts(
                symbol=SymbolType.ARROW, symbol_size=4, color="blue"
            ),
            linestyle_opts=opts.LineStyleOpts(curve=0.2),
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title="全国新冠病毒确诊数及武汉航班情况"))
    )

c.render()
