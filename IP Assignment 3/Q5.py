import time

def grade(d,pol,cutoffs):
    for i in pol:
        s=[]
        for j in d:
            if d[j]["Total"]>pol[i]-2 and d[j]["Total"]<pol[i]+2: #+/-2 policy
                s.append(d[j]["Total"])
        if s==[]: #if no marks in the above range
            cutoff=pol[i]
        else:
            s.sort()
            diff=0
            cutoff=0
            for i in range(len(s)-1):
                if s[i+1]-s[i]>diff: #midpoint of consecutive values with max difference
                    diff=s[i+1]-s[i]
                    cutoff=(s[i+1]+s[i])/2
        cutoffs.append((i,cutoff))
        for j in d:
            if d[j]["Total"]>=cutoff:
                d[j]["Grade"]=i

def summary(dict,n,c,assess,l):
    print(f"Course name: {n}\nCredits: {c}")
    for i in assess:
        print(i[0],i[1],sep=" : ")
    print("Cutoffs: ")
    for i in l:
        print(i[0],i[1],sep=" : ")
    print()
    a=0
    b=0
    c=0
    d=0
    f=0
    for i in dict:
        if dict[i]["Grade"]=="A":
            a+=1
        elif dict[i]["Grade"]=="B":
            b+=1
        elif dict[i]["Grade"]=="C":
            c+=1
        elif dict[i]["Grade"]=="D":
            d+=1
        elif dict[i]["Grade"]=="F":
            f+=1
    print(f"A: {a}\nB: {b}\nC: {c}\nD: {d}\nF: {f}")

policy={"F":0,"D":40,"C":50,"B":65,"A":80}
f=open("marks.txt","r") #assuming that marks are normalised according to weightage
rec=f.readlines()
name=input("Enter course name: ")
l1=input("Enter assessments: ").split()
l2=input("Enter weightage of each: ").split()
cred=int(input("Enter credits: "))
assess=zip(l1,l2)
stu={}
for i in rec:
    i=list(map(int,i.split(",")))
    total=sum(i[1:])
    stu[i[0]]={}
    stu[i[0]]["Labs"]=i[1]
    stu[i[0]]["Midsem"]=i[2]
    stu[i[0]]["Assignments"]=i[3]
    stu[i[0]]["Endsem"]=i[4]
    stu[i[0]]["Total"]=total
    stu[i[0]]["Grade"]=None
f.close()
cutoffs=[]
# N=1000
# initial=time.time()
grade(stu,policy,cutoffs)
# final=time.time()
# timetaken=final-initial
# print(timetaken)
cutoffs=cutoffs[::-1]
print("1. Generate summary\n2. Print grades for all\n3. Search")
while True:
    opt=input("Enter option: ")
    if opt=="":
        break
    opt=int(opt)
    if opt==1:
        summary(stu,name,cred,assess,cutoffs)
    elif opt==2:
        f1=open("Grade.txt","w")
        for i in stu:
            print(i,stu[i]["Total"],stu[i]["Grade"],sep="  ")
            f1.writelines([str(i),", ",str(stu[i]["Total"]),", ",str(stu[i]["Grade"]),"\n"])
        f1.close()
        print("File written")
    elif opt==3:
        # initial=time.time()
        stu_roll=int(input("Enter roll no: "))
        for i in stu[stu_roll]:
            print(i,stu[stu_roll][i],sep=": ")
        # l=[1001,1002,1003,1004,1005]
        # for i in l:
        #     print(i,stu[i],sep=": ")
        # final=time.time()
        # print(final-initial)
    else:
        print("Enter valid option")
        continue