import sklearn.datasets as datasets
import numpy as np
from sklearn.linear_model import LogisticRegression as LR

digits = datasets.load_breast_cancer()
x_s = digits.data
y_s = digits.target 
num=len(y_s)
x=x_s[:int(0.8*num)]
y=y_s[:int(0.8*num)]

L=0.1
eps=0.001

w=np.array([0 for example in range(len(x[0]))])
b=0

def normalize(x):
    return (x-np.min(x))/(np.max(x)-np.min(x))

def loss(w,b):
    sum=0
    for i in range(len(x)):
        sum+=y[i]*(np.dot(w,x[i])+b)-np.log(1+np.exp(np.dot(w,x[i])+b))
    return sum

def loss_grad1(w,b):
    sum=np.array([0 for example in range(len(x[0]))])
    for i in range(len(x)):
        sum=sum+(y[i]-np.exp(np.dot(w,x[i])+b)/(1+np.exp(np.dot(w,x[i])+b)))*x[i]
    return sum
def loss_grad2(w,b):
    sum=0
    for i in range(len(x)):
        sum=sum+(y[i]-np.exp(np.dot(w,x[i])+b)/(1+np.exp(np.dot(w,x[i])+b)))
    return sum

w1=w+L*loss_grad1(w,b)
b1=b+L*loss_grad2(w,b)
while np.abs(loss(w1,b1)-loss(w,b))>eps:
    w,b=w1,b1
    w1=w+L*loss_grad1(w,b)
    b1=b+L*loss_grad2(w,b)
    print(w,'\t',b,'\t',np.abs(loss(w1,b1)-loss(w,b))) 

#print(w,b)
