import numpy as np
from collections import defaultdict 
import csv
import matplotlib.pylab as plt
from sklearn.utils import shuffle

# best result with shuffling at k=77, without shffling its 70 ith random state=0
#The accuracy of the model could vary highly depending on the shuffling of the dataset.
class KNearestNeighbor:
    def __init__(self):
        pass

    def train(self, X, y):
        self.X_train=X
        self.Y_train=y
    
    def L1(self,X):
        norms=np.linalg.norm(X,axis=1,ord=1)
        return norms
    
    def L2(self,X):
        norms=np.linalg.norm(X,axis=1)
        return norms
        
    def test(self,X,k=1):
        labels=[]
        for i in range(0,X.shape[0]):
            #remember already an array
            #print 'xtrain is ',self.X_train - X[i]
            norms=self.L2(self.X_train-X[i]) 
            
            norms=norms.tolist()
            distances=[j[0] for j in sorted(enumerate(norms),key=lambda x:x[1])]
            kNearestNeiboughours=distances[:k] # now we have the indexes of the 
            kNearestNeiboughours=np.asarray(kNearestNeiboughours)
            labelsOfNeighbours=self.Y_train[kNearestNeiboughours]
            labelsOfNeighbours=labelsOfNeighbours.tolist()
            d=defaultdict(int)
            for m in labelsOfNeighbours:
                d[m]+=1
            result=max(d.iteritems(),key=lambda x:x[1])
            # result would be in the form of like (4,6) ,4 occurs 6 times
            label=result[0]
            labels.append(label)
        labels=np.asarray(labels)
        return labels
       
    def checkAccuracy(self,predicted,goldset):
        predicted=predicted.tolist()
        goldset=goldset.tolist()
        correct=0
        for i in range(0,len(predicted)):
            if goldset[i]==predicted[i]:
                correct+=1
        
        return (float(correct)/len(predicted))*100
        

    def crossValidate(self,K=10,k=1):
        datasetsX=[]
        labelsy=[]
        for i in range(1,11):
            Xname="data"+str(i)+".csv"
            fx=open(Xname)
            xReader=csv.reader(fx)
            X=[]
            y=[]
            for row in xReader:
                row=[float(x) for x in row]
                X.append(row)
            X=np.asarray(X)
            datasetsX.append(X)
            #print 'row is ',datasetsX
            yname="labels"+str(i)+'.csv'
            fy=open(yname)
            yReader=csv.reader(fy)
            for row in yReader:
                row=[int(x) for x in row]
                y.append(row[0])
            y=np.asarray(y)
            labelsy.append(y)
            
            #print 'labels are ',labelsy
        
        #now we make cross validation datasets
        kcross=[]
        for i in range(0,K):
            kcross.append(i)
        for i in range(0,K-1):
            kcross.append(i)
        for i in range(0,K):
            testX=datasetsX[kcross[i]]
            testY=labelsy[kcross[i]]
            accuracies=[]
            trainX=datasetsX[kcross[i+1]]
            trainy=labelsy[kcross[i+1]]
            #print '1 labels is ',trainy.shape
            for j in range(i+2,i+K):
                trainX=np.vstack((trainX,datasetsX[kcross[j]]))
                trainy=np.hstack((trainy,labelsy[kcross[j]]))
            #trainX,trainy=shuffle(trainX, trainy, random_state=0)
             
            self.train(trainX,trainy)
            #print 'Now testing------>'
            predicted=self.test(testX,k)
            accuracy=self.checkAccuracy(predicted,testY)  
            accuracies.append(accuracy)
        print 'accuracy with k=',k,' is is ',np.mean(accuracies)  
                
        return  np.mean(accuracies)        
                
knn=KNearestNeighbor()
accuracy=[]
ks=[]
for k in range(1,30):
    ks.append(k)
    accuracy.append(knn.crossValidate(K=10,k=k))
    

plt.plot(ks,accuracy,label='Mean Accuracy') 
plt.xlabel('Values of k in knn')
plt.ylabel('mean accuracy in each K fold iteration')
plt.title('my exp Variation of Accuracy with increasing k in k Nearest Neighbours')

plt.show()        
maxAcc=max(accuracy)
print 'maximum accuracy of  ',maxAcc,'occurs at k= ',ks[accuracy.index(maxAcc)]   
                           
        
            
