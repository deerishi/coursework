import simplejson
import nltk
import json
import numpy as np

f=open('TrainHamDict.txt','r')
hamDict=json.load(f)
f.close()
f=open('TrainSpamDict.txt','r')
spamDict=json.load(f)
numSpam=spamDict['SPAMCOUNT']
numHam=hamDict['HAMCOUNT']

def saveFile(data,name):
    with open(name, 'w') as outfile:
        json.dump(data, outfile)

def train(dictionary):
    f=open(dictionary,'r')
    vocabulary=simplejson.load(f)
    print 'the vocabulary length is ',len(vocabulary)
    thetaSpam={}
    thetaHam={}
    thetaSPaml=[]
    thetaHaml=[]
    
    for word in vocabulary:
        #print 'word is ',word
        if word in spamDict:
            TSpam=((float(spamDict[word]+1))/(numSpam+1)) #using Beta(2,1) as the prior
        else:
            TSpam=((1.0)/(numSpam+1))
        if word in hamDict:
            THam=((float(hamDict[word]+1))/(numHam+1))
        else:
           THam=((1.0)/(numHam+1)) 
           
           #estimating the bernoulli document model parameters
        thetaHam[word]=THam
        thetaSpam[word]=TSpam
        thetaSPaml.append(TSpam)
        thetaHaml.append(THam)
    
    thetaSpaml=np.asarray(thetaSPaml)  
    thetaHaml=np.asarray(thetaHaml)  
    theta=np.vstack((thetaSpaml,thetaHaml))
    np.save('thetaArray',theta)
    saveFile(thetaSpam,'thetaSpam.txt')
    saveFile(thetaHam,'thetaHam.txt')
    print 'the tspam length is ',len(thetaSpam)
    print 'the tham length is ',len(thetaHam)
if __name__=='__main__':
    train('dictionary.txt')
