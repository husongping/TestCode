'''
print("hello world！");
print(2333)
print(123.123)
print(False)
print(True)
xx = int(input("请输入第一个数："))
yy = int(input("请输入第二个数："))
zz = xx + yy
print("两个数的和为：",zz)
print("第一个数大于第二个数的布尔值",xx > yy)
aa = input("请输入要计算字段的内容")
print("您输入的字数是",len(aa))
print("您输入的数据格式是",type(aa))
bb = (1,"哈哈哈","希希",True,None,2.33,2.33) #元组
print("元组的值：",bb[1])
cc = bb.count(2.33)
print("元组里统计的值的个数：",cc)
dd = bb.index(1)
print("元组中1的下标是",dd)

ff = [1,3,"haha","xixi",2333,(2,3,6,5,2,33)]#数组
ff.append(123456)#往数组末尾里插入数值（参数是插入的数据）
print(ff)
ff.insert(0,"insert插入的值")#往数组中指定位置插入数据（参数是数组的下标和插入的数据）
print(ff)
a = ff.pop(3)#从数组中取出一个数据（参数是下标）
print(a)
print(ff)
ff.remove(2333)#从数组中删除一个数据（参数是元素值）
print(ff)

xx = {
    "name":"张三",
    "age":18,
    "high":"175cm",
    "grade":[89,76.880]
    }
print(xx["name"])
print(xx)
xx["school"] = "北京大学"
print(xx)
del xx["grade"]
print(xx)
print(xx.get("high"))

a = input("请输入你要输出的名字：")
b = input("请输入你的年龄：")
c = input("请输入你的职业：")
xx = "输出的名字是{name},年龄是{age}，职业是{job}".format(name=a,age=b,job=c)#format格式化字符串
print(xx)
print(xx[0])

money = input("请输入发红包的值：")
for i in money:
    if i  not in "0123456789.":
        print("请输入符合要求的数字")
        exit()
xx=money.count(".")
if xx > 1:
    print("输入的值不合法")
else:
    if "." in money:
        yy = money.index(".")+1
        zz = len(money)
        floatlen = zz-yy
        if floatlen > 2:
            print("只能有两位小数")
        else:
            if money >= 0.01 and money <= 200:
            print("发送红包成功！金额{}".format(money))
            else:
            print("{}不符合红包发送范围，请检查后输入".format(money))
    else:
        money = float(money)
        if money>=0.01 and money<=200:
            print("发送红包成功！金额{}".format(money))
        else:
            print("{}不符合红包发送范围，请检查后输入".format(money))


num = int(input("请输入一个分数"))
if num>100:
    print("你输入的值大于100")
elif num>=90:
    print("你输入的值大于90小于100")
elif num>=80:
    print("你输入的值大于80小于90")
elif num>=70:
    print("你输入的值大于70小于80")
elif num>=60:
    print("你输入的值大于60小于70")
else:
    print("你输入的值小于60，不及格")

xx = ["你好","菜鸟","张山","测试"]
a = 0
for i in xx:
    a = a+1
print(a)


for i in range(1,10):
    for j in range(1,i+1):#九九乘法表
        print("{i}*{j}={f}".format(i=i,j=j,f=i*j),end = " ")
    print()

xx=[34,565,77,435,23,45,67,78,43,234,56,78,98,66,16,456,456,56]
xa=[]
xb=[]
print("数列x中一共有：{a}个数字".format(a=a))#分割数组
for i in xx:
    if xx[i] > 100:
        xa.append(i)
    else:
        xb.append(i)
print("大于100的数组xa为：{a}小于100的数组xb为：{b}".format(a=xa,b=xb))

for i in [1,2,3,4,5,6,7,8,9]:
    for j in [1,2,3,4,5,6,7,8,9,]:
        print("{}*{}={}".format(i,j,i*j),end = " ")
    print()
for i in range(1,10):
    for j in range(1,i+1):#九九乘法表
        print("{i}*{j}={f}".format(i=i,j=j,f=i*j),end = " ")
    print()

xx=[34,565,77,435,23,45,67,78,43,234,56,78,98,66,16,456,456,56]
xa=[]
xb=[]
for i in xx:
    if i > 100:
        xa.append(i)
    else:
        xb.append(i)
print("大于100的数组xa为：{a}小于100的数组xb为：{b}".format(a=xa,b=xb))

a = int(input("请输入年份"))
b = int(input("请输入月份"))
c = int(input("请输入日期"))
d = 0
month = [31,31,30,31,30,31,31,30,31,30,31]
if a%400==0 or(a%4==0 and a%100!=0):
    month.insert(1,29)
    for i in range(b-1):
        d = d + month[i]
else:
    month.insert(1,28)
    for i in range(b-1):
        d = d + month[i]
print("今天是{year}年的第{x}天".format(year=a,x=d+c))

num = int(input("请输入一个五位数的数字："))
num = str(num)
print("".join(reversed(num)))

a = 10 
while a > 1:
    print(a)
    a = a - 1
 
xx = ["nihao",233.33,44,55,66,77,"哈哈","拉拉"]
for i in xx:
    if(type(i) is not int) and (type(i) is not float):
        continue
    print(i)

import time
for i in 
'''  
from mysql import query,commit