"""
    整个工具/框架运行的入口
"""
import unittest
from utils.HTMLTestRunner import HTMLTestRunner#导入utils里面的html网页测试报告工具

#1、加载所有的测试用例
#查找cases文件夹里面所有test_开头以.py结尾的文件
#class里面的成员方法都必须是test_开头
testcases = unittest.defaultTestLoader.discover('cases','test_*.py')#test_*.py是正则表达式，表示以所有test_开头以.py结尾的文件

#2、把测试用例装在测试套件中
testsuite = unittest.TestSuite()
testsuite.addTests(testcases)

#3、运行所有的测试用例，并且生成测试报告
title = "测试报告"
descr = "测试报告的描述"
report = "./report/report.html"#生成测试报告的文件路径可以自定义位置

with open(report,"wb") as f:    #创建或者覆盖report执行的文件，再把这个文件对象给变量f(as f相当于f = ...)
    runner = HTMLTestRunner(stream=f,title=title,description=descr) #初始化htmltestrunner
    runner.run(testsuite)                                           #使用run方法运行所有测试