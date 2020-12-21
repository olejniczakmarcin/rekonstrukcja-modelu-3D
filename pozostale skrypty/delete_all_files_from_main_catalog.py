import os
import shutil
import glob

PATH_TO_TEST_IMAGES_DIR_m = './'
searchstr_m = os.path.join(PATH_TO_TEST_IMAGES_DIR_m, '*.yuv')
list_of_images_m = glob.glob(searchstr_m)
for i in range(len(list_of_images_m)):
    name=list_of_images_m[i].replace('\\','/')
    if(os.path.exists(name)):
        os.remove(name)

if os.path.exists('./_DEPH/'):
    shutil.rmtree('./_DEPH/')
if os.path.exists('./fot_tel/'):
    shutil.rmtree('./fot_tel/')
if os.path.exists('./_SEQ/'):
    shutil.rmtree('./_SEQ/')
if os.path.exists('./_CLOUD/'):
    shutil.rmtree('./_CLOUD/')
if os.path.exists('./MeshroomCache/'):
    shutil.rmtree('./MeshroomCache/')
if os.path.exists('./fot/'):
    shutil.rmtree('./fot/')
if os.path.exists('./exry/'):
    shutil.rmtree('./exry/')
if os.path.exists('./ders_gen/'):
    shutil.rmtree('./ders_gen/')
if os.path.exists('./znearzfar.txt'):
    os.remove('./znearzfar.txt')
if os.path.exists('cam_param_dog.txt'):
    os.remove('cam_param_dog.txt')
if os.path.exists('cameras.sfm'):
    os.remove('cameras.sfm')
if os.path.exists('config.txt'):
    os.remove('config.txt')
if os.path.exists('config_new.txt'):
    os.remove('config_new.txt')
if os.path.exists('dlugosc_wektora.txt'):
    os.remove('dlugosc_wektora.txt')
if os.path.exists('exr_name.txt'):
    os.remove('exr_name.txt')
if os.path.exists('test.mg'):
    os.remove('test.mg')
if os.path.exists('./undistort/matches/'):
    shutil.rmtree('./undistort/matches/')
if os.path.exists('./undistort/reconstruction_global/'):
    shutil.rmtree('./undistort/reconstruction_global/')
    shutil.rmtree('./undistort/matches/')
if os.path.exists('./undistort/reconstruction_sequential/'):
    shutil.rmtree('./undistort/reconstruction_sequential/')
if os.path.exists('./undistort/sfm_data.json'):
    os.remove('./undistort/sfm_data.json')
if os.path.exists('wektor_translacji.txt'):
    os.remove('wektor_translacji.txt')
