# 可变 不可变 类型

# 不可变:(对象所指向的内存中的值是不可变的)
# 不可变类型: int       str     float       tuple
num = 10
num1 = 12
print('intId:', id(num), '^', id(num1))
str1 = 'asd'
str2 = 'asdf'
print('strId:', id(str1), '^', id(str2))
fl = True
fl2 = False
print('floatId:', id(fl), '^', id(fl2))
t1 = (1, 2, 3)
t2 = (1, 2, 3, 4)
print('tupleId:', id(t1), '^', id(t2))

# 可变的:(对象所指向的内存中的值是可变的)
# 可变类型:  list      dict      set
l1 = [1, 2, 3]
print('list删除之前的id:', id(l1))
l1.remove(3)
print(l1)
print('list删除之后的id:', id(l1))

d1 = {1: 'aa', 2: 'bb'}
print('dict删除之前的id:', id(d1))
d1.pop(1)
print(d1)
print('dict删除之后的id:', id(d1))

set1 = {1, 2, 3}
print('set删除之前的Id:', id(set1))
set1.remove(1)
print(set1)
print('set删除之后的id:', id(set1))


list1 = [1, 3, 4, 5, 6, 7]
list2 = list1
list1.remove(3)
print(list2)  # [1, 4, 5, 6, 7]
# 解释:因为List1和list2指向同一个内存地址,又因为list1是可变类型即不用开辟新的地址,
# 所以list1内存中做了改变,list2可以看到变化,所以list2指向的内存变了

s1 = 'abc'
s2 = s1
result = s1.split('a')
print(result)
print(s2)
# 解释:因为s1和s2指向同一个内存地址,但是因为s1是不可变类型,所以当s1无法改变内存,
# 所以要开辟一个新的内存和地址,但是s2已经指向s1的内存地址了,也就不会在指向s2新开辟的
# 地址了.即最后s1和s2打印出来的结果不同
