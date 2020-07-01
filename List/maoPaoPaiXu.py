#泡泡排序 
myList = [4,1,7,0]  #4
#外层控制轮数
for i in range(len(myList)-1):  #i= 0 1 2 
#内层两两比较
    for j in range(0,len(myList)-1-i):
        if myList[j] > myList[j+1]:
            myList[j],myList[j+1] = myList[j+1],myList[j]
print(myList)
'''
注意点 :
len(myList)-1 : 因为列表的元素要两两比较,4个数字比较三次 即4-1=3次
  当 len(myList)-1从0开始时:
  for i in range(3)
    #当i = 0时

    -----------------------------------------------------
    for j in range(0,3):  #j抓取0:
        if myList[0]>myList[1]:  #4>1    
         4,1=1,4 #替换               #1 4 7 0
    ------------------------------------------
    for j in range(0,3):  #j抓取1:
        if myList[1]>myList[2]:  #4>7    
            结束                     # 1 4 7 0
    ------------------------------------------
    for j in range(0,3):  #j抓取2:
        if myList[2]>myList[3]:  #7>0
            7,0=0,7 #替换            # 1 4 0 7    此时找到末尾最大元素

    #当i= 1时
    ------------------------------------------------------
    for j in range(0,2): #j抓取0:
        if myList[0]>myList[1]:  #1>4  
            结束                     #1 4 0 7
    ----------------------------------------
    for j in range(0,2): #j抓取1:
        if myList[1]>myList[2]:  #4>0: 
            4,0=0,4                 # 1 0 4 7
    -----------------------------------------
    for j in range(0,2): #j抓取2:
            if myList[2]>myList[3]: #4>7: 
               结束                 # 1 0 4 7

    #当i = 2时
    -------------------------------------------------------
    for j in range(0,1): #j抓取0:
            if myList[0]>myList[1]: #1>0: 
             1,0=0,1                # 0 1 4 7                 
    ----------------------------------------
      for j in range(0,1): #j抓取1:
            if myList[1]>myList[2]: #1>4: 
             结束                    最后结果: 0 1 4 7      
'''