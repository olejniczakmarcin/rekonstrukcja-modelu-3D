from PIL import Image
import os
import glob
import sys
import shutil

def main(argv):
    PATH_TO_TEST_IMAGES_DIR_m = './fot_org/'
    searchstr_m = os.path.join(PATH_TO_TEST_IMAGES_DIR_m, '*.jpg')
    list_of_images_m = glob.glob(searchstr_m)
    path2='./fot_tel/'
    if os.path.exists(path2):
        shutil.rmtree(path2)
    os.mkdir(path2)
    resize_size=int(sys.argv[1])

    for i in range(len(list_of_images_m)):
        name=list_of_images_m[i].replace('\\','/')
        img=Image.open(name)
        width, height = img.size
        new_width=width-resize_size
        new_height=height-resize_size
        left = int((width - new_width)/2)
        top = int((height - new_height)/2)
        right = int((width + new_width)/2)
        new_img=img.crop((left, top, right, height))
        name=name.split('/')
        path='fot_tel/'+ name[2]
        new_img.save(path)

if __name__ == "__main__":
   main(sys.argv[1])
   print('cropp image operation')