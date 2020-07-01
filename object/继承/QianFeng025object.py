# 关联 has a  和 is a
# has a
import random
'''
公路:Road:
        属性:公路名称,公路长度
车 Car :
        属性:车名 时速
        方法:1,求车名在那条公路上以多少的时速行驶了多长
            get_time(self,road)
            2.初始化车属性信息__init__方法
            3.打印对象显示车的属性
'''

# 声明(定义)Road类


class Road:

    def __init__(self, name, len):
        self.name = name
        self.len = len

# 声明(定义)Car类


class Car:

    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def get_time(self, road):  # rood参数 = 对象r  rood 和 r 指向同一块地址空间
        self.road = road
        ran_time = random.randint(1, 10)
        msg = '{}品牌的车在{}公路上,以{}km/h行驶了{}h'.format(
            self.brand, road.name, self.speed, ran_time)
        print(msg)

    def __str__(self):
        return '{}品牌的,速度:{}'.format(self.brand, self.speed)


# 创建实例化对象
r = Road('进藏高速', 20)  # name len
audi = Car('奥迪', 60)
r.name = '京哈高速'
print(audi)
audi.get_time(r)  # r对象作为参数
