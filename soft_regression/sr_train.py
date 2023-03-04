# coding:UTF-8
import numpy as np
import os

cwd=os.getcwd()

#首先实现对于一个np.mat矩阵，不同元素值计数
def count_diff(mats):
    '''实现矩阵不同元素的计数
    input:  mats(mat)输入矩阵
    output: elements(int)不同元素的个数
    '''
    element,count=np.unique(np.array(mats.T),return_counts=True)
    return len(element)

#计算损失函数
def loss(expo,labels):
    '''计算损失函数值
    input:  expo(mat):概率exp因子
            labels(mat):标签值
    '''
    num=np.shape(expo)[0]
    loss_total=0
    for i in range(num):
        loss_total+=np.log(expo[i,labels[i,0]]/np.sum(expo[i,:]))
    return -(1/num)*loss_total

#梯度下降求解模型参数
def gradascent(features,labels,epochs,alpha):
    '''利用梯度下降法训练softmax模型
    input:  features(mat):特征
            labels(mat):标签
            epochs(int):迭代次数
            alpha(float):学习率
    output: weights(mat):权重
    '''
    num,n=np.shape(features)    #m样本个数，n特征个数
    k=count_diff(labels)        #labels里有k个类
    weights=np.mat(np.ones((n,k)))#初始权重
    i=0
    while i<=epochs:
        expo=np.exp(features*weights)
        if i%100==0:
            print("\t-----iter:",i,",loss:",loss(expo,labels))
        expo_sum=-expo.sum(axis=1)   #求和求完后变成(num,1)的列矩阵，所以需要复制k次
        expo_sum=expo_sum.repeat(k,axis=1)
        pr=expo/expo_sum
        for i in range(num):
            pr[i,labels[i,0]]=1+pr[i,labels[i,0]]
        weights=weights+(alpha/num)*features.T*pr
        i+=1
    return weights

#导入数据
def load_data(filepath):
    '''
    input:  filepath(str)训练集文件路径
    output: features(mat)特征
            labels(mat)标签
    '''
    file=open(filepath)
    features=[]
    labels=[]
    for row in file.readlines():
        features_temp=[]
        features_temp.append(1)
        row=row.strip().split('\t')
        for i in range(len(row)-1):
            features_temp.append(float(row[i]))
        labels.append(int(row[-1]))
        features.append(features_temp)
    file.close()
    return np.mat(features),np.mat(labels).T

#保存数据
def save_model(filepath,weights):
    '''保存最后的模型
    input:  filepath(str):保存的路径
            weights(mat):保存的权重
    '''
    file=open(filepath)
    n,k=np.shape(weights)
    for i in range(n):
        weights_temp=[]
        for j in range(k):
            weights_temp.append(str(weights))   #实际上这里就是单纯做了一个格式转换，把矩阵里的float转化成str，方便用open()方法存储
        file.write('\t'.join(weights_temp)+'\n')
    file.close()

#训练数据主函数
if __name__=='__main__':
    filename=os.path.join(cwd,'soft_regression\\SoftInput.txt')
    print('1.loading')
    features,labels=load_data(filename)
    print('2.training')
    weights=gradascent(features=features,labels=labels,epochs=1000,alpha=0.4)
    print('3.saving')
    save_model('model',weights=weights)


