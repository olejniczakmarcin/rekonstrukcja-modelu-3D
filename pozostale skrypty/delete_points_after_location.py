import os

if os.path.exists('./_CLOUD/cloud_new_pos.txt'):
    os.remove('./_CLOUD/cloud_new_pos.txt')
ff=open('./_CLOUD/cloud_new_pos.txt','a+')
f=open('./_CLOUD/newcloud.txt').readlines()
if os.path.exists('./_CLOUD/cloudxyz_pos.xyz'):
    os.remove('./_CLOUD/cloudxyz_pos.xyz')
fff=open('./_CLOUD/cloudxyz_pos.xyz','a+')
for i in range(len(f)):
    f[i]=f[i].split(' ')

i=0
t1=False
t2=False
t3=False
position=0.3

while(i<len(f)):
    t1=False
    t2=False
    t3=False
    if(float(f[i][0])<-position):
        t1=True
    if(float(f[i][0])>position):
        t1=True
    if(float(f[i][1])<-position):
        t2=True
    if(float(f[i][1])>position):
        t2=True
    if(float(f[i][2])<-position):
        t3=True
    if(float(f[i][1])>position):
        t3=True
    if(t1 and t2 and t3):
        i+=1
    if(t1==False and t2==False and t3==False):
        for j in range(len(f[i])):
            ff.write(f[i][j])
            if j<(len(f[i])-1):
                ff.write(' ')
        i+=1
    else:
        i+=1
ff.close()
i=0
fd=open('./_CLOUD/cloud_new_pos.txt').readlines()
for i in range(len(fd)):
    fd[i]=fd[i].split(' ')
for i in range(len(fd)):
    for j in range(len(fd[i])):
        fff.write(fd[i][j])
        if j<(len(fd[i])-1):
            fff.write(' ')
fff.close()