# 定义类和属性
# 类中方法
# 定义类


class Stundent:
    # 类属性
    name = 'xiaowei'
    age = 2


# 使用类,创建对象
xiaowei = Stundent()
# 对象属性
xiaowei.age = 18  # 赋值操作,只会在xiaowei内存空间里增加
print(xiaowei.age)  # 优先对象空间里找,其次再从类空间找找
print(xiaowei.name)

yupeng = Stundent()
yupeng.name = 'yupeng'
yupeng.sex = '男'
print(yupeng.name, yupeng.sex)

# 更改类属性
Stundent.name = '老八'
laoba = Stundent()
print(laoba.name)


# 类中方法:动作
# 种类:普通方法;类方法;静态方法;魔术方法
'''
普通方法:  
def 方法名(self[参数,..]):
'''


class Phone:
    brand = 'xiaomi'
    price = 4999
    type = '黑鲨'

    # Phone类里面的:方法(放在类里面的函数叫方法):
    def call(self):
        print('此时self的地址是:', self)
        # print('正在访问通讯录:')
        # for person in self.address_book:
        #     print(person.items())  #普通函数里面需要考虑self的更新源有没有address_book这个属性;没有会报错

        print('留言',self.note)
        print('正在打电话..')


# 对象
phone1 = Phone()
phone1.note = '我是phone1的note'
phone1.address_book = [{'123456479': '宇鹏'}, {'98745612': '小红'}]
print(phone1, '---------1------')
phone1.call()  # 相当于把Phone1当作参数传递给 call(self) 所以print(slef)的地址和phone1的地址是一个地址
# 也就是说 self参数是动态变化的,只要对象中有 对象.函数() 的代码就说明要把自己的属性或者方法传给类
print('*'*30)

phone2 = Phone()
phone2.note = '我是phone2的note'
print(phone2, '--------2--------')
phone2.call()
