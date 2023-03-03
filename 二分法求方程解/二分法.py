def func(x):
    return x**2-2*x+1/2
def binary_solve(a,b,eps):
    left=a
    right=b
    if func(left)>=0 and func(right)<0:
        while right-left>eps:
            mid=(left+right)/2
            if func(mid)>0:
                left=mid
            else:
                right=mid
    else:
        while right-left>eps:
            mid=(left+right)/2
            if func(mid)<0:
                left=mid
            else:
                right=mid
    return mid

print(binary_solve(0,1,0.001))