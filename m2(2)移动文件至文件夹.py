import easywork.m2启动会 as method
import glob,shutil,os
#将同一目录下的文件逐个放置对应文件夹
for a in range(len(method.frame)):
	file=glob.glob(os.path.dirname(method.path)+'\\'+'*'+method.frame.iloc[a]['文件英文名']+'*')[0]
	shutil.move(file,file.replace(os.path.dirname(file),os.path.dirname(file)+'\\'+str(method.frame.iloc[a]['中文含义'])))

