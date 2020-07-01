'''
__init__.py 文件 :
特点:
    当导入包的时候,默认执行__init__.py 这个文件

作用:
1. 当导入包的时候,把一些初始化的函数,变量,类定义在__Init__.py文件中
2,此文件中的函数,变量,等的访问只需要通过包名.函数..
3.结合__all__==['通过*可以访问的模块']

'''

'''
1.from 模块 import *
#表示可以使用模块里面的所有内容,
# 如果没有定义__all__=['函数/类/变量'] 所有的都可以访问,但是如果加上__all__=['']
#则只能访问列表中的东西

2.from 包 import *
表示包中的内容是不能访问的,就需要在__init__.py文件中定义__all__=['可以通过*访问的模块']


'''

# from 包名 import *
from QianFeng.QFmodels.user import *

user = models.User('admin',
                   '123')
user.show()

print(test.MAX)

