# 函数
# 作用:将重复的代码,封装到函数,只要使用的时候直接调用此函数
# 增强代码的模块化和提高代码的重复利用率

# def 函数名 ([参数,...]):
# 函数体 ----->重复的代码

'''
定义函数 随机数的的产生
'''
import random


def generate_randaom():
    for i in range(10):
        ren = random.randint(1, 200)
        print(i+1, ':', ren)


print(generate_randaom)
# <function generate_randaom at 0x034D9190> 地址

generate_randaom()  # 找到改地址上的内存,并执行内存内的函数代码
