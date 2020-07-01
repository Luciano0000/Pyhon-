'''可变参数   :   *args                      **kwargs   ---->  key word args
# 定义方式   :   def 函数名([不可变参数1,...],可变参数):

# 底层机制:
#   *args:当要调用含不可变参数的函数时,系统会自动开辟一个空tuple来用作存放实参,实参可以是
str int list tuple类型
# 类似a,*b=(1,2,3,4)----->a=(1),b=[2,3,4]

#   **kwargs:调用含可变参数的函数时,系统会自动开辟一个空dict 来存放key=value类型的实参,然后
装包封装成字典{key:value}
# **kwargs就说明,只要外面给函数送值,送的值必须符合key=value

# 关键字参数: key=value:   当要调用含关键字参数的函数时,如果实参用键值对的方式来天坑的话会覆盖形参,
# 否则将会用关键字参数对函数体赋值


# 为什么要用**kwarg形参和**dict的原因: 因为无法确定用户到底是否能够按照要求定义实参来赋值函数
# 如果不用'可变参数'，用户如果没有定义实参则系统会报错，所以运用‘可变参数’是为了保证：即使不定义实参
# 程序依然平稳运行
'''


def add(name, age, *args):

    sum = 0
    if len(args) > 0:
        for i in args:
            sum += i
        print('年龄为:%d的%s累加的和是%d:' % (age, name, sum))
    else:
        print('没有元素可计算')


add('飞飞', 18)
add('老马', 30, 1)
add('张飞', 28, 1, 2)
add('马化腾', 37, *[2, 3])  # 实参*list 代表把list拆包成 2,3


#关键字参数: key=value

def add3(a, b=1, c=10):  # b=1 c=10  叫做:有关键字的默认值
    result = a+b+c
    print(result)


add3(1, 2)  # a=1,b=2 b=2覆盖形参
add3(1, 2, c=3)  # a=1,b=2,c=3 c=3覆盖形参


# 可变参数kwargs:


def kwargs_test(**kwargs):
    print(kwargs)


kwargs_test(a=1, b=2, c=5)  # key=value
# 分析:**kwargs就说明,只要外面给函数送值,送的值必须符合key=value


# 函数:打印计算每一位同学的姓名年龄
students = {'001': ('蔡徐坤', '23'), '002': ('吴亦凡', '22'),
            '003': ('王源', '20'), '004': ('王俊凯', '21')}


def print_boy(name1, **persons):
    print('{}喜欢的小鲜肉有:'.format(name1))
    if isinstance(persons, dict):
        values = persons.values()
        for name1, age1 in values:
            print('{}的年龄是{}'.format(name1, age1))


# 调用
print_boy('王大锤', **students)
# 分析: 若实参里有**变量,那就说明实参变量要b进行拆包了,即{'001':('蔡徐坤','23')}拆解
# 为:  001=('蔡徐坤','23') 符合 key=value的条件


'''
使用注意:
如果在开发的时候，已知有一个字典要赋值给函数，而且还需要顾忌实参为空的情况。那么
就是用第二种可变参数:关键字可变参数（**kwargs）并且实参要求也是：**变量 这种方式
'''


def bb(a, b, *c, **d):
    print(a, b, c, d)


bb(1, 2)  # 1,2 () {}
bb(1, 2, 3, 4)  # 1,2 (3,4)
bb(1, 2, x=3, y=5)  # 1,2 () {x:3,y:5}
bb(1, 2, 3, x=100)  # 1,2,(3),{x:100}
# bb(1,2,x=100,5,6)  #error 原因 :
# 1赋值给a,2赋值给b,关键字赋值不了*c即跳过*c，赋值给**d
# 而由于跳过*c 而5,6无从赋值，所以报错(除了关键字,关键字可以无顺序排列形参可以找到)
