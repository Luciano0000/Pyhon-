
# 案例1 :实现登陆 加入购物车功能


islogin = False  # 默认状态没有登陆


def add_shoppingcart(names, goodsName):  # gooodsName 商品
    global islogin  # 允许islogin从函数体内部与外部交互
    if islogin:  # 如果islogin=True:
        if goodsName:
            # 登陆的
            print('{}成功将{}加入到购物车'.format(names, goodsName))
        else:
            print('没有选中任何商品')
    else:
        # 没有登陆
        answer = input('用户没有登陆! 是否登陆用户(yes/no)')
        # 登陆
        if answer == 'yes':
            name = input('请输入用户名:')
            word = input('请输入密码:')
            # 调用login函数
            islogin = login(name, word)  # 在一个函数中可以调用另一个函数
            add_shoppingcart('老八', '粑粑')
        else:
            print('拜拜')


def login(username, password):  # 登陆函数
    if username == 'admin' and password == '123':
        # 登陆成
        print('登陆成功')
        return True
    else:
        print('用户名或者密码错误!')
        return False


name = input('请输入用户名:')
word = input('请输入密码:')
islogin = login(name, word)  # 将返回值(True,False)传递给islogin
add_shoppingcart('老八', '粑粑')  # 调用函数


#案例2 :用户登陆输入用户名输入密码输入验证码
'''

import random
def generrate_cheakcode(n):# 定义:产生验证码函数
    s = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    code = ''
    for i in range(n):
        ran = random.randint(0, len(s)-1)  # 随机个s的下标给ran
        code += s[ran]  # 下标下的值赋值给code
    return code  # 把验证码扔出


def login():  # 登陆函数
    username = input('请输入用户名')
    password = input('请输入密码')
    # 得到一个验证码
    codes = generrate_cheakcode(5)  # 调用generrate_cheakcode(n)函数
    print('验证码是:', codes)
    code1 = input('输入验证码:')

    if codes.lower() == code1.lower():   # 验证验证码

        if username == 'admin' and password == '123':  # 验证码输入正确
            print('登陆成功')
        else:
            print('用户名或者密码有误')

    else:
        print('验证码有误')


# 调用
login()

'''

