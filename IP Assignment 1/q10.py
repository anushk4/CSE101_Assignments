def polynomial(x):
    f=x**3 - 10.5*x**2 + 34.5*x - 35
    return f

def slope(x):
    df=3*x**2-21*x+34.5
    return df

def slopeeq(x1):
    x=(-polynomial(x1)/slope(x1))+x1
    return x

x0=float(input("Enter initial root: "))
i=0
while True:
    if abs(polynomial(x0))<=0.2:
        print(round(x0,1))
        break
    else:
        x0=slopeeq(x0)
    i+=1   
    if i>=100:
        print("No solution possible")
        break