# -*- coding:utf-8 -*-

#!/usr/bin/env python

'''
python 2.7

'''

__auther__ = 'github/mashaz'


import os


def get_filenames():

	abspwd = os.getcwd()
	files = os.listdir(abspwd)
	file_list = []
	for a_file in files:
		if a_file!='.DS_Store' and os.path.isdir(a_file) :  # 筛选需要操作的目录
			file_list.append(a_file)

	return file_list

if __name__ == '__main__':
	file_list = get_filenames()
	for a_file in file_list:
		if a_file[-6:]=='_files':
			a_file = a_file.replace(' ','\\ ')  #只有os.system()里的空格才需要转义
			a_file = a_file.replace('(','\\(')  # ()也需要转义
			a_file = a_file.replace(')','\\)')  
			execute_rename = 'mv ' + str(a_file) + ' ' +str(a_file.rstrip('_files')) 
			os.system(execute_rename)
	