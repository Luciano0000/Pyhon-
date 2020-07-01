__all__ = ['add', 'number', 'name', 'reduce', 'Calulate']
# 变量
number = 100
name = 'calulate'


# 函数
def add(*args):
    if len(args) > 1:
        sum = 0
        for i in args:
            sum += i
        return sum

    else:
        print('至少传入两个参数')
        return 0


def reduce(*args):
    if len(args) > 1:
        m = 0
        for i in args:
            m -= i
        return m

    else:
        print('至少传入两个参数')


def multiply(*args):
    pass


def divide(*args):
    pass


# 类
class Calulate:
    def __init__(self, num):
        self.num = num

    def test(self):
        print('正在使用 类计算', self.num)

    @classmethod
    def test1(cls):
        print('------->类方法', number)


def test():

    if __name__ == '__main__':
        print('我是测试,....')


print('__name__:',__name__)  
#在本模块中 __name__是: __main__
#而在要调用此模块的其他.py文件中打印的却是:__name__:calculate
# 所以 test()函数中的内容 在其他.py文件中 就不能调用
test()