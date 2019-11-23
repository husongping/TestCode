#导入pytest
#所有的pytest文件和方法名字都需要以test_开头
import pytest   
import requests

#定义pytest测试用例
def test_01_login_success():
    url = "http://132.232.44.158:5000/userLogin/"
    data =  {"username":"test", "password":"123456", "captcha":"123456"}
    res = requests.post(url = url, json=data)
    print(res.text)

    #断言http状态码
    assert 200  == res.status_code
    #断言返回值
    assert '"code": 200' in res.text