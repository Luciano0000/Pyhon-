
# 开发模式:单例模式

# 单列模式:


# class Student:
#     pass


# s = Student()
# s1 = Student()
# # 每创建一个对象实例就开辟一个空间,费内存
# print(s)
# print(s1)
class Singleton(object):
    # 私有化 当前类实例
    __instance = None
    name = 'jack'
    # __new__是开辟空间的,__init__产生地址

    # 重写__new__
    def __new__(cls):
        print('----->__new__')
        if Singleton.__instance is None:

            # 借助父类的__new__方法开辟空间
            cls.__instance = object.__new__(cls)

            return cls.__instance
        else:
            return cls.__instance

    def show(self, n):

        # 类中方法调用 类属性 必须在属性前面指明
        print('------>shwo:', Singleton.name, n)


s = Singleton()
s1 = Singleton()
print(s)
print(s1)
s.show(5)
s1.show(7)

'''
底层机制:

    说明:因为在定义对象的时候访问类中方法的顺序是: 1.__new__() 2.__init__()
所以首先系统先访问 __new__() 并执行 然后 将 __new__() 中返回值抛出,return给__init__(),若
代码中没有事先声明__init__()函数,则系统会自动开辟一个__init__()函数用来存放__new__中的返回值
然后给对象交互


    流程:系统开辟一块内存空间存放Singleton类,存放__instance
        进入__new__(cls): 执行代码 
            如果cls.__instance=None 即 类 中的__instance是空的:
                cls.__instance = object.__new__(cls)
                从父类中开辟一个内存空间0xXXXXX赋值给类中的__instance   "__new__(cls)是开辟空间的意思"
                return cls.__instance  --->将返回的内存空间抛出函数体默认传给__init__()
        此时s对象访问__init__的地址空间就是上面流程所开辟的空间

        而s1在访问类的时候由于cls.__instance即类中的私有属性已经不为None了,所以直接执行return cls.__instance
        即返回出去的地址空间依然是上次从父类中开辟的内存空间0xXXXXX 所以__init__依然还是上一个空间
        从而s1访问的地址空间和s访问的地址空间是一致的
这样就避免了重复开辟空间的内存浪费问题




'''
