import pymysql
'''
1、连接数据库
2、选择数据库
3、获取游标
4、增删改查
'''
def query(sql):
    '''
    数据库查询
    '''

    db = pymysql.connect(host="localhost",user="root",password="123456",db="testdb")
    cursor = db.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    db.close()
    return res

aa = query("select * from t_class;")
print(aa[1][1])

def debeishu(x,y):
    z = y*x
    return z

b = debeishu(2,16)
print(b)

def commit(sql):
    '''
    数据库修改方法
    '''

    db = pymysql.connect(host="localhost",user="root",password="123456",db="testdb")
    cursor = db.cursor()#获取游标
    try:#异常捕获，如果下面代码运行错误，则执行except的内容
        cursor.execute(sql)
        db.commit()#应用改变
        db.close()
        return True
    except:
        return "sql语句错误，请重新输入"

v = commit("insert into t_class(id,classname,teacher)values(5,'张三','菜鸡')")
print(v)