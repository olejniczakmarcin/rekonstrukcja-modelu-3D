import os

if os.path.exists('./_CLOUD/new_cam_param_final.txt'):
    os.remove('./_CLOUD/new_cam_param_final.txt')
ff=open('./_CLOUD/new_cam_param_final.txt','a+')
f=open('./cam_param_dog.txt').readlines()
con=open('config.txt','r').readlines()
con2=open('config_new.txt','r').readlines()
t2=con2[0].replace('\n','')
t3=con2[1]
t0=con[0].replace('\n','')
t1=con[1]
diffx=(int(t0)-int(t2))/2
diffy=(int(t1)-int(t3))/2
for i in range(len(f)):
    f[i]=f[i].split(' ')
k=0
for i in range(len(f)):
    if(i==(10*k+1+k)):
        f[i][2]=str(float(f[i][2])-diffx)
        f[i+1][2]=str(float(f[i+1][2])-diffy)
        f[i][2]=f[i][2]+'\n'
        f[i+1][2]=f[i+1][2]+'\n'
        k+=1
for i in range(len(f)):
    for j in range(len(f[i])):
        ff.write(f[i][j])
        if(len(f[i])>1 and j<(len(f[i])-1)):
            ff.write(' ')
ff.close()


