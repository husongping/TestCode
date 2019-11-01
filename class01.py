#方法和为类的尾巴需要加:
#类
#普通的变量
a = 12
b = [1,2,3,4,5,6]
c = True

def ccc():#普通的方法
    print("cccc123456")


#类包含了属性(特征)和方法（行为，能干什么）
class Person():#类名首字母大写，需使用驼峰命名法
class Person():#类名首字母大写，需使用驼峰命名法
    #成员变量，无论哪一个地方都能使用成员变量
    name = "胡颂平"
    age = 21
    hight = 183
    sex = "男"
    #成员方法：以self参数开头的方法
    #self:类本身的实例化对象
    def sing(self):
        print("大家好，我是练习时长两年半的练习生，我会唱")
        print("跳")
        print("rap")
        print("篮球")
        self.rap()
    #成员方法的传参
    def jump(self,wd):
        print("我会跳{}舞蹈".format(wd))
    #self的用法
    #self和实例化对象一样：self在类里面用，实例化对象在类外面使用
    def rap(self):
        # a = self.name
        print(self.name)
        self.sing()


#实例化类：p是Person的实例化对象
# 引用类，不要放到类里面去
p = Person()    #赋值语句
# print(p.name)   #引用类的成员变量
# p.sing()        #引用类的成员方法
# p.jump("民族舞") #成员方法的传参数
p.rap()