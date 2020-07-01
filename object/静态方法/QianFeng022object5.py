#静态方法    很类似 类方法
'''
特点:
1.需要装饰器 @staticmethod
2.静态方法无需传递参数(self/cls)
3.只能访问类的属性和方法,而对象的无法访问
4.加载时机同类方法

总结:
静态方法和类方法在实际开发中很少用到,面试可能会考
类方法  静态方法
    不同:1.装饰器不同
        2.类方法有参数 静态方法无参数
    相同:1.都可以访问类的属性和方法
        2.都可以通过类名去调用访问
        3.都可以在创建在没有对象之前使用,因为不依赖与对象
普通方法与两者的区别:
    不同:1.无装饰器
        2.普通方法永远是要依赖对象,因为每个普通方法都有一个self
        3.只有创建了对象才能调用普通方法,否则无法调用
'''

class Person:
    __age=18 #age私有化,只能在类里面修改

    def __init__(self,name):
        self.name=name

    def show(self):
        print('------->',Person.__age)

    @classmethod
    def update_age(cls):
        cls.__age=20

    @classmethod
    def show_age(cls):
        print('修改后的age:',cls.__age)

    @staticmethod
    def test():
        print('---------->静态方法')
        # print(self.name) 语法错误
        print(Person.__age)

Person.test()