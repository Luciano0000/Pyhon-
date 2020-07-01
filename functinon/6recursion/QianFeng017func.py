# 递归函数:函数自己调用自己
'''
普通函数:
    def func(): pass
匿名函数:
    lambda 参数:返回结果
递归函数:
    普通函数的另外一种表现形式
    特点:
        1.递归函数必须要设定终点
        2.通常会有一个入口和出口
'''

# 递归函数


def sum(n):  # 1~100的累加和
    if n == 0:  # 终点
        return 0
    else:  # 出口
        return n+sum(n-1)  # 10+9+8+....0


# 调用
result = sum(100)  # 入口
print(result)

# 等价于

# for遍历
sum1 = 0
for i in range(101):  # 0~100
    sum1 += i
print(sum1)


def f1(n):
    if n > 0:
        print('----->', n)
        f1(n-1)
    else:
        print('----->', n)


f1(5)
