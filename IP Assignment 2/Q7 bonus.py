#Address book merged with Aarzoo (2022008)

import json

f1=open("anushka.json","r")
f2=open("aarzoo.json","r")
f3=open("merged.json","w")
x1=json.load(f1)["Address Book"]
x2=json.load(f2)["Address Book"]
merged={"Address Book":{}}
for i in x1:
    if i in x2:
        merged["Address Book"][i]=[x1[i],x2[i]]
    else:
        merged["Address Book"][i]=x1[i]
for i in x2:
    if i in x1:
        merged["Address Book"][i]=[x1[i],x2[i]]
    else:
        merged["Address Book"][i]=x2[i]
print("Merged addressbook: ")
print(json.dumps(merged,indent=4))
f3.write(json.dumps(merged,indent=4))
f1.close()
f2.close()
f3.close()