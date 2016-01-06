import numpy as np
import csv
from sklearn.feature_extraction import DictVectorizer
import json

dictList=[]
order=[]

dictList2=[]

#for pdays remember to remove the 99 thing
numerics=['age','duration','campaign','pdays','previous']
categoricalColumns=['job','marital','education','default','housing','loan','contact','month','day_of_week']
v=DictVectorizer(sparse=False,sort=False)
def saveFile(name,dataset):
    np.save(name,dataset)

def saveDict(name,dataset):
    with open(name,'w') as file1:
        json.dump(dataset,file1)
    
def prepare(name):
    i=1
    labels=[]
    with open(name,'r') as file1:
        data=csv.reader(file1)
        for line in data:
            
            
            print 'processing ',i
            if i==1:
                #print '\n\nline1 is ',line,' n i= ',i,'\n'
                for word in line[0:-1]:
                    order.append(word)
                    
                i=i+1
                
            else:
                d={}
                d2={}
                #print '\n\nline1 is ',line,' n i= ',i,'\n'
                for j in range(0,len(order)):
                    try:
                        d[order[j]]=float(line[j])
                        
                    except:
                        d[order[j]]=line[j]
                        
                    try:
                        if(order[j]!='duration'):
                            d2[order[j]]=float(line[j])
                        
                    except:
                        if(order[j]!='duration'):
                            d2[order[j]]=line[j]      
                     
                
                if(line[-1]=='no'):
                    labels.append(0)
                else:
                    labels.append(1)  
                
                dictList.append(d)   
                dictList2.append(d2)  
                #print 'order is ',order,' n len is ',len(order)
               # print 'd is ',d,' and label is ',labels 
                i=i+1        
                    
                    
    print '\nthe length is dictList is ',len(dictList),' & 2 is ',len(dictList2),' and of labels is ',len(labels),'\n'   
    print '\n\n\n the order for 1  is ',dictList[0],' \n and for 2 is ',dictList2[0],'\n\n'    
    saveDict('FullDictionary.txt',dictList)
    saveDict('DurationRemoved.txt',dictList2)
    data=v.fit_transform(dictList) 
    labels=np.asarray(labels)        
    data2=v.fit_transform(dictList2)
    saveFile("FullData",data)
    saveFile("Without Duration Field",data2)
    saveFile("allLabels",labels)
    print '\nthe length is data is ',data.shape,' & data2 is ',data2.shape,' and of labels is ',labels.shape,'\n'               
            

if __name__=='__main__':
    #prepare('bank-additional/bank-additional-full.csv')
    prepare('bank-additional/temp.csv')
            
                
    
