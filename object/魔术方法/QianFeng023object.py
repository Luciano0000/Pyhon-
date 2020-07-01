#魔术函数 __init__
# 猫
class Cat:
    type = '猫'  # 固定不变的量

    # 通过__init__初始化的特征
    def __init__(self, nickname, age, color):  # 可能变化的量
        self.nickname = nickname
        self.age = age
        self.color = color

    # 动作:方法
    def eat(self, food):
        print('{}喜欢吃{}'.format(self.nickname, food))

    def catch_mouse(self, color, weight):
        print('{}抓了一只{}颜色{}kg的老鼠'.format(self.nickname, color, weight))

    def sleep(self, hour):
        if hour < 5:
            print('继续睡觉....')
        else:
            print('起床抓老鼠!')

    def show(self):
        print('猫的详细信息')
        print(self.nickname, self.color, self.age)


# 创建对象开辟cat1内存空间
cat1 = Cat('花花', 2, '灰色')
# 通过对象调用方法
cat1.catch_mouse('黑色', 2)  # 抓老鼠
cat1.eat('粑粑')
cat1.sleep(8)
cat1.show()
