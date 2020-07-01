import os
#文件复制
src_path=r'D:\QianFengPRGM\ok'
target_path=r'D:\QianFengPRGM\oktarget'

#封装:
def copy(src,target):

    if os.path.isdir(src) and os.path.isdir(target):
        filelist=os.listdir(src) #['aa.txt','',..]

        for file in filelist: #aa.txt
            path=os.path.join(src,file) #目录,文件
            with open(path,'rb') as rstream:
                container=rstream.read()

            
            path1=os.path.join(target,file)
            with open(path1,'wb') as wstream:
                wstream.write(container)
        else:
            print('复制完毕')

#调用
copy(src_path,target_path)