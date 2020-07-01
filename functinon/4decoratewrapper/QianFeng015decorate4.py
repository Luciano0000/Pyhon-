# 装饰器带参数
'''
总结:
带参数的 装饰器 : @装饰器名(参数) 
    带参数的装饰器是三层的
    最外层的函数负责接收装饰器参数
    里面的内容还是原装饰器的内容
'''


def outer(a):  # 第一层 负责接收装饰器的参数

    def decorate(func):  # 第二层 负责接收函数

        def wrapper(*args, **kwargs):  # 第三层 负责接收函数的参数
            func(*args)
            print('------> 铺地砖{}块'.format(a))

        return wrapper  # 返回的是第三层的函数名

    return decorate  # 返回的是第二层函数名


@outer(a=10)  # 也可以直接(10)
def house(time):
    print('我是{}买到毛坯房'.format(time))


@outer(1000)
def street(name):
    print('新修的街道名字是:{}'.format(name))


house('2020年4月11号')
street('北安路')
