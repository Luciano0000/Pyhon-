# 面向对象
'''
程序    现实中
对象    具体的事务

现实中的事务 --> 转成电脑程序.
世间万物皆对象

好处:
    1.可复用
    2.灵活性高

面向对象:
    类
        手机                
    对象:(对象集合)
        小红的手机
        小刚的手机       
    属性:(共同特征)
        品牌
        颜色
        大小
        价格
        内存
    方法:(动作)
        打电话
        发短息
        上网
        游戏


'''
# 所有的类名首字母大写,多个单词使用驼峰命名
# ValueError  TypeError  StopIterable
# class 类名[(父类)]:
# 属性:
# 方法:


class Phone(object):  # python独有:可以有空方法
    brand = 'huwei'
    size = '18'


# 利用类创建对象 类名后面加() --->构造对象
xh_phone = Phone()
print(xh_phone)  # <__main__.Phone object at 0x030EE7F0>
print(xh_phone.brand)

xg_phone = Phone()
print(xg_phone)
xg_phone.brand='iphone'
print(xg_phone.brand)