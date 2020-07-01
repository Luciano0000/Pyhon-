a = 'qwertyui'
b = input('输入')

print(any(num in b for num in a))# num 在 b?  for  num 在 a?
'''
需求：掷色子

1.欢迎进入游戏
2.输入用户名，默认用户没有金币
3.提示用户充值买币（100块钱=30游戏币，充值必须是100的倍数，充值不成功可以再次充值）
4.玩一局扣除2个币，猜大小（系统用随机数模拟筛子产生值）
5.只要猜对了则奖励1个游戏币，可以继续玩（想玩就玩，没币自动推出）

'''
import random
print('*'*20)
print('欢迎来到澳门赌场')
print('*'*20)

name = input('请输入用户名:')
money = 0
strb='qwertyuiopasdfghjklzxcvbnm1234567890'
answer = input('是否要进入游戏:(y/n)')
if answer == 'y':
    while money < 2:
        #钱包小于2执行以下代码
        n = int(input('请充值（100块钱=30游戏币，充值必须是100的倍数，充值不成功可以再次充值）'))
        if n % 100 == 0 and n > 0:
            money = (n // 100) * 30
            print('{}充值成功,当前游戏币为{}'.format(name, money))
            print('已进入游戏，系统正在随机产生两枚筛子')
        elif n<100:
            print('您输入有误')
        #充值成功，进入游戏
            break
        #充值成功后进入下层游戏循环，如果用户不手动关闭游戏，系统则会在用户把金币花完之后自动推出游戏
        while True:
            
            a=random.randint(1,6)
            b=random.randint(1,6)
            say = input('请输入（大/小）')
            
            if ((a+b)>6 and say=='大') or ((a+b)<=6 and say=='小'):
                
                print('猜对了，奖励一枚游戏币')
                money += 1
                money -= 2
                print('当前游戏币为{}:'.format(money))
                if money<=0:
                    print('当前账户不足')
                    break

            # elif say in strb:
            #     print('您输入有问题,系统已经重新初始化')
            else:
                if any(num in say for num in strb):   #判断（任意次序排列）的字符串是否在另一个字符串里 返回值为布尔类型
                    print('输入非法字符,系统已初始化')
                    continue
                
                money -= 2
                print('猜错了')
                print('当前余额:{}'.format(money))
                answer_1 = input('是否继续(y/n)')
                if answer_1!='y' or answer_1=='n':
                    break
                else:
                    pass      
                if money <= 0:
                    print('当前账户不足')  
                    break
else:
    print('拜拜！')














