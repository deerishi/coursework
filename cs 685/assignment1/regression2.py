import numpy as np
import csv
import matplotlib.pylab as plt
from sklearn.utils import shuffle
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from sklearn import datasets, linear_model

class Regression():
    
    def __init__(self):
        pass
        
    def regularization_loss(self,weights,lamda):
        print 'weights are ',weights,' lamda is ',lamda ,' returning ',0.5*lamda*(sum([i**2 for i in weights]))
        return 0.5*lamda*(sum([i**2 for i in weights]))
    
    def mse_loss(self,predicted,goldset):
        diff=goldset-predicted
        print 'diff returning ',0.5* (sum([i**2 for i in diff]))/diff.shape[0]
        return 0.5* (sum([i**2 for i in diff]))/diff.shape[0]
            
    def total_loss(self,predicted,goldset,weights,lamda):
        return self.mse_loss(predicted,goldset) + self.regularization_loss(weights,lamda)
     
    def test(self,X,weights):
        predicted=np.dot(X,weights)
        return predicted
        
        
    def train(self,X,y,lamda):
        
        self.X_train=X
        self.y_train=y
        
       
        A=np.dot(X.T,X) # X is mxd , we want A to be dxd
        regularization_term=lamda*np.diag(np.ones(X.shape[1])) #remember to add the one dimension to X
        A=A+regularization_term
        
        b=np.dot(X.T,y)
        
        #print 'the shape of  A is ',A.shape,' and b is ',b.shape
        weights=np.dot(np.linalg.inv(A),b)
        #print 'lamda= ',lamda,' and  weight is ',weights
        return weights
        
        
        
    def crossValidate2(self,K=10,lamda=1):
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
            trainX=datasetsX[kcross[i+1]]
            trainy=labelsy[kcross[i+1]]
            #print '1 labels is ',trainy.shape
            for j in range(i+2,i+K):
                trainX=np.vstack((trainX,datasetsX[kcross[j]]))
                trainy=np.hstack((trainy,labelsy[kcross[j]]))
                
                #print 'trainX is ',trainX,'\n j= ',j
            diabetes = datasets.load_diabetes()
            trainX=np.array([[1],[2],[3],[4],[4],[5],[5],[6],[6],[7]])
            trainy=np.array([7,8,9,8,9,11,10,13,14,13])
            testX=np.array([[1],[2],[3]])
            testY=np.array([7,8,9])
            #diabetes_X = diabetes.data[:, np.newaxis, 2]
            #trainX=diabetes_X[:-20]
            #trainy=diabetes.target[:-20]
            #testX=diabetes_X[-20:]
            #testY=diabetes.target[-20:]
            bias=np.ones((trainX.shape[0],1))
            #trainX-np.mean(trainX)
            trainX=np.hstack((trainX,bias))
            #trainX,trainy=shuffle(trainX, trainy, random_state=0)

            bias2=np.ones((testX.shape[0],1))
            testX=np.hstack((testX,bias2))
            regr = linear_model.Ridge(alpha=lamda)
            
            regr.fit(trainX,trainy)
            #lamda=1
            #print 'shapes train is ',trainX.shape,' and trainy is ',trainy.shape
            weights=self.train(trainX,trainy,lamda)
            #print 'Now testing------>'
            predicted=regr.predict(testX)
            predicted_train=regr.predict(trainX)
            loss=self.total_loss(predicted,testY,weights,lamda)
            
            
            if lamda==1 or lamda ==2 or lamda==3 or lamda ==0:
                fig = plt.figure()
                #ax = fig.add_subplot(111, projection='3d')
                #ax.scatter(trainX[:,0],trainX[:,1],trainy)
                #ax.plot_trisurf(trainX[:,0],trainX[:,1],predicted_train,color=(0,0,0,0))
                plt.plot(trainX,trainy,'*')
                plt.plot(trainX,predicted_train,'-')
                plt.title('Regression Surface with lamda= '+str(lamda))
                plt.show()
            losses.append(loss)
        print 'total loss with lamda=',lamda,' is is ',np.mean(losses) ,'\n\n' 
                
        return  np.mean(losses) 
        
        
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
            trainX=datasetsX[kcross[i+1]]
            trainy=labelsy[kcross[i+1]]
            count=1
            #print '1 labels is ',trainy.shape
            for j in range(0,1):
                trainX=np.vstack((trainX,datasetsX[kcross[j]]))
                trainy=np.hstack((trainy,labelsy[kcross[j]]))
                
                #print 'trainX is ',trainX,'\n j= ',j
            diabetes = datasets.load_diabetes()
            trainX=np.array([[1],[2],[3],[4],[4],[5],[5],[6],[6],[7]])
            trainy=np.array([2,3,5,6,7,8,9,9,11,11])
            testX=np.array([[1],[2],[3]])
            testY=np.array([7,8,9])
            #diabetes_X = diabetes.data[:, np.newaxis, 2]
            #trainX=diabetes_X[:-20]
            #trainy=diabetes.target[:-20]
            #testX=diabetes_X[-20:]
            #testY=diabetes.target[-20:]
            
            bias=np.ones((trainX.shape[0],1))
            trainX=np.hstack((trainX,bias))
            #trainX,trainy=shuffle(trainX, trainy, random_state=0)
            #lamda=0.5
            bias2=np.ones((testX.shape[0],1))
            testX=np.hstack((testX,bias2))
            #print 'shapes train is ',trainX.shape,' and trainy is ',trainy.shape
            weights=self.train(trainX,trainy,lamda)
            #print 'Now testing------>'
            predicted=self.test(testX,weights)
            predicted_train=self.test(trainX,weights)
            loss=self.total_loss(predicted_train,trainy,weights,lamda)
            if count==1:
                fig = plt.figure()
                #ax = fig.add_subplot(111, projection='3d')
                #ax.scatter(trainX[:,0],trainX[:,1],trainy)
                #ax.plot_trisurf(trainX[:,0],trainX[:,1],predicted_train)
                plt.plot(trainX,trainy,'*')
                plt.plot(trainX,predicted_train,'-')
                #ax.contour(trainX[:,0],trainX[:,1],predicted_train,cmap=cm.coolwarm)
                plt.title('Regression Surface with lamda= '+str(lamda))
                plt.show()
                count=2
            losses.append(loss)
        print 'total loss with lamda=',lamda,' is is ',np.mean(losses) ,'\n\n' 
                
        return  np.mean(losses) 

lsr=Regression()
lamdas=np.arange(1,20,1)
losses=[]
for lamda in lamdas:
    losses.append(lsr.crossValidate(K=3,lamda=lamda))

plt.plot(lamdas,losses) 
plt.xlabel('Values of lamda in Least squares Regression')
plt.ylabel('mean loss in each K fold iteration')
plt.title('my exp Variation of Accuracy with increasing lamda in Least squares Regression')

plt.show()        
minLoss=min(losses)
print 'minimum loss of  ',minLoss,'occurs at lamda= ',lamdas[losses.index(minLoss)] 
                                   
