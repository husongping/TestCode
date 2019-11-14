#unittest的测试用例

#必须先导入unittest
"""生命周期：
setUpClass> setUp(01) >test_01>tearDown(01)>  setUp(02) >test_02>tearDown(02) > tearDownClass
"""

import unittest
from selenium import webdriver
import time

#1、测试用例必须继承unittest.TestCase
class TestCaseLogin(unittest.TestCase):







  
    #2、成员方法名字必须要以test_开头（unittest强制规定）
    #测试用例：
    def test_01_login_success(self):
        #chromedriver = 'D:\\TestCode\\UnittestTests\\driver\\chromedriver.exe'#绝对路径
        chromedriver = 'driver\\chromedriver.exe'#相对路径
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
        #chromedriver = 'D:\\TestCode\\UnittestTests\\driver\\chromedriver.exe'#绝对路径
        chromedriver = 'driver\\chromedriver.exe'#相对路径
        driver = webdriver.Chrome(executable_path=chromedriver)#实例化浏览器。打开浏览器获得操作对象
        driver.maximize_window()
        driver.get("http://132.232.44.158:9999/shopxo/admin.php")#打开网址
        #去查找元素输入哟个户名和密码登录
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div/div[1]/input').send_keys("admin")
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div/div[2]/input').send_keys('shopxo1')
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div/div[3]/button').click()
        time.sleep(3)
        #断言 - unittest断言，断言失败时输出F
        url = driver.current_url
        self.assertEqual(url,"http://132.232.44.158:9999/shopxo/admin.php?s=/index/index.html")
        
    def test_03_login_failed(self):
        #chromedriver = '错误抛出E/D:\\TestCode\\UnittestTests\\driver\\chromedriver.exe'#绝对路径
        chromedriver = '错误抛出Edriver\\chromedriver.exe'#相对路径
        driver = webdriver.Chrome(executable_path=chromedriver)#实例化浏览器。打开浏览器获得操作对象
        driver.maximize_window()
        driver.get("http://132.232.44.158:9999/shopxo/admin.php")#打开网址
        #去查找元素输入哟个户名和密码登录
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div/div[1]/input').send_keys("admin1")
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div/div[2]/input').send_keys('shopxo')
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div/div[3]/button').click()
        time.sleep(3)
        #断言 - unittest断言，断言失败时输出F
        url = driver.current_url
        self.assertEqual(url,"http://132.232.44.158:9999/shopxo/admin.php?s=/index/index.html")

#unittest自带的运行方法，不需要实例化的类
# unittest.main() 
"""执行结果
    . 成功：方法正常执行完了
    E 报错：方法执行时出现了异常，代码错误导致无法运行
    F 失败：方法执行时断言失败了，断言失败时抛出F
"""