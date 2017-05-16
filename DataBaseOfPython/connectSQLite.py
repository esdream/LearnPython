# -*- coding: utf-8 -*-
import sys, os, sqlite3

def init_dbfile(dbName):
    db_file = os.path.join(os.path.dirname(__file__), dbName)
    if(os.path.isfile(db_file)):
        os.remove(db_file)

    # 初始数据
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    try:
        cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
        cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
        cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
        cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
        conn.commit()
    except:
        pass
    finally:
        cursor.close()
        conn.close()

def get_score_in(dbName, low, high):
    '返回指定分数区间的名字，按分数从低到高排序'
    conn = sqlite3.connect(dbName)
    cursor = conn.cursor()
    try:
        cursor.execute(r"select * from user where score > ? and score < ? order by score desc", (low, high))
        values = cursor.fetchall()
        conn.commit()
    except:
        pass
    finally:
        cursor.close()
        conn.close()
        return values

if(__name__ == '__main__'):
    dbFile = 'MyData.db'
    init_dbfile(dbFile)
    print(get_score_in(dbFile, 20, 100))
