import numpy as np
import nltk
import json

f=open('TrainHamDict.txt','r')
hamDict=json.load(f)
f.close()
f=open('TrainSpamDict.txt','r')
spamDict=json.load(f)
f.close()
numSpam=spamDict['SPAMCOUNT']
numHam=hamDict['HAMCOUNT']


def NB_YPrior():
    total=numSpam+numHam
    pSpam=float(numSpam)/(total)
    pHam=float(numHam)/(total)
    return (pHam,pSpam) #  no prior required on the Y  
    
def logProd(X):
    #here X is the sentence that needs to be preprocessced
    words=nltk.word_tokenize(X)
    resSpam=0
    resHam=0
    for word in words:
        if word in spamDict:
            resSpam+=np.log((float(spamDict[word]+1))/(numSpam+1)) #using Beta(2,1) as the prior
        else:
            resSpam+=np.log((1.0)/(numSpam+1))
        if word in hamDict:
            resHam+=np.log((float(hamDict[word]+1))/(numHam+1))
        else:
            resHam+=np.log((1.0)/(numHam+1))  
        print 'word is ',word,' resSpam is ',resSpam,' resHam is ',resHam 
    pHam,pSpam=NB_YPrior()      
    resSpam+=np.log(pSpam)
    resHam+=np.log(pHam)
    return (resSpam,resHam)
    
    
    
