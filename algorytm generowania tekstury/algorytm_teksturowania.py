import os
import numpy as np
import easygui
import imageio
import glob
import collections
from collections import Counter
from plyfile import PlyData, PlyElement
from copy import copy, deepcopy
def int_list_faces(listt): # zwraca face jako wartosc int
    tmp={}
    list_t={}
    for i in range(len(listt)):
        list_t=[0,0,0]
        for j in range(3):
            list_t[j]=int(listt[i][j+1])
        tmp[i]=['f',list_t]
    return tmp
def float_list_vertex(listt): #zwraca vertex jako float
    tmp={}
    list_t={}
    for i in range(len(listt)):
        list_t=[0.0,0.0,0.0]
        for j in range(3):
            list_t[j]=float(listt[i][j])
        tmp[i]=['v',list_t]
    return tmp
def xy_minmax(xy_list, sorted_block_size): 
    block_size = np.empty((len(l_face), 2))
    last = len(area) - 1 
    for face in range((len(l_face))):
        a = l_face[face][1][0]
        b = l_face[face][1][1]
        c = l_face[face][1][2]
        p = int (area[last][face])
        xa = pos[p][a][0]
        ya = pos[p][a][1]
        xb = pos[p][b][0]
        yb = pos[p][b][1]
        xc = pos[p][c][0]
        yc = pos[p][c][1]
        x_temp = [xa, xb, xc]
        y_temp = [ya, yb, yc]
        x_min = min(x_temp) -3 
        x_max = max(x_temp) +3
        y_min = min(y_temp) -3
        y_max = max(y_temp) +3
        xy_list[face][0] = x_min
        xy_list[face][1] = x_max
        xy_list[face][2] = y_min
        xy_list[face][3] = y_max
        block_size[face][0] = face
        if (x_min<0 or y_min<0 or x_max>=width or y_max>=height or xa<0 or xa>=width or xb<0 or xb>=width or xc<0 or xc>=width or ya<0 or ya>=height or yb<0 or yb>=height or yc<0 or yc>=height):
            block_size[face][1] = 0
        else:
            block_size[face][1] = (x_max-x_min) * (y_max-y_min)
    sorted_block_size = block_size[np.argsort(block_size[:, 1])]
    temp = {}
    temp = [xy_list, sorted_block_size]
    return temp
    
# Wczytanie siatki do programu (format siatki .OFF)
path=easygui.fileopenbox()
if(path == None):
    print("Brak siatki do teksturowania")
    os._exit(100)
filename, file_extension = os.path.splitext(path)

# Wczytanie zdjęć z folderu ./zdjecia
searchstr_m = os.path.join('./zdjecia', '*.jpg')
list_of_images = glob.glob(searchstr_m)
if(len(list_of_images) == 0):
    print("Folder 'zdjecia' jest pusty lub nie istnieje")
    os._exit(101)

width,height,rgb=imageio.imread(list_of_images[0]).shape

# Wpisanie zdj do pamięci
images=np.empty((len(list_of_images),width,height,rgb))
for i in range(len(list_of_images)):
    images[i,:,:,:] = imageio.imread(list_of_images[i])

# Załadowanie parametrów kamery i systemu kamer
K = np.empty((4,4))
R = np.empty((len(list_of_images),3,3))
t = np.empty((len(list_of_images),3,1))
if os.path.exists('cam_param_dog.txt'):
    param_file = open('cam_param_dog.txt').readlines()
else:
    print("Plik cam_param_dog.txt nie istnieje \n")
    os._exit(1)
if len(param_file) == 0:
    print("Plik nie zawiera parametrów kamer")
    os._exit(1)
for i in range(len(param_file)):
    param_file[i] = param_file[i].split(' ')
for i in range(3):
    for j in range(3):
        K[i][j]=float(param_file[i+1][j])
        if j == 2:
            K[i][3] = 0
K[3][0] = 0
K[3][1] = 0
K[3][2] = 0
K[3][3] = 1
for i in range(len(list_of_images)):
    for j in range(3):
        for k in range(4):
            if k != 3:
                R[i,j,k] = float(param_file[6+i+j+10*i][k])
            else:
                t[i,j,0] = float(param_file[6+i+j+10*i][k])
C = np.empty((len(list_of_images),3,1))
R_t = np.empty((len(list_of_images),4,4))
for pic in range (len(list_of_images)):
    C[pic] = -R[pic].dot(t[pic])
for i in range (len(list_of_images)):
    for j in range (4):
        if j == 3:
             R_t[i][j][0] = 0
             R_t[i][j][1] = 0
             R_t[i][j][2] = 0
             R_t[i][j][3] = 1
        else:
            R_t[i][j][0] = R[i][j][0]
            R_t[i][j][1] = R[i][j][1]
            R_t[i][j][2] = R[i][j][2]
            R_t[i][j][3] = C[i][j]     
#Wczytanie siatki do programu
if file_extension == '.ply':
    f=open(path,'rb')
    plyfile=PlyData.read(f)
    l_face=plyfile._elements
    l_face=l_face[1]
    l_face=l_face.data # dostep do wartosci face element
    l_vert=plyfile._elements
    l_vert=l_vert[0]
    l_vert=l_vert.data #dostep do wartosci vertex l_vert[0][0] 1 wiersz 1 element
