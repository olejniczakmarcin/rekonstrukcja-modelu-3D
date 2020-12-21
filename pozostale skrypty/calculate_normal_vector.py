import numpy as np
import math
import os
wektor_nr1=4
wektor_nr2=3
index1=4*wektor_nr1+1
index2=4*wektor_nr2+1
list_of_lists = []
list_of_lists=open('wektor_translacji.txt','r').readlines()
wektor1={}
wektor2={}
for i in range(3):
    wektor1[i]=list_of_lists[index1+i]
    wektor2[i]=list_of_lists[index2+i]
wektor3={}
for i in range(3):
    t1=float(wektor1[i])
    t2=float(wektor2[i])
    wektor3[i]=t1-t2
l=math.sqrt((wektor3[0]*wektor3[0])+(wektor3[1]*wektor3[1])+(wektor3[2]*wektor3[2]))
ff=open('dlugosc_wektora.txt','w')
ff.write(str(l))
ff.close()