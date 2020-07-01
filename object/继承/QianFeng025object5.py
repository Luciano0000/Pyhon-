# 多继承--->python独有 一个儿子有多个爹
'''
python允许多继承,
def 子类(父类1,父类n):
    pass

如果父类中有相同名称的方法,则搜索顺序是
经典类:从左到右,深度优先
新式类(类名(object)):广度优先 #python3之后不区分经典类和新式类(都是广度优先) 但是python2中区别经典类和新式类
'''
import inspect


class Base:
    def test(self):
        print('-------Base')


class A(Base):
    def test(self):
        print('--_---A')


class B(Base):
    def test1(self):
        print('-----B--')


class C(Base):
    def test2(self):
        print('----->C')


class D(A, B, C):
    pass


d = D()
d.test()  # -----A


print(inspect.getmro(D))  # 搜索顺序
print(D.__mro__)  # 搜索顺序
