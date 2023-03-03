#李航给的信贷情况训练集
import math
import TreePlot as tp
class reset():
    def creat_database(self):
        data=[
            ['青年','否','否','一般','否'],
            ['青年','否','否','好','否'],
            ['青年','是','否','好','是'],
            ['青年','是','是','一般','是'],
            ['青年','否','否','一般','否'],
            ['中年','否','否','一般','否'],
            ['中年','否','否','好','否'],
            ['中年','是','是','好','是'],
            ['中年','否','是','非常好','是'],
            ['中年','否','是','非常好','是'],
            ['老年','否','是','非常好','是'],
            ['老年','否','是','好','是'],
            ['老年','是','否','好','是'],
            ['老年','是','否','非常好','是'],
            ['老年','否','否','一般','否']
            ]
        features=['年龄','有工作','有自己的房子','信贷情况']
        return (data,features)

class tree():
    '树的主体'
    def __init__(self):
        pass

    def most_class(self,c): 
        '给定一个列表，寻找重复次数最多的元素，并输出该元素'
        count={}
        for word in c:
            if word not in count.keys():
                count[word]=0
            count[word]+=1
        sorted_count=sorted(count.items(),key=lambda x:x[1],reverse=True)
        return sorted_count[0][0]
    
    def entropy(self,data):
        y_class=[example[-1] for example in data]   #y标签列表
        y_class_sets=set(y_class)                   #y标签的不同类的个数，也就是K
        y_class_nums=[]                             #用来计数不同类的重复次数
        for word in y_class_sets:
            y_class_nums.append(y_class.count(word))
        pr_list=[y_class_nums_element/len(y_class) for y_class_nums_element in y_class_nums]#最似然估计计算经验概率
        entropy_tot=0
        for p in pr_list:
            entropy_tot+=-p*math.log(p,2)
        return entropy_tot

    def entropy_A(self,list:list):
        list_set=set(list)
        list_element_num=[]
        for element in list_set:
            list_element_num.append(list.count(element))
        pr_list=[num/len(list) for num in list_element_num]
        entropy_A=0
        for p in pr_list:
            entropy_A+=-p*math.log(p,2)
        return entropy_A

    def choose_features(self,data:list):
        entropy_D=self.entropy(data)
        gain=[]
        for i in range(len(data[0])-1):
            feature_value_list=[element[i] for element in data]
            entropy_A=self.entropy_A(feature_value_list)
            unique=set(feature_value_list)
            sum=0
            for word in unique:
                sum+=feature_value_list.count(word)/len(feature_value_list) * self.entropy(self.split_data(data,i,word))
            gain.append((entropy_D-sum)/entropy_A)
        gain_max=max(gain)
        return gain.index(gain_max)

    def split_data(self,data,feature_index,feature_value):
        result=[]
        for vec in data:
            if vec[feature_index]==feature_value:
                newvec=vec[:feature_index]
                newvec1=vec[feature_index+1:]
                result.append(newvec+newvec1)
        return result
    def creat_tree(self,data,features):
        '创建决策树'
        y_class=[example[-1] for example in data]   #设定输出y值
        if y_class.count(y_class[0])==len(y_class): #给出两个结束递归的条件
            return y_class[0]
        if len(data[0])==1:
            return self.most_class(y_class)
        best_feature_index=self.choose_features(data)
        best_feature=features[best_feature_index]
        decide_tree={best_feature:{}}
        del(features[best_feature_index])
        feature_value=[example[best_feature_index] for example in data]
        unique_feature=set(feature_value)
        
        for values in unique_feature:
            features_next=features[:]
            decide_tree[best_feature][values]=self.creat_tree(self.split_data(data,best_feature_index,values),features_next)
        return decide_tree

if __name__=='__main__':
    new=reset()
    data,features=new.creat_database()
    newtree=tree()
    mytree=newtree.creat_tree(data,features)
    print(mytree)
    tp.createPlot(mytree)