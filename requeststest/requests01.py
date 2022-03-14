import requests                                         #导入requests
from utils.db_tools import query                                   
url = "http://www.weather.com.cn/data/sk/101010100.html"#定义变量url存放网站
res = requests.get(url)                                 #试用get方法请求网址，把获取的结果保存在一个变量res中
a = res.text                                            #获取返回值文本
# print(a)

#取返回值里面time的值
b = res.json() #把返回值转换成字典
print(b)
print(b["weatherinfo"]["time"])#取出time值

url1 = "http://132.232.44.158:8080/morning/getAllGoods"
print(requests.get(url1).text)
print(requests.get(url1).json)

res1 =requests.get(url1)
assert res1.status_code == 200
assert res1.json()["success"] == True
# 连接查询数据库
aa = query("select * from tb_goods")
assert len(aa)!=0
print(aa)

print("true")