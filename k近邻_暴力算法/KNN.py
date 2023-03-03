#为了方便，这里我掉包numpy和matplotlib
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
#设定训练集
np.random.seed(40)
train=np.random.rand(10,2)*10
trainout=np.sign(np.random.normal(0,1,10))
#设定测试输入点
x=np.array([[4,5]])
X=np.concatenate([train,x],axis=0)
dist_sq=np.sum((X[:,np.newaxis,:]-X[np.newaxis,:,:])**2,axis=-1)
nearest=np.argsort(dist_sq,axis=1)
#若是最近邻算法k=1
out=trainout[nearest[-1,1]]
#若是k近邻算法k=4
k=4
result=[]
for i in range(1,k+1):
    result.append(trainout[nearest[-1,i]])
out=Counter(result)
print(out)