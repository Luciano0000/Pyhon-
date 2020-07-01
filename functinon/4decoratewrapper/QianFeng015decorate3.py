#装饰器
'''
如果装饰器时多层的
@被装饰函数 优先调用 离函数最近的 @装饰器 以此类推
'''
def zhuang1(func):
    print('-----> 1 start')

    def wrapper(*args,**kwargs):
        func()
        print('刷漆')

    print('-------> 2 end')
    
    return wrapper

def zhuang2(func):
    print('-----> 2 start')

    def wrapper(*args,**kwargs):
        func()
        print('铺地板')

    print('-----> 2 end')

    return wrapper

@zhuang2
@zhuang1
def house():
    print('一个毛坯房')
house()
