import numpy as np
from sklearn import preprocessing as p
from sklearn.utils import shuffle


def saveFile(name,dataset):
    np.save(name,dataset)


def prepare(splitFactor,randomState):
    f=open('data_banknote_authentication.txt','r')
    print 'splitFactor is ',splitFactor
    arr=[]
    labels=[]
    for line in f:
        nums=line.split(',')
        l=[]
        labels.append(int(nums[-1].split('\r')[0]))
        for num in nums[0:-1]:
            l.append(float(num)) #appened the number to the arry
        arr.append(l)
        
    arr=np.asarray(arr)
    labels=np.asarray(labels)
    arr,labels=shuffle(arr,labels,random_state=randomState)
    print 'arr is ',arr.shape,' labels are ',labels.shape
    print 'arr is ',arr,' labels are ',labels
    saveFile("full labels",labels)
    saveFile('full data',arr) 
        
    
    sp=int(splitFactor*arr.shape[0])
    Xtrain=arr[0:sp,:]
    Ytrain=labels[0:sp]
    print 'earlier xtrain.mean is ',Xtrain.mean(axis=0)
    scaler=p.StandardScaler().fit(Xtrain)
    Xtrain=scaler.transform(Xtrain)
    
    
    Xtest=arr[sp:,:]
    Ytest=labels[sp:]
    
    Xtest=scaler.transform(Xtest)
    saveFile('Train/Xtrain with sp='+str(splitFactor),Xtrain)
    saveFile('Train/Ytrain with sp='+str(splitFactor),Ytrain)
    saveFile('Test/Xtest with sp='+str(splitFactor),Xtest)
    saveFile('Test/Ytest with sp='+str(splitFactor),Ytest)
    print '\n\ntrain is ',Xtrain.shape,' and ',Ytrain.shape
    print 'test is ',Xtest.shape,' and ',Ytest.shape
    print 'xtrain.mean is ',Xtrain.mean(axis=0),'\n\n'
#    
    
    
if __name__=='__main__':
    l=[0.7,0.8,0.9]
    for i in range(0,3):
        prepare(l[i],i) 
    
