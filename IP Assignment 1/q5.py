def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f

def sin(x):
    x=3.14*x/180
    sine=0
    n=0
    for i in range(1,101,2):
        sine+=(((-1)**n)*(x**i))/fact(i)
        n+=1
    return sine

def cos(x):
    x=3.14*x/180
    cosine=0
    n=0
    for i in range(0,101,2):
        cosine+=(((-1)**n)*(x**i))/fact(i)
        n+=1
    return cosine

def tan(x):
    tangent=sin(x)/cos(x)
    return tangent

angle=float(input("Enter angle: "))
base=float(input("Enter base distance: "))
print("Height of pole: ",round(tan(angle)*base))
print("Distance from person to top of pole: ",round(base/cos(angle),2))
