# #从另一个py文件导入类
# from class01 import Person
# p = Person()
# #从另一个py文件导入方法
# from class01 import ccc
# ccc()
# #从另一个py文件导入变量
# from class01 import a
# print(a)
from selenium import webdriver
import time
print("欢迎使用自制的查天气系统")
a = input("请输入要查询的地址")
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("http://www.weather.com.cn/")
time.sleep(1)
e1 = driver.find_element_by_xpath('//*[@id="txtZip"]')
e1.click()
e1.send_keys(a)
s = driver.find_element_by_xpath('//*[@id="btnZip"]')
s.click()
time.sleep(1)
c = driver.find_element_by_xpath('//*[@id="today"]/div[1]/div')
print(c.text)
