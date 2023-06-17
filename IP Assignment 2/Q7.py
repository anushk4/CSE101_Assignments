def addname(name,info):
    if name in addressbook:
        addressbook[name].append(info)
    else:
        addressbook[name]=[info]

def checkemail(un):
    f=False
    u=un.split("@")
    if u[1].endswith(".com"):
        f=True
    else:
        return f
    for i in u:
        if i==u[1]:
            i=i.rstrip(".com")
        for j in i:
            if j.isalnum() or j=="_":
                f=True
            else:
                f=False
                break
        if f==False:
            break
    return f

addressbook={}
f=open("addrbook.txt","a+")
f.seek(0,0)
if f.read()!={}:
    f.seek(0,0)
    addressbook=eval(f.read())
print("1. Insert new entry")
print("2. Delete an entry")
print("3. Find matching entries given a partial name")
print("4. Find entry with phone number/email")
print("5. Exit")
while True:
    ch=int(input("Enter option: "))
    if ch==1:
        name=input("Enter name: ")
        add=input("Enter address: ")
        phone=input("Enter phone no: ")
        if len(phone)!=10:
            print("Phone number should be 10 digits long only")
            continue
        email=input("Enter email: ")
        if checkemail(email)==0:
            print("Invalid format for email")
            continue
        addname(name,{"Address":add,"Phone no":phone,"Email":email})
        print("Record added")
    if ch==2:
        name=input("Enter name to be deleted: ")
        if len(addressbook[name])>1:
            phone=input("Enter to search by phone number: ")
            for k in addressbook[name]:
                if phone in list(k.values()):
                    addressbook[name].remove(k)
                    print("Record deleted")
                    break
        else:
            del addressbook[name]
            print("Record deleted")
    if ch==3:
        partial=input("Enter partial name: ")
        for i in addressbook:
            if partial in i:
                if len(addressbook[i])>1:
                    for k in addressbook[i]:
                        print(i+", "+", ".join(list(k.values())))
                else:
                    print(i+", "+", ".join(list(addressbook[i][0].values())))
    if ch==4:
        contact=input("Enter phone or email: ")
        for i in addressbook:
            if len(addressbook[i])>1:
                for k in addressbook[i]:
                    if contact in list(k.values()):
                        print(i+", "+", ".join(list(k.values())))
            else:
                if contact in list(addressbook[i][0].values()):
                    print(i+", "+", ".join(list(addressbook[i][0].values())))
    if ch==5:
        break
    print()
f.truncate(0)
f.writelines(str(addressbook))
f.close()