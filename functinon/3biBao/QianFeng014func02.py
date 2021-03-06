# 闭包:
'''因为在嵌套函数中,函数体外部不能直接调用嵌套函数中的内部函数,但是可以用return来
抛出内部函数,然后在函数体外部声明一个变量用来接收内部函数,最后调用:变量()即:内部函数
'''
# 闭包条件:
'''
1.外部函数中定义了内部函数
2.外部函数是有返回值的
3.返回的值是:内部函数名(注意:不能加())
4.内部函数内引用了外部函数的变量
'''
# 闭包函数格式:
'''
def 外部函数名():
    ........
    def 内部函数名():
        ......
    return 内部函数名
'''
# 闭包的作用:
'''
1.可以使用同级的作用域
2.读取其他元素的内部变量
3.延长作用域
'''
# 闭包总结:
'''
优点:闭包优化了变量,原来需要类对象完成的工作,闭包也可以完成
        代码变得整洁,便于阅读
缺点:由于闭包引用了外部函数的局部变量,使外部函数的局部变量内存没有及时的释放,
        消耗内存,且作用域没有那么的直观
闭包是理解"装饰器"的基础
'''

'''
等价下式
def func():
    a=100
    def inner_func():
        b=99
        print(a,b)
    inner_func()
func()
'''
def func():  # 外层函数
    a = 100

    def inner_func():  # 内层函数
        b = 99
        print(a, b)

    return inner_func  # 返回内层函数,(切记不要写(),return inner_func()表示调用)!!


# x接收返回值:inner_fun, 即x()等价于inner_func()
x = func()

# 调用
x()  # 100 99


# 案例 闭包函数的保存状态功能:
def func1(a, b):
    c = 10

    def inner_func1():
        s = a+b+c
        print('相加之后的结果是:', s)
    return inner_func1


# 接收内部函数
ifunc1 = func1(1, 2)
# 此时 ifunc1已经接受到内部函数,并保存当前状态值于一块内存中
print(id(ifunc1))  # id=(59216200)
ifunc2 = func1(3, 4)
# ifunc2也接收到这个内部函数(不同参数),并保存当前状态于一块内存中
print(id(ifunc2))  # id=(59216128)
# 调用内部函数
ifunc2()  # 17
ifunc1()  # 13



