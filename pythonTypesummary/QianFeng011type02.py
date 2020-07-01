#类型转换
#str()  int()   list()  dict()  set()   tuple()


#str()>>>>> int,    list,   set,   tuple
#反过来str()<<< int,list,set,tuple,dict,float

#list>>>>set() , tuple(),   dict要符合 [(key,value),()..]
#反过来list<<<<  tuple() , set() ,  dict 只是将key保存在list中
s = '2'
i = int(s)
print(type(i),i)

s = 'abc'
l = list(s)
print(type(l),l)

s = set(s)
print(type(s),s)

s = tuple(s)
print(type(s),s)

#反过来
#int()>>>>>str
i1 = 8
s1 = str(i1)
print(type(s1),s1)
#list()>>>>str
list1 = ['a','b','c']
l2= str(list1)
print(type(l2),l2)

