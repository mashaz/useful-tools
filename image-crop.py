# -*- coding:utf-8 -*-
#!/usr/bin/env python

from PIL import Image
import os
import sys

FileNames=os.listdir('images')  
i = 0

for imgfile in FileNames:
	if imgfile!='.DS_Store' and imgfile!='orgin_croped':
		img = Image.open("images/%s"%(imgfile))
		region = (344,344,750,830)  #数字请自行调整
		print("图片宽{0}px,高{1}px".format(img.size[0],img.size[1]))
		#裁切图片
		cropImg = img.crop(region)
		cropImg.save('imagesCroped/%s'%(imgfile))
		print i
		i += 1
