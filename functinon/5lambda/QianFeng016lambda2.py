# map()     reduce()    filter()    sorted()    max()   min()

# map(function,*iterables) #(函数,可迭代对象)

# reduce(function,sequence,initial=None) #(函数,元组,默认值)

# filter(fuction:None,iterables) #(函数,可迭代对象)

# sorted(*iterbales,key=function,[reverse:bool])
# max(*iterbales,key=function)
from functools import reduce


list1 = [1, 23, 3, 4, 5, 5, 6, 43]

# 对列表+2操作
result = map(lambda x: x+2, list1)
print(list(result))
# 等价与
for index, i in enumerate(list1):
    list1[index] = i+2
print(list1)


# 对列表中的奇数进行+1操作
result = map(lambda x: x if x % 2 == 0 else x+1, list1)
print(list(result))


# reduce() 对元组的元素进行可迭代的加减乘除的运算
tuple1 = (3, 4, 5, 66, 7, 9, 54)
result = reduce(lambda x, y: x+y, tuple1)
print(result)  # 148

tuple2 = (1, 2)
result = reduce(lambda x, y: x-y, tuple2, 10)
print(result)  # 10-1-2=7


# filter() 对可迭代对象过滤操作
list1 = [12, 6, 8, 123, 65, 99, 35]

result = filter(lambda x: x > 10, list1)
print(list(result))  # [12, 123, 65, 99, 35]
# 等价于
list2 = []
for i in list1:
    if i > 10:
        list2.append(i)
print(list2)
