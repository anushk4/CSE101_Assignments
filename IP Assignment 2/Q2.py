def sgpafunc(l,total):
    sum1=0
    for i in l:
        print(i[0],": ",i[2],sep="")
        sum1+=int(i[1])*d_grade[i[2]]
    return sum1/total

def checkname(t):
    f=False
    c=-1
    if t[0].isalpha():
        cp="digit"
    else:
        return False
    for i in t:
        if i.islower():
            return False
        if i.isalpha() and cp=="digit":
            c+=1
            cp="alphabet"
        elif i.isdigit() and cp=="alphabet":
            c+=1
            cp="digit"
        elif i.isalnum()==0:
            c+=1
    if c==1:
        f=True
    return f

def checkcredit(t):
    f=False
    if t in ["1","2","4"]:
        f=True
    return f

def checkgrade(t,d):
    f=False
    if t in list(d.keys()):
        f=True
    return f

d_grade={"A+":10,"A":10,"A-":9,"B":8,"B-":7,"C":6,"C-":5,"D":4,"F":2}
l=[]
total=0
f=True
while True:
    f=True
    x=tuple(input("Enter course name, course credits and grade: ").split())
    if len(x)!=3 and len(x)!=0:
        print("Values missing/overflow")
        continue
    if x==():
        break
    if checkname(x[0])==0:
        print("Improper course no")
        f=False
    if checkcredit(x[1])==0:
        print("Incorrect credit")
        f=False
    if checkgrade(x[2],d_grade)==0:
        print("Incorrect grade")
        f=False
    if f==True:
        l.append(x)
        total+=int(x[1])
    else:
        continue
l.sort()
sgpa=sgpafunc(l,total)
print("SGPA: %.2f"%sgpa)