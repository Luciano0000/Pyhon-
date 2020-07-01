i = 0
while i < 10:
    print(i)  # 0123456789
    i += 1    # i=10
while i >= 10:
    print(i)   # i=10
    break
print('打印完毕')

# 打印 1-30 之间的所有3的倍数的数字
# 方法1：较为灵活，但是运算慢
u = 1
while u <= 30:
    u += 1
    if u % 3 == 0:
        print(u)
    
print('打印完毕')
# 方法二：运行速度快，但需要提前人工计算
u = 3
while u <= 30:
    print(u)
    u += 3

'''
需求1：
使用while计算1-20的累加和
1+2+3+4.......+20
'''
w = 1
sum_1 = 0
while w <= 20:
    sum_1 += w
    # print(e)
    w += 1
print("1-20的累加和为:", sum_1)

# 打印直角三角形
ceng = 1      # 初始 层 的个数
while ceng <= 5:
    # print('*' * ceng)    # python独有的方式避免重复while
    star = 1   #初始 *的个数
    while star <= ceng:
        print('*', end='')   # print('',end='') 中  end='' 代表不换行
        star += 1
    print()                # print() ==print(/t) --=--- 换行
    ceng += 1

ceng_1 = 1
while ceng_1<=9:
    num = 1
    while num<=ceng_1:
        print('{}*{}={}'.format(ceng_1,num,(ceng_1*num)),end='')
        num += 1
    print()
    ceng_1 += 1



# 打印9x9的乘法表
# ceng_2 = 1
# while ceng_2 <= 9:
#     num = 1
#     while num <= ceng_2:
#         print('{}*{}={}   '.format(num,ceng_2,(num*ceng_2)), end='')
#         num += 1
#     print()
#     ceng_2 += 1

