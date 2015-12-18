import json
import numpy as np
from os.path import expanduser

spamDict={}
hamDict={}


def saveFile(data,name):
    with open(name+'.txt', 'w') as outfile:
        json.dump(data, outfile)

def wcount(filename):
    f=open(filename,'r')
    for line in f:
        words=line.split(' ')
        if(words[0]=='ham'):
            for i in range(1,len(words)):
                word=words[i]
                if word in hamDict:
                    hamDict[word]+=1
                else:
                    hamDict[word]=1
        else:
            for i in range(1,len(words)):
                word=words[i]
                if word in spamDict:
                    spamDict[word]+=1
                else:
                    spamDict[word]=1

    saveFile(spamDict,'spamDict')  
    saveFile(hamDict,'hamDict')  
    
    
if '__name__'=='_main_':
    wcount('text3.txt')

