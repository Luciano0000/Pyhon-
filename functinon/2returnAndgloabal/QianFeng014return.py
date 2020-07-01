# 返回值:将函数中运算的结果 通过rerurn关键字 '扔出来'
def add(a, b):
    result = a+b
    print(result)  # 仅仅限于打印在终端上,辅助查看,但是外部无法使用的
    return 'ada', 1, 2


add(2, 6)  # 8

x = add(2, 6)
print(x)  # 8 ('ada',1,2)
'''
   底层逻辑:  若函数体中存在return ,相当于把内存中的函数空间 打开一个通道 用来向函数体外传递return后面的值
传递出去的值 需要有一个tuple去容纳, 所以在调用的时候就需要开辟一个变量 用来存放返回值 
即 变量=函数(实参)
'''