elif file_extension == '.off':
    f=open(path,'r').readlines()
    tmp={}
    list_face={}
    list_vertex={}
    k=0
    l=0
    for i in range(len(f)):
        tmp[i]=f[i].split(' ')
    for i in range(len(tmp)):
        if(len(tmp[i])==3 and i>1):
            list_vertex[l]=tmp[i]
            l+=1
        if(len(tmp[i])==4):
            list_face[k]=tmp[i]
            k+=1
    #listy z podzielalem na v i f oraz zamienione na inty lub float danymi
    l_face=np.empty((len(list_face),4))
    l_vert=np.empty((len(list_vertex),3))
    l_face=int_list_faces(list_face) # wartosci face
    l_vert=float_list_vertex(list_vertex)
# Macierz z wyliczonymi współrzędnymi x y dla wszystkich zdjęć
pos = np.empty((len(list_of_images),len(l_vert),2)) 
for pic in range(len(list_of_images)): 
    P = K.dot(R_t[pic])
    for pnt in range(len(l_vert)):
        M=[l_vert[pnt][1][0],l_vert[pnt][1][1],l_vert[pnt][1][2],1]
        zm = P.dot(M)
        pos[pic][pnt][0] = round(zm[0]/zm[2]) 
        pos[pic][pnt][1] = round(zm[1]/zm[2]) 
print(pos[0][0][0])
print(pos[0][0][1])
area = np.empty((len(list_of_images) + 1,len(l_face)))
for face in range((len(l_face))):  
    a = l_face[face][1][0]
    b = l_face[face][1][1]
    c = l_face[face][1][2]
    for pic in range(len(list_of_images)): 
        xa = pos[pic][a][0]
        ya = pos[pic][a][1]
        xb = pos[pic][b][0]
        yb = pos[pic][b][1]
        xc = pos[pic][c][0]
        yc = pos[pic][c][1]
        if (xa<0 or xa>width or xb<0 or xb>width or xc<0 or xc>width or ya<0 or ya>height or yb<0 or yb>height or yc<0 or yc>height):
            area[pic][face] = 0
        else:
            area[pic][face] = abs(xa*yb + xb*yc + xc*ya - xc*yb - xa*yc - xb*ya)

for face in range((len(l_face))): 
    val = 0
    position = 0
    for pic in range(len(list_of_images)):
        if area[pic][face] > val:
            val = area[pic][face]
            position = pic 
    area[pic + 1][face] = position
 
xy_list = np.empty((len(l_face), 4)) 
sorted_block_size = np.empty((len(l_face), 2))
[xy_list, sorted_block_size ] = xy_minmax(xy_list, sorted_block_size)
size_factor = 0.1
i = 0
h=(len(l_vert))
last = len(area) - 1
other_faces = [[] for y in range((len(l_vert)))]
while i <= len(sorted_block_size) - 1:
    face_index = int(sorted_block_size[i][0])
    a = l_face[face_index][1][0]
    b = l_face[face_index][1][1]
    c = l_face[face_index][1][2]
    p = int (area[last][face_index])
    other_faces[a].append(p)
    other_faces[b].append(p)
    other_faces[c].append(p)
    i += 1
i = 0
pic_max ={}
while i <= len(sorted_block_size) - 1:
    pic_max = [[0] for x in range(len(list_of_images)) ]
    face_index = int(sorted_block_size[i][0])
    a = l_face[face_index][1][0]
    b = l_face[face_index][1][1]
    c = l_face[face_index][1][2]
    p = int (area[last][face_index])
    if len(sorted_block_size) - 1 -i == 6489: 
        rty=0
    for j in range( len(list_of_images)):
        a_num = other_faces[a].count(j)
        b_num = other_faces[b].count(j)
        c_num = other_faces[c].count(j)
        pic_max[j] = a_num + b_num + c_num

    pic_num = int(np.argmax(pic_max))
    if area[pic_num][face_index] >= (area[last][face_index] * size_factor ):
        area[last][face_index] = pic_num
    i += 1

