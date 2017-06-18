# -*- coding:utf-8 -*-

#!/usr/bin/env python

import os


def get_filenames():

	abspwd = os.getcwd()
	files = os.listdir(abspwd)
	file_list = []
	for a_file in files:
		if a_file!='.DS_Store' and a_file[-2:]!='py' :  # 筛选需要操作的文件
			file_list.append(a_file)

	return file_list


def del_files(file_list):

	for a_file in file_list:
		
		
		if a_file[-4:] == 'html':
			'''
			Delete .html
			'''
			a_file = a_file.replace(' ','\\ ')  #只有os.system()里的空格才需要转义
			execute_shell = 'rm -rf '+str(a_file)
			# print execute_shell
			os.system(execute_shell)
			print  str(a_file)+' is deleted!'

		else:
			'''
			下一层目录
			'''
			second_dic_files = []

			if os.path.isdir(a_file):  #这里的不用转义

				file_list = os.listdir(a_file)
				for file_name in file_list:
					file_name = str(a_file) +'/'+ str(file_name)
					second_dic_files.append(file_name)
			
			for a_file in second_dic_files:
				'''
				Delete ^.jpg
				'''
				if a_file[-3:] != 'jpg':
					a_file = a_file.replace(' ','\\ ')  #只有os.system()里的空格才需要转义
					a_file = a_file.replace('(','\\(')  # ()也需要转义
					a_file = a_file.replace(')','\\)')  
					execute_shell = 'rm -rf ' + str(a_file)
					print execute_shell
					os.system(execute_shell)
					print  str(a_file)+' is deleted!'

if __name__ == '__main__':

	file_list = get_filenames()

	del_files(file_list)
	
		


