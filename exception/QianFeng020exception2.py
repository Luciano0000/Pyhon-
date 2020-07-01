# 抛出异常 raise Exception('异常')
# 系统抛出: ValueError ..
# 特殊情况 手动抛出 (系统没有定义的异常我们可以自己定义异常)
# 注册 用户名必修6位


def register():
    username = input('输入用户名(6位):')
    if len(username) < 6:
        raise Exception('len of username is not 6 you need input >6')  # 要抛出的异常
    # Exception: len of username is not 6 you need input >6
    else:
        print('username is:', username)


try:
    register()
except Exception as err:
    print(err)
else:
    print('注册成功')
