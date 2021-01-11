from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Map
c = (
        Map()
        .add("确诊人数", [list(z) for z in zip(['China','Canada','Brazil','United States','Russia','Japan','Thailand','South Korea','Singapore','Malaysia','Vietnam','Germany','Australia','France','Britain','United Arab Emirates','Italy','Philippines','India','Spain','Belgium','Nepal','Finland','Sweden','Sri Lanka','Cambodia'], [59885,7,1,14,2,247,33,28,50,18,16,16,15,11,9,8,3,3,3,2,1,1,1,1,1,1])], "world")
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="全球确诊患者人数"),
            visualmap_opts=opts.VisualMapOpts(max_=20),
        )
    )
c.render()
