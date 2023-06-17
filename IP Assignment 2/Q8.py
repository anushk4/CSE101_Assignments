f=open("pages.txt","r")
set_of_links={}
links={}
init_importance={}
for i in f.readlines():
    x=i.split(": ")
    url=x[0].split(", ")
    links[url[0]]={}
    set_of_links[url[0]]={}
    init_importance[url[0]]={}
    unique=set()
    for j in x[1].split():
        if j.startswith("URL"):
            unique.add(j.rstrip(", "))
    init_importance[url[0]]=float(url[1])
    links[url[0]]=len(list(unique))
    set_of_links[url[0]]=list(unique)
overall={}
for i in init_importance:
    n=0
    for j in set_of_links:
        if i in set_of_links[j]:
            n+=init_importance[j]/links[j]
    overall[i]=n
final_dict={}
for i in overall:
    final_dict[i]={}
    final_dict[i]["init_importance"]=init_importance[i]
    final_dict[i]["overall_importance"]=overall[i]
    final_dict[i]["set_of_links"]=set_of_links[i]
print(final_dict)
N=int(input("Enter how many pages you want to see: "))
temp_d={}
for i in overall:
    temp_d[overall[i]]=i
sorted_keys=sorted(temp_d,reverse=True)
ordered={}
for i in sorted_keys:
    ordered[temp_d[i]]=float(i)
x=0
while True:
    for i in ordered:
        print("URL page: ",i)
        print("init_importance: ",final_dict[i]["init_importance"])
        print("overall importance: ",final_dict[i]["overall_importance"])
        print("unique links: ",final_dict[i]["set_of_links"])
        print()
        x+=1
        if x==N:
            break
    break