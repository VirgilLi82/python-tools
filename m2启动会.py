#作为文件处理方法的初始输入
import pandas as pd
#输入excel文件，所有启动会文件应在等同此excel的目录下
path=input('输入启动会文件的目录路径,需要是xlsx格式')
path=path.replace('\"','')
#利用pandas导入文件
try:
    frame=pd.read_excel(path)
    print(frame)
#读取出现状况时报错
except:
    print('路径不对，读取文件有问题')