#post方法的demo
import requests

#json：字典格式{"username":"abc","passwd","123456"}
url = "http://132.232.44.158:5000/userLogin/"#接口地址
data = {"username":"test", "password":"123456", "captcha":"123456"}

res = requests.post(url = url,json=data)#向url接口使用post方法传递data的json数据
print(res.text)#打印返回值

#form-data:推荐用postman生成代码来实现