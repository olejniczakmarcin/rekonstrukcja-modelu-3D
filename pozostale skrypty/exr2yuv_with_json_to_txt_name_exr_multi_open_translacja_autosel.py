import imageio
import numpy as np
import scipy.misc
import easygui
from PIL import Image
import os
import json
import Imath
import OpenEXR
import numpy
import matplotlib.pyplot as plt
import glob

def WriteYUV(filename,yuv,dx,dy):
    fid = open(filename,'wb')
    y = np.reshape(np.transpose(yuv[:,:,0]),(dx*dy,1))
    y=y.astype(np.uint8)
    fid.write(y)
    u = np.array(Image.fromarray(yuv[:,:,1]).resize((dy//2,dx//2)))
    v = np.array(Image.fromarray(yuv[:,:,2]).resize((dy//2,dx//2)))
    sm=(dx*dy)//4
    u = np.reshape(np.transpose(u),(sm,1))
    v = np.reshape(np.transpose(v),(sm,1))
    u=u.astype(np.uint8)
    v=v.astype(np.uint8)
    fid.write(u)
    fid.write(v)
    fid.close()

switch=0 # 0 jak chcemy uklad macierzy [0 3 6][1 4 7][2 5 8] , 1 gdy chcemy uklad [0 1 2][3 4 5]..
mod=0 # 0 to pobiera z pliku conf nowy rozmiar 1 orginal zdjecia
newdx=0
newdy=0
if mod==0:
    conf=open('config.txt','r').readlines()
    newdx = conf[0].split('\n') # zmienic z obrazkiem nowy rozmiar
    newdx=int(newdx[0])
    newdy = int(conf[1])
else:
    with open('cameras.sfm', 'rb+') as f:
        data=json.load(f)
        intrici=data['intrinsics']
        he=intrici[0]
        newdx=int(he['width']) # orginalny rozmiar prosto z aparatu
        newdy=int(he['height']) 

lenghtt=0 
q=0
k=0
dzies=0
jedn=0
w=0

if os.path.exists("exr_name.txt"):
    os.remove("exr_name.txt")
if os.path.exists("wektor_translacji.txt"):
    os.remove("wektor_translacji.txt")
if os.path.exists("cam_param_dog.txt"):
    os.remove("cam_param_dog.txt")
FLOAT = Imath.PixelType(Imath.PixelType.FLOAT)
with open('cameras.sfm', 'rb+') as f:
    data=json.load(f)
wesrion = data["views"]
for i in data["views"]:
    lenghtt=lenghtt+1
with open('cameras.sfm', 'rb+') as f:
    data=json.load(f)
intrici=data['intrinsics']
he=intrici[0]
ogr_dx=he['width'] # orginalny rozmiar prosto z aparatu
org_dy=he['height']
ogr_dx=float(ogr_dx)
org_dy=float(org_dy)
x=ogr_dx/newdx
y=org_dy/newdy 
poses=data['poses']
intri=data['intrinsics']
pxFocal=intri[0]
pxFocal=pxFocal["pxFocalLength"]
principal_x=intri[0]
principal_x=principal_x["principalPoint"]
principal_x=principal_x[0] 
principal_y=intri[0]
principal_y=principal_y["principalPoint"]
principal_y=principal_y[1]
a=float(pxFocal)
a=a/x #x
b=float(pxFocal)
b=b/y #y
c=float(principal_x)
c=c/x #x
d=float(principal_y)
d=d/y #y
# wczytanie wszytkich zdjec z katalogu
PATH_TO_TEST_IMAGES_DIR_m = './fot'
searchstr_m = os.path.join(PATH_TO_TEST_IMAGES_DIR_m, '*.jpg')
list_of_images_m = glob.glob(searchstr_m)
filename2=list_of_images_m
if(filename2==None):
    os._exit(1)
#wybor trybu dzialania
if switch==0:
    for i in range(lenghtt):
        fileName = filename2[i]
        sciez, nazwa = os.path.split(fileName)
        index_of_dot = nazwa.index('.')
        nazwa = nazwa[:index_of_dot]
        f = open(".//cam_param_dog.txt","a")
        f1= open(".//wektor_translacji.txt","a")
        for i in range(lenghtt):
            w1=wesrion[i] 
            # w1 bedzie iterowac
            path=w1[ "path"]
            sciezka, nazwa_zdj = os.path.split(path)
            index_of_dot = nazwa_zdj.index('.')
            nazwa_zdj = nazwa_zdj[:index_of_dot]
            viewId=w1["viewId"]
            if nazwa==nazwa_zdj:
                for j in range(lenghtt):
                    posesId=poses[j]
                    id=posesId["poseId"]
                    if viewId==id:
                        transform=poses[j]
                        transform=transform["pose"]
                        transform=transform["transform"]
                        rotation=transform["rotation"]
                        center=transform["center"]
                        f.write("param_v"+str(dzies)+str(jedn))
                        f.write("\n")
                        f.write(str(a))
                        f.write(" ")
                        f.write(str(0))
                        f.write(" ")
                        f.write(str(c))
                        #f.write(" ")
                        f.write("\n")
                        f.write(str(0))
                        f.write(" ")
                        f.write(str(b))
                        f.write(" ")
                        f.write(str(d))
                        #f.write(" ")
                        f.write("\n")
                        f.write('0.0000000000000000')
                        f.write(" ")
                        f.write('0.0000000000000000')
                        f.write(" ")
                        f.write('1.0000000000000000')
                        #f.write(" ")
                        f.write("\n")
                        f.write(str(0))
                        f.write("\n")
                        f.write(str(0))
                        f.write("\n")
                        f.write(str(rotation[0]))
                        f.write(" ")
                        f.write(str(rotation[3]))
                        f.write(" ")
                        f.write(str(rotation[6]))
                        f.write(" ")
                        f.write(str(center[0]))
                        f.write("\n")
                        f.write(str(rotation[1]))
                        f.write(" ")
                        f.write(str(rotation[4]))
                        f.write(" ")
                        f.write(str(rotation[7]))
                        f.write(" ")
                        f.write(str(center[1]))
                        f.write("\n")
                        f.write(str(rotation[2]))
                        f.write(" ")
                        f.write(str(rotation[5]))
                        f.write(" ")
                        f.write(str(rotation[8]))
                        f.write(" ")
                        f.write(str(center[2]))
                        f.write("\n")
                        f.write('0.0000000000000000')
                        f.write(" ")
                        f.write('0.0000000000000000')
                        f.write(" ")
                        f.write('0.0000000000000000')
                        f.write(" ")
                        f.write('1.0000000000000000')
                        f.write("\n")
                        f.write("\n")
                        f1.write("param_v"+str(dzies)+str(jedn))
                        f1.write("\n")
                        f1.write(str(center[0]))
                        f1.write("\n")
                        f1.write(str(center[1]))
                        f1.write("\n")
                        f1.write(str(center[2]))
                        f1.write("\n")
                        f.close()
                        f1.close()
                        jedn=jedn+1
                        if jedn==10:
                            jedn=0
                            dzies=dzies+1 
                        path11='./exry/'+id+'.exr'
                        filee=open("exr_name.txt","a")
                        fp1=id+"_depthMap.exr"
                        fp2=id+"_simMap.exr"
                        filee.write(fp1)
                        filee.write("\n")
                        filee.write(fp2)
                        if(i<lenghtt):
                            filee.write("\n")
                        img = OpenEXR.InputFile(path11)
                        print(img.header())

                        dw = img.header()['dataWindow']
                        size = (dw.max.y - dw.min.y + 1,dw.max.x - dw.min.x + 1)
                        arrayR = numpy.fromstring(img.channel('R',FLOAT), dtype='f')#*255
                        arrayG = numpy.fromstring(img.channel('G',FLOAT), dtype='f')#*255
                        arrayB = numpy.fromstring(img.channel('B',FLOAT), dtype='f')#*255
                        print(arrayR.shape)
                        print(size)

                        arrayRR = numpy.reshape(arrayR,size)
                        arrayGG = numpy.reshape(arrayG,size)
                        arrayBB = numpy.reshape(arrayB,size)

                        arrayRRGGBB = numpy.zeros((size[0],size[1],3))
                        arrayRRGGBB[:,:,0] = arrayRR
                        arrayRRGGBB[:,:,1] = arrayGG
                        arrayRRGGBB[:,:,2] = arrayBB

                        data = numpy.zeros( (size[0],size[1],3), dtype=numpy.uint8)
                        data[:,:,:] = arrayRRGGBB[:,:,:]*255

                        img = Image.fromarray(data, 'RGB')
                        #path = easygui.fileopenbox()
                        #img = cv2.imread('img_test.png')
                        #img = imageio.imread('img_test.png')
                        yuv = img
                        YUVImg=img.convert('YCbCr')
                        yuv = np.array(YUVImg)
                        y = yuv[:,:,0]
                        u = yuv[:,:,1]
                        v = yuv[:,:,2]

                        y = np.array(Image.fromarray(np.transpose(yuv[:,:,0])).resize((newdy,newdx)))
                        u = np.array(Image.fromarray(np.transpose(yuv[:,:,1])).resize((newdy,newdx)))
                        v = np.array(Image.fromarray(np.transpose(yuv[:,:,2])).resize((newdy,newdx)))
                        dy,dx = y.shape
                        yuvnew = np.zeros((dy,dx,3))
                        yuvnew[:,:,0] = y
                        yuvnew[:,:,1] = u
                        yuvnew[:,:,2] = v
                        if(q==10):
                            q=0
                            k=k+1
                        pom='zdj'+str(k)+str(q)+'_'+str(newdx)+'x'+str(newdy)+'.yuv'
                        WriteYUV(pom,yuvnew,newdx,newdy)
                        q=q+1
if switch==1:
    for i in range(lenghtt):
        fileName = easygui.fileopenbox(msg='zdj typu jpg',title='wczytaj zdjecia w posortowane rosnąco',filetypes = ["*.jpg"])
        if(fileName==None):
            break
        sciez, nazwa = os.path.split(fileName)
        index_of_dot = nazwa.index('.')
        nazwa = nazwa[:index_of_dot]
        f = open(".//cam_param_dog.txt","a")
        for i in range(lenghtt):
            w1=wesrion[i] 
            # w1 bedzie iterowac
            path=w1[ "path"]
            sciezka, nazwa_zdj = os.path.split(path)
            index_of_dot = nazwa_zdj.index('.')
            nazwa_zdj = nazwa_zdj[:index_of_dot]
            viewId=w1["viewId"]
            if nazwa==nazwa_zdj:
                for j in range(lenghtt):
                    posesId=poses[j]
                    id=posesId["poseId"]
                    if viewId==id:
                        transform=poses[j]
                        transform=transform["pose"]
                        transform=transform["transform"]
                        rotation=transform["rotation"]
                        center=transform["center"]
                        f.write("param_v"+str(dzies)+str(jedn))
                        f.write("\n")
                        f.write(str(a))
                        f.write(" ")
                        f.write(str(0))
                        f.write(" ")
                        f.write(str(c))
                        #f.write(" ")
                        f.write("\n")
                        f.write(str(0))
                        f.write(" ")
                        f.write(str(b))
                        f.write(" ")
                        f.write(str(d))
                        #f.write(" ")
                        f.write("\n")
                        f.write('0.0000000000000000')
                        f.write(" ")
                        f.write('0.0000000000000000')
                        f.write(" ")
                        f.write('1.0000000000000000')
                        #f.write(" ")
                        f.write("\n")
                        f.write(str(0))
                        f.write("\n")
                        f.write(str(0))
                        f.write("\n")
                        f.write(str(rotation[0]))
                        f.write(" ")
                        f.write(str(rotation[1]))
                        f.write(" ")
                        f.write(str(rotation[2]))
                        f.write(" ")
                        f.write(str(center[0]))
                        f.write("\n")
                        f.write(str(rotation[3]))
                        f.write(" ")
                        f.write(str(rotation[4]))
                        f.write(" ")
                        f.write(str(rotation[5]))
                        f.write(" ")
                        f.write(str(center[1]))
                        f.write("\n")
                        f.write(str(rotation[6]))
                        f.write(" ")
                        f.write(str(rotation[7]))
                        f.write(" ")
                        f.write(str(rotation[8]))
                        f.write(" ")
                        f.write(str(center[2]))
                        f.write("\n")
                        f.write('0.0000000000000000')
                        f.write(" ")
                        f.write('0.0000000000000000')
                        f.write(" ")
                        f.write('0.0000000000000000')
                        f.write(" ")
                        f.write('1.0000000000000000')
                        f.write("\n")
                        f.write("\n")
                        f1.write("param_v"+str(dzies)+str(jedn))
                        f1.write("\n")
                        f1.write(str(center[0]))
                        f1.write("\n")
                        f1.write(str(center[1]))
                        f1.write("\n")
                        f1.write(str(center[2]))
                        f1.write("\n")
                        f.close()
                        f1.close()
                        jedn=jedn+1
                        if jedn==10:
                            jedn=0
                            dzies=dzies+1
                        path11='./exry/'+id+'.exr'
                        filee=open("exr_name.txt","a")
                        fp1=id+"_depthMap.exr"
                        fp2=id+"_simMap.exr"
                        filee.write(fp1)
                        filee.write("\n")
                        filee.write(fp2)
                        if(i<lenghtt):
                            filee.write("\n")
                        img = OpenEXR.InputFile(path11)
                        print(img.header())

                        dw = img.header()['dataWindow']
                        size = (dw.max.y - dw.min.y + 1,dw.max.x - dw.min.x + 1)
                        arrayR = numpy.fromstring(img.channel('R',FLOAT), dtype='f')#*255
                        arrayG = numpy.fromstring(img.channel('G',FLOAT), dtype='f')#*255
                        arrayB = numpy.fromstring(img.channel('B',FLOAT), dtype='f')#*255
                        print(arrayR.shape)
                        print(size)

                        arrayRR = numpy.reshape(arrayR,size)
                        arrayGG = numpy.reshape(arrayG,size)
                        arrayBB = numpy.reshape(arrayB,size)

                        arrayRRGGBB = numpy.zeros((size[0],size[1],3))
                        arrayRRGGBB[:,:,0] = arrayRR
                        arrayRRGGBB[:,:,1] = arrayGG
                        arrayRRGGBB[:,:,2] = arrayBB

                        data = numpy.zeros( (size[0],size[1],3), dtype=numpy.uint8)
                        data[:,:,:] = arrayRRGGBB[:,:,:]*255

                        img = Image.fromarray(data, 'RGB')
                        #path = easygui.fileopenbox()
                        #img = cv2.imread('img_test.png')
                        #img = imageio.imread('img_test.png')
                        yuv = img
                        YUVImg=img.convert('YCbCr')
                        yuv = np.array(YUVImg)
                        y = yuv[:,:,0]
                        u = yuv[:,:,1]
                        v = yuv[:,:,2]

                        y = np.array(Image.fromarray(np.transpose(yuv[:,:,0])).resize((newdy,newdx)))
                        u = np.array(Image.fromarray(np.transpose(yuv[:,:,1])).resize((newdy,newdx)))
                        v = np.array(Image.fromarray(np.transpose(yuv[:,:,2])).resize((newdy,newdx)))
                        dy,dx = y.shape
                        yuvnew = np.zeros((dy,dx,3))
                        yuvnew[:,:,0] = y
                        yuvnew[:,:,1] = u
                        yuvnew[:,:,2] = v
                        if(q==10):
                            q=0
                            k=k+1
                        pom='zdj'+str(k)+str(q)+'_'+str(newdx)+'x'+str(newdy)+'.yuv'
                        WriteYUV(pom,yuvnew,newdx,newdy)
                        q=q+1    

'''
for i in range(lenghtt):
    fileName = easygui.fileopenbox(msg='zdj typu jpg',title='wczytaj zdjecia w posortowane rosnąco',filetypes = ["*.jpg"])
    if(fileName==None):
        break
    sciez, nazwa = os.path.split(fileName)
    index_of_dot = nazwa.index('.')
    nazwa = nazwa[:index_of_dot]
    f = open(".//cam_param_dog.txt","a")
    for i in range(lenghtt):
        w1=wesrion[i] 
        # w1 bedzie iterowac
        path=w1[ "path"]
        sciezka, nazwa_zdj = os.path.split(path)
        index_of_dot = nazwa_zdj.index('.')
        nazwa_zdj = nazwa_zdj[:index_of_dot]
        viewId=w1["viewId"]
        if nazwa==nazwa_zdj:
            for j in range(lenghtt):
                posesId=poses[j]
                id=posesId["poseId"]
                if viewId==id:
                    transform=poses[j]
                    transform=transform["pose"]
                    transform=transform["transform"]
                    rotation=transform["rotation"]
                    center=transform["center"]
                    f.write("param_v"+str(dzies)+str(jedn))
                    f.write("\n")
                    f.write(str(a))
                    f.write(" ")
                    f.write(str(0))
                    f.write(" ")
                    f.write(str(c))
                    f.write(" ")
                    f.write("\n")
                    f.write(str(0))
                    f.write(" ")
                    f.write(str(b))
                    f.write(" ")
                    f.write(str(d))
                    f.write(" ")
                    f.write("\n")
                    f.write('0.0000000000000000')
                    f.write(" ")
                    f.write('0.0000000000000000')
                    f.write(" ")
                    f.write('1.0000000000000000')
                    f.write(" ")
                    f.write("\n")
                    f.write(str(0))
                    f.write("\n")
                    f.write(str(0))
                    f.write("\n")
                    f.write(str(rotation[0]))
                    f.write(" ")
                    f.write(str(rotation[1]))
                    f.write(" ")
                    f.write(str(rotation[2]))
                    f.write(" ")
                    f.write(str(center[0]))
                    f.write("\n")
                    f.write(str(rotation[3]))
                    f.write(" ")
                    f.write(str(rotation[4]))
                    f.write(" ")
                    f.write(str(rotation[5]))
                    f.write(" ")
                    f.write(str(center[1]))
                    f.write("\n")
                    f.write(str(rotation[6]))
                    f.write(" ")
                    f.write(str(rotation[7]))
                    f.write(" ")
                    f.write(str(rotation[8]))
                    f.write(" ")
                    f.write(str(center[2]))
                    f.write("\n")
                    f.write("\n")       
                    f.close()  
                    jedn=jedn+1
                    if jedn==10:
                        jedn=0
                        dzies=dzies+1
                    path11='./zdj/'+id+'.exr'
                    img = OpenEXR.InputFile(path11)
                    print(img.header())

                    dw = img.header()['dataWindow']
                    size = (dw.max.y - dw.min.y + 1,dw.max.x - dw.min.x + 1)
                    arrayR = numpy.fromstring(img.channel('R',FLOAT), dtype='f')#*255
                    arrayG = numpy.fromstring(img.channel('G',FLOAT), dtype='f')#*255
                    arrayB = numpy.fromstring(img.channel('B',FLOAT), dtype='f')#*255
                    print(arrayR.shape)
                    print(size)

                    arrayRR = numpy.reshape(arrayR,size)
                    arrayGG = numpy.reshape(arrayG,size)
                    arrayBB = numpy.reshape(arrayB,size)

                    arrayRRGGBB = numpy.zeros((size[0],size[1],3))
                    arrayRRGGBB[:,:,0] = arrayRR
                    arrayRRGGBB[:,:,1] = arrayGG
                    arrayRRGGBB[:,:,2] = arrayBB

                    data = numpy.zeros( (size[0],size[1],3), dtype=numpy.uint8)
                    data[:,:,:] = arrayRRGGBB[:,:,:]*255

                    img = Image.fromarray(data, 'RGB')
                    #path = easygui.fileopenbox()
                    #img = cv2.imread('img_test.png')
                    #img = imageio.imread('img_test.png')
                    yuv = img
                    newdx = 712
                    newdy = 400
                    YUVImg=img.convert('YCbCr')
                    yuv = np.array(YUVImg)
                    y = yuv[:,:,0]
                    u = yuv[:,:,1]
                    v = yuv[:,:,2]

                    y = np.array(Image.fromarray(np.transpose(yuv[:,:,0])).resize((newdy,newdx)))
                    u = np.array(Image.fromarray(np.transpose(yuv[:,:,1])).resize((newdy,newdx)))
                    v = np.array(Image.fromarray(np.transpose(yuv[:,:,2])).resize((newdy,newdx)))
                    dy,dx = y.shape
                    yuvnew = np.zeros((dy,dx,3))
                    yuvnew[:,:,0] = y
                    yuvnew[:,:,1] = u
                    yuvnew[:,:,2] = v
                    if(q==10):
                        q=0
                        k=k+1
                    pom='zdj'+str(k)+str(q)+'_'+str(newdx)+'x'+str(newdy)+'.yuv'
                    WriteYUV(pom,yuvnew,newdx,newdy)
                    q=q+1
'''