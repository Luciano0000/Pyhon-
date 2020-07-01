# 开发:登陆验证
import time

islogin = False  # 默认没有登陆

# 定义一个登陆函数


def login():
    username = input('输入用户:')
    password = input('输入密码:')
    if username == 'admin' and password == '123':
        return True
    else:
        return False

# 定义一个装饰器用来进行付款验证


def login_required(func):
    
    def wrapper(*args, **kwargs):
        global islogin
        print('------------付款-------------')
        # 验证用户是否登陆:
        if islogin:
            func(*args, **kwargs)
        else:
            # 跳转到登录页面
            print('用户没有登陆,不能付款')
            islogin = login()
            print('result:', islogin)

    return wrapper


# 付款模块

@login_required
def pay(monney):
    print('付款金额是{}'.format(monney))
    print('付款中......')
    time.sleep(2)
    print('付款完成!')

#调用
pay(10000)
pay(800)