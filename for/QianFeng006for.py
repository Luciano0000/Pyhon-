# 循环结构 :
# for 变量名 In 集合:
# range(m,n,step)‘范围()’   integer整形    Sequence序列 队列   Exclude不包含

# 使用系统给定range()完成范围指定
print(range(8))     # [0,8)里的整形数字,即0,1,2...7八个数字

for i in range(1, 51):
    sum = 0
    if i % 2 == 0:
        sum += i
print(sum)
print(i)   #由于i 一直在做if判断，所以当for循环抓取到50结束之后返才回给print(i)，最后打印结果就是50
#下一个则是循环3次打印抓取结果
for i in range(1, 4):
    print('打印i', i)     # range(3)  集合里产生0,1,2数字。'for'会按照顺序
                           #重复的抓取集合里的结果传递给一直在等待接收的变量'i' ，
print('for结束之后我才出来！！！')


user1 = 'abcdefg'
#把'abcdefg'连续的抓取给i
for i in user1:
    print(i,end='')
print()





# 应用场景：
# 消消乐---反复充值
# 用户的登录 用户名 密码  -->错误 ---->重复输入 出现“验证码”（避免暴力破解）
# 猜大小 ---反复猜

# 1-20不能被3整除的数做累加：
sum = 0
for i in range(20):

    # 方法一:
    # if i % 3 != 0:
    #     sum += i

    # 方法二:
    if i % 3 == 0:
        continue       #:continue 跳出下方的语句不执行，继续执行下一次循环
    sum += i
print('1-20不能被3整除的数为做累加:', sum)



name = '赵飞'
# 方式一：
for i in range(5):
    print('{}很饿，正在吃{}个馒头'.format(name, i+1))  # 0+1-->1+1-->2+1-->3+1-->4+1

# 方式2：
for i in range(1, 6):  # 12345
    print('{}很饿，正在吃{}个馒头'.format(name, i))
print('{}说终于吃饱了'.format(name))

# 5个馒头中第三个馒头中有毒
Name = '张无忌'
for i in range(1, 6):
    #判断i 的值是多少,i==3 不吃
    if i == 3:
        print('{}赶快扔掉这个馒头，"鹤顶红"有剧毒。'.format(Name))   #当循环到第三次i==3时进入if程序结束后,继续向下执行代码
    else:
        print('{}很饿，正在吃{}个馒头'.format(Name, i))

print('{}说:终于吃饱了'.format(Name))
#for i in range(3)
#    if 条件:
#       表达式1
#    else:
#       表达式 2
# 表达式3
# /  顺序:   第i次循环 判断条件进入相应的条件中,表达式3

'''
for i in 范围:
    范围里'有'数据执行的语句
else:
    范围里'没有'数据执行的语句
......
pass 
'''
num = int(input('请输入需要的馒头数量:'))
for i in range(num):
    print('{}很饿，正在吃{}个馒头'.format(Name, i+1))
else:    # 当for i in range(0)空循环时候执行else      python独有的
    print('还没有给我满头，{}饿哭了'.format(Name))
print('--------')

# pass   空语句，不报语法Error
if 10 < 7:
    print('10是大')
else:
    pass     # 为了保证条件句结构的完整
print('--判断结束---')

for i in range(3):
    pass




#用户的账号密码登录，而且只能登录三次，如果三次未成功则锁定账户不能登陆
# break ------->强制退出循环,继续执行循环外下面的代码
t = 0           #次数
for i in range(3):
    t += 1                #循环一次 t+1
    usernmae = input('请输入用户名:')
    password = input('请输入密码:')
    if usernmae == 'admin' and password == '123':
        print('登录成功')
        print('------------轻松购物吧！--------------')  # 登录成功时
        break                                              #成功直接跳出循环

    elif t < 3:                   # 次数<3 用户名密码有误，继续进入第i+1次循环
        print('用户名或者密码有误！')
    else:                           # 次数>3 输出账户锁定，与此同时i=3 循环结束
        print('重复超过三次，账户锁定，需要重新激活')
#第二种方法

for i in range(3):
    usernmae = input('请输入用户名:')
    password = input('请输入密码:')
    if usernmae == 'admin' and password == '123':
        print('登录成功')
        print('------------轻松购物吧！--------------')  # 登录成功时
        break                                              #成功直接跳出循环
    else:
        print('用户名或者密码有误！')
else:                              # 输入用户名密码错误i次 range(3-i)--->range(0)时直接进入for循环结构中的 else中
    print('重复超过三次，账户锁定，需要重新激活')






# 黑店馒头铺的故事：用户吃到第二个馒头发现有毒，不吃，进入小鞋大门
for i in range(3):   # 0 1 2
    if i == 1:
        print('呕！这馒头有毒~~~')
        break
# break 跳出循环

    else:
        print('这家馒头的味道怪怪的！')
print('------进入消费者协会大门进行投诉')

for i in range(1,100,5):  # 若是要用step，则前面的两个参数一定要有
    print(i)





