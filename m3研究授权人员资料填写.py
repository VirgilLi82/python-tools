import pandas as pd
path=input('输入中心及人员信息列表的目录路径,需要是xlsx格式')
path=path.replace('\"','')
try:
    catogory_项目信息=pd.read_excel(path,sheet_name='项目信息')
    catogory_中心信息列表=pd.read_excel(path,sheet_name='中心信息列表')
    catogory_人员信息列表=pd.read_excel(path,sheet_name='人员信息列表')
    print('你已成功打开中心及人员信息列表')
except:
    print('列表打开有误，请检查路径')