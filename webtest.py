#编写selenium脚本

#导入selenium的第三方包
from selenium import webdriver
import time
time.sleep(3)#停顿三秒
#打开谷歌浏览器，实例化浏览器，driver称为浏览器操作的句柄-以后的操作全部使用driver来操作
driver = webdriver.Chrome(executable_path="chromedriver.exe")
#打开网址http://132.232.44.158:9999/shopxo/index.php
driver.get("http://132.232.44.158:9999/shopxo/index.php")
#定位元素

# class可能会重复
# 定位元素的原则是定位方式的值尽量唯一
# 没有唯一就用xpath


#1、使用id定位元素
#使用id值定位元素,将id对应的元素赋值给一个变量
e = driver.find_element_by_id("search-input")
#给元素中传入（输入）关键字
e.send_keys("huawei")
#定位元素
s = driver.find_element_by_id("ai-topsearch")
#点击元素
s.click()
#2、使用name值定位元素
e1 = driver.find_element_by_name()
#3、xpath定位元素
e2 = driver.find_element_by_xpath('//*[@id="search-input"]]')
#4、使用css_selector定位元素
e3 = driver.find_elements_by_('#search-input')
#5、link_text 适用a标签超链接
e4 = driver.find_elements_by_link_text('登录')
#6、partial_link_tex定位元素
e5 = driver.find_elements_by_partial_link_text('登')
#一般不采用下面两个，因为会有可能重复
#7、classname定位元素
driver.find_element_by_class_name('submit am-btn')
#8、tag_name
driver.find_element_by_tag_name('xxx')

