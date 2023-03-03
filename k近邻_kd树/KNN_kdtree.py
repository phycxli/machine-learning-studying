'''Author: Chengxi Li'''
from math import sqrt
class node():
    '''
    用来存储结点数据，结点数据包含左右子树和结点值、划分维度
    '''
    def __init__(self,lchild=None,rchild=None,value=None,layer=None):
        self.lchild=lchild
        self.rchild=rchild
        self.value=value
        self.layer=layer

class kdtree():
    def __init__(self,data):
        self.data=data
        self.nn_dist=float('inf')
        self.nn_point=None
    def split_dim(self,layer):
        '''第layer层的切分轴方向'''
        return layer%len(self.data[0])
    def mid(self,tree_data,layer):
        '''当前数据对应切分维的中位数'''
        tree_data=sorted(tree_data,key=lambda x:x[self.split_dim(layer)])
        mid_num=int(len(tree_data)/2)
        return tree_data[mid_num]
    def get_left_data(self,tree_data,layer):
        '''获取左子树数据，切片'''
        tree_data=sorted(tree_data,key=lambda x:x[self.split_dim(layer)])
        mid_num=int(len(tree_data)/2)
        return tree_data[:mid_num]
    def get_right_data(self,tree_data,layer):
        '''获取右子树数据，切片'''
        tree_data=sorted(tree_data,key=lambda x:x[self.split_dim(layer)])
        mid_num=int(len(tree_data)/2)
        return tree_data[mid_num+1:]
    def creat_kdtree(self,tree_data,layer=1):
        '''创造kd树，递归'''
        if len(tree_data)==0:
            return None
        else:
            now_data=self.mid(tree_data,layer)
            left=self.creat_kdtree(self.get_left_data(tree_data,layer),layer+1)
            right=self.creat_kdtree(self.get_right_data(tree_data,layer),layer+1)
            return node(lchild=left,rchild=right,value=now_data,layer=layer)
    def ecd_dist(self,x1:list,x2:list):
        '''计算欧氏距离'''
        sum=0
        for i in range(len(x1)):
            sum+=(x1[i]-x2[i])**2
        return sqrt(sum)
    def visit_node(self,node:node,target):
        '''访问目标点所在的叶结点'''
        if node is None:
            return None
        dist=node.value[self.split_dim(node.layer)]-target[self.split_dim(node.layer)]
        if dist>0:
            self.visit_node(node.lchild,target)
        else:
            self.visit_node(node.rchild,target)
        ecd=self.ecd_dist(node.value,target)
        if ecd <self.nn_dist:
            self.nn_dist=ecd
            self.nn_point=node
        if self.nn_dist>abs(dist):
            if dist>0:
                self.visit_node(node.rchild,target)
            else:
                self.visit_node(node.lchild,target)
    def get_nn(self,root,target):
        self.visit_node(root,target)
        return self.nn_point.value,self.nn_dist
if __name__=='__main__':
    data=[[1,3],[4,7],[2,9]]
    kd=kdtree(data)
    root=kd.creat_kdtree(data,0)
    nnp,nnd=kd.get_nn(root,[4,6])
    print(nnp,nnd)
    #print(root.value)