#开发中看到的一些私有化处理 : 装饰器
class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __str__(self):
        return '姓名:' + str(self.name)+',年龄:'+str(self.__age)

    # 老版本的私有化获取方式
    # def setAge(self, age):
        # if age > 0 and age <= 120:
        #     self.__age = age
        # else:
        #     print('年龄不在规定范围内')

    # def getAge(self):
    #     return self.__age


    # 升级版  装饰器

    @property  # 类似get
    def age(self):  # 把方法当作属性,可以访问私有属性
        # if self.__age < 0 or self.__age > 120:
        #     print('年龄格式有误')
        # else:
        return self.__age

    @age.setter  # 类似set
    def age(self, age):
        if age > 0 and age <= 120:
            self.__age = age
        else:
            print('年龄不在规定范围内')


s = Student('kam', 20)
s.name = '小鹏'
print(s.name)

# 私有化赋值两种方式

#1. 老版本的私有属性赋值
# s.setAge(30)
# print(s.getAge())

#2. 装饰器的私有化属性赋值
s.age=200
print(s.age)
