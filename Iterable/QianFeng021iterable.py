# 可迭代对象: 1.生成器 2.集合,列表,元组,字典,字符串
# 如何判断一个对象是否是可迭代?
from collections.abc import Iterable

list1 = [1, 2, 3, 4]
f = isinstance(list1, Iterable)
print(f)  # true

print(isinstance('abc', Iterable))  # true

print(isinstance(11, Iterable))  # false

g = (x+1 for x in range(10))
print(isinstance(g, Iterable))  # true

'''
描述:
迭代器是访问集合元素的一种方式,迭代器是一个可以记住遍历的位置的对象
迭代器对象从集合的第一个元素开始访问,直到所有的元素被访问完结束.迭代器

特点:只能往前不会往后退

定义:可以被next()函数调用并不断返回下一个值的对象,称为迭代器 :Iterator

可迭代的 是不是肯定就是 迭代器? ---->错 List 本身不是迭代器Iterator
    生成器是可迭代的,同样也是迭代器
    但是 list是可迭代的,但不是迭代器 but可以通过iter()函数将List变成迭代器


'''
list1 = [1, 2, 456, 6]
# print(next(list1))#TypeError: 'list' object is not an iterator


# iter()
list1 = iter(list1)
print(next(list1))

'''
综上分析 生成器与迭代器的关系:
可知: 迭代器 分两类:
第一类:生成器(包括{1.通过类似列表推导式 2.函数中 用yeild关键字})
第二类:借助iter()下转化的可迭代对象 即iter(list/tuple/set/dict)
'''
