# 构造数据，整合各种操作
import time
import random
from mysql_oper import insert, query
from sale_info import SaleInfo
from excel_oper import readTemplate, writeExcel, common_merge_excel
from analysis import analysis

db = 2
dbOrExcel = 1
provinces = ('福建', '广州', '上海', '海南', '北京')
goods = ('女包', '拎包', '手拿包', '钱包')
colors = ('红', '黄', '蓝', '绿')
discounts = (0.5, 0.6, 0.7, 0.9)
prices = (200, 250, 220, 280, 500, 1000)
# 每个省份最多生成几条数据
perProvinceCount = 500
data = []

class mainPy():
    def __init__(self, where):
        global dbOrExcel
        dbOrExcel = where
        # 构造随机条数数据
        provinceNum = random.randint(100, perProvinceCount)
        print(provinceNum)
        for i in range(provinceNum):
            buy = 'mjhy' + str(i)
            province = provinces[random.randint(0, len(provinces) - 1)]
            good = goods[random.randint(0, len(goods) - 1)]
            color = colors[random.randint(0, len(colors) - 1)]
            price = prices[random.randint(0, len(prices) - 1)]
            discount = discounts[random.randint(0, len(discounts) - 1)]
            discountPrice = price * discount
            data.append(SaleInfo(buy, province, good, color, price, discountPrice))

    # 决定写数据库还是写excel
    def write(self):
        if(dbOrExcel == db):
            self.writeDB()
        else:
            df = readTemplate()
            # 将数据转成excel
            for info in data:
                row = [info.buy, info.province, info.good, info.color, info.discountPrice, info.price]
                df.loc[len(df)] = row
            now = time.strftime('%Y%m%d-%H%M%S')
            writeExcel(df, now)

    def writeDB(self):
        now = time.strftime('%Y-%m-%d-%H:%M:%S')
        sql = 'insert into t_sale_info(buy, province, good, color, price, discount_price, create_time) values '
        for info in data:
            sql += '('
            sql += '\'' + info.buy + '\', '
            sql += '\'' + info.province + '\', '
            sql += '\'' + info.good + '\', '
            sql += '\'' + info.color + '\', '
            sql += str(info.price) + ', '
            sql += str(info.discountPrice) + ', '
            sql += '\'' + now + '\''
            sql += '),'
        sql = sql[:len(sql) - 1]
        insert(sql)

    # 统计分析
    def analysis(self):
        df = readTemplate()
        if(dbOrExcel == db):
            res = query('select * from t_sale_info')
            for re in res:
                row = [re[1], re[2], re[3], re[4], re[6], re[5]]
                df.loc[len(df)] = row
        else:
            df = common_merge_excel()
        # 分析
        analysis(df)

if __name__ == '__main__':
    # 构造数据，excel = 1，db = 2，默认excel
    buildable = mainPy(1)
    # 写入db或excel，参数db or excel
    # buildable.write()
    # 从db或excel统计分析，参数db or excel
    buildable.analysis()