import os
import re
from os.path import expanduser
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer


stop=stopwords.words('english')
stemmer=PorterStemmer()
lemmer=WordNetLemmatizer()
home=expanduser("~")

nonWords=['[',']','{','}','/','_','|']

f=open("SMSSpamCollection",'r')
f2=open("spamFileCleaned.txt",'w')

def preProcess(source,destination):
    f=open(source,'r')
    f2=open(destination,'w')
    j=1
    for line in f:
        #words=line.split(' ')
        
        print 'line is ',line ,' at j = ',j
        j=j+1
        line=line.lower()
        line=line.strip()
        
        cleaned1=re.sub(r'[,.!?&$@%/\\"-;:()+*^`<>#`~=]',"",line)
        cleaned2=re.sub(r'\d',"",cleaned1)
        cleaned2=re.sub(r"'s","",cleaned2)
        cleaned2=re.sub(r"'","",cleaned2)
        cleaned2=re.sub(r'"',"",cleaned2)
        
        for ch in nonWords:
            try:
                cleaned2=cleaned2.replace(ch,'')
            except:
                pass
        words=nltk.word_tokenize(cleaned2)
        tags=nltk.pos_tag(words)
        sentence=""
        sentence+=words[0]+" "
        for i in range(1,len(tags)):
            tag=tags[i]
            #print 'tag is ',tag
            try:
                if tag[1][0].lower() in ['a','v','n','s','r']:
                    word=lemmer.lemmatize(tag[0],tag[1][0].lower())
                else:
                    word=lemmer.lemmatize(tag[0])
                sentence+=word+" "
            except Exception:
                pass
            
            
        #print 'the lemmatized sentence is ',sentence
        for stopWord in stop:
            try:
                cleaned2=sentence.replace(stopWord,"")
            except Exception:
                pass
            
        cleaned2.strip()
        f2.write(cleaned2+'\n')
        


if __name__=='__main__':
    preProcess('SMSSpamCollection','SMSSpamCollection.txt')
    #preProcess('text2.txt','text3.txt')
