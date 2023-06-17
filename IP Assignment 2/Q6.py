f1=open("IPMarks.txt","r")
f2=open("IPgrades.txt","w")
wts=[(10,5),(20,15),(40,25),(10,5),(20,15),(40,35)]
normal=[]
d_grade={80:"A",70:"A-",60:"B",50:"B-",40:"C",35:"C-",30:"D"}
grade=None
y=f1.readlines()
f1.seek(0,0)
for i in range(len(y)):
    k=0
    sum1=0
    x=list(map(float,f1.readline().split(",")))
    for j in x[1:]:
        sum1+=(wts[k][1]/wts[k][0])*j
        k+=1
    for j in d_grade:
        if sum1>=j:
            grade=d_grade[j]
            break
    else:
        if sum1<30:
            grade="F"
    sum1="% .4f" % sum1
    normal.append([str(int((x[0])))+", "+str(sum1)+", "+grade])
f1.close()
f2.writelines(["R_no, total_marks, grade","\n"])
for i in normal:
    f2.writelines(i)
    f2.writelines(["\n"])
print("Grades written")
f2.close()