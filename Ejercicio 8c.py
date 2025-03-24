import math
x=0.1
def fun(x):
    x=x*(2+(2*x*math.log(x))/(1-2*x))
    return x
i=1
while i<100000:
    x=fun(x)
    if i<=8:
        print(x)
    i+=1

print(x)