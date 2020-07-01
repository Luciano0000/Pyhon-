'''
案例:
course = ['html','mysql','python']
'''


def func1(name, *args):
    if len(args) > 0:
        for i in args:
            print('{}学过{}'.format(name, i))
    else:
        print('{}没有学过任何编程'.format(name))


course = ['html', 'mysql', 'python']
func1('阿giao', course)
func1('小啊giao', *course)  # 拆包
