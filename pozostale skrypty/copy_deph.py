import glob
import os
import shutil

if os.path.exists('./_DEPH/'):
    shutil.rmtree('./_DEPH/')
os.mkdir('./_DEPH/')
if os.path.exists('./_CLOUD/'):
    shutil.rmtree('./_CLOUD/')
os.mkdir('./_CLOUD/')
if os.path.exists('./_SEQ/'):
    shutil.rmtree('./_SEQ/')
os.mkdir('./_SEQ/')
path='./_SEQ/'
path2='./_DEPH/'
con=open('config.txt','r').readlines()
t0=con[0].replace('\n','')
t1=con[1]
PATH_TO_TEST_IMAGES_DIR_m = './'
searchstr_m = os.path.join(PATH_TO_TEST_IMAGES_DIR_m, '*.yuv')
list_of_images_m = glob.glob(searchstr_m)
for i in range(len(list_of_images_m)):
    if(os.path.exists(list_of_images_m[i])):
        shutil.copy(list_of_images_m[i], path)
pom=list_of_images_m.copy()
for i in range(len(pom)):
    pom[i]=pom[i].split('_')
    pom[i][1]=pom[i][1].split('.')
for i in range(len(list_of_images_m)):
    list_of_images_m[i]=list_of_images_m[i].replace('\\','/')
    list_of_images_m[i]=list_of_images_m[i].split('.')
for i in range(len(list_of_images_m)):
    name='.'+'/_SEQ/'+'zdj'+pom[i][1][0]+'_cam'+str(i)+'.'+list_of_images_m[i][2]
    name1='.'+'/_SEQ'+list_of_images_m[i][1]+'.'+list_of_images_m[i][2]
    if(os.path.exists(name1)):
        os.rename(name1, name)
list_deph={}
list_deph1={}
list_deph2={}
ww=0
kk=0
for l in range(len(list_of_images_m)):
    if ww==10:
        ww=0
        kk+=1
    list_deph[l]="./ders_gen/E_"+str(kk)+str(ww)+"_"+str(t0)+"x"+str(t1)+"_0_3_1_62d_16bps_cf400.yuv"
    list_deph1[l]="./E_"+str(kk)+str(ww)+"_"+str(t0)+"x"+str(t1)+"_0_3_1_62d_16bps_cf400.yuv"
    list_deph2[l]="./E"+"_"+str(t0)+"x"+str(t1)+"_0_3_1_62d_16bps_cf400.yuv"
    ww+=1
for i in range(len(list_deph)):
    if(os.path.exists(list_deph[i])):
        shutil.copy(list_deph[i], path2)
for i in range(len(list_deph)):
    list_deph1[i]=list_deph1[i].replace('\\','/')
    list_deph1[i]=list_deph1[i].split('.')
    list_deph2[i]=list_deph2[i].replace('\\','/')
    list_deph2[i]=list_deph2[i].split('.')
for i in range(len(list_of_images_m)):
    name='.'+'/_DEPH'+list_deph2[i][1]+'_cam'+str(i)+'.'+list_deph2[i][2]
    name1='.'+'/_DEPH'+list_deph1[i][1]+'.'+list_deph1[i][2]
    if(os.path.exists(name1)):
        os.rename(name1, name)
if(os.path.exists('./_CLOUD/')):
    shutil.copy('D:\\opencv\\PCV-apk20200519-vs2017\\bin\\!Street.bat', './_CLOUD/')
    shutil.copy('D:\\opencv\\PCV-apk20200519-vs2017\\bin\\point_cloud_viewer_x64_Release.exe', './_CLOUD/')
    shutil.copy('D:\\opencv\\PCV-apk20200519-vs2017\\bin\\synthesizer_PoznanStreet.cfg', './_CLOUD/')
    shutil.copy('D:\\poznan_strert\\Poznan_Street_CamParams_virt.cfg', './_CLOUD/')