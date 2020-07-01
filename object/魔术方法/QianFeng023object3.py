# 魔术方法续:
# __str__
'''
触发时机:使用print(对象名)或者str(对象名)的时候触发去调用__str__里面的内容
参数：一个self接收对象
返回值：必须要在__str__中有返回值且是字符串类型
作用：print（对象时）进行操作，得到字符串，通常用于快捷操作
注意：无
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'name是:'+self.name+',age是:'+str(self.age)


p = Person('tom', 20)
print(p)
# 单纯的打印对象名称则出来的时一个地址,这个地址对于开发者来说无意义
# 如果想在打印对象名的时候能够给开发者更多的一些信息量
p1 = Person('jack', 27)
print(p1)
# str(p1)

'''
总结魔术方法:s
重点:
__init__ (构造方法,创建完空间之后调用的第一个方法)  __str__   
非重要:
__new__ 作用 开辟空间
__del__ 作用 没有指针引用的时候会调用,99%都不需要重写
__cal__ 作用 想不想将对象当成函数用



'''