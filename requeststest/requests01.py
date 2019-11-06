import requests                                         #导入requests
url = "http://www.weather.com.cn/data/sk/101010100.html"#定义变量url存放网站
res = requests.get(url)                                 #试用get方法请求网址，把获取的结果保存在一个变量res中
a = res.text                                            #获取返回值文本
# print(a)


#取返回值里面time的值
b = res.json() #把返回值转换成字典
print(b)
print(b["weatherinfo"]["time"])#取出time值
