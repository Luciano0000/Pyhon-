# 文件夹和包
# 文件夹: 存储一些非.py文件
# 包 : 存放.py文件
# 一个包中可以存放多个模块
# 项目> 包 > models > 类,函数,变量
# from 包名.模块名 import 类/函数/变量

# 使用包中 模块中的user类
from user.models import *

u = User('admin', '123')
u.show()
from articale.models import Article

a = Article('个人总结', '邹旭尧')
a.show()
'''
article 
    |--models.py
    |--__init__
user
    |--models.py

QianFeng027package.ppy

from 包 import models
form 包.models import 类/变量/函数
from 包.models import *
'''
