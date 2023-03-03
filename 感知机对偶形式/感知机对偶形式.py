#按照李航的教材来设定训练集
#这里我不绝不用任何包来做，一定！！！
x=[[3,3],[4,3],[1,1]]
y=[1,1,-1]
w,b=[0,0],0
a=[0,0,0]
lr=1
i=0
def inner(x:list,y:list):
    sum=0
    for i in range(len(x)):
        sum+=x[i]*y[i]
    return sum

gram=[[0]*3 for i in range(3)]
for i in range(len(gram)):
    for j in range(len(gram)):
        gram[i][j]=inner(x[i],x[j])
print('Gram矩阵为:',gram)

while i<len(x):
    sum=0
    for j in range(len(x)):
        sum+=a[j]*y[j]*gram[j][i]
    if y[i]*(sum+b)<=0:
        a[i]=a[i]+lr
        b=b+lr*y[i]
        print(a[0],a[1],a[2],b)
        i=0
    else:
        i+=1
for i in range(len(x)):
    w[0]+=a[i]*y[i]*x[i][0]
    w[1]+=a[i]*y[i]*x[i][1]
print('超平面系数为:',w[0],w[1],b)
def perceptron(x1,x2):
    if w[0]*x1+w[1]*x2+b>0:
        return 1
    else:
        return 0
x_1=float(input('输入测试点坐标1:'))
x_2=float(input('输入测试点坐标2:'))
print('感知机结果为:',perceptron(x_1,x_2))