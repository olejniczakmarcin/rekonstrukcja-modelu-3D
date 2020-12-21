import glob
import os
import shutil
import re

def sort_b(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

f=open('./_CLOUD/synthesizer_PoznanStreet.cfg','r').readlines()
if os.path.exists('./_CLOUD/synthesizer_PoznanStreet.cfg'):
    os.remove('./_CLOUD/synthesizer_PoznanStreet.cfg')
list_mod={}
o=0

pom_path=os.path.abspath("./_CLOUD/synthesizer_PoznanStreet.cfg")
pom_path=pom_path.split('\\')
pathh=pom_path[0]+'/'+pom_path[1]+'/'+pom_path[2]+'/'+pom_path[3]+'/'+pom_path[4]+'/'+pom_path[5]
PATH_TO_TEST_IMAGES_DIR_m = pathh+'/_SEQ/'
searchstr_m = os.path.join(PATH_TO_TEST_IMAGES_DIR_m, '*.yuv')
list_of_images_m = glob.glob(searchstr_m)
PATH_TO_TEST_IMAGES_DIR = pathh+'/_DEPH/'
searchstr = os.path.join(PATH_TO_TEST_IMAGES_DIR, '*.yuv')
list_of_images = glob.glob(searchstr)
number_cam={}
num2={}
num3={}
for ll in range(len(list_of_images)):
    list_of_images[ll]=list_of_images[ll].split('_')
    number_cam[ll]=list_of_images[ll][9].split('.')
    num2[ll]=number_cam[ll][0].replace('cam','')
lista_cam=''
for i in range(len(num2)):
    num2[i]=int(num2[i])
num2=sort_b(num2)
for i in range(len(num2)):
    kk=i
    lista_cam=lista_cam+str(num2[i])
    if i<len(num2)-1:
        lista_cam=lista_cam+', '
    if i==len(num2)-1:
        lista_cam=lista_cam+'\n'
con=open('config.txt','r').readlines()
con2=open('config_new.txt','r').readlines()
t2=con2[0].replace('\n','')
t3=con2[1]
t0=con[0].replace('\n','')
t1=con[1]
t0=str(int(t0)-(int(t0)-int(t2)))
t1=str(int(t1)-(int(t1)-int(t3)))
for i in f:
    list_mod[o]=i
    o+=1
list_mod[0]="FileNameInT           : "+'"'+pathh+"/_SEQ/zdj"+t0+"x"+t1+"_cam[CamId].yuv"+'"'+"\n"
list_mod[1]="FileNameInD           : "+'"'+pathh+"/_DEPH/E_"+t0+"x"+t1+"_0_3_1_62d_16bps_cf400_cam[CamId].yuv"+'"'+"\n"
list_mod[7]="WidthIn               : "+t0+'\n'
list_mod[8]="HeightIn              : "+t1+'\n'
list_mod[9]="WidthOut              : "+t0+'\n'
list_mod[10]="HeightOut             : "+t1+'\n'
list_mod[20]="RealCamParamsFile     : "+'"'+pathh+"/_CLOUD/Poznan_Street_CamParams_real.cfg"+'"'+"\n"
list_mod[21]="VirtCamParamsFile     : "+'"'+pathh+"/_CLOUD/Poznan_Street_CamParams_virt.cfg"+'"'+"\n"
list_mod[23]="RealCamIds            : "+lista_cam
ff=open('./_CLOUD/synthesizer_PoznanStreet.cfg','a+')
for i in range(len(list_mod)):
    ff.writelines(list_mod[i])
ff.close()