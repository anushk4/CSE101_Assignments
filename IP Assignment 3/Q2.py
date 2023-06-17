def opt1(d):
    f=open("record.txt","w")
    stu_name=input("Enter student name: ")
    f.write("Record for "+stu_name+"\n")
    for i in d[stu_name]:
        f.writelines([i[0]," ",i[1]," ",i[2],"\n"])
    f.close()
    print("Written")
    cur_time="".join(input("Enter current time: ").split(":"))
    for i in range(len(d[stu_name])):
        j="".join(d[stu_name][i][2].split(":"))
        if j==cur_time:
            if d[stu_name][i][0]=="ENTER":
                print("On campus")
            else:
                print("Off campus")
            break
        if j>cur_time:
            if d[stu_name][i-1][0]=="ENTER":
                print("On campus")
            else:
                print("Off campus")
            break

def opt2(d):
    f=open("time interval.txt","w")
    initial="".join(input("Enter starting time: ").split(":"))
    final="".join(input("Enter ending time: ").split(":"))
    l=[]
    for i in d:
        for j in d[i]:
            k="".join(j[2].split(":"))
            if k>=initial and k<=final:
                l.append([j[2],j[1],j[0],i])
    l.sort()
    for i in l:
        for j in reversed(i):
            print(j,end="  ")
        f.writelines([i[3],", ",i[2],", ",i[1],", ",i[0],"\n"])
        print()

def opt3(d):
    enter=0
    exit=0
    gate=input("Enter gate number: ")
    for i in d:
        for j in d[i]:
            if j[1]==gate:
                if j[0]=="ENTER":
                    enter+=1
                elif j[0]=="EXIT":
                    exit+=1
    return gate,enter,exit

f1=open("sorted_data.txt","r")
x=f1.readline()
d={}
while True:
    l=f1.readline().split(",")
    if "" in l:
        break
    for i in range(len(l)):
        l[i]=l[i].lstrip(" ")
        l[i]=l[i].rstrip("\n")
    if l[0] not in d:
        d[l[0]]=[]
    if l[1]=="ENTER":
        try:
            if d[l[0]][-1][0]=="ENTER":
                continue
        except:
            pass
        d[l[0]].append([l[1],l[2],l[3]])
    if l[1]=="EXIT":
        try:
            if d[l[0]][-1][0]=="EXIT":
                temp=d[l[0]].pop()
        except:
            pass
        d[l[0]].append([l[1],l[2],l[3]])
print("1. Show the record of moving in and out and current status")
print("2. Record of everyone entering and exiting within a given timeframe")
print("3. No of times a gate is used for entering and exiting")
ch="y"
while ch=="y":
    opt=int(input("Enter option: "))
    if opt==1:
        opt1(d)
    elif opt==2:
        opt2(d)
    elif opt==3:
        gate,enter,exit=opt3(d)
        print("No of times gate",gate,"used for entry:",enter)
        print("No of times gate",gate,"used for exit:",exit)
    else:
        print("Enter a valid option")
        continue
    ch=input("Do you want to do it again?(y/n)").lower()