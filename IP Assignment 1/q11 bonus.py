# WAP to create a unique user id and password for signing up. Password should have the following conditions:
# 1. Should be atleast 7  character long
# 2. Should have a combination of digits and alphabets
# 3. Should have atleast 1 special character: $,@,%

def userid():
    global user_id
    user_id=input("Enter User id: ")
    return user_id
    
def pwf():
    global pw
    pw=input("Enter password: ")
    checkl(pw)
    
def checkl(pw):
    if len(pw)<=7:
        print("Password too short. Try again")
        pwf()
    else:
        checknum(pw)

def checknum(pw):
    c=0
    for i in pw:
        if i.isdigit():
            c+=1
    if c==0:
        print("Password must have atleast 1 digit")
        pwf()
    else:
        checksym(pw)

def checksym(pw):
    global q
    l=["$","@","%"]
    s=0
    invalid=0
    for i in pw:
        if i in l:
            s+=1
        if i not in l and i.isalnum()==0:
            invalid+=1
    if invalid>0:
        print("Invalid character entered")
        pwf()
    elif s==0:
        print("Password must have atleast @,$ or %")
        pwf()
    else:
        q=pw 
    
data=["user123","user@123","user_123","userrrr"]
while True:
    m=userid()
    for i in data:
        if i==m:
            print("User-id already exists")
            print("Re-enter")
            break
    else:
        break
pwf()
print()
print("Password set: ","*"*len(q))
print()
ch=input("Do you want to view user name and password?(y/n)")
if ch=="y":
    print("User name: ",m)
    print("Password:  ",q)
else:
    print("End of program")