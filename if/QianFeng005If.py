# 条件判断语句
   # 应用场景： 1.用户名和密码登陆 2.用户的登陆验证（判断用户是否登陆）3.
username = '123'
if username == '123':
    print("dadada")
print("-"*20)
# # ----------两种If语句实现同一个功能------------

print('dadada') if username == '123' else print('第二次----')   # 格式 :  结果 if 表达式  else 结果
print("-"*20)                                                #三目运算符  格式： 表达式  ? 真 : 假

a=6
b=5
result = (a+b) if a > b else (b-a)
print(result)
#    #判断表达式 是true 还是 false
   #如果是true 则 if前面的内容进行运算，并将结果赋值给result
   #如果是false则将else后面的内容运算结果，并将结果赋值给result

# age = int(input('请输入年龄:'))
# username1 = input('请输入用户名:')
#
# if age>18 and username1:
#     print('{}今年{}岁'.format(username1,age))  # tab键缩进键
# print('Game Over')


'''
需求： 消消乐 
        lv1 
        lv2
        ...
    if lv1 :免费玩
       lv2 :充值 升级  买道具 继续玩
'''

print('*'*10, '欢迎来到消消乐', '*'*10)
level = int(input('输入你的级别(1,2):'))
if level == 1:
    print('大佬！随便玩')
else:
    print('已经进入付费级别，请充值！！')
    money = int(input('请充值金币(100的倍数):'))
                                                     # if 语句可以嵌套if，但要注意缩进
    if money % 100 == 0 and money >= 0 :
        print('充值成功，金额是:', money)
    else:
        print('输入有误')

'''
 需求2：
            If 100-90:
             优+
            elif 90-80
              优-
            elif 80-70
              良
            elif 70-60
              及格
            else
              不及格
'''
# 多层 If
age = int(input('请猜猜Jiji的年龄'))
if age < 18:
    print('你拥有一颗善良的心')
elif age > 18 and age < 30:
    print('人家还是个宝宝')
elif age > 30 and age <= 40:
    print('唉！！！')
else:
    print('输入错误')


# for循环语句
# 跳转语句/









