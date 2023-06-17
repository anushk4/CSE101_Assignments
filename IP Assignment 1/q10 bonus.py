def polynomial(x,dx,y):
    x=x+dx
    f=eval(y)
    return f

def slope(x,y):
    s=(polynomial(x,0.1,y)-polynomial(x,0,y))/0.1
    return s    

def slopeeq(x,y):
    x_f=(-polynomial(x,0,y)/slope(x,y))+x
    return x_f


x1=float(input("Enter range: "))
x2=float(input("Enter range: "))
x=x1
y=input("Enter equation: ")
if "^" in y:
    y=y.replace("^","**")
roots=[]
i=0
while x<=x2:
    if len(roots)==int(y[(y.index("x")+3)]):
        break
    if abs(polynomial(x,0,y))<=0.2:
        if round(x,1) not in roots:
            roots.append(round(x,1))
            x=x2
    else:
        x=slopeeq(x,y)
    i+=1
    if i>=100:
        break
j=0
if roots==[]:
        print("No roots found")
else:
    for r in roots:
        print("Root: ",r)