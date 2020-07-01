import re

# 第2种引用分组方法:
# 针对代码比较多的
# 起名: (?P<名字>正则式)  ---- (?P=名字)
msg = '<html><h1>abc</h1></html>'

result = re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>', msg)
# (?P<name1>\w+): ?P<name1>\w+ 表示给 "\w+"  起名:name1
print(result.group(3))


# sub('正则表达式',新的内容,'旧内容')    替换

def func(temp):
    num = temp.group()
    num1 = int(num) + 1
    return str(num1)


result = re.sub(r'\d+', func, 'java:99 ,python:68')
print(result)
# 新内容可以是 函数
# 符合正则表达式的旧字符串 当作参数 传入参数中


# split(pattern,str)切割

result = re.split(r'[,:]', 'java:99 ,python:68')
print(result)

# 贪婪 非贪婪
'''
python 里数量词默认是贪婪的(在少数语言中也可能是默认非贪婪),总是尝试匹配可能多的字符;

非贪婪则相仿,总是尝试匹配尽可能少的字符

在"*""+""?""{m,n}"后面加上? ,使贪婪变成非贪婪
'''

msg = 'abc123abc'
result = re.match(r'abc\d+', msg)
print(result)  # match='abc123' 此时默认是贪婪的

#量词后面加上? -->贪婪变换成"非贪婪"
print(re.match(r'abc\d+?',msg)) # 变成非贪婪 match='abc1'