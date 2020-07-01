# 内部函数
'''
特点:
1.可以访问外部函数的变量
2.内部函数可以修改外部函数可变类型的变量
    内部函数可以 利用 "nolocal  获取修改外部函数内的不可变类型的变量的权限"
3."内部函数修改全局的不可变变量时,需要在内部函数声明 glabal  权限"
    内部函数修改外部函数不可变变量时,需要在内部函数中声明nolocal权限
4.locals() 查看本地变量有哪些,以字典的形式输出
    globals() 查看全局变量有哪些,以字典的形式输出(注意里面会有系统的一些键值对)
'''


def func():  # 声明外部函数
    # 声明变量
    n = 100  # 局部变量
    list1 = [1, 5, 4, 2]  # 局部变量

    def iner_func():  # 声明内部函数
        nonlocal n  # 获得修改外部函数不可变类型变量的权限
        n += 100  # 对外部变量修改
        # 对list1元素进行+5
        for index, i in enumerate(list1):
            list1[index] = i+n  # list1[0]=1+n ......

        list1.sort()

    # 调用下内部的函数

    iner_func()
    print(list1)


func()

a = 100  # 全局变量

print(globals())  # 使用globals()函数可以查看到在当前的函数中声明的内容有哪些


def func1():
    b = 99

    def iner_func1():
        global a
        nonlocal b
        b += 1
        c = 88
        c += 2
        a += 100
        # 尝试打印abc的值
        print(a, b, c)
    iner_func1()  # 调用内部函数
    print(locals())  # 使用lacals()函数可以查看到在当前的函数中声明的内容有哪些
    # locals()是个字典:{key:value }即 {函数名:变量}


func1()  # 调用函数
