#!/usr/bin/env python3
import math

def bin(N):
    if N == 0:
        return [0,]
    else:

        lconst = int(math.log2(N))          #Maximum power of 2
        M=N                                 #Set new variable, as N cannot change (if N changes lconst changes)
        list=[]
        l = int(math.log2(M))               #Power of 2, will change
        for i in range (0,l+1):             #Create the main string, fill with zeroes
            list.append(0)
        list[0]=1                           #Set first element of list to 1
        while M > 0:
            l= int(math.log2(M))            #Get the power of 2
            list[lconst-l]=1                #Add that to the list
            M = M-2**l                      #Get the remainder and start over
        return list
print(bin(1024))
