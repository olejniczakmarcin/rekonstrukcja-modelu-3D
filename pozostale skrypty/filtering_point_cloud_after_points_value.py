import os

if os.path.exists('./_CLOUD/cloud_new.txt'):
    os.remove('./_CLOUD/cloud_new.txt')
ff=open('./_CLOUD/cloud_new.txt','a+')
f=open('./_CLOUD/cloud.xyz').readlines()
if os.path.exists('./_CLOUD/cloud_black.xyz'):
    os.remove('./_CLOUD/cloud_black.xyz')
ff2=open('./_CLOUD/cloud_black.xyz','a+')
for i in range(len(f)):
    f[i]=f[i].split(' ')
i=0
value_color=30

while(i<len(f)):
    if(int(f[i][3])<value_color and int(f[i][4])<value_color and int(f[i][5])<value_color):
        i+=1
    else:
        for j in range(len(f[i])):
            ff.write(f[i][j])
            if j<(len(f[i])-1):
                ff.write(' ')
        i+=1
ff.close()
fg=open('./_CLOUD/cloud_new.txt').readlines()
for i in range(len(fg)):
    fg[i]=fg[i].split(' ')
for i in range(len(fg)):
    for j in range(3):
        ff2.write(fg[i][j])
        if j<2:
            ff2.write(' ')
        if j==2:
            ff2.write('\n')
ff2.close()