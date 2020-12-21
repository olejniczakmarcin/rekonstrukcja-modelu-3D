from PIL import Image
import glob
import os
import shutil
import sys

def main(argv):
    right=0
    new_height=0
    new_dx=int(sys.argv[1])
    new_dy=int(sys.argv[2])

    PATH_TO_TEST_IMAGES_DIR_m = './fot_tel'
    searchstr_m = os.path.join(PATH_TO_TEST_IMAGES_DIR_m, '*.jpg')
    list_of_images_m = glob.glob(searchstr_m)
    path2='./fot/'
    if os.path.exists(path2):
        shutil.rmtree(path2)
    os.mkdir(path2)
    for i in range(len(list_of_images_m)):
        name=list_of_images_m[i].replace('\\','/')
        img=Image.open(name) # paste image in python folder
        new_img=img.resize((new_dx,new_dy), Image.ANTIALIAS)
        new_width=new_dx-100
        new_height=new_dy-100
        left = (new_dx - new_width)/2
        top = (new_dy - new_height)/2
        right = (new_dx + new_width)/2
        new_img=new_img.crop((left, top, right, new_dy))
        name=name.split('/')
        path='fot/'+name[len(name)-1]
        new_img.save(path)
    if os.path.exists('config.txt'):
        os.remove('config.txt')
    f=open('config.txt','w')
    f.writelines(str(int(right)))
    f.writelines('\n')
    f.writelines(str(int(new_height)))
    f.close()

if __name__ == "__main__":
   main(sys.argv[1])