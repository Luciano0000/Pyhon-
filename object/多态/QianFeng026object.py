# 多态  封装   继承 ---->面向对象
# 多态 python不是严格意义上的多态,需要借助isinstance(obj,类)来判断


class Person:
    def __init__(self, name):
        self.name = name

    def feed_pet(self, pet):  # pet既可接收cat也可以接收dog还可以接收tiger
        # isinstance(obj,类) --> 验证obj是否是这个类的子类的对象或者是否是这个类的对象
        if isinstance(pet, Pet):  # 判断pet是不是Pet类
            print('{}喜欢养宠物:{},昵称是{}'.format(self.name, pet.role, pet.nickname))
        else:
            print('不是宠物')


class Pet:
    role = 'Pet'

    def __init__(self, nickname, age):
        self.nickname = nickname
        self.age = age

    def show(self):
        print('昵称:{},年龄:{}'.format(self.nickname, self.age))


class Cat(Pet):
    role = '猫'

    def catch_mouse(self):
        print('抓老鼠..')


class Dog(Pet):
    role = '狗'

    def watch_house(self):
        print('看家高手')


class Tiger:
    def eat(self):
        print('太可怕了能吃人 ,不能当宠物养')

# 创建对象


cat = Cat('花花', 2)
dog = Dog('哈士奇', 4)
person = Person('主人')
person.feed_pet(cat)  # 传对象
person.feed_pet(Tiger)


# pet 父类  cat dog 子类
# pet 大类型  cat  dog 小类型
