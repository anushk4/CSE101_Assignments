menu = [("Samosa", 15), ("Idli", 30), ("Maggie", 50), ("Dosa", 70), ("Tea", 10), ("Coffee", 20), ("Sandwich", 35), ("Cold Drink", 25)]
print("Menu".center(21,"-"))
for i in range(len(menu)):
    print(i+1,"    ",menu[i][0]," "*(len("cold drink")-len(menu[i][0])+4),menu[i][1],sep="")
print()
l=[]
while True:
    x=list(map(int,input("Enter item no and quantity: ").split()))
    if x==[]:
        break
    l.append(x)
total=0
items=0
for i in l:
    print(menu[i[0]-1][0],", ",i[1],", ","Rs ",menu[i[0]-1][1]*i[1],sep="")
    total+=menu[i[0]-1][1]*i[1]
    items+=i[1]
print("TOTAL, ",items," items, ","Rs ",total,sep="")