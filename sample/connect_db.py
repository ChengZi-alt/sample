# -*- coding:utf-8 -*-

import pymysql


# 指定数据库名和表名即从mysql中读取数据
def LoadData(db, sql):
    conn = pymysql.connect(host='172.16.10.161',port=3306,user='root',password='root',db=db,charset='utf8')
    with conn.cursor() as cur:
        cur.execute(sql)
        Result = cur.fetchall()
    return Result


# 获取事件Items
def GetItems():
    #---------------------------------数据库名称---------------------------------
    db = "bbg"
    ##----------------------------指定数据库中的表名-----------------------------
    sql = "Select GROUP_CONCAT(subclass) as subclass_id from bbg.cat; "
    dataset = LoadData(db, sql)
    # print(dataset)
    # 将获取的事件具体信息的格式由元组改为列表
    DataSet = ('1','2')
    for data in dataset:
        for i in data:
            DataSet01 = i.split(',')
            DataSet = tuple(set(DataSet01))
    DataSet = set(DataSet)
    print(DataSet)
    return DataSet

# 获取事件ISample
def GetSample():
    #---------------------------------数据库名称---------------------------------
    db = "tmp"
    ##----------------------------指定数据库中的表名-----------------------------
    sql = "select subclass_id from  tmp.tran_seq_no_subclass_id "
    dataset = LoadData(db, sql)
    # print(dataset)
    # 将获取的事件具体信息的格式由元组改为列表
    DataSet = []

    for data in dataset:
        for i in data:
            datasettmp = []
            datasettmp =set(i.split(','))
            # print(datasettmp)
            DataSet.append(datasettmp)
    # print(DataSet)
    return DataSet

if __name__ ==  '__main__':
    GetItems()
