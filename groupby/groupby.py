import pandas as pd
import numpy as np

df = None


class GroupBy():

    def __init__(self, dfr):
        global df
        df = dfr

    def agg(self):
        # 统计平均值和总数，按平均值升序排序
        res = df.groupby(['意向购车点']).agg(平均值=pd.NamedAgg(column='到店次数', aggfunc='mean'), 总数=pd.NamedAgg(column='到店次数', aggfunc='sum')).reset_index().sort_values(by='总数', ascending=True)
        res = res[res['总数'] > 0]
        # 多样统计
        res = df.groupby(['意向购车点']).agg({'到店次数': [np.mean, 'sum']}).reset_index()
        # print(res['到店次数']['sum'])

    def lamda(self):
        res = df.groupby(['意向购车点'])['到店次数'].apply(np.mean)
        res = df.groupby(['意向购车点']).apply(lambda x: x['到店次数'] * 10).reset_index()
        # print(res)

    def transform(self):
        # 想使用原数组的 index 的话 transform
        res = df.groupby(['意向购车点'])['到店次数'].transform('count')
        print(res)


# 一定写在类后面
if __name__ == '__main__':
    # 获取数据
    df = pd.read_excel(r'D:\PycharmProjects\first\46705工单数据.xlsx')
    # 分组 统计数量
    res = df.groupby(['意向购车点'])['门店线索编号'].count().reset_index(name='数量')
    groupBy = GroupBy(df)
    # 统计
    groupBy.agg()
    # lamda
    groupBy.lamda()
    # transform
    groupBy.transform()
