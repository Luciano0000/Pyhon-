'''
案例:
用户注册功能
username
password
email
phone
'''
#分析:准备一个List容器用来存放dict里的信息 [{......}]
datebase = [] #模拟数据库
while True:
    print('--------------欢迎来到"智联招聘"注册界面:')
    username = input('输入用户名:')
    password = input('输入密码:')
    repassword = input('重新输入密码:')
    email = input('输入email:')
    phone = input('输入手机号:')

    #定义字典
    user = {}
    #将信息保存到dict中
    user['username'] = username
    if password == repassword:
        user['password'] = password 
    else:
        print('两次密码不一致!')
        continue

    user['email'] = email
    user['phone'] = phone

    #保存到数据库
    datebase.append(user)
    
    answer = input('是否继续注册(y/n)')
    if answer!='y':
        break
print(datebase)
#--->[{'username': 'asd', 'password': '123', 'email': '123', 'phone': '123'},{},{}......]