import struct
import numpy as np
from numpy import *
import os
import glob
import sys
import shutil

def yuv_import(filename, dims, startfrm, resize_size):
    fp=open(filename,'rb')
    if (fp == None):
        print ("Error open yuv image")
        return
    blk_size=prod(dims)
    fp.seek(int(blk_size*startfrm), 0)
    xt = zeros((dims[0],dims[1],3),uint16)
    yt = zeros((dims[0],dims[1],3),uint16)
    for wn in range(dims[0]):
        for hn in range(dims[1]):
            yt[wn,hn,0]=struct.unpack('H',fp.read(2))[0]
    i=0
    j=0
    c=resize_size//2
    xt[0:c,0:c,0]=0
    xx=dims[0]-resize_size//2
    xxx=dims[1]-resize_size//2
    xt[xx:dims[0],xxx:dims[1],0]=0
    for wn in range(c,dims[0]-c):
        for hn in range(c,dims[1]-c):
            xt[wn,hn,0]=yt[wn,hn,0]
    fp.close()
    return xt

def WriteYUV(filename,yuv,dx,dy):
    fid = open(filename,'wb')
    y = np.reshape(np.array(yuv[:,:,0]),(dx*dy,1))
    fid.write(y)
    fid.close()

path2='./_DEPH/'
list_pom={}
list_pom2={}
list3={}
resize_size=300
dx=0
dy=0

PATH_TO_TEST_IMAGES_DIR_m = './_DEPH/'
searchstr_m = os.path.join(PATH_TO_TEST_IMAGES_DIR_m, '*.yuv')
list_of_images_m = glob.glob(searchstr_m)
if len(list_of_images_m)==0:
    if os.path.exists('./_DEPH'):
        PATH_TO_TEST_IMAGES_DIR_ders = './ders_gen/'
        searchstr_ders = os.path.join(PATH_TO_TEST_IMAGES_DIR_ders, '*.yuv')
        list_of_images_ders = glob.glob(searchstr_ders)
        list_pom=list_of_images_ders.copy()
        for l in range(len(list_of_images_ders)):
            list_pom[l]=list_pom[l].split('_')
        for i in range(len(list_pom)):
            for j in range(len(list_pom[i])):
                if list_pom[i][j] =='gen\\E':
                    list_pom2[i]=list_of_images_ders[i]
        for i in range(len(list_pom2)):
            if(os.path.exists(list_pom2[i])):
                shutil.copy(list_pom2[i], path2)
        k=0
        PATH_TO_TEST_IMAGES_DIR_dd = './_DEPH/'
        searchstr_dd = os.path.join(PATH_TO_TEST_IMAGES_DIR_dd, '*.yuv')
        list_of_images_dd = glob.glob(searchstr_dd)
        list3=list_of_images_dd.copy()
        for i in range(len(list3)):
            list3[i]=list3[i].split('_')
        if len(list3[0])!=0:
            size_p=list3[0][3].split('x')
            dx=int(size_p[0])
            dy=int(size_p[1])
        for i in range(len(list_pom2)):
            name='.'+'/_DEPH/'+'E_'+list3[i][3]+'_'+list3[i][4]+'_'+list3[i][5]+'_'+list3[i][6]+'_'+list3[i][7]+'_'+list3[i][8]+'_cf400'+'_cam'+str(int(list3[i][2]))+'.yuv'
            data=yuv_import(list_pom2[i], (dy,dx), 0, resize_size)
            os.remove(list_of_images_dd[i])
            WriteYUV(name,data,dy,dx)

else:
    size_pom=''
    size_pom=list_of_images_m[0].split('_')
    size_pom=size_pom[2].split('x')
    dx=int(size_pom[0])
    dy=int(size_pom[1])
    for i in range(len(list_of_images_m)):
        path=list_of_images_m[i]
        path=path.split('\\')
        path1=path[1].split('_')
        size=path1[2].split('x')
        pp=path1[len(path1)-1].split('.')
        data=yuv_import(list_of_images_m[i], (dy,dx), 0, resize_size)
        os.remove(list_of_images_m[i])
        WriteYUV(list_of_images_m[i],data,dy,dx)