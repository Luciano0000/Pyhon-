#父类的私有属性子类中无法访问与修改
#但是可以通过在子类中重写父类私有属性,访问自己私有属性即可

class Person(object):
    def __init__(self):
        self.__money = 200
        self.name = 'da'
    def show1(self):
        print(self.name,self.__money)

class Student(Person):
    def __init__(self):
        super().__init__()
        self.__money = 500

    def show(self):
        print('monney:{},name:{}'.format(self.__money,self.name))


s = Student()
s.show()
s.show1()
