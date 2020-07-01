# 私有化(伪装的私有)
# 封装: 1.私有化属性    2.定义公有的set和get方法 set赋值  get取值
# __属性: 将属性私有化,访问范围仅限于类中
'''
好处:
1. 隐藏属性不被外界随意的修改
2. 也可以修改 : def setXXXX(self,xxx):  
3. 筛选赋值的内容 if xxx 是否符合条件 if else

4.如果想要获取具体的某一个属性 就可以使用getxxx(self):      return self.xxx
'''
# 为何叫做伪装的私有: 因为通过以上的定义与解释我们知道私有化的属性是无法在类外进行直接修改 需要得到set 和 get
# 的帮助才可以修改私有属性,但是通过查看dir(对象)可以看到有 "_类名__ 私有方法名" 这个属性,也就是说私有并不是真的私有
# 而是把属性加了一层外衣,这样我们依然可以从类的外面调用到私有属性,且只需调用伪装的属性即可


class Student:
    __age = 18  # 类属性

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        self.__scose = 59

    def __str__(self):
        return '姓名:' + str(self.__name)+',年龄:'+str(self.__age)+',考试分数:'+str(self.__scose)

     # 定义公有的set和get方法
    def setAge(self, age):
        if age > 0 and age <= 120:
            self.__age = age
        else:
            print('年龄不在规定范围内')

    def getAge(self):  # 取值
        return self.__age  # 把私有化的值扔出去

    def setName(self, name):
        if len(name) <= 6:
            self.__name = name
        else:
            print('字符长度超过6,不符合规定')

    def getName(self):
        return self.__name


kam = Student('kam', 20)
# kam.age = 22
# kam.__scose = 95  # 更改失败
print(kam)
kam.setAge(12)  # 限制了对象取值范围
kam.setName('abcdef')
print(kam)  # 找到__str__内容
print('getAge:', kam.getAge())
print('getName:', kam.getName())

print(dir(Student))
print(dir(kam))
print(kam._Student__age)  # 私有属性的伪装
