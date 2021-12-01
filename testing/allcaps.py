#!/usr/bin/env python3
import math

def smol(word):
    '''Turn all letters of a word into lower case'''
    listword  = str2list(word)
    for i in range (0,len(listword)):
        listword[i] = listword[i].lower()
    b = ""
    for char in listword:
        b = b + char

    return b

def str2list(word):
    '''Convert word to a list'''
    l=[]
    for c in word:
        l.append(c)
    return(l)

def conv(l, stri):
    '''Capitalise letters of a word according to given list that represents a binary number'''
    lisw=str2list(stri)                  #First convert given word to list
    for i in range(0,len(l)):
        if l[i]==1:
            lisw[i]=lisw[i].upper()
    return lisw

def fil(n):
    '''Fill a list with zeroes'''
    L=[]
    for i in range (0,n):
        L.append(0)
    return L

def bin(N):
    '''Convert a base 10 number into base 2 (binary)'''
    if N == 0:
        return [0,]

    else:
        lconst = int(math.log2(N))          #Maximum power of 2
        M=N                                 #Set new variable, as N cannot change (if N changes lconst changes)
        list=[]
        l = int(math.log2(M))               #Power of 2, will change
        list = fil(l+1)
        list[0]=1                           #Set first element of list to 1
        while M > 0:
            l= int(math.log2(M))            #Get the power of 2
            list[lconst-l]=1                #Add that to the list
            M = M-2**l                      #Get the remainder and start over
        return list


def caps(word):
    '''Return all variations (capitalisation) of a given word.'''
    word = smol(word)
    length = len(word)

    masternumberlist = fil(length)                  #First create a list with zeroes (number of zeroes is equal to length of word)

    listofbins = []
    for i in range(0, 2**length):                   #Create a list of the binary versions of numbers going up to the length
        binarynum = bin(i)                          #of the word -1
        listofbins.append(binarynum)

    newlistofbins = []
    for ilist in listofbins:                        #Now make sure the binary numbers created above have the same lenth (filled with a necessary amount of zeroes) as the length of the word
        diff = len(masternumberlist) - len(ilist)   #Determine how many zeroes are needed to add to each binary number
        dummylist = fil(diff)                       #Create a list filled with that amount of zeroes
        newilist = dummylist + ilist                #Add that list to the binary number
        newlistofbins.append(newilist)              #Add new binary numbers to a masterlist

    final = []
    for list in newlistofbins:                      #Take each binary number from the masterlist created above.
        Word = conv(list, word)                     #Convert those binary numbers into lists of words with necessary capitalisation.
        final.append(Word)                          #Add each letter-list to a masterlist

    Final = []                                      #This the final answer-list
    for el in final:                                #For each letter-list in the above masterlist
        a = ""                                      #Set an empty string
        for i in el:                                #For each letter in the letter-list
            a = a + i                               #Basically create the word from the list of letters
        Final.append(a)                             #Add words to the final answer-list :)

    return Final

userinput = input("Give me a word! : ")
print(caps(userinput))
