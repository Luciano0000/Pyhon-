# 带参数的函数
'''
格式:
定义:
def 函数名 (参数,...):
    函数体

调用:
    pass
'''
import random
# 定义一个随机数的函数,产生的个数???


def generate_random(number):  # 形参:挖坑
    for i in range(number):
        ren = random.randint(1, 20)
        print(i+1, ':', ren)


print(generate_random)
# 调用
generate_random(1)  # 实参:填坑
generate_random(5)

# 定义一个求加法的函数


def add(a, b):
    result = a+b
    print(result)


add(1, 2)
