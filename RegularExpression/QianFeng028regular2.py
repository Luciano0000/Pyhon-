# 正则表达式 分组:
# 需求 : 匹配数字0-100之间的数字  不能匹配开头位0的数字
import re

n = '100'
result = re.match(r'[1-9]\d?', n) # 非贪婪
print(result)  # <re.Match object; span=(0, 1), match='10'> 不符合规则
# 原因: [1-9]? 意思是第一位可以是1~9之间的数字的或者没有数字 ,而0不在这个匹配区间内 所以直接回从\d中匹配 匹配0之后 没有匹配区间了 所以没有结果没有9

# 改建版:
result = re.match(r'[1-9]?\d?$|100$', n)
print(result)
'''
符号:
 "|"  :或者
 (word|word|word) : 1.()里面的是整体的字母  区别 [word|word|word] 表示的是单个字母
                    2. 用作分组 '()()' 第一个括号就是第一组
'''

# 验证邮箱 163 qq 126
email = '1215661@qq.com'
result = re.match(r'\w{5,20}@(163|qq|126)\.(com|cn)$', email)
print(result)

# 不是以4,7结尾的手机号码(11位)
phone = '15151515149'
result = re.match(r'1\d{9}[0-35-68-9]', phone)
print(result)

# 爬虫相关:

# 区号可以是3 或者4位 分别打印区号和尾号
phone = '010-12345678'
result = re.match(r'(\d{3}|\d{4})-(\d{8})$', phone)  # () -->分组
print(result.group())
# 分别提取
print('第一组:', result.group(1))  # 提取到第一组的内容
print('第二组:', result.group(2))

# 标签  提取 标签里面的内容
msg = '<html><h1>abc</html>'
msg1 = '<h1>hello</h1>'
result = re.match(r'<[0-9a-zA-Z]+>(.+)</[0-9a-zA-Z]+>$', msg)
print(result)
print(result.group(1))



# 引用分组 方式:
# 方式1:\number 引用分组
result = re.match(r'<([0-9a-zA-Z]+)>(.+)</\1>$', msg1)  # \1 :代表 引用前面的第一个()内的匹配方式 从而节省代码
print(result)
print(result.group(1))
print(result.group(2))

# 结合上述方法
msgs = '<html><h1>abc</h1></html>'
result = re.match(r'<([0-9a-zA-Z]+)><([0-9a-zA-Z]+)>(.+)</\2></\1>$', msgs)
print(result)
print(result.group(3))
