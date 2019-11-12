# from appium import webdriver

# desired_caps = {}
# desired_caps['platformName'] = 'Android'                    # 打开什么平台的app，固定的 > 启动安卓平台         
# desired_caps['platformVersion'] = '9'                       # 安卓系统的版本号：adb shell getprop ro.build.version.release
# desired_caps['deviceName'] = 'GT-I9103'                 # 手机/模拟器的型号：adb shell getprop ro.product.model
# desired_caps['appPackage'] = 'io.appium.android.apis'       # app的名字:        # 安卓8.1之前：adb shell dumpsys activity | findstr "mFocusedActivity"
# desired_caps['appActivity'] = '.ApiDemos'                   # app的启动页名字： # 安卓8.1之后：adb shell dumpsys activity | findstr "mResume"

# desired_caps['unicodeKeyboard'] = True                      # 为了支持中文
# desired_caps['resetKeyboard'] = True                        # 设置成appium自带的键盘

# # 去打开app，并且返回当前app的操作对象
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# # 题目：
# #     10001个无序整数，取值范围是1-10000，就是说只有一个数重复了，把重复的数找出来。
aa = [123,256,66,15,64,1234,331,56,64,62]
for i in aa:
    # b = i #输出数组里的每个元素赋值给a
    if aa.count(i) > 1:
        print(i)
        break
    else:
        print("没有")

