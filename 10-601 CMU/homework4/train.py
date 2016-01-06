import numpy as np
import pylab as pl


def Kfold_CrossValidation(k,Xtrain,XTest,yTrain,yTest):
    bsize=int(Xtrain.shape[0]/k)
    i=1
    batches=[]
    batchesl=[]
    while(i<k):
        batch=Xtrain[bsize(i-1):bsize*i,:]
        #batch2=
        batches.append(batch)
        i=i+1
    
    batch=Xtrain[bsize(i-1):,:]
    batches.append(batch)
    for i in range(0,len(batches)):
        ktrain=batches[i]
        m=i+1
        for j in range(1,k-1):
            if m == len(batches):
                m=0
            ktrain=ktrain.vstack((ktrain,batches[m]))
            m=m+1
        if m >=len(batches):
            m=0
        ktest=batches[m]
        # so now we have k-1 training sets and the kth is the test set    
        what=LR_GradientAscent(Xtrain,yTrain,i)
        pl.figure()
        pl.scatter(Xtrain[:, 0], Xtrain[:, 1], marker='o', c=yTrain)
        x1=[-3,3]
        y1=-1*(what[0]+what[1]*(x1[0]))/what[2]
        y2=-1*(what[0]+what[1]*x1[1])/what[2]
        
        pl.plot(x1,[y1,y2])
        pl.show()
        
    

def LR_CalcObj(Xtrain,yTrain,what):
    w0=what[0]
    w=what[1:]
    obj=0
    for i in range(0,Xtrain.shape[0]):
        cterm=w0+np.dot(Xtrain[i],w)
        obj+=yTrain[i]*cterm - np.log(1+np.exp(cterm))
        
    return obj


    
    
def LR_CalcObj_with_L2_Regularizer(Xtrain,yTrain,what,lamda):
    w0=what[0]
    w=what[1:]
    obj=0
    for i in range(0,Xtrain.shape[0]):
        cterm=w0+np.dot(Xtrain[i],w)
        obj+=yTrain[i]*cterm - np.log(1+np.exp(cterm)) -lamda*(np.dot(w,w) + w0*w0 )
        
    return obj

def LR_CalcObj_with_L1_Regularizer(Xtrain,yTrain,what,lamda):
    w0=what[0]
    w=what[1:]
    obj=0
    for i in range(0,Xtrain.shape[0]):
        cterm=w0+np.dot(Xtrain[i],w)
        obj+=yTrain[i]*cterm - np.log(1+np.exp(cterm)) -lamda*(np.sum(np.abs(w)) + np.abs(w0) )
        
    return objw

def check_Convergence(newObj,oldObj,tolerance):
    
    diff=np.abs(newObj - oldObj)
    if diff<=tolerance:
        return True
    else:
        return False
        

def LR_CalcGrad(Xtrain,yTrain,what):
    w0=what[0]
    w=what[1:]
    obj=0
    grad_wrt_w0=0
    grad_wrt_w=0
    for i in range(0,Xtrain.shape[0]):
        cterm=w0+np.dot(Xtrain[i],w)
        cterm2=np.exp(w0+np.dot(Xtrain[i],w))
        p_y_1=cterm2/(1+cterm2)
        #print ' ctem2 is ',cterm2,' p(y=1|x) is ',p_y_1
        grad_wrt_w0+=yTrain[i] - p_y_1
        grad_wrt_w+=Xtrain[i]*grad_wrt_w0
        
    return (grad_wrt_w0,grad_wrt_w)    

def LR_CalcGrad2(Xtrain,yTrain,what):
    w0=what[0]
    w=what[1:]
    obj=0
    grad_wrt_w0=0
    grad_wrt_w=0
    for i in range(0,Xtrain.shape[0]):
        cterm=w0+np.dot(Xtrain[i],w)
        cterm2=np.exp(w0+np.dot(Xtrain[i],w))
        p_y_1=cterm2/(1+cterm2)
        grad_wrt_w0+=yTrain - p_y_1
        grad_wrt_w+=Xtrain[i]*grad_wrt_w0
        
    return (grad_wrt_w0,grad_wrt_w) 

    
def LR_CalcGrad_L2(Xtrain,yTrain,what,lamda):
    w0=what[0]
    w=what[1:]
    wt=w
    
    obj=0
    grad_wrt_w0=0
    grad_wrt_w=0
    for i in range(0,Xtrain.shape[0]):
        cterm=w0+np.dot(Xtrain[i],w)
        cterm2=np.exp(w0+np.dot(Xtrain[i],w))
        p_y_1=cterm2/(1+cterm2)
        grad_wrt_w0+=yTrain[i] - p_y_1 
        grad_wrt_w+=Xtrain[i]*grad_wrt_w0
        
    return (grad_wrt_w0-lamda*w0,grad_wrt_w-lamda*w)    
 
