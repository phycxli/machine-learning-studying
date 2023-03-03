import numpy as np
import TreePlot as tp

# 计算数据集的平方误差
def calcMSE(dataSet):
    means = np.mean(dataSet)
    sums = sum([(i - means) * (i - means) for i in dataSet])
    return sums


# 选择最优的划分点
def chooseBestFeatureToSplit(dataSet):
    nums = len(dataSet) - 1
    if nums == 0:
        return 0
    best = 0
    bestMES = 100000
    for i in range(nums):
        temp = calcMSE(dataSet[:i + 1]) + calcMSE(dataSet[i + 1:])
        if temp <= bestMES:
            bestMES = temp
            best = i
    return best


# 建树过程
def createTree(dataSet, datalabel, left, right):
    if right - left == 1:
        # return dataSet[left]
        return datalabel[left]
    if left >= right:
        return None
    # 最优划分函数加上left为原数据集上的最优划分下标
    bestchoose = left + chooseBestFeatureToSplit(dataSet[left:right])
    # print bestchoose+1
    mytree = {datalabel[bestchoose]: {}}
    mytree[datalabel[bestchoose]]['left'] = createTree(dataSet, datalabel, left, bestchoose)
    mytree[datalabel[bestchoose]]['right'] = createTree(dataSet, datalabel, bestchoose + 1, right)
    return mytree


dataSet = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
datalabel = [4.5, 4.75, 4.91, 5.34, 5.8, 7.05, 7.9, 8.23, 8.7, 9]

mytree = createTree(dataSet,datalabel,0,len(dataSet))
tp.createPlot(mytree)
print (mytree)