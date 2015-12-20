from  computeLog import logProd, NB_YPrior
import nltk
import json
import simplejson
import numpy as np

#assume spam is tp
def kpi(tp,fp,fn,tn,correct):
    
    precision=float(tp)/(tp+fp)
    recall=float(tp)/(tp+fn)
    f1=float(2.0*precision*recall)/(precision+recall)
    accuracy=float(correct*100)/(tp+tn+fp+fn)
    return (precision,recall,f1,accuracy)
        
f=open('dictionary.txt','r')
vocabulary=simplejson.load(f)
f.close()

pHam,pSpam=NB_YPrior()
   
theta=np.load('thetaArray.npy')
thetaSpam=np.log(theta[0])
thetaHam=np.log(theta[1])

One_thetaSpam=np.log(1-theta[0])
One_thetaHam=np.log(1-theta[1])

    
def createFeatureVector(words):
    vector=np.zeros(len(vocabulary),dtype=np.int)
    for word in words:
        index=vocabulary.index(word)
        vector[index]=1
    return vector
    

def classify(data):
    f=open(data,'r')
    tp=0
    tn=0
    fn=0
    c=0
    c2=0
    fp=0
    correct=0
    for line in f:
        words=nltk.word_tokenize(line)
        sentence=""
        label=words[0]
        featureVector=createFeatureVector(words[1:])
        
        for word in words[1:]:
            sentence+=word+" "
        
        resSpam=np.dot(featureVector,thetaSpam)+ np.dot(1-featureVector,One_thetaSpam) + np.log(pSpam)   
        resHam=np.dot(featureVector,thetaHam) + np.dot(1-featureVector,One_thetaHam) + np.log(pHam)
        
        #resSpam,resHam=logProd(sentence)
        res=''
        #print 'resSpam is ',resSpam,' resHam is ',resHam
        
        if resSpam > resHam :
            res='spam'
        else:
            res='ham'
        #print 'line is ',line
        #print 'Predicted ',res,' : actual label is ',label
            
        if label=='ham' and res==label:
            tn+=1
            correct+=1
        elif label=='ham' and res!=label:
            fp+=1
        if label=='spam' and res==label:
            tp+=1
             
            correct+=1
        elif label=='spam' and res!=label:
            fn+=1
            
    precision,recall,f1,accuracy=kpi(tp,fp,fn,tn,correct)  
    print 'Precision is ',precision,'\nRecall is ',recall,'\nF1 is ',f1,'\nAccuracy is ',accuracy,'%'
       
         
if __name__=='__main__':
    classify('test.txt')    


