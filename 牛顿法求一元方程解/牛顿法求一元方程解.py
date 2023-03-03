def func(x):
    return x**2-2*x+1/2

def gradf(x):
    return 2*x-2

def newton_solve(eps):
    x=0.9
    x1=x-func(x)/gradf(x)
    while abs(x1-x)>eps:
        x=x1
        x1=x-func(x)/gradf(x)
    return x
print(newton_solve(0.0001))