'''
符号: 
    ==              判断两个集合内容是否一样 返回true false 

    +(不支持)
    *(不支持)

    -               差集
    difference()    等价于 -
    difference_update() 对称差集并赋值

    &               交集
    intersection()  等价于&
    intersection_update() 对称交际并赋值

    |               并集
    union()         等价与|
    union()_update() 对称并集并赋值

    ^               两个list中不一样的元素
    symmetric_difference()
    symmetric_difference_update()


'''
set2 = {1,2,3,4}
set3 = {3,4,5,6,7}

# set4 = set2+set3
# print(set4)

#   - 差集 difference()
set4 = set3-set2
print(set4)
#{3,4,5,6,7}-{1,2,3,4}={5, 6, 7}
set4 = set3.difference(set2)#等价上式
print(set4)
# set3.difference_update(set2)#等价上式
# print(set3)

#    & 交集  intersection()
set6 = set3 & set2
print(set6)
#{3, 4}
set7 = set3.intersection(set2)#等价上式
print(set7)
# set3.intersection_update(set2)#等价上式
# print(set3)

#   | 并集 union() 联合
set8 = set2 | set3
print(set8)
#{1, 2, 3, 4, 5, 6, 7}
set9 = set2.union(set3)#等价上式
print(set9)