# 数据库操作
import pymysql

conn = None
cursor = None

def connect():
    global conn
    global cursor
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='root', db='test', charset='utf8')
    cursor = conn.cursor()

def query(sql):
    print('sql:' + sql)
    connect()
    # 4.执行sql语句
    cursor.execute(sql)
    result = cursor.fetchall()
    closeConn()
    return result

def insert(sql):
    print('sql:' + sql)
    connect()
    # 4.执行sql语句
    result = cursor.execute(sql)
    conn.commit()
    closeConn()
    return result

def closeConn():
    # 5.关闭连接，游标和连接都要关闭
    cursor.close()
    conn.close()