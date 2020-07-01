'''
在python中 ,模块是代码组织的,把功能相近的函数或者类放到一个文件中,
一个文件(.py)就是一个模块,模块名就是文件去掉后缀py

这样做的好处是:
-提高代码的可复用,可维护性.一个模块编写完毕后,可以很方便的在其他项目中导入
-解决了命名冲突的问题,不同模块中相同的命名不会冲突

1.自定义模块
2.使用系统模块


导入模块:
1.import 模块名 
    模块名.变量  模块名.函数   模块名.类
2.from 模块名 import 变量/函数/类
    在代码中直接可以使用变量,函数,类
3.from 模块名 import *
    1).* 代表该模块中所有的内容
    2).但是如果想限制获取的内容.可以在模块中使用:
        __all__=['*可以用的内容1',.....]

4.在导入模块的时候会"加载"模块中的"所有代码"动作
    如果不希望其进行"全部调用",就会用到 __name__
    在模块里面__name__叫:__main__
    如果在其他的.py文件中通过导入的方式去调用的话__name__就叫:模块名
'''

# 自定义模块

# # 导入模块
# import calculate

# list1 = [1, 3, 5, 7, 8, 9]
# # 使用自定义模块中的函数  ---模块名.变量/函数/类
# c = calculate.add(*list1)  # 拆 列表
# print(c)

# # 使用模块变量
# print(calculate.number)

# #使用模块类魔术/普通方法
# cal=calculate.Calulate(5)
# cal.test()
# #使用模块类方法
# calculate.Calulate.test1()

from calculate import *

list1 = [1, 3, 5, 7, 8, 9]
result = add(*list1)  # 拆列表
print(result)

sums = result+number
print(sums)

cal = Calulate(80)
cal.test()
