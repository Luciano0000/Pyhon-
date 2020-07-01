# 魔术方法汇总:
# __init__    __new__(不常用)    __call__    __del__(不常用)   __str__
'''
__init__ 初始化魔术方法 自动执行方法
触发时机:初始化对象时触发(不是实例化触发,但是和实例化在一个操作中)
参数:至少有一个self,接收对象
返回值:无
作用:初始化对象的成员
注意:使用该方式初始化的成员都是直接写入对象中,类无法具有
'''
'''
__new__ 实例化的魔术方法
触发时机:实例化时触发
参数:至少一个cls 接收当前类
返回值:必须返回一个对象实例
作用:实例化对象
注意:实例化对象时Object类底层实现,其他类继承了OBject的__new__才能够实现实例化对象
    没事别碰这个魔术方法,先触发__new__才会触发__init__

'''
'''
__call__ 调用对象的魔术方法
触发时机:将对象当作函数调用来触发 对象()
参数:至少一个self接收对象,其余根据调用时参数决定
返回值:根据情况而定
作用:可以将复杂的步骤进行合并操作,减少调用的步骤,方便使用
注意:无
'''
'''
__del__ 析构魔术方法 delete的缩写
    1.对象赋值:p=Person()        p1=p  说明p 和 p1 共同指向同一个地址
    2.删除地址的引用 del p1 即删除p1对地址的引用
    3.查看对地址的引用次数 import sys       sys.getrefcount(p1)
    4.当一块空间没有了任何引用,默认执行__del__
触发时机:当对象没有用(没有任何变量引用)的时候触发 ref=0
参数:一个self结婚搜对象
返回值:无
作用:使用完对象是收回资源
注意:del不一定会触发当前的方法,只有当前对象没有任何变量接收时才会触发
#自己最好不要使用这个方法
'''




import sys
class Person:
    def __init__(self, name):
        print('---------->__init__', self)  # 0x00FBD238
        self.name = name

    def __new__(cls, *args, **kwargs):  # __new__向内存申请地址空间
        print('---------->__new__')
        position = object.__new__(cls)  # 0x00FBD238
        print(position)
        return position  # 地址

    def __call__(self, *args, **kwargs):
        print('执行对象得到的参数是:', *args)
        print('--------->__call__')


p = Person('aa')  # 初始化对象成员
print(p)  # <__main__.Person object at 0x00FBD238>
# 底层机制:1.先进入__new__开辟一块地址内存,返回地址 2.再进入__init__中 3.把地址给p赋值
# 正常来说对象都是-->对象名.属性/方法 但是对于__call__来说 对象可以当作时函数,即:对象名()
p('luciano')  # 搜索call --------->__call__

print("*"*50)


class Person2:
    def __init__(self, name):
        self.name = name
        print('--------->__init__')

    def __del__(self):
        print('--------->__del__')
        print(self.name)


p1 = Person2('jack')
# --------->__init__
# --------->__del__
p2 = p1
p3 = p1
p2.name = 'tom'
print(Person, p1, p2, p3)  # 4个空间地址都是0x015C65F8
print(p2.name)
print(p3.name)
# 底层机制: 目前有4块内存空间 分别是Person2 ,p1 ,p2, p3 而 p1,p2,p3都指向Person2,当
# 更改p1,p2,p3中假设改变p1地址的属性,则其余的两块空间属性也会跟着改变,因为p1,p2,p3都指向Person2
# 对象赋值
print(sys.getrefcount(p1))  # 4
del p3
print('删除p3引用后打印',p1.name) #3
print(sys.getrefcount(p1)) 
del p2
print('删除p2引用后打印',p1.name) #2
print(sys.getrefcount(p1)) 
#python底层机制: 内存释放机制通俗的讲:垃圾回收机制 ,即把连接在内存的剩下的
#引用全部回收即释放内存,然后当refcount=0这个时刻触发__del__