def LR_CalcGrad_L1(Xtrain,yTrain,what,lamda):
    w0=what[0]
    w=what[1:]
    obj=0
    grad_wrt_w0=0
    grad_wrt_w=0
    for i in range(0,Xtrain.shape[0]):
        cterm=w0+np.dot(Xtrain[i],w)
        cterm2=np.exp(w0+np.dot(Xtrain[i],w))
        p_y_1=cterm2/(1+cterm2)
        grad_wrt_w0+=yTrain[i] - p_y_1 
        grad_wrt_w+=Xtrain[i]*grad_wrt_w0
        
    return (grad_wrt_w0-lamda,grad_wrt_w-lamda)  
    
def LR_UpdateParams(what,grad,eta):

    w0=what[0]
    w=what[1:]
    
    grad_wrt_w=grad[1:]
    grad_wrt_w0=grad[0]
    
    w0=w0+ eta*grad_wrt_w0
    w=w+ eta*grad_wrt_w
    
    what=[w0]
    what.extend(w.tolist())
   
    
    return np.asarray(what)
    
    
def LR_GradientAscent(Xtrain,yTrain,sp):

    epocs=2000
    errorList=[]        
    objList=[]
    eta=0.01
    tolerance=0.07
    what=np.random.rand(Xtrain.shape[1]+1) #initialize random weights from uniform distribution of [0,1]
    print 'w is ',what
    lamda=2
    obj=LR_CalcObj(Xtrain,yTrain,what)
    print 'initial obj value is ',obj
    oldObj=newObj=obj
    for i in range(0,epocs):
        oldObj=newObj
        grad_wrt_w0,grad_wrt_w=LR_CalcGrad(Xtrain,yTrain,what)
        grad=[grad_wrt_w0]
        grad.extend(grad_wrt_w.tolist())
        grad=np.asarray(grad)
        #print 'grad is ',grad
        what=LR_UpdateParams(what,grad,eta)
        #print 'after updating what is ',what
        obj=LR_CalcObj(Xtrain,yTrain,what)
        
        newObj=obj
        status=check_Convergence(newObj,oldObj,tolerance)
        print 'epoch is ',i ,' old obj is ',oldObj,' newobj value is ',newObj, ' n status is ',status
        
        objList.append(obj)
        if status==True:
            break;
     
    x2=[]
    for i in range(0,len(objList)):
       x2.append(i)
    pl.figure()
    pl.plot(x2,objList,'*')
    pl.xlabel('Epocs')
    pl.ylabel('Objective Function Value')
    pl.title('Split of '+str(sp))
    pl.show()
    return what
     


def LR_GradientAscent2(Xtrain,yTrain,sp):

    epocs=100
    errorList=[]        
    objList=[]
    eta=0.01
    what=np.random.rand(Xtrain.shape[1]+1) #initialize random weights from uniform distribution of [0,1]
    print 'w is ',what
    obj=LR_CalcObj(Xtrain,yTrain,what)
    print 'initial obj value is ',obj
    for i in range(0,epocs):
        for i in range(0,Xtrain.shape[0]):
            grad_wrt_w0,grad_wrt_w=LR_CalcGrad2(Xtrain[i],yTrain[i],what)
            grad=[grad_wrt_w0]
            grad.extend(grad_wrt_w.tolist())
            grad=np.asarray(grad)
            what=LR_UpdateParams(what,grad,eta)
            obj=LR_CalcObj(Xtrain,yTrain,what)
            print 'obj value is ',obj
            objList.append(obj)
     
    x2=[]
    for i in range(0,len(objList)):
       x2.append(i)
    pl.figure()
    pl.plot(x2,objList)
    pl.xlabel('Epocs')
    pl.ylabel('Objective Function Value')
    pl.title('Split of '+str(sp))
    pl.show()

def kpi(tp,fp,fn,tn,correct):
    
    precision=float(tp)/(tp+fp)
    recall=float(tp)/(tp+fn)
    f1=float(2.0*precision*recall)/(precision+recall)
    accuracy=float(correct*100)/(tp+tn+fp+fn)
    return (precision,recall,f1,accuracy)

     
