
def func():
    a = 100

    def inner_func1():
        b = 90
        s = a+b
        print(s)

    def inner_func2():
        inner_func1()  # 调用内部函数inner_func1()
        print('-----> inner_fun1', a)
        return 'hello'
    return inner_func2  # 返回的是一个地址


f = func()  # f接到func()和 返回值地址
ff = f()  # 接收 返回值hello
print(ff)


# 计数器
def generate_count():
    container = [0]  # 计数容器

    def add_one():
        container[0] = container[0]+1
        print('当前是第{}次访问:'.format(container[0]))
        print(container[0])

    return add_one


# 内部函数就是个计数器
counter = generate_count()
counter()  # 第一次访问
counter()  # 第二次访问
counter()  # 第三次访问
