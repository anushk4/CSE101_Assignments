import random

def totalwords(s):
    sl=""
    i=0
    while i<len(s):
        if s[i]=="\n":
            sl+=" "
        if s[i].isalnum() or s[i]==" ":
            sl+=s[i]
        i+=1
    sl=sl.lower().split()
    for i in range(len(sl)):
        sl[i]=sl[i].strip()
    return len(sl)

def f1(s):
    sl=""
    i=0
    while i<len(s):
        if s[i]=="\n":
            sl+=" "
        if s[i].isalnum() or s[i]==" ":
            sl+=s[i]
        i+=1
    sl=sl.lower().split()
    for i in range(len(sl)):
        sl[i]=sl[i].strip()
    return len(set(sl))/len(sl),sl

def f2(s):
    sl=""
    i=0
    while i<len(s):
        if s[i]=="\n":
            sl+=" "
        if s[i].isalnum() or s[i]==" ":
            sl+=s[i]
        i+=1
    sl=sl.lower().split()
    d={}
    for i in sl:
        d[i]=sl.count(i)
    l=sorted(list(d.values()),reverse=True)[:5]
    i=0
    d_top={}
    while i<5:
        for j in d:
            if d[j]==l[i]:
                d_top[j]=d[j]
                if len(d_top)==5:
                    break
        i+=1
    total=sum(d_top.values())
    return total/len(sl),d_top

def f3(s):
    char=[",",".",":",";"]
    temp=s.split(".") #assuming a full stop is used to end one sentence
    lines=[]
    for i in range(len(temp)):
        if temp[i]=="" or temp[i]=="\n":
            continue
        else:
            lines.append(temp[i])
    for i in range(len(lines)):
        lines[i]=lines[i].strip()
        lines[i]=lines[i].strip("\n")
    for i in char:
        while i in lines:
            lines.remove(i)
    i=0
    while i<len(lines):
        if lines[i][0].isalnum()==0:
            del lines[i]
        else:
            i+=1
    count=0
    for i in lines:
        i=i.split()
        for j in range(len(i)):
            for k in char:
                i[j]=i[j].strip(k)
        if len(i)>35 or len(i)<5 and i!=['']:
            count+=1
    return count/len(lines)

def f4(s):
    char=[",",".",":",";"]
    con=False
    count=0
    group=0
    for i in s:
        if i in char:
            if con==False:
                count=0
            con=True
            count+=1
        else:
            con=False
        if con==False and count>1:
            group+=1
            count=0
    return group/totalwords(s)

def f5(s):
    if totalwords(s)>750:
        return 1
    else:
        return 0

filename=["file1.txt","file2.txt","file3.txt","file4.txt"]
f_output=open("scores.txt","w")
for x in filename:
    f=open(x,"r")
    s=f.read()
    f1v,r=f1(s)
    f2v,d=f2(s)
    f3v=f3(s)
    f4v=f4(s)
    f5v=f5(s)
    net=4+f1v*6+f2v*6-f3v-f4v-f5v
    print("Net: ",net)
    f_output.write(x.upper()+"\n")
    f_output.write("\n")
    f_output.writelines(["Score: ",str(net)])
    f_output.write("\n")
    f_output.write("\n")
    f_output.write("Top 5 words: "+"\n")
    for i in d:
        f_output.writelines([i," ",str(d[i]),"\n"])
    f_output.write("\n")
    f_output.write("5 random words: "+"\n")
    rand=[]
    for i in range(5):
        ind=random.randint(0,totalwords(s)-1)
        rand.append(ind)
    for i in rand:
        f_output.writelines([r[i],"\n"])
    f_output.write("\n")
    print(x,"written")
    f.close()
f_output.close()