# 魔术方法 
# 作用:模板的统一化 统一性
# 解释: self 和 对象 指向的是同一块内存的空间 而self其实就是做了一个将对象和
# 类中的方法起到一个动态交互的一个更新接口


class Phone:
    price=1 #类属性 
    # 魔术方法之一:称作魔术方法 __名字__()
    def __init__(self):  # init-->初始的,初始化
        self.brand = 'xiaomi'  # 动态的的给self空间中添加了两个属性
        self.price = 4499 #self动态属性 与类属性不同 此属性类调用不了

    def call(self):
        print('----> call')
        print('价格')



p = Phone()
p1 = Phone()
p1.call()
print(p1.brand) #self.brand
print(p1.price) # 优先调用self属性即p1内存空间中的属性

# 1.找到有没有一块空间是Phone
# 2.利用Phone类,向内存申请和Phone一样的一块内存空间(但是ip不一样)
# 3.向类里找是否有__init__ 如果没有:则将开辟的类Phone内存给了对象名:P
# 4.如果有__init__ 则会进入__init__中执行里面的动作 即执行__init__(p的地址)
# 5.将内存地址赋值给对象p


class Person:
    name='张三'
    def __init__(self,name,age):
        self.name=name
        self.age=age

   
      

    def eat(self,food):
        print('{}正在吃{}!..'.format(self.name,food))

    def run(self):
        print('{}今年{}岁,正在跑步!'.format(self.name,self.age))
        
p=Person('传给类里面的名字',20)
p.name='lisi'
p.eat('红烧肉')
p.run()


