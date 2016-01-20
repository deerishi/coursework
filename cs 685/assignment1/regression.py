import numpy as np
import csv
import matplotlib.pylab as plt
from sklearn.utils import shuffle
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib import cm

class Regression():
    
    def __init__(self):
        pass
        
    def regularization_loss(self,weights,lamda):
        return 0.5*lamda*(sum([i**2 for i in weights]))
    
    def mse_loss(self,predicted,goldset):
        diff=goldset-predicted
        #print 'diff returning ',0.5* (sum([i**2 for i in diff]))
        return 0.5* (sum([i**2 for i in diff]))
            
    def total_loss(self,predicted,goldset,weights,lamda):
        return self.mse_loss(predicted,goldset) #+ self.regularization_loss(weights,lamda)
     
    def test(self,X,weights):
        predicted=np.dot(X,weights)
        return predicted
        
        
    def train(self,X,y,lamda):
        
        self.X_train=X
        self.y_train=y
        
        
        A=np.dot(X.T,X) # X is mxd , we want A to be dxd
        regularization_term=lamda*np.diag(np.ones(X.shape[1])) #remember to add the one dimension to X
        #print 'regularization_term is ',regularization_term
        A=A+regularization_term
        
        b=np.dot(X.T,y)
        
        #print 'the shape of  A is ',A.shape,' and b is ',b.shape
        weights=np.dot(np.linalg.inv(A),b)
        #print 'lamda= ',lamda,' and  weight is ',weights
        return weights
        
        
        
    def crossValidate(self,K=10,lamda=1):
        datasetsX=[]
        labelsy=[]
        for i in range(1,11):
            Xname="Regression/fData"+str(i)+".csv"
            fx=open(Xname)
            xReader=csv.reader(fx)
            X=[]
            y=[]
            for row in xReader:
                row=[float(x) for x in row]
                X.append(row)
            X=np.asarray(X)
            datasetsX.append(X)
            
            yname="Regression/fLabels"+str(i)+'.csv'
            fy=open(yname)
            y=[]
            yReader=csv.reader(fy)
            for row in yReader:
                row=[float(x) for x in row]
                #print 'row is ',row[0]
                y.append(row[0])
            y=np.asarray(y)
            labelsy.append(y)
            
            
        
        #now we make cross validation datasets
        kcross=[]
        for i in range(0,K):
            kcross.append(i)
        for i in range(0,K-1):
            kcross.append(i)
        for i in range(0,K):
            testX=datasetsX[kcross[i]]
            testY=labelsy[kcross[i]]
            losses=[]
            r2s=[]
            trainX=datasetsX[kcross[i+1]]
            trainy=labelsy[kcross[i+1]]
            #print '1 labels is ',trainy.shape
            for j in range(i+2,i+K):
                trainX=np.vstack((trainX,datasetsX[kcross[j]]))
                trainy=np.hstack((trainy,labelsy[kcross[j]]))
                
                #print 'trainX is ',trainX,'\n j= ',j
            bias=np.ones((trainX.shape[0],1))
            trainX=np.hstack((trainX,bias))
            #trainX,trainy=shuffle(trainX, trainy, random_state=0)
            
            bias2=np.ones((testX.shape[0],1))
            
            testX=np.hstack((testX,bias2))
            #print 'shapes train is ',trainX.shape,' and trainy is ',trainy.shape
            #lamda=-8
            weights=self.train(trainX,trainy,lamda)
            #print 'Now testing------>'
            predicted=self.test(testX,weights)
            predicted_train=self.test(trainX,weights)
            meany=np.mean(trainy)
            diff2=predicted_train - meany
            Stt=sum([l**2 for l in diff2])
            Ssm=self.mse_loss(predicted_train,trainy)*2
            r2s.append(Ssm/Stt)
            loss=self.total_loss(predicted,testY,weights,lamda)
            #fig = plt.figure()
            #ax = fig.add_subplot(111, projection='3d')
            #ax.scatter(trainX[:,0],trainX[:,1],trainy)
            #ax.plot_trisurf(trainX[:,0],trainX[:,1],predicted_train,color=(0,0,0,0))
            #plt.title('Regression Surface with lamda= '+str(lamda))

            #plt.show()
            losses.append(loss)
        print 'total loss with lamda=',lamda,' is is ',np.mean(losses),' mean r2 is ',np.mean(r2s)  
                
        return  np.mean(losses) 

lsr=Regression()
lamdas=np.arange(0,4,0.1)
losses=[]
for lamda in lamdas:
    losses.append(lsr.crossValidate(K=10,lamda=lamda))

plt.plot(lamdas,losses) 
plt.xlabel('Values of lamda in Least squares Regression')
plt.ylabel('mean loss in each K fold iteration')
plt.title('my exp Variation of Accuracy with increasing lamda in Least squares Regression')

plt.show()        
minLoss=min(losses)
print 'minimum loss of  ',minLoss,'occurs at lamda= ',lamdas[losses.index(minLoss)] 
                                   
