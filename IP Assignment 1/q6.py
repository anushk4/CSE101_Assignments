def pattern(n):
    space=2*n-2
    for i in range(1,n+1):
        print("*"*i," "*space,"*"*i,sep="")
        space-=2

n=int(input("Enter n: "))
pattern(n)