# random 模块
import random

ren = random.random()  # 0~1之间的随机小数
print(ren)

# randrange(start,stop,step)  [1....,10) step=2  -->1,3,5...
ran = random.randrange(1, 10, 2)
print(ran)

ran = random.randint(1, 10)  # [1,...,10]
print(ran)

# 随机选择字符串类型（点名）******字符串!!!!!******
list1 = ['张三', '里斯', '王五']
ran = random.choice(list1)  # 随机选择列表的内容
print(ran)

# shuffle 洗牌s
pai = ['红桃A', '黑桃K', '梅花8']
random.shuffle(pai)  # 打乱顺序
print(pai)


# 验证码 4位大小写字母与数字的组合 随机产生


def func():
    code = ''
    for i in range(4):
        ran1 = str(random.randint(0, 9))
        ran2 = chr(random.randint(65, 90))  # ASCIL码 中 65=A 90=Z  chr()是将数字变成字母
        # ASCIL码 中 65=a 90=b  chr()是将数字变成字母
        ran3 = chr(random.randint(97, 122))
        r = random.choice([ran1, ran2, ran3])  # 列表里必须是字符串类型

        code += r
    return code


d = func()
print(d)

# chr ord

print(chr(65))  # Unicode码 --》str
print(ord('A'))  # str-->Unicode码
print(ord('大'))  # 22823
