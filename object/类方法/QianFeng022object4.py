#类方法
# 特点:
# 1.定义需要依赖装饰器
# 2.类方法中的参数不是一个对象,而是类
# 3.类方法中只可以使用类属性1


#作用:
# 1.因为只能访问类属性和类方法,所以可以在对象创建之前能完成一些功能,即不依赖与对象
# 可以独立于对象去完成一些事务
class Dog:
    dogtype='金毛'
    def __init__(self,nickname):
        self.nickname=nickname

    def run(self): #self 对象
        print('{}在院子里跑步'.format(self.nickname))

    def eat(self):
        print('吃饭了,,')
        self.run()  #也可以实现函数间相互调用,需要通过self.方法名()
    @classmethod #类方法
    def test(cls): # cls 类
        print(cls) #只能访问类属性不能访问对象属性
        # print(self.nickname)#NameError: name 'self' is not defined
        # 类方法中不能调用其他函数方法
Dog.test()

d=Dog('大黄')
d.test()
d.eat()

print("*"*30)
#补充类方法:
class Person:
    __age=18 #age私有化,只能在类里面修改

    def show(self):
        print('------->',Person.__age)

    @classmethod
    def update_age(cls):
        cls.__age=20

    @classmethod
    def show_age(cls):
        print('修改后的age:',cls.__age)
            

#需求:不依赖对象更改类里面的age
Person.update_age()
Person.show_age()