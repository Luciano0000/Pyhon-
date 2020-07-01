list1 = [3, 4, 5, 6]
m = max(list1)
print('list最大值:', m)

list2 = [
    {'a': 10, 'b': 23},
    {'a': 17, 'b': 21},
    {'a': 12, 'b': 29}
]

m = max(list2, key=lambda x: x['a'])
print('列表的最大值:', m)


students = [
    {'name': 'tom', 'age': 20},
    {'name': 'lucy', 'age': 23},
    {'name': 'kam', 'age': 18},
    {'name': 'mark', 'age': 13},
    {'name': 'kary', 'age': 22},
    {'name': 'jack', 'age': 19},
    {'name': 'strven', 'age': 30},
]
# 找出student中年龄大于20的学生
result = filter(lambda x: x['age'] >= 20, students)
print(list(result))

# 按照年龄从大到小排序
students = sorted(students, key=lambda x: x['age'], reverse=True)
print(students)

students=sorted(students,key=lambda x: x['age'])
print(students)