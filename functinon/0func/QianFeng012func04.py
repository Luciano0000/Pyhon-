# 找出列表中的最大值,最小值的函数
# iterable 可迭代的
# isinstance(变量,类型)函数:判断是不是什么类型


def max(iterable):
    max1 = iterable[0]
    for i in iterable:
        if i > max1:
            max1 = i
    print('最大值是:', max1)


def min(iterable):
    min1 = iterable[0]
    for i in iterable:
        if i < min1:
            min1 = i
    print('最小值是:', min1)


# 调用:测试能否找到最大值
list1 = [1, 23, 545, 777, 81]
tuple1 = (1, 3, 45, 6, 77, 2)
max(list1)
max(tuple1)
min(list1)
min(tuple1)

isinstance(2, int)

# 写一个判断输入的内容是否为某个类型的函数


def type_list(islist):
    if isinstance(anwser, int):
        print('type:int')
    elif isinstance(anwser, str):
        print('type:str')
    elif isinstance(anwser, tuple):
        print('type:tuple')
    elif isinstance(anwser, list):
        print('type:list')
    elif isinstance(anwser, set):
        print('type:set')
    elif isinstance(anwser, dict):
        print('type:dict')


anwser = input('输入任意类型的值:')
type_list(anwser)


# 模拟一个enumerate()功能的函数
def enumerate(value):

    list1 = []
    index = 0
    for i in value:
        t1 = (index, i)
        list1.append(t1)

        index += 1
    print(list1)


# 调用
s = {2, 3, 5, 6, 7, 8}
enumerate(s)
