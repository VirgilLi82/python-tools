import easywork.m2启动会 as method
import os,glob,shutil
#遍历excel中dataframe的中文含义，然后在sop存放的文件夹寻找
for num in range(len(method.frame)):
    try:
        sop=glob.glob(r"C:\Users\U1092451\Desktop\个人文件\培训\SOP表格使用方法\\"+"*"+str(method.frame.iloc[num]['中文含义'])+'*')
        #如果有项目自己的sop，那么搜索后会出现不止一个
        if len(sop)>1:
            #需要选择合适的sop
            #这里做一个小处理，将目录隐去
            print([os.path.basename(sopname) for sopname in sop])
            select_number=input('请从左到右按照0、1、2.....顺序选择输入sop,最多输入到--'+str(len(sop)-1)+'--，请输入：')
            select_number=int(select_number)
            #选好sop后开始移动至对应的文件夹,先用glob定位path对应文件夹
            #文件夹是通过os.path.split分解m2.path得到母目录（【0】），然后通过中文含义定位
            filesrc=glob.glob(os.path.split(method.path)[0]+'\\'+str(method.frame.iloc[num]['中文含义']))[0]
            #将SOP移动至对应的文件夹里
            #初始地址可以从先前的sop变量中获得，
            #目标地址从filesrc中获得根目录（path的上级目录），然后文件目录通过os.path.split分解sop选择的地址，选择【1】最后一个分隔符右边的内容
            shutil.copy(sop[select_number],filesrc+'\\'+os.path.split(sop[select_number])[1])    
        elif len(sop)==1:
            #只有一个sop，就直接放进去
            filesrc=glob.glob(os.path.split(method.path)[0]+'\\'+str(method.frame.iloc[num]['中文含义']))[0]
            shutil.copy(sop[0],filesrc+'\\'+os.path.split(sop[0])[1])
        else:
            print('无法搜索文件，此文件名是'+str(method.frame.iloc[num]['中文含义']))
            continue
    finally:
        #判断使用须知是否存在，不存在就放到path下
        if os.path.exists(os.path.split(method.path)[0]+'\\'+'使用须知.docx')==False:
            shutil.copy(r"C:\Users\U1092451\Desktop\个人文件\培训\SOP表格使用方法\使用须知.docx",os.path.split(method.path)[0]+'\\'+'使用须知.docx')