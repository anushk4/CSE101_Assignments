#check for plagiarism

def totalwords(s):
    return len(listofwords(s))

def listofwords(s):
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
    return sl

def fCW(s1,s2):
    s1=listofwords(s1)
    s2=listofwords(s2)
    common={}
    comw=list(set(s1).intersection(set(s2)))
    for i in comw:
        common[i]=min(s1.count(i),s2.count(i))
    return common

def nSW(com):
    return sum(com.values())

def nSUW(com):
    return len(com)

filename=["file1.txt","file2.txt","file3.txt","file4.txt"]
f_out=open("plag.txt","w")
for x in range(len(filename)):
    for y in filename[x+1:]:
        f1=open(filename[x],"r")
        f2=open(y,"r")
        s1=f1.read()
        s2=f2.read()
        fCWd=fCW(s1,s2)
        nSWn=nSW(fCWd)
        nSUWn=nSUW(fCWd)
        sim_index=(((nSWn/totalwords(s1))+(nSUWn/len(set(listofwords(s1)))))/2)*100
        if sim_index>50:
            sim_index=str(sim_index)+" %"
            f_out.writelines([filename[x]," ",y," ",sim_index,"\n"])
    f1.close()
    f2.close()
f_out.close()
print("File written")