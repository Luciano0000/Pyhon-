# 装饰器:函数作为参数,
'''
开发中的应用:
    加入购物车
        判断用户的登陆状态
    付款

    修改收获地址等

'''


def func(number):
    a = 100

    def inner_func():
        nonlocal a
        nonlocal number
        number += 1

        for i in range(number):
            a += 1

        print('修改后的a的值', a)

    return inner_func


f = func(5)
f()

# 函数作为参数
b = 50
f1 = func(b)  # a是一个实参
print(f1)  # <function func.<locals>.inner_func at 0x013F9100>
f1()

print('*'*50)


# 地址的引用问题:
'''
特点:
    1.函数A是作为参数出现(函数B就接收函数A作为参数)
    2.要有闭包的特点
'''


def test():
    print('----test---')


print(test)  # <function func.<locals>.inner_func at 0x013F9100>
t = test  # 把上面的内存地址告诉t
t()  # t调用test地址上的内存


def func2(f):
    print(f)
    f()
    print('------>func2')


# 调用
func2(test)  # 实参也可以是函数


# 定义一个装饰器
'''
分析:
    1.hourse:被装饰函数
    2.将被装饰函数作为参数传给装饰器@decorate
    3.底层执行装饰器函数decorate函数
    4.底层将返回值又赋值给hourse(皮:hourse,肉:return wrapper) 
'''
def decorate(fuc):
    a = 100
    print('wrapper外层打印测试')

    def wrapper():
        fuc()
        print('刷漆')
        print('装门')
        print(a)
        
    print('wrapper加载完成')
    return wrapper

# 使用装饰器:    @装饰器名字

@decorate
def hourse():  # fuc=hourse()    hourse=wrapper
    print('我是毛坯房...')


# 调用函数hourse
print(hourse)  # <function decorate.<locals>.wrapper at 0x00D69100>
hourse() #调用的是wrapper的地址 并且return wrapper的接收变量就是hourse
