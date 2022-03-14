import pymysql

# db = pymysql.connect(host="192.144.148.91",user="root",password="1qaz!QAZ",db="testdb")
# cursor = db.cursor()
# cursor.execute("show tables;")
# res = cursor.fetchall()
# #print(res)


def query(sql):
    '''
    这是数据库的查询方法
    '''
    db = pymysql.connect(host="122.51.207.203",user="root",password="123456",db="db_morning")
    cursor = db.cursor()  # 获取游标
    try:
        cursor.execute(sql)  # 执行SQL
        res = cursor.fetchall()  # 获取所有结果
        db.close()  # 关闭数据库连接
        return(res)
    except:
        print("辣鸡！sql语句写错了！")


def gaibian(sql):
    '''
    数据库的修改，新增，删除的方法
    '''
    db = pymysql.connect(host="122.51.207.203",user="root",password="123456",db="db_morning")
    cursor.execute(sql)
    db.commit()  # 应用/提交
    db.close()


# query("select * from t_class;")
# query("select * from t_student;")
# print(query(" tables;","ljtestdb"))
# query("desc t_class;")
