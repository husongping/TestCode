#元素定位
#导入appium的python第三方包
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'                    # 打开什么平台的app，固定的 > 启动安卓平台         
desired_caps['platformVersion'] = '9'                       # 安卓系统的版本号：adb shell getprop ro.build.version.release
desired_caps['deviceName'] = 'Redmi Note 5'                 # 手机/模拟器的型号：adb shell getprop ro.product.model
desired_caps['appPackage'] = 'io.appium.android.apis'       # app的名字:        # 安卓8.1之前：adb shell dumpsys activity | findstr "mFocusedActivity"
desired_caps['appActivity'] = '.ApiDemos'                   # app的启动页名字： # 安卓8.1之后：adb shell dumpsys activity | findstr "mResume"

desired_caps['unicodeKeyboard'] = True                      # 为了支持中文
desired_caps['resetKeyboard'] = True                        # 设置成appium自带的键盘

# 去打开app，并且返回当前app的操作对象
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#定位app按钮

#accessibility id
app = driver.find_element_by_accessibility_id("App")
app.click()

#xpath
# app = driver.find_element_by_xpath('//android.widget.TextView[@content-desc="App"]')
# app.click()
# #resource-id
# app = driver.find_element_by_id('android:id/text1')
# app.click()
#文本值
# app = driver.find_element_by_android_uiautomator('new UiSelector().text("Content")')
# app.click()

s = driver.find_element_by_accessibility_id("Search")
s.click()

i = driver.find_element_by_accessibility_id("Invoke Search")
i.click()

#send_keys输入方法
inp = driver.find_element_by_id("io.appium.android.apis:id/txt_query_prefill")
#inp.send_keys("123456中文")    #输入较慢，是使用复制粘贴输入，支持中文
#set_value输入方法
driver.set_value(inp,"asdas")   #输入快，使用键盘输入，不支持中文
inp.clear()                     #删除已经输入的值
driver.quit()                   #退出测试