from math import sqrt as s
dist=0
x0=5.0
y0=5.0
x_f,y_f=x0,y0
while True:
    x=float(input())
    if x<=0:
        break
    elif x<=25:
        dist+=x
        y_f+=x
    elif x<=50:
        dist+=x
        y_f-=x
    elif x<=75:
        dist+=x
        x_f+=x
    elif x>=76:
        dist+=x
        x_f-=x
print("Final Coordinate: ("+str(x_f)+","+str(y_f)+")")
print("Total distance travelled: ",dist)
print("Total displacement: ",s((x_f-x0)**2+(y_f-y0)**2))