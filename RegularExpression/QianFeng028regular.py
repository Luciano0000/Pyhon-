''''''
'''
*****************************************************
*********************永远都是验证"字符串类型"的*************
*********************************************************

正则表达式的定义 :
正则表达式是对字符串操作的一种逻辑公式,就是用事先定义好的一些特定字符,及这些特定字符的组合,组成一个"规则字符串",这个"规则字符串"
正则表达式是对字符串(包括普通字符(例如,a 到 z之间的字母)和特殊字符(称为"元字符"))操作的一种逻辑公式,就是用事先定义的一些特定的字符,
    及这些特定字符的组合,组合成一个"规则字符串" ,这个"规则字符串" 用来表达对字符串的一种过滤逻辑.正则表达式是一种文本模式,模式描述在
    搜索文本时要匹配的一个或多个字符串.


正则表达式的作用和特点
给定一个正则表达式和另一个字符串,我们可以达到如下目的:
    1.给定的字符串是否符合正则表达式的过滤逻辑(称作:"匹配")
    2.可以通过正则表达式,从字符串中获取我们想要的特定部分

正则表达式 模块: re
match()  search()  findall()  sub()  split()
'''
import re

msg = '娜扎热巴黛丝佟丽娅'
pattern = re.compile('佟丽娅')
result = pattern.match(msg)  # 没有匹配
print(result)
print('-' * 20)
# 使用正则模块方法：match()
s = '娜扎佟丽娅热巴黛丝'
result = re.match('佟丽娅', s)  # match() 从开头开始匹配，如果匹配不成功则返回None
print(result)
print('*'*20)
result = re.search('佟丽娅', s)
print(result, 'span:', result.span())  # search() 进行正则字符串匹配方法，匹配的是整个字符串.  即：查找
# .span(start,end) 返回值：位置   原则：包前不包后

print(result.groups())
print(result.group())
# 使用group：提取到匹配的内容，即match='group'


# a2b h6k

s = '哈哈5a'
result = re.search('[0-9][a-z]', s)  # [0-9] 0~9任意数字  [a-z] a~z任意字符
print(result)
# <re.Match object; span=(2, 4), match='5a'>

msg = 'abcd65165ashtrhtr0ds0r'
# serch()  匹配整个字符串，但是只找一次 就停
result = re.search('[a-z][0-9][a-z]', msg)  #
print(result.group())

# findall()  #  匹配整个完整字符串  即：一直检索，一直到末尾元素
result = re.findall('[a-z][0-9][a-z]', msg)
print(result)
'''
# 正则符号
# 定义正则验证次数：
# '.' :用于匹配除了换行符(\n) 之外的任意字符
# '{m}'  用于验证将前面的模式匹配m次
# '{m,}' 用于验证将前面的模式匹配m次 或者 多次  即：>=m
# '{m,n}'用于验证将前面的模式匹配>=m次 and <= n次
# '^' 行首
# '$' 行尾
'''
'''
# 正则预定义:
# \d: 数字等价于[0-9]  digit
# \D: 非数字[0-9]
# \s: 任意空白字符 等价于[\t\n\r\f]     space
# \S: 非空白字符
# \w: 匹配 任意字符数字及下划线,等价于[a-zA-Z0-9_]  word_
# \W: 非[a-zA-Z0-9_]
# \\: 匹配斜杠 \
# \b: 边界 指单词和空格间的位置. 例如'py\b'可以匹配"python"中的'py',但不能匹配"openpyxl"中的'py'

# 量词:
# "*" :>=0
# "+" :>=1
# "?" :没有 或者 有一个

 "|"  :或者
 (word|word|word) : 1.()里面的是整体的字母  区别 [word|word|word] 表示的是单个字母
                    2. 用作分组 '()()' 第一个括号就是第一组
                    
# 引用分组 方式:
# 方式1:\number 引用分组         
#方式2: 起名  ?P<名字>正则式)  ---- (?P=名字)
'''



# a7a  a88a  a7878a
msg = 'das12ddfs1ds1fd2f33fd3ggg333ga'
result = re.findall('[a-z][0-9]+[a-z]', msg)  # 0~9 后面的数可以是>=1的
print('要字母任意数字长度字母：', result)

# qq号码验证 5~11位  开头不能是0
qq = '1035232713'  # 第一位：0~9十个数 后面的4个数 到 算上这4个数的十个数 1~9随意数字 即 4<=x<=10
# 从开头开始匹配 用 match() 第一位19~ 后面的额
res = re.match('^[1-9][0-9]{4,10}$', qq)
print(res)

# 用户名可以是字母或者是数字下划线,不能是数字开头,用户名长度必须是6位以上 [0-9a-zA-Z]

username = 'admin001_'
result = re.search('^[a-zA-z][\w]{5,}$', username)
print(result)

# 检索.py文件
msg = 'aa*py ab.txt  bb.py       kk.png uu.py  b.txt'
result = re.findall(r'\w+\.py', msg) #\. 解释: 因为aa*py不是.py文件,所以需要.py 但是在正则里面.是正则符号 ,所以需要转义下字符 即:\.py
print(result)



#手机号正则式:  首位必须是1 第二位可以是35789
phone=input('输入手机号:')
result=re.match('1[35789]\d{9}$',phone)
print(result)