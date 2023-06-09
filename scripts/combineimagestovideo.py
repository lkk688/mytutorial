import cv2
import numpy as np
import glob
 
img_array = []
filenamelist = glob.glob('/Volumes/Samsung_T5/Datasets/Nuscenes/jpgs/eval*.jpg')
for filename in filenamelist:
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)

# basefilename = '/Volumes/Samsung_T5/Datasets/Nuscenes/nuscenes_testfigs/radarfront_'
# for i in range(154):
#     filename = basefilename + str(i) + ".png"
#     img = cv2.imread(filename)
#     height, width, layers = img.shape
#     size = (width,height)
#     img_array.append(img)
 
fourcc = cv2.VideoWriter_fourcc(*'mp4v') #(*'XVID') #cv2.VideoWriter_fourcc(*'DIVX') ->.dvi
out = cv2.VideoWriter('bev.mp4',fourcc, 5, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()