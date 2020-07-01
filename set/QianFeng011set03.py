# enumerate()枚举
s = {1, 3, 5, 7, 8, 9}


for index, i in enumerate(s):
    print(index+1, ':', i)

print(enumerate(s))  # <enumerate object at 0x0108D528>


list1 = []
index = 0
for i in s:
    t1 = (index, i)
    list1.append(t1)

    index += 1
print(list1)



