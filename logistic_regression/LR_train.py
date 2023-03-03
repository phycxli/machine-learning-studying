# coding:UTF-8
import numpy as np
def sig(x):
    '''sigmoid函数
    '''
    return 1/(1+np.exp(-x))

#损失函数
def loss(h,label):
    '''计算当前损失函数值
    input:  h(mat):预测值
            label(mat):实际值
    output: loss/m(float):损失率
    '''
    num=np.shape(h)[0]  #num表示样本数量(x_i,y_i)，i=1,2,..,num的个数
    sum_loss=0.0
    for i in range(num):
        if h[i,0]>0 and (1-h[i,0])>0:
            sum_loss=sum_loss-(label[i,0]*np.log(h[i,0])+(1-label[i,0])*np.log(1-h[i,0]))
        else:
            sum_loss=sum_loss-0
        return sum_loss/num
    
#梯度下降
def lr_train(feature,label,epoch,alpha):
    '''利用梯度下降法训练LR模型
    input:  feature(mat)特征
            label(mat)标签
            epoch(int)最大迭代次数
            alpha(float)学习率
    '''
    n=np.shape(feature)[1]  #特征个数
    w=np.mat(np.ones((n,1)))#初始化权重 np.ones(m,n)表示建立m×n的向量，np.mat表示矩阵化
    i=0
    while i<=epoch:
        i+=1
        h=sig(feature*w)
        err=label-h #表示标签y_i与lr模型值的差，可以理解成误差
        if i%100==0:
            print("\t---------iter="+str(i)+", train error rate="+str(loss(h,label)))
        w = w + alpha * feature.T * err
    return w

def load_data(file_name):
    '''
    input:  file_name(str)训练数据的路径地址
    output: features(mat)特征
            labels(mat)标签
    '''
    file=open(file_name)
    features=[]
    labels=[]
    for row in file.readlines():
        features_temp=[]
        labels_temp=[]
        rows=row.strip().split('\t')
        features_temp.append(1)
        for i in range(len(rows)-1):
            features_temp.append(float(rows[i]))
        labels_temp.append(float(rows[-1]))
        features.append(features_temp)
        labels.append(labels_temp)
    file.close()
    return np.mat(features),np.mat(labels)

def save_model(file_name,w):
    '''保存模型参数
    input:  file_name(string)文件名
            w(mat)LR模型的权重参数
    '''
    num=np.shape(w)[0]  #样本数量
    file_w=open(file_name,'w')
    w_array=[]
    for i in range(num):
        w_array.append(str(w[i,0]))
    file_w.write('\t'.join(w_array))
    file_w.close()

if __name__=='__main__':
    print('loading data')
    feature,label=load_data('./logistic_regression/data.txt')
    print('training')
    w=lr_train(feature=feature,label=label,epoch=1000,alpha=0.01)
    print('saving model')
    save_model('model',w)

