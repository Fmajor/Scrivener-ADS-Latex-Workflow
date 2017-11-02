import numpy as np
import os
import copy

N = 0
fatherStack = ["can not be this"]
lastStackLevel = 0
tagList  = []
fatherList  = []

tagSystemPath=os.path.join(os.path.dirname(__file__),"tagSystem.txt")
f = open(tagSystemPath, "r")
for eachLine in f:
    eachLine = eachLine.split("#")[0].rstrip()
    if not eachLine:
        continue
    stackLevel  = 0
    while eachLine[stackLevel]=="\t":
        stackLevel+=1
    thisName = eachLine.strip()
    if stackLevel==lastStackLevel:
        fatherStack[-1] = thisName
    elif stackLevel==lastStackLevel + 1:
        fatherStack.append(thisName)
    elif stackLevel<lastStackLevel:
        fatherStack = fatherStack[:stackLevel+1]
        if not fatherStack:
            fatherStack.append(thisName)
        else:
            fatherStack[-1] = thisName
    lastStackLevel = stackLevel

    tagList.append(thisName)
    fatherList.append(copy.copy(fatherStack[:-1]))
    N += 1
    index = N-1
    print("{}{}".format("\t"*stackLevel, thisName))

debug = 0
if debug:
    for each, eachFathers in zip(tagList, fatherList):
        print(each, eachFathers)
