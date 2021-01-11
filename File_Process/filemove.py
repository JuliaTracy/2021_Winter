import shutil
import os

def remove_file(old_path, new_path):
    print(old_path)
    print(new_path)
    filelist = os.listdir(old_path) #列出该目录下的所有文件,listdir返回的文件列表是不包含路径的。
    #print(filelist)
    #filelist=["南阳市_10.txt", "平顶山市_10.txt", "三门峡市_10.txt", "商丘市_10.txt", "新乡市_10.txt", "信阳市_10.txt", "许昌市_10.txt", "郑州市_10.txt", "周口市_10.txt", "驻马店市_10.txt", "恩施土家族苗族自治州_10.txt", "鄂州市_10.txt", "黄冈市_10.txt", "黄石市_10.txt", "荆门市_10.txt", "荆州市_10.txt", "潜江市_10.txt", "神农架林区_10.txt", "十堰市_10.txt", "随州市_10.txt", "天门市_10.txt", "武汉市_10.txt", "咸宁市_10.txt", "仙桃市_10.txt", "孝感市_10.txt", "宜昌市_10.txt", "常德市_10.txt", "长沙市_10.txt", "郴州市_10.txt", "衡阳市_10.txt", "怀化市_10.txt", "娄底市_10.txt", "邵阳市_10.txt", "湘潭市_10.txt", "湘西土家族苗族自治州_10.txt", "益阳市_10.txt", "永州市_10.txt", "岳阳市_10.txt", "张家界市_10.txt", "株洲市_10.txt", "常州市_10.txt", "淮安市_10.txt", "连云港市_10.txt", "南京市_10.txt", "南通市_10.txt", "宿迁市_10.txt", "苏州市_10.txt", "泰州市_10.txt", "无锡市_10.txt", "徐州市_10.txt", "盐城市_10.txt", "扬州市_10.txt", "镇江市_10.txt", "抚州市_10.txt", "赣州市_10.txt", "吉安市_10.txt", "景德镇市_10.txt", "九江市_10.txt", "南昌市_10.txt", "萍乡市_10.txt", "上饶市_10.txt", "新余市_10.txt", "宜春市_10.txt", "鹰潭市_10.txt", "白城市_10.txt", "白山市_10.txt", "长春市_10.txt", "吉林市_10.txt", "辽源市_10.txt", "四平市_10.txt", "松原市_10.txt", "通化市_10.txt", "延边朝鲜族自治州_10.txt", "鞍山市_10.txt", "本溪市_10.txt", "朝阳市_10.txt", "大连市_10.txt", "丹东市_10.txt", "抚顺市_10.txt", "阜新市_10.txt", "葫芦岛市_10.txt", "锦州市_10.txt", "辽阳市_10.txt", "盘锦市_10.txt", "沈阳市_10.txt", "铁岭市_10.txt", "阿拉善盟_10.txt", "包头市_10.txt", "巴彦淖尔市_10.txt", "赤峰市_10.txt", "呼和浩特市_10.txt", "呼伦贝尔市_10.txt", "鄂尔多斯市_10.txt", "通辽市_10.txt", "乌兰察布市_10.txt", "乌海市_10.txt", "锡林郭勒盟_10.txt", "兴安盟_10.txt", "固原市_10.txt", "石嘴山市_10.txt", "吴忠市_10.txt", "银川市_10.txt", "中卫市_10.txt", "果洛藏族自治州_10.txt", "玉树藏族自治州_10.txt", "海北藏族自治州_10.txt", "海南藏族自治州_10.txt", "海西蒙古族藏族自治州_10.txt", "黄南藏族自治州_10.txt", "西宁市_10.txt", "安康市_10.txt", "宝鸡市_10.txt", "汉中市_10.txt", "商洛市_10.txt", "铜川市_10.txt", "渭南市_10.txt", "西安市_10.txt", "咸阳市_10.txt", "襄樊市_10.txt", "海东地区_10.txt"]
    for file in filelist:
        src = os.path.join(old_path, file)
        dst = os.path.join(new_path, file)
        print('src:', src)
        print('dst:', dst)
        shutil.move(src, dst)

if __name__ == '__main__':
    remove_file(r"F:\科研\实验室\11.23\prediction\输入数据\2年\2_241-342", r"F:\科研\实验室\11.23\prediction\输入数据\2年")
