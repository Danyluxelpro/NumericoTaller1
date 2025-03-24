import math

def fun(y):
    y=y-(y*math.exp(y)-1)*0.4043537
    return y

def fun1(y):
    
    return y
a=0.399
i=0
while a<=0.7:
    y=0.5
    while i<10000000:
        z=y
        y=y-(y*math.exp(y)-1)*a
        if abs(y-z)<0.00000001:
            print(i)
            print(y)
            i=1000000000000
        
        i+=1
    print(a)
    a+=0.1
    i=0
    
