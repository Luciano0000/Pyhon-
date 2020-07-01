#global 函数内部修改全局变量的权限
# 局部变量(函数内部声明的变量,只有函数内部可访问)
# 全局变量(声明在函数外部的变量,所有的函数都可以访问)
# 不可变全局变量类型:str
# 可变全局变量类型:list

name = '吃粑粑'  # 全局变量


def func():
    s = '老八'
    s += '如厕'  # 局部变量
    print(s)


func()

# print(s) 无法调用局部变量,报错


def func1():
    global name  # 此name是全局变量 因为加了global使得可以对全局变量进行完全修改
    print(name)
    '''
    # 正常来说函数内部不能对全局变量修改,
    #但是global完美解决了函数内部无法修改全局变量的缺点
    '''


def func2():
    name = '阿giao'  # 局部变量与全局变量同名情况下,优先局部变量
    print(name)


func2()
