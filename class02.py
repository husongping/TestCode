#类的构造方法

class Person():
    name = "胡颂平"
    sex = "男"
    #构造方法，固定写法：初始化类
    def __init__(self,xb,mz):#在这里使用__init__方法传入参数
        self.sex = xb
        self.name = mz       #在这里更改属性的名字
        self.test()

    def test(self):
        print("这是test方法")
p = Person("女","张三") 
# 在这里传入所更改的属性的参数，
# 需注意顺序一定要按照传入参数的顺序填入（第7行）
print(p.sex,p.name)

#类的继承和重写
#类和类的关系：继承，子类继承父类的属性和方法
class DongWu():
    tizhong = 100
    def run(self):
        print("动物能跑！")

class Man(DongWu):#类的继承
    tizhong = 200       #重写（覆盖）父类的属性
    def run(self):
        print("人能跑！")#重写（覆盖）父类的方法
    pass                #占坑防止报错
r = Man()
print(r.tizhong)
r.run()