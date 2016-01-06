from sklearn.datasets import make_blobs, make_classification,make_gaussian_quantiles
import matplotlib.pyplot as plt
import numpy as np
import sklearn.preprocessing as p

def saveFile(name,dataset):
    np.save(name,dataset)
    


#X1,Y1=make_blobs(n_samples=100, n_features=2, centers=2)
X1,Y1=make_gaussian_quantiles(n_samples=500,n_features=2, n_classes=2)
plt.figure()
plt.subplot(1,2,1)
plt.scatter(X1[:, 0], X1[:, 1], marker='o', c=Y1)
print 'X.shape is ',X1.shape,' y is ', Y1

plt.subplot(1,2,2)

scalar=p.StandardScaler().fit(X1)
X1=scalar.fit_transform(X1)
plt.scatter(X1[:, 0], X1[:, 1], marker='o', c=Y1)
plt.show()

sp=int(0.8*X1.shape[0])
X1train=X1[0:sp]
Y1train=Y1[0:sp]

X1test=X1[sp:]
Y1test=Y1[sp:]
saveFile("tempXtrain2",X1train)
saveFile("tempYtrain2",Y1train)
saveFile("tempXtest2",X1test)
saveFile("tempYtest2",Y1test)


