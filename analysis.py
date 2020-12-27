# 统计分析模块
from excel_oper import getWriter

writer = getWriter('统计结果')


def analysis(df):
    # 统计销售量（例：福建省女包）
    groupSaleCount(df)
    # 去重统计销售品类
    dropDuplicates(df)
    # 统计某门店单品销售量总额
    sumByStore(df)
    # 统计某省份折扣
    discountByProvince(df)
    writer.save()


# 统计销售量
def groupSaleCount(df):
    result = df.groupby(['买家所在省份', '商品名称', '商品颜色']).count().reset_index()
    result = result[['买家所在省份', '商品名称', '商品颜色', '买家会员名']]
    result = result.rename(columns={'买家会员名': '数量'})
    # 忽略行索引
    result.to_excel(writer, '销售量', index=False)


# 去重统计销售品类
def dropDuplicates(df):
    result = df.drop_duplicates(subset=['买家所在省份', '商品名称'])
    result = result[['买家所在省份', '商品名称']]
    result = result.sort_values(by=['买家所在省份'], ascending=True)
    result.to_excel(writer, '销售品类', index=False)


# 统计某门店单品销售量总额
def sumByStore(df):
    result = df.groupby(['买家所在省份']).sum().reset_index()
    result = result[['买家所在省份', '商品价格']]
    result.to_excel(writer, '省份销售额', index=False)


# 统计某省份折扣
def discountByProvince(df):
    result = df.groupby(['买家所在省份']).sum().reset_index()
    result['折扣'] = round(result['商品价格'] / result['吊牌价格'] * 100, 2)
    result.to_excel(writer, '省份折扣', index=False)

# vlookup功能
