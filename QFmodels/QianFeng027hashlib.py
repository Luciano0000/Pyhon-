# 加密算法：md5--可逆
#   sha1
#  sha256  base64
# decode  encode

import hashlib
msg = '今天晚上五点炸毁五角大楼！'

md5 = hashlib.md5(msg.encode('utf-8'))  # 加密
# hexdigest：十六进制 （hex）-----》  2c2513cee18a1889a3a581fa02449161
print(md5.hexdigest())

sha1 = hashlib.sha1(msg.encode('utf-8'))
print(sha1.hexdigest())  # 63074262a05b5a80dba118e939b1c7c3aab31516

sha256 = hashlib.sha256(msg.encode('utf-8'))
# c27fcada633b07fcd4616b1c17c270a6f3bbe2d54c3f16210cc49f94c983537f
print(sha256.hexdigest())

# 查看md5 sha1 sha256的字符长度
print('md5:', len(md5.hexdigest()), 'sha1:', len(
    sha1.hexdigest()), 'sha256:', len(sha256.hexdigest()))
# md5: 32 sha1: 40 sha256: 64

# 加密密码
password = '123456'  # 加密目标密码
dataBase_list = []  # 模拟数据库
password_sha256 = hashlib.sha256(password.encode('utf-8'))  # 将密码加密
dataBase_list.append(password_sha256.hexdigest())  # 将加密后的密码装入模拟数据库中
# ['8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92']
print(dataBase_list)

pwd = input('请输入密码：')
# 把输入的密码进行sha256加密
pwd_sha256 = hashlib.sha256(pwd.encode('utf-8'))
for i in dataBase_list:  # 输入的加密密码 与 数据库中的加密密码对比 遍历
    if pwd_sha256.hexdigest() == i:
        print('登陆成功')
