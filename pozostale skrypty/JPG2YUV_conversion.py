import numpy as np
import imageio
import easygui
from numpy import *
from PIL import Image
import os
import glob

def WriteYUV(filename,yi,ui,vi,dx,dy):
    fid = open(filename,'wb')
    y = np.reshape(np.array(yi),(dx*dy,1))
    y=y.astype(np.uint8)
    fid.write(y)
    u = np.array(Image.fromarray(ui).resize((dy//2,dx//2)))
    v = np.array(Image.fromarray(vi).resize((dy//2,dx//2)))
    sm=(dx*dy)//4
    u = np.reshape(np.array(u),(sm,1))
    v = np.reshape(np.array(v),(sm,1))
    u=u.astype(np.uint8)
    v=v.astype(np.uint8)
    fid.write(u)
    fid.write(v)
    fid.close()

PATH_TO_TEST_IMAGES_DIR = './'
searchstr = os.path.join(PATH_TO_TEST_IMAGES_DIR, '*.yuv')
list_of_yuv = glob.glob(searchstr)
if(len(list_of_yuv)>0):
    for i in range(len(list_of_yuv)):
        name_y=list_of_yuv[i].replace('\\','/')
        if(os.path.exists(name_y)):
            os.remove(name_y)

PATH_TO_TEST_IMAGES_DIR_m = './fot/'
searchstr_m = os.path.join(PATH_TO_TEST_IMAGES_DIR_m, '*.jpg')
list_of_images_m = glob.glob(searchstr_m)
jedn=0
dzies=0
for l in range(len(list_of_images_m)):
    img  = imageio.imread(list_of_images_m[l])
    dx,dy,z=img.shape
    y=zeros((dx,dy))
    u=zeros((dx,dy))
    v=zeros((dx,dy))
    for i in range(dx):
        for j in range(dy):
            y[i,j]=0.257*img[i,j,0] + 0.504*img[i,j,1] + 0.098*img[i,j,2] + 16
            u[i,j]=-0.148*img[i,j,0] - 0.291*img[i,j,1] + 0.439*img[i,j,2]+128
            v[i,j]=0.439*img[i,j,0]- 0.368*img[i,j,1] - 0.071*img[i,j,2]+128
    fnam="./zdj"+str(dzies)+str(jedn)+'_'+str(dy)+'x'+str(dx)+'.yuv'
    print(fnam)
    print('\n')
    WriteYUV(fnam,y,u,v,dy,dx)
    jedn+=1
    if jedn==10:
        dzies+=1
        jedn=0