import requests

url = "http://132.232.44.158:8080/morning/user/userLogin"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"user.loginName\"\r\n\r\n123@qq.com\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"user.loginPassword\"\r\n\r\na123456\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'cache-control': "no-cache",
    'Postman-Token': "d0e42289-94b9-4636-8332-dbd6ea562921"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print("响应值是：{}".format(response.text))

#1、判断http的响应状态码
a = response.status_code
assert a == 200             #断言http响应状态码是否等于200
print("http响应断言通过了")


#2、和接口文档对比判断返回值
b = response.json()         #前端后台传输数据的格式，接口的字典格式
assert b["success"] == True #断言返回值的success的值是否为true
print("响应值断言通过了")
