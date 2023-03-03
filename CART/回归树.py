import TreePlot as tp
class data_reset():
    def __init__(self) -> None:
        self.data=[[1,4.50],[2,4.75],[3,4.91],[4,5.34],[5,5.80],[6,7.05],[7,7.90],[8,8.23],[9,8.70],[10,9.00]]
        self.x=[example[0] for example in self.data]
        self.y=[example[-1] for example in self.data]
    def reset(self):
        return self.data
class regression_tree():
    def __init__(self) -> None:
        pass
    def loss(self,split,data):
        '''计算切分点s对应的二乘法损失值'''
        #data_x=[example[0] for example in data]
        data_y=[example[-1] for example in data]
        avr1=sum(data_y[:split+1])/len(data_y[:split+1])
        avr2=sum(data_y[split+1:])/len(data_y[split+1:])
        sum1,sum2=0,0
        for i in range(split+1):
            sum1+=(data_y[i]-avr1)**2
        for i in range(split+1,len(data_y)):
            sum2+=(data_y[i]-avr2)**2
        return sum1+sum2
    def find_min_split(self,data):
        '''寻找最小二乘法切分点'''
        result=[]
        for s in range(len(data)-1):
            result.append(self.loss(split=s,data=data))
        min_result=min(result)
        return result.index(min_result)
    def creat_tree(self,data,left,right):
        '''创建回归树'''
        data_y=[example[-1] for example in data]
        if right-left==1:
            return data_y[left]
        if left>=right:
            return None
        split=left+self.find_min_split(data[left:right])
        reg_tree={data_y[split]:{}}
        reg_tree[data_y[split]]['Less']=self.creat_tree(data,left,split+1)
        reg_tree[data_y[split]]['Greater']=self.creat_tree(data,split+1,right)
        return reg_tree


if __name__=='__main__':
    reset=data_reset()
    data=reset.reset()
    tree=regression_tree()
    tp.createPlot(tree.creat_tree(data,0,len(data)))
    print(tree.creat_tree(data,0,len(data)))