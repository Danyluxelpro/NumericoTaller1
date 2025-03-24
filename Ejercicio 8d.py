import numpy as np
x=np.matrix('-200000000000 -200000000')

def func(x):
    y=[x.item(1)-x.item(0)**2+2,(x.item(0)/4)**2+(x.item(1)/2)**2-1]
    return y
def funny(x):

    A=np.matrix([[-2*x.item(0), 1] , [x.item(0)/8, x.item(1)/2]])
    y=np.linalg.norm(np.dot(A.I,func(x)))
    x=x-np.dot(A.I,func(x))
    
    return x,y
i=0
while i<1000:
   
    x,y=funny(x)
    if y<0.00000001:
        print(x)
        print(i)
        exit()
    i+=1
    
print(x)