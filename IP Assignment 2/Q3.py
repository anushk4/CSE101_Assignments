f=open("question3.txt","r")
d_year={}
x=f.readline()
d_year[x.rstrip(":\n")]={}
while x!="":
    x=f.readline()
    if x=="\n":
        x=f.readline()
        d_year[x.rstrip(":\n")]={}
f.seek(0,0)
x=f.readline()
for i in d_year:
    while True:
        x=f.readline()
        if x.rstrip(":\n") in d_year:
            break
        if x=="\n" or x=="":
            break
        l=x.split(",")
        d_year[i][l[0]]=int(l[1].rstrip("\n"))
    x=f.readline()
f.close()
maxs=""
maxv=0
mins=""
minv=1e7
for i in d_year:
    c=0
    for j in d_year[i]:
        if d_year[i][j]==1:
            c+=1
    if c>maxv:
        maxv=c
        maxs=i
    if c<minv:
        minv=c
        mins=i

#Yearbook dictionary created: {'Ashish': {'Shreyas': 1, 'Rayka': 0, 'Manas': 1, 'Kavya': 0, 'Parul': 0}, 
#'Shreyas': {'Ashish': 0, 'Rayka': 1, 'Manas': 1, 'Kavya': 0, 'Parul': 1}, 'Rayka': {'Shreyas': 1, 'Ashish': 1, 'Manas': 1, 'Kavya': 0, 'Parul': 1},
#'Manas': {'Shreyas': 1, 'Rayka': 0, 'Ashish': 0, 'Kavya': 1, 'Parul': 1}, 'Kavya': {'Shreyas': 0, 'Rayka': 1, 'Manas': 1, 'Ashish': 1, 'Parul': 0},
# 'Parul': {'Shreyas': 1, 'Rayka': 0, 'Manas': 1, 'Kavya': 0, 'Ashish': 1}}

print("Person with maximum signatures:",maxs)
print("Person with minimum signatures:", mins)