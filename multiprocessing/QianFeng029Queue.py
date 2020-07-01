# 进程间的通信:
'''

两个进程是两个平行线 互补干扰 是各干各的 互不影响
但是 进程间如何传递数据??

方法: Queue  ---> 队列   (两个进程间的桥梁)

'''
from multiprocessing import Queue

q = Queue(5) # 5 :队列长度
# 放入队列
q.put('a')
q.put('b')
q.put('c')
q.put('d')
q.put('e')
print(q.qsize())  # 队列长度
# q.put('e')  # 如果Queue满了则只能等待.... , 除非有"空地"则才能添加成功
if not q.full():  # q.full() 判断队列是否满了   q.empty()  判断队列是否空了
    q.put('f',timeout=3)
else:
    print('队列已经满了')

# 获取队列的值
for i in range(5):
    print(q.get())
#
# q.put_nowait()
# q.get_nowait()

