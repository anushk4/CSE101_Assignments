from math import log as l

def f(t):
    f=2000*l(140000/(140000-2100*t))-9.8*t
    return f

a=float(input("a: "))
b=float(input("b: "))
dx=0.25

#f(t)=velocity=dx/dt
#dx=f(t)*dt
#integrating both sides we get the distance

d=0
i=a
while i<=b-dx:
    #d+=dx*f(i)  #integration through adding areas
    d+=((f(i)+f(i+dx))/2)*dx   #integration through the given hint
    i+=dx

print("Distance covered by the rocket: ",d)