[xy_list, sorted_block_size ] = xy_minmax(xy_list, sorted_block_size)
##tekstura
dimension = round(2 * height) 
texture = np.full((dimension, dimension, 3), 255)  
black_block = np.zeros((500,500,3))
i = len(sorted_block_size) - 1
UV_pos = np.empty((len(sorted_block_size), 6))
index_x = 0 
index_y = 0
index_xmax = dimension
index_ymax = 0
texture_num = 0
tex_pos = {}
while i >= 0:
    face_index = int(sorted_block_size[i][0])
    if len(sorted_block_size) - 1 -i == 6489:
        wtra = 0
    a = l_face[face_index][1][0]
    b = l_face[face_index][1][1]
    c = l_face[face_index][1][2]
    p = int (area[last][face_index])
    diff_x = int(round(xy_list[face_index][1]) - round(xy_list[face_index][0]))
    diff_y = int(round(xy_list[face_index][3]) - round(xy_list[face_index][2]))
    if (index_x + diff_x + 3) >= index_xmax: 
        index_x = 0
        index_y = index_ymax + 3 
    
    if ((diff_y + index_y )>=dimension):
        tex_pos[texture_num] = [texture_num, i]
        print("zapis texture x")
        imageio.imwrite('texture'+str(texture_num)+'.png', texture[:, :, :])
        texture_num += 1
        texture = np.full((dimension, dimension, 3),255)
        index_x = 0 
        index_y = 0
        index_xmax = dimension
        index_ymax = 0
        
    for img_y in range( 0, ( diff_y + 1 )):
        for img_x in range(0, ( diff_x + 1 )): 
            pos_x = (img_x + int(xy_list[face_index][0]))
            pos_y = (img_y + int(xy_list[face_index][2]))
            if(sorted_block_size[i][1]==0):
                texture[(img_y + index_y)][(img_x + index_x)][:] = black_block[img_y][img_x][:]
            else:
                texture[(img_y + index_y)][(img_x + index_x)][:] = images[p][pos_y][ pos_x ][:]
            if(pos_x == pos[p][a][0]) and (pos_y == pos[p][a][1]):
                UV_pos[i][0] = (img_x + index_x) / (dimension)
                UV_pos[i][1] = 1-((img_y + index_y) / (dimension))
            elif(pos_x == pos[p][b][0]) and (pos_y == pos[p][b][1]):
                UV_pos[i][2] = (img_x + index_x) / (dimension)
                UV_pos[i][3] = 1-((img_y + index_y) / (dimension))
            elif(pos_x == pos[p][c][0]) and (pos_y == pos[p][c][1]):
                UV_pos[i][4] = (img_x + index_x) / (dimension)
                UV_pos[i][5] = 1-((img_y + index_y) / (dimension))
    index_x += diff_x + 3 
    if index_y + diff_y > index_ymax:
        index_ymax = index_y + diff_y
    i -= 1
imageio.imwrite('texture'+str(texture_num)+'.png', texture[:, :, :])
tex_pos[texture_num] = [texture_num, i]

obj_file = open('model.obj', 'w')
obj_file.write("# Textured Model \n#\n#\n")
obj_file.write("# Praca magisterska \n")
obj_file.write("# Mateusz Mrozek \n# Marcin Olejniczak \n#\n#\n")
obj_file.write("mtllib info.mtl \n")
obj_file.write("g model \n \n")
for pnt in range(len(l_vert)): 
    obj_file.write("v  ")
    obj_file.write(str(l_vert[pnt][1][0]))
    obj_file.write("  ")
    obj_file.write(str(l_vert[pnt][1][1]))
    obj_file.write("  ")
    obj_file.write(str(l_vert[pnt][1][2]))
    obj_file.write("  \n")
i = len(sorted_block_size) - 1
while i >= 0:
    obj_file.write("vt  ")
    obj_file.write(str(UV_pos[i][0]))
    obj_file.write("  ")
    obj_file.write(str(UV_pos[i][1]))
    obj_file.write("  \n")
    obj_file.write("vt  ")
    obj_file.write(str(UV_pos[i][2]))
    obj_file.write("  ")
    obj_file.write(str(UV_pos[i][3]))
    obj_file.write("  \n")
    obj_file.write("vt  ")
    obj_file.write(str(UV_pos[i][4]))
    obj_file.write("  ")
    obj_file.write(str(UV_pos[i][5]))
    obj_file.write("  \n")
    i -= 1
number = tex_pos[0][0]
iteration = tex_pos[0][1]
obj_file.write("usemtl tex"+str(number)+" \n")
number += 1
i = len(sorted_block_size) - 1
j = 0
while i >= 0:
    face_index = int(sorted_block_size[i][0])
    a = l_face[face_index][1][0]
    b = l_face[face_index][1][1]
    c = l_face[face_index][1][2]
    if( i == iteration):
        obj_file.write("usemtl tex"+str(number)+" \n")
        if(number <= len(tex_pos)):
            iteration = tex_pos[number][1]
            number += 1
    obj_file.write("f  ")
    obj_file.write(str(a + 1))
    obj_file.write("/")
    obj_file.write(str(3*j + 1))
    obj_file.write("  ")
    obj_file.write(str(b + 1))
    obj_file.write("/")
    obj_file.write(str(3*j + 2))
    obj_file.write("  ")
    obj_file.write(str(c + 1))
    obj_file.write("/")
    obj_file.write(str(3*j + 3))
    obj_file.write("  \n")
    j += 1
    i -= 1
obj_file.close()
mtl_file = open('info.mtl', 'w')
mtl_file.write("# Material file \n#\n#\n")
mtl_file.write("# Praca magisterska \n")
mtl_file.write("# Mateusz Mrozek \n# Marcin Olejniczak \n#\n#\n")
for i in range(len(tex_pos)):

    mtl_file.write("newmtl tex"+str(i)+" \n")
    mtl_file.write("illum 1 \n")
    mtl_file.write("Ns 0.000000 \n")
    mtl_file.write("map_Kd texture"+str(i)+".png \n \n")
mtl_file.close()
stop = 0
