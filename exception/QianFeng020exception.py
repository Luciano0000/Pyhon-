# 语法错误和异常
# 语法错误(红色波浪线)
# 异常:程序运行的时候报出来的, xxxError

# 异常处理:
'''
格式:
try:
    可能出现异常的代码
except:
    如果有异常执行的代码
[finally:]
    无论是否存在异常都会被执行



    情况1:
    try:
        有可能会产生多种异常
    except 异常类型1:
        ...
    except 异常类型2:
        ...
    except Exception [as err]: 
    print(err) 获取错误原因err

    如果是多个 except,异常类型的顺序需要注意,最大的Exciption要放到最下面

    情况2:
    try:
        又可能发生的多种异常
    except 异常类型1:
        pass
    else:
        如果try中没有发生异常则进入else中的代码


    注意:如果使用try--else ,则在try代码中不能出现return

    情况3:
    文件操作-->close stream ,数据库操作-->释放资源
    try:
        pass
        return 1
    except:
        pass
        return 2
    finally:
        pass 
        return 3 

finally:无论代码是否有异常都会执行此代码,而且如果代码中有return返回值,则finally下的
返回值会覆盖try和except中的返回值,如果finally没有返回值则不会覆盖上面代码的返回值 
    '''


def func():
    try:
        n1 = int(input('输入第一个数字:'))
        n2 = int(input('输入第二个数字:'))
        # 加法
        per = input('输入运算符:+-*/')

        if per == '+':
            result = n1+n2
            print('两个数的和:', result)
        elif per == '-':
            result = n1-n2
            print('两个数的相减:', result)
        elif per == '*':
            result = n1*n2
            print('两个数的乘法:', result)
        elif per == '/':
            result = n1/n2
            print('两个数的除:', result)
        else:
            print('符号输入有误')

        # 操作列表
        list1 = []
        list1.pop()  # 肯定有问题

        # 文件操作:
        # with open(r'D:\QianFengPRGM\ok\result/txt','w') as wstream:
        #     wstream.write('本次运算为:{}'.format(result))

        with open(r'D:\QianFengPRGM\ok\result/txt', 'r') as rstream:
            print(rstream.read())

    except ZeroDivisionError:
        print('除数不能为0!!!')
    except ValueError:
        print('必须输入数字!!!')
    except Exception as err:
        print('出错了!!!出错原因:', err)


func()


def func1():
    try:
        n1 = int(input('请输入数字:'))
        print(n1)
        # return 1 #return 出去之后 就不再向下执行代码(else不执行)
    except ValueError:
        print('必须是数字')
        # return 2
    else:
        print('数字输入完毕!')  # 没有异常才会执行代码块


# r=func1()
func1()
# print(r)


def fucn2():
    stream = None  # 定义一个空stream流 用来获取finally
    try:
        stream = open(r'D:\QianFengPRGM\ok\aa.txt', 'r')
        container = stream.read()
        print(container)
        return 1  
        # 若有finally有返回值 则这个返回值会被finally覆盖 ,反之执行
    except Exception as err:
        print(err)
        return 2  # 同上
    finally:
        print('------finally-----')
        if stream:  # if stream: -->代表如果stream有值,即不为空,则:
            stream.close()
        return 3  # 执行


x = fucn2()
print(x)
