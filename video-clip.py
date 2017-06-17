# -*- coding:utf-8 -*-
#!/usr/bin/env python

import os

def get_filenames():
	abspwd = os.getcwd()
	files = os.listdir(abspwd)
	file_list = []
	for a_file in files:
		if a_file!='.DS_Store' and a_file[-3:]=='mp4' and a_file[0:6]!='edited':  # 筛选需要操作的文件
			file_list.append(a_file)

	return file_list

if __name__ == '__main__':
	file_list = get_filenames()
	for video_file in file_list:
		video_file = video_file.replace(' ','\\ ')
		execute_ffmpeg = 'ffmpeg -ss 00:00:04 -i '+str(video_file) + \
						' -vcodec copy -acodec copy '+'edited-' + str(video_file)
		print execute_ffmpeg
		os.system(execute_ffmpeg) 
		print video_file + ' completed !'
