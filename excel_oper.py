# excel操作模块
import os
import time

import pandas as pd
import glob

root = "D:/pythonProject/excel_demo"
saveRoot = "D:/pythonProject/excel_demo/results/"


def readTemplate():
    file_path = root + "/" + "销售数据模板.xls"
    df = pd.read_excel(file_path)
    return df


def writeExcel(df, filename):
    writer = pd.ExcelWriter(filename + '.xls')
    df.to_excel(writer, 'sheet1')
    writer.save()

# 定义writer
def getWriter(filename):
    if not os.path.exists(saveRoot):
        os.makedirs(saveRoot)
    now = time.strftime('%Y%m%d-%H%M%S')
    writer = pd.ExcelWriter(saveRoot + filename + now + '.xls')
    return writer

# 公共的合并表格函数
def common_merge_excel():
    file_list = []

    """
    用glob模块可以查找符合特定规则的文件路径名
    查找文件只用到三个匹配符："*", "?", "[]"
    "*"匹配0个或多个字符；"?"匹配单个字符；"[]"匹配指定范围内的字符，如：[0-9]匹配数字
    """
    files = glob.glob(root + "\*.xls")  # 查找并返回所有.xls文件名
    for file_name in files:
        if(not file_name.endswith('销售数据模板.xls')):
            file_list.append(file_name)
    res = pd.read_excel(file_list[0])
    for i in range(1, len(file_list)):
        A = pd.read_excel(file_list[i])
        # 拼接表并排序
        res = pd.concat([res, A], ignore_index=False, sort=True)
    return res