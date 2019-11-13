#unittest的测试用例

#必须先导入unittest
import unittest
from selenium import webdriver
import time

#1、测试用例必须继承unittest.TestCase
class TestCaseLogin(unittest.TestCase):
    #2、成员方法名字以test_开头
    #测试用例：
    def test_01_login_success(self):
        chromedriver = 'D:\\TestCode\\UnittestTests\\driver\\chromedriver.exe'
        driver = webdriver.Chrome(executable_path=chromedriver)#实例化浏览器。打开浏览器获得操作对象
        driver.maximize_window()
        driver.get("http://132.232.44.158:9999/shopxo/admin.php")#打开网址
        #去查找元素输入哟个户名和密码登录
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div/div[1]/input').send_keys("admin")
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div/div[2]/input').send_keys('shopxo')
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div/div[3]/button').click()
        time.sleep(3)
        #断言 - unittest断言，断言失败时输出F
        url = driver.current_url
        self.assertEqual(url,"http://132.232.44.158:9999/shopxo/admin.php?s=/index/index.html")
        print("登陆成功")

    def test_02_login_failed(self):
        print("登录失败")

#unittest自带的运行方法
unittest.main() 
"""执行结果
    . 成功：方法正常执行完了
    E 报错：方法执行时出现了异常，代码错误导致无法运行
    F 失败：方法执行时断言失败了，断言失败时抛出F
"""