import struct
import numpy as np
from numpy import *
from PIL import Image
import os
import glob
import sys

def yuv_import(filename, dims, startfrm, resize_size):
    fp=open(filename,'rb')
    if (fp == None):
        print ("Error open yuv image")
        return
    blk_size=prod(dims)
    fp.seek(int(blk_size*startfrm), 0)
    yt2 = zeros((dims[0]-resize_size,dims[1]-resize_size),uint8)
    ut2 = zeros(((dims[0]-resize_size)//2,(dims[1]-resize_size)//2),uint8)
    vt2 = zeros(((dims[0]-resize_size)//2,(dims[1]-resize_size)//2),uint8)
    
    yt = zeros((dims[0],dims[1]),uint8)
    ut = zeros((dims[0]//2,dims[1]//2),uint8)
    vt = zeros((dims[0]//2,dims[1]//2),uint8)

    for wn in range(dims[0]): #y
        for hn in range(dims[1]):
            byte=fp.read(1)
            yt[wn,hn]=struct.unpack('B',byte)[0]

    for wn in range(dims[0]//2): #U
        for hn in range(dims[1]//2):
            byte=fp.read(1)
            ut[wn,hn]=struct.unpack('B',byte)[0]

    for wn in range(dims[0]//2): #V
        for hn in range(dims[1]//2):
            byte=fp.read(1)
            vt[wn,hn]=struct.unpack('B',byte)[0]
    rr=resize_size//2
    yt2[:,:] = yt[int(rr):-int(rr),int(rr):-int(rr)]    
    yt3 = zeros((dims[0],dims[1]),uint8)
    o=0
    p=0
    for wn in range(rr,dims[0]-rr):
        p=0
        for hn in range(rr,dims[1]-rr):
            yt3[wn,hn]=yt2[o,p]
            p+=1
        o+=1
    fp.close()
    return [yt3,ut,vt]

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

PATH_TO_TEST_IMAGES_DIR_m = './_SEQ/'
searchstr_m = os.path.join(PATH_TO_TEST_IMAGES_DIR_m, '*.yuv')
list_of_images_m = glob.glob(searchstr_m)
resize_size=300
if os.path.exists('./config_new.txt'):
    os.remove('./config_new.txt')
ff=open('./config_new.txt','a+')
dx=0
dy=0
size_pom={}
if len(list_of_images_m[0])!=0:
    size_pom=list_of_images_m[0].split('\\')
    size_pom=size_pom[1].split('_')
    size_pom=size_pom[0].split('x')
    dy=int(size_pom[1])
    size_pom=size_pom[0].replace('zdj','')
    dx=int(size_pom)
for i in range(len(list_of_images_m)):
    path=list_of_images_m[i].split('\\')
    path1=path[1].split('_')
    path2=path1[1]
    [y,u,v]=yuv_import(list_of_images_m[i], (dy,dx), 0, resize_size)
    os.remove(list_of_images_m[i])
    WriteYUV(list_of_images_m[i],y,u,v,dy,dx)
ff.writelines(str(dx))
ff.writelines('\n')
ff.writelines(str(dy))
ff.close()