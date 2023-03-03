import numpy as np
def func(x,y):
    return x**2+y**2

def gradf(x,y):
    return np.array([2*x,2*y])

def Hessian(x,y):
    return np.array([[2,0],[0,2]])

def newton_solution(eps):
    x=np.array([1,1])
    x1=x-np.dot(np.linalg.inv(Hessian(x[0],x[1])),gradf(x[0],x[1]))
    while (gradf(x[0],x[1])[0])**2+(gradf(x[0],x[1])[1])**2>=eps**2:
        x=x1
        x1=x-np.dot(np.linalg.inv(Hessian(x[0],x[1])),gradf(x[0],x[1]))
    return x

print(newton_solution(0.0001))
