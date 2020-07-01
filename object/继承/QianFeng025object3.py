# is a  | base classs 基类(父类)
# 对象调用函数的顺序: 1.去类中先找__new__ 2.再去找__init__3.其次就是其他的函数
'''
继承:
    Student ,Employee ,Doctor --->属于Person 类
    都有相同的代码-->代码冗余,可读性不高
    将相同的代码提取出来--->Person类
    Student ,Employee ,Doctor =====>继承Person

    class Student(Person):
        pass


特点:
    1.如果类中不定义__init__()方法,则默认调用super class的__init__
    2.如果类继承了父类也需要定义自己的__init__,需要在当前类的__init__中调用
    以下父类__init__
    3.如何调用父类的__init() :
        super().__init__(参数)
        super(类名,对象).__init__(参数)
        父类名().__init(self)
    4.重写(覆盖)override:   如果父类有eat(),子类也有eat()方法,默认搜索原则:优先找当前类,再去找父类
    父类提供的方法不能满足子类的需求,就需要在子类中定义同名的方法,这种行为就成为重写
    5.子类的方法可以调用父类的方法:
        super().父类方法名(参数)
'''


class Person(object):

    def __init__(self, name,age):
        self.name = name
        self.age = 20

    def eat(self):
        print(self.name+'正在吃')

    def run(self):
        print(self.name+'正在跑步')


class Student(Person):
    def __init__(self, name, age, clazz):
        # print('----->student的init')
        # 如何调用父类__init__()中的属性
        super().__init__(name,age)  
        #上面就等价于
        #self.name = name
        #self.age = 20  因为父类已经有代码了就不用重复去写了直接super就可以
        self.clazz = clazz #

    def study(self, course):
        print('{} is study: {} '.format(self.name, course))

    def eat(self, food):  # 和父类有相同方法的时候优先调用自身方法
        super().eat()
        print('{}'.format(food))


class Employee(Person):

    def __init__(self, name, age, salary, manager):
        super().__init__(name, age)
        self.salary = salary
        self.manager = manager


class Doctor(Person):

    def __init__(self, name, age, patients):
        super(Doctor, self).__init__(name, age)  # 加了一层判断 self对象是不是Doctor类型造出来的
        self.patients = patients


s = Student('lucy', 20, '4班')
s.study('python')
s.eat('鱼香肉丝')
s.run()

e = Employee('tom',23,10000,'king')
e.run()

lists=['病人1','病人2']
d = Doctor('doc jerry',30,lists)
d.run()
