#按照李航的教材来设定训练集
#这里我不绝不用任何包来做，一定！！！
x=[[3,3],[4,3],[1,1]]
y=[1,1,-1]
w,b=[0,0],0
lr=1
i=0
while i<len(x):
    if y[i]*(w[0]*x[i][0]+w[1]*x[i][1]+b)<=0:
        w[0]=w[0]+lr*y[i]*x[i][0]
        w[1]=w[1]+lr*y[i]*x[i][1]
        b=b+lr*y[i]
        print('误分类点为:',i+1)
        print('权重系数为:',w[0],w[1],b)
        i=0
    else:
        i+=1
print('超平面函数为:',w[0],'x[1]+',w[1],'x[2]+',b)
def perceptron(x1:float,x2:float):
    if w[0]*x1+w[1]*x2+b>0:
        return 1
    else:
        return 0
x_1=float(input('输入测试点坐标1:'))
x_2=float(input('输入测试点坐标2:'))
print('感知机结果为:',perceptron(x_1,x_2))