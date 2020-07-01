
# 1 name 变量对应的值的前3个字符 逆序输出 

a = 'name'
print(a[2::-1])


# 2 开发敏感词语过滤程序,提示用户输入内容,如果用户输入的内容包含特殊字符:
# 如'草泥马','尼玛死了',则将内容替换成***


user = input('请输入一个字符串("苍老师","东京热"等敏感词汇禁止输入):')

if user=='草泥马':
    errorname = user.replace('草泥马','***')
    print('输入非法字符{}'.format(errorname))
elif user=='尼玛死了':
     errorname = user.replace('尼玛死了','***')
     print('输入非法字符{}'.format(errorname))
else:
     print('您输入的结果为:{}'.format(user))

#3 循环提示用户输入:用户名,密码,邮箱(要求用户输入的长度
# 不超过20个字符串,如果超过则只有前20个字符有效)
#打印输出: 
# '''
#    用户名 密码 邮箱
 #    admin 123 dasdas@.com
#     ....   ..   . .  
# '''如果用户输入q或Q表示不再继续输入
while True:
    admin = input('请输入用户名(不能超过20个字符串长度),密码,邮箱(请按照格式输入):')
    
    l = admin.find(',')
    admin_user = admin[0:l]#切片用户名
    admin_user_len = len(admin_user) #用户名字符串长度
    #判断用户名是否为20
    if admin_user_len <= 20:
        print('您输入的内容为:{}'.format(admin))
        break
    else:
        answer = input('输入的字符串长度超过20,是否重新输入(y/q)')
        
        if answer.lower() =='y':
            pass
        elif answer.lower() =='q':
            break


# 4.执行程序产生的验证码,提示用户输入用户名,密码和验证码
#如果正确,则提示登陆成功,否则重新输入(要求产生新的验证码)

# 分析 用户输入用户名,密码,验证码 
# 系统随机产生验证码(a-z,0-9) 与与用户输入的验证码作比较
# 若验证码相同则登陆成功否则重新输入用户名密码及验证码

import random
user = input('请输入用户名及密码')
while True:
    coin = 'qwertyuiopasdfghjklzxcvbnm1234567890'#验证码的全部序列
    sum1 = ''  #存取验证码的容器
    #四位验证码
    for i in range(4):
        #产生随机数
        num = random.randint(0,len(coin)-1)
        sum1 += coin[num]
    print('验证码:{}'.format(sum1))

    user_coin = input('请输入验证码')
    #判断验证码是否相同:
    if user_coin.lower() == sum1.lower():
        print('登陆成功!')
        break
    else:
        print('输入验证码有误,请重新输入')



# 5.输入一行字符,统计其有多少个单词,每两个单词直接按以空格隔开

word = input('请输入一句英文短语')
num_l = word.count(' ') #查看空格的个数
word_l = word.replace(' ','')# 替换输入的空格
num_p = len(word_l)  #查看没有空格字符串长度
print(num_l)
print('您输入的单词个数为:',num_p)


# 6.输入两个字符串,从第一字符串中删除第二个字符串中所有的字符
#例如:'They are student.'和'aeiou',则删除之后的第一个字符串变成
#'They r stdnts.'


a = input('请输入一句英文短语')
b = input('请输入要删除的')  
c = ''
#方法一:利用replace()替换
# for i in b:   #遍历b[i] 
#     a = a.replace(b,'')  #替换b[i]中的i元素为''
# print(a)

#方法二:利用逆向思维,不要a[i]=b的元素

for i in a:
    if i not in b: #要a[i]不在b里的字母,例如:a=i like you ;b=i,l
        c += i    # c= ke you
a = c
print(a)
        
    




'''********难点*********
小易喜欢的单词有以下特性:
   1.单词每个字母都是大写
   2.单词没有连续相等的字母
例如:
 不喜欢"ABBA",因为这里有两个连续的"B"
 不喜欢"A","ABA","ABCBA"这两个单词
 用户输入一个单词,系统回答小易是否会喜欢这个单词

'''
# 分析:1. 如果输入的字母没有在A~Z之间就是不是都大写  
#      2. 如果在输入的单词中 第i个单词与第i+1个单词相等则不喜欢

print('小易喜欢(1.单词每个字母都是大写2.单词没有连续相等的字母3.不喜欢"A","ABA","ABCBA"这两个单词)')
word1 = input('请输入单词:')
# 因为涉及到要判断每一个字母的操作,所以需要连续从0-n来自动查看字母,即需要用for 循环
for i in range(len(word1)):  # G O O D 脚标=0 1 2 3  长度=4
    #A !~ Z
    if word1[i]<'A' or word1[i]>'Z': 
        print('不喜欢,单词中没有有大写')
        break
    else:
        # 每个字母i(0,1,2,3)<字母长度(4)-1 (由于需要从第0个字母与第1个字母作比较,比较到第4个字母和第5字母的时候就超出了单词的总长度,
        # 所以只能比较i-1次,比较的时候不能算上最后一个字母否则会报错)
        if i<len(word1)-1 and word1[i]==word1[i+1]: # GOOD第3位无法与第4位判断  
            print('不喜欢,单词中存在叠词')
            break
        elif word1 == 'A' or word1=='ABA' or word1=='ABCBA':
            print('不喜欢,A ABA ABCBA')
            break
else:
    print('喜欢')
        

    



    
    








    