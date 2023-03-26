import glob
import img2pdf as itp
import os


def 批量图片转换pdf():
	for a in glob.glob(r'C:\Users\U1092451\Desktop\*.jpg'):
		file=open(a.replace('jpg','pdf'),'ab')
		content=itp.convert(a)
		file.write(content)
		file.close()

def 删除图片():
	for a in glob.glob(r'C:\Users\U1092451\Desktop\*.jpg'):
		os.remove(a)