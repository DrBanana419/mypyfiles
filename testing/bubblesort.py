#!/usr/bin/env python3

#import random as rd
#l=[]
#for i in range(0,6):
#    l.append(rd.randint(0,9))

l=[9,8,7,6,5,4]
c=True
while c:
    c = False
    for i in range(0,len(l)-1):
        if l[i]>l[i+1]:
            (l[i],l[i+1])=(l[i+1],l[i])
            c=True
    print(l)
