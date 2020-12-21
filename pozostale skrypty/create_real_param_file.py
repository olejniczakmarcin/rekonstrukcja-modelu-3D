import os
import glob 
import re

if(os.path.exists('./_CLOUD/Poznan_Street_CamParams_real.cfg')):
    os.remove('./_CLOUD/Poznan_Street_CamParams_real.cfg')
f=open('./_CLOUD/Poznan_Street_CamParams_real.cfg','a+')
kernit=open('./cam_param_dog.txt','r').readlines()
for i in range(len(kernit)):
    kernit[i]=kernit[i].split(' ')
for i in range(len(kernit)):
    kernit[i][len(kernit[i])-1]=kernit[i][len(kernit[i])-1].split('\n')
con=open('config.txt','r').readlines()
con2=open('config_new.txt','r').readlines()
t2=con2[0].replace('\n','')
t3=con2[1]
t0=con[0].replace('\n','')
t1=con[1]
diffx=(int(t0)-int(t2))/2
diffy=(int(t1)-int(t3))/2
t0=str(int(t0)-(int(t0)-int(t2)))
t1=str(int(t1)-(int(t1)-int(t3)))
far=open('znearzfar.txt','r').readlines()
znear=far[0].split('\n')
znear=znear[0]
zfar=far[1]
PATH_TO_TEST_IMAGES_DIR_m = './'
searchstr_m = os.path.join(PATH_TO_TEST_IMAGES_DIR_m, '*.yuv')
list_of_images_m = glob.glob(searchstr_m)

f.writelines('#!!! DESCRIPTION !!!\n')
f.writelines('#[CameraXXX]     camera name - single camera section\n')
f.writelines('#  Location    = camera location in system (as X,Y or X,Y,Z)\n')
f.writelines('#  Resolution  = camera original resolution (valid for intrin params)\n')
f.writelines('#  Projection  = camera projection type (Perspective or Equirectangular)\n')
f.writelines('#  Intrinsic   = intrinsic matrix\n')
f.writelines('#  Extrinsic   = extrinsic matrix\n')
f.writelines('#  Znear       = Z near\n')
f.writelines('#  Zfar        = Z far\n')
f.writelines('#  AngleOfView = angle of view in equirectangular representation (L, R, T, B)\n')
f.writelines('\n')
f.writelines('\n')
f.writelines('\n')
for i in range(len(list_of_images_m)):
    f.writelines('[real'+str(i)+']'+'\n')
    f.writelines('  Location    = 0, 0 # in X, Y\n')
    f.writelines('  Resolution  = '+str(t0)+'x'+str(t1)+'\n')
    f.writelines('  Projection  = Perspective\n')
    f.writelines('  Intrinsic   = '+kernit[i*11+1][0]+', '+kernit[i*11+1][1]+', '+str(float(kernit[i*11+1][2][0])-diffx)+','+'\n')
    f.writelines("                   "+kernit[i*11+2][0]+', '+kernit[i*11+2][1]+', '+str(float(kernit[i*11+2][2][0])-diffy)+','+'\n')
    f.writelines("                   "+kernit[i*11+3][0]+', '+kernit[i*11+3][1]+', '+kernit[i*11+3][2][0]+'\n')
    f.writelines("  Extrinsic   = "+kernit[i*11+6][0]+', '+kernit[i*11+6][1]+', '+kernit[i*11+6][2]+', '+kernit[i*11+6][3][0]+','+'\n')
    f.writelines("                "+kernit[i*11+7][0]+', '+kernit[i*11+7][1]+', '+kernit[i*11+7][2]+', '+kernit[i*11+7][3][0]+','+'\n')
    f.writelines("                "+kernit[i*11+8][0]+', '+kernit[i*11+8][1]+', '+kernit[i*11+8][2]+', '+kernit[i*11+8][3][0]+'\n')
    f.writelines('  Znear       = '+znear+'\n')
    f.writelines('  Zfar        = '+zfar+'\n')
    f.writelines('\n')
f.writelines('\n')
f.close()