def classify(X,Y,what,threshold):
    
    tp=0
    tn=0
    fn=0
    c=0
    c2=0
    fp=0
    
    tpList=[]
    fpList=[]
    tnList=[]
    fnList=[]
    
    correct=0   
    w0=what[0]
    w=what[1:]
    for i in range(0,X.shape[0]):
        cterm=w0+np.dot(X[i],w)
        cterm2=np.exp(w0+np.dot(X[i],w))
        p_y_1=cterm2/(1+cterm2)
        label=1
        
        if p_y_1 > threshold :
            label=1
        else:
            label=0
        if label==Y[i] and label==1:
            tp+=1;
            correct+=1
        elif label==1 and Y[i]==0:
            fp+=1
        elif label==0 and Y[i]==0:
            tn+=1
            correct+=1
        elif label==0 and Y[i]==1:
            fn+=1
    
    return (tp,fp,fn,tn,correct)
   
         

def train():
    l=[0.7,0.8,0.9]
    for i in l:
        Xtrain=np.load('Train/Xtrain with sp='+str(i)+'.npy')
        yTrain=np.load('Train/Ytrain with sp='+str(i)+'.npy')
        #Xtrain=np.load('tempXtrain.npy')
        #yTrain=np.load('tempYtrain.npy')
        Xtrain=Xtrain
        yTrain=yTrain
        print 'X is ',Xtrain,' n yTrain ',yTrain
        pl.figure()
        pl.scatter(Xtrain[:, 0], Xtrain[:, 1], marker='o', c=yTrain)
        pl.show()
        what=LR_GradientAscent(Xtrain,yTrain,i)
        pl.figure()
        what2=what[1:].tolist()
        w1=max(what2)
        idx1=what2.index(w1)
        what2.remove(w1)
        
        w2=max(what2)
        idx2=what2.index(w2)
        if idx2 >= idx1:
            idx2+=1
        pl.scatter(Xtrain[:, idx1], Xtrain[:, idx2], marker='o', c=yTrain)
        x1=[-3,3]
        y1=-1*(what[0]+w1*(x1[0]))/w2
        y2=-1*(what[0]+w1*x1[1])/w2
        
        pl.plot(x1,[y1,y2])
        pl.show()
        Xtest=np.load('Test/Xtest with sp='+str(i)+'.npy')
        yTest=np.load('Test/Ytest with sp='+str(i)+'.npy')
        Xtest=Xtest
        #yTest=Ytest
        print 'now testing on the test set'
        (tp,fp,fn,tn,correct)=classify(Xtest,yTest,what,0.5)
        precision,recall,f1,accuracy=kpi(tp,fp,fn,tn,correct)  
        print 'Precision is ',precision,'\nRecall is ',recall,'\nF1 is ',f1,'\nAccuracy is ',accuracy,'%'
        print 'X.shape is ',Xtest.shape,' y is ', yTest.shape
        
def train2():
    l=[1]
    for i in l:
        
        Xtrain=np.load('tempXtrain2.npy')
        yTrain=np.load('tempYtrain2.npy')
        Xtest=np.load('tempXtest2.npy')
        yTest=np.load('tempYtest2.npy')
        
        print 'X is ',Xtrain,' n yTrain ',yTrain
        pl.figure()
        pl.scatter(Xtrain[:, 0], Xtrain[:, 1], marker='o', c=yTrain)
        pl.show()
        sizel=np.arange(400,440,40)
        
        trainError=[]
        testError=[]
        for i in range(0,sizel.shape[0]):
            X=Xtrain[0:sizel[i]]
            Y=yTrain[0:sizel[i]]
            print ' training a size of ',i
            what=LR_GradientAscent(X,Y,i)
            pl.figure()
            pl.scatter(X[:, 0], X[:, 1], marker='o', c=Y)
            x1=[-3,3]
            y1=-1*(what[0]+what[1]*(x1[0]))/what[2]
            y2=-1*(what[0]+what[1]*x1[1])/what[2]
        
            pl.plot(x1,[y1,y2])
            pl.show()
            print 'now testing on the test set '
            (tp,fp,fn,tn,correct)=classify(Xtest,yTest,what,0.5)
            precision,recall,f1,accuracy=kpi(tp,fp,fn,tn,correct)  
            print 'On Test Precision is ',precision,'\nRecall is ',recall,'\nF1 is ',f1,'\nAccuracy is ',accuracy,'%'
            testError.append(1-(accuracy/100))
            print 'now testing on the train set'
            (tp,fp,fn,tn,correct)=classify(X,Y,what,0.5)
            precision,recall,f1,accuracy=kpi(tp,fp,fn,tn,correct)  
            print 'On Train Precision is ',precision,'\nRecall is ',recall,'\nF1 is ',f1,'\nAccuracy is ',accuracy,'%'
            trainError.append(1-(accuracy/100))
            
        
        
        pl.figure()
        pl.plot(sizel,trainError,label='trainError')
        pl.legend()
        pl.plot(sizel,testError,label='testError')
        pl.legend()
        pl.title('training error vs test error')
        pl.show()
               

if __name__=='__main__':
    train2()
    
