#m2下的操作，按照excel文件中文含义生成文件夹

#导出easypdf下的m2,旗下的变量及方法引用至m2（1）模块
import easywork.m2启动会 as method
import os
#遍历中文含义的dataframe列，生成文件夹
for a in method.frame['中文含义']:
    os.mkdir(os.path.dirname(method.path)+'\\'+str(a))