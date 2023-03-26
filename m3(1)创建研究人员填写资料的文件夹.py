import easywork.m3研究授权人员资料填写 as method
import os,glob
#初始化非文件夹文件数量
file_notdir=0
#定义最初的文件储存的列表
list_of_file_base_storage=os.listdir(os.path.dirname(method.path))
#初始化授权人员信息的列表
list_of_personnal_information_with_role=[method.catogory_人员信息列表.iloc[i]['授权职位']+method.catogory_人员信息列表.iloc[i]['中文姓']+method.catogory_人员信息列表.iloc[i]['中文名'] for i in range(len(method.catogory_人员信息列表['授权职位']))]
#遍历每一个文件夹的名字，是否有文件，有文件是否属于文件夹，有文件夹是否在授权职位和中文姓名组合的列表内，如果不是，创建文件夹
for filename in list_of_file_base_storage:
    #什么文件夹也没有,直接生成文件
    if len(list_of_file_base_storage)==0:
        for i in range(len(method.catogory_人员信息列表['授权职位'])):
            #从左往右第一个join系人员信息下的扫描版草稿版，第二个join系文件储存列表和人员信息
            os.makedirs(os.path.join(os.path.join(os.path.dirname(method.path),method.catogory_人员信息列表.iloc[i]['授权职位']+method.catogory_人员信息列表.iloc[i]['中文姓']+method.catogory_人员信息列表.iloc[i]['中文名']),'草稿版'))
            #已经有makedirs产生了人员信息下的扫描版，然后直接在扫描版下目录创建一个草稿版即可
            os.mkdir(os.path.join(os.path.join(os.path.dirname(method.path),method.catogory_人员信息列表.iloc[i]['授权职位']+method.catogory_人员信息列表.iloc[i]['中文姓']+method.catogory_人员信息列表.iloc[i]['中文名']),'扫描版'))
        filename='[]'
    #如果有文件都是非文件夹，非文件夹文件数量+1
    if os.path.isdir(os.path.join(os.path.dirname(method.path),filename))==False:
        file_notdir=file_notdir+1
        #如果非文件夹文件数量=所有文件数量，直接生成文件
        if file_notdir==len(list_of_file_base_storage):
            for i in range(len(method.catogory_人员信息列表['授权职位'])):
                os.makedirs(os.path.join(os.path.join(os.path.dirname(method.path),method.catogory_人员信息列表.iloc[i]['授权职位']+method.catogory_人员信息列表.iloc[i]['中文姓']+method.catogory_人员信息列表.iloc[i]['中文名'])
,'扫描版'))
                os.mkdir(os.path.join(os.path.join(os.path.dirname(method.path),method.catogory_人员信息列表.iloc[i]['授权职位']+method.catogory_人员信息列表.iloc[i]['中文姓']+method.catogory_人员信息列表.iloc[i]['中文名'])
,'草稿版'))
    #分三部分核对，第一是必须是文件夹且第二在人员信息列表内，在人员信息列表中移去相应的人信息
    if os.path.isdir(os.path.join(os.path.dirname(method.path),filename)) and filename in list_of_personnal_information_with_role:
        list_of_personnal_information_with_role.remove(filename)
    #先判断不是listdir=[]情况
    if filename!='[]':
            #再列表的index判断filename是否属于它所在文件夹迭代的最后一个文件,且人员列表最后不为空，且非文件夹文件不等于所有文件数量
        if list_of_file_base_storage.index(filename)+1==len(list_of_file_base_storage) and len(list_of_personnal_information_with_role)!=0 and file_notdir!=len(list_of_file_base_storage):                
                #遍历人员信息的列表，生成文件夹
                for file_of_personal_information in list_of_personnal_information_with_role:
                    os.makedirs(os.path.join(os.path.join(os.path.dirname(method.path),file_of_personal_information),'草稿版'))
                    os.mkdir(os.path.join(os.path.join(os.path.dirname(method.path),file_of_personal_information),'扫描版'))
#使用glob获取每个文件的草稿版，如果生成的各个研究人员文件夹里面没有文件，就导入启动会需要签署的文件夹
file_of_draft=glob.glob(os.path.join(os.path.join(os.path.dirname(method.path),'*'),'草稿版'))
number_of_import=0
for file_in_draft in file_of_draft:
    if os.listdir(file_in_draft)==[]:
        if number_of_import==0:
            import easywork.m2启动会 as method2
            number_of_import=number_of_import+1
    #根据启动会需要每个人分别需要签署的文件创立文件夹,最里面的join是到method.path\\草稿版，第二层join是method\\草稿版\\各个文件
    #鉴证代码表,原始数据确认表,研究人员培训表,研究人员授权表,研究物资确认函,筛选入选表,访视确认函,启动会签到表无需放入
        for personal_filename in [documento for documento in method2.frame['中文含义'] if documento not in ['访视确认函','筛选入选表','研究物资确认函','研究人员授权表','研究人员培训表','原始数据确认表','鉴证代码表','启动会签到表']]:
            os.mkdir(os.path.join(file_in_draft,personal_filename))
    #如果授权职位非PI，Sub-I，移除FDF，代码通过判断文件名中是否包含PI和Sub-I，利用列表行列式遍历导入的excel中授权岗位中一栏生成的岗位名称，再判断是否符合
    #利用file_in_draft（也就是草稿版这一层文件夹），往上推一层路径（研究人员职位+姓名），再获取basename        
            if os.path.basename(os.path.dirname(file_in_draft)) in [method.catogory_人员信息列表.iloc[i]['授权职位']+method.catogory_人员信息列表.iloc[i]['中文姓']+method.catogory_人员信息列表.iloc[i]['中文名'] for i in range(len(method.catogory_人员信息列表)) if method.catogory_人员信息列表.iloc[i]['授权职位']!='PI' or 'Sub-I']==True:
                os.remove(os.path.join(file_in_draft,'研究人员财务披露表'))
        print(os.path.basename(os.path.dirname(file_in_draft))+'已创建文件夹，无缺失')               
    if os.listdir(file_in_draft)!=[]:
        print('请使用m3(2)检查是否有缺文件')