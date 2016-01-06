import numpy as np
import csv
from sklearn.feature_extraction import DictVectorizer
from sklearn.utils import shuffle



v=DictVectorizer(sparse=False,sort=False)
def saveFile(name,dataset):
    np.save(name,dataset)
    
    
def split(splitFactor):
    X1=np.load('FullData.npy')
    X2=np,load('Without Duration Field.npy')
    Y=np.load('allLabels.npy')
    
    X1,Y1=shuffle
    
    sp=int(X1.shape[0]*splitFactor)
    train1=X1[0:sp,:]
    test1=X1[sp:,:]
    label_train1=Y[0:sp]
    label_test1=Y[sp:]
    
    train2=X2[0:sp,:]
    test2=X2[sp:,:]
    label_train2=Y[0:sp]
    label_test2=Y[sp:]
    
