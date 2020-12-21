import os
import shutil
import glob

path1='D:/ders_mapy/'
folder_name=input("wprowadz nazwe nowego folderu")
path1=path1+folder_name
path2="./_DEPH/"
path3="./_SEQ/"
if os.path.exists(path1):
    shutil.rmtree(path1)
os.mkdir(path1)
PATH_TO_TEST_IMAGES_DIR_m = path2
searchstr_m = os.path.join(PATH_TO_TEST_IMAGES_DIR_m, '*.yuv')
list_of_images_m = glob.glob(searchstr_m)
for i in range(len(list_of_images_m)):
    shutil.copy(list_of_images_m[i], path1)
PATH_TO_TEST_IMAGES_DIR_m = path3
searchstr_m = os.path.join(PATH_TO_TEST_IMAGES_DIR_m, '*.yuv')
list_of_images_m = glob.glob(searchstr_m)
for i in range(len(list_of_images_m)):
    shutil.copy(list_of_images_m[i], path1)