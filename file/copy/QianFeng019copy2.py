import os
src_path = r'D:\QianFengPRGM\ok'  # 想要复制的目录下
target_path = r'D:\QianFengPRGM\oktarget2'  # 想要粘贴的目录下

def copy(src_path,target_path):
    filelist = os.listdir(src_path)  # 查看被复制的目录下的文件
    print(filelist)  # ['aa.txt', 'test.py']

    for file in filelist:  # 遍历filelist
        # 文件夹,文件[i] (i=0,i++)
        #file[index=0]--->aa.txt
        #file[index=1]--->test.py
        #file[index=2]--->haha    -----是文件夹
        path = os.path.join(src_path, file)
        #path[0]--->D:\QianFengPRGM\ok\aa.txt
        #path[1]--->D:\QianFengPRGM\ok\test.py
        #path[2]--->D:\QianFengPRGM\ok\haha
        # 判断path是不是个文件夹(path[2]是文件夹),而open()不能直接复制粘贴文件夹
        if os.path.isdir(path):  # true
            target_path1=os.path.join(target_path,file)#在想要粘贴的目录下拼接file[2]
            os.mkdir(target_path1) #创建D:\QianFengPRGM\oktarget2\haha
            #调用copy()
            copy(path,target_path1)
        else:  # false
            # 直接复制文件即可
            with open(path,'rb') as rstream:#with open(目录/文件名[0]) as (读)管道
                container=rstream.read()

            path1=os.path.join(target_path,file)#with open(目标目录/文件名[0]) as (写)管道
            with open(path1,'wb') as wstream:
                wstream.write(container)

#调用
copy(src_path ,target_path)