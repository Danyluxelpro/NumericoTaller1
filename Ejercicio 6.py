x=0.0001 
i=0
def f(x): 
    x=x-(x**3)*0.5 
    return x
while i<100000000:
     x=f(x) 
     i+=1
print(x)