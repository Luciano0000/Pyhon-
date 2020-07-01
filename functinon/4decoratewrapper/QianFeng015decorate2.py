# (校验器)
#断点是个很好的理解方式
import time

# 定义装饰器


def decorate(func):

    def wrapper(*x,**kwx):
        print('正在校验中....')
        time.sleep(2)
        print('校验完毕...用时2s')
        # 调用参数,即:被装饰函数
        func(*x,**kwx) 
    return wrapper

# 要被校验的函数
@decorate
def f1(n):
    print('---------f1-------',n)

f1(1) #f1地址指向的是wrapper

@decorate
def f2(name,age):
    print('--------f2------',name,age)
name1='老八'
f2(name1,20)

@decorate
def f3(students,clazz='1905'):
    print('{}班级的学生如下'.format(clazz))
    for stu in students:
        print(stu)

students=['老八','窝窝头','菠菜','阿giao']

f3(students,clazz='1904')



