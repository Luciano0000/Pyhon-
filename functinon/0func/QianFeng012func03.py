'''
定义一个登陆函数,参数是:username  password
函数体:
判断参数传过来的username,password 是否正确,如果正确则登陆成功,否则打印登陆失败
'''


def login(username, password):
    for i in range(3):
        if username == 'admin' and password == '123':
            print('success')
            break
        else:
            print('error')
            username2 = input('请输入用户名:')
            password2 = input('请输入密码:')
    else:
        print('输入超过三次,用户已锁定')


username2 = input('请输入用户名:')
password2 = input('请输入密码:')
login(username2, password2)
