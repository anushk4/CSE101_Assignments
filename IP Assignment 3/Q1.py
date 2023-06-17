def toppattern(n,i,x):
    if n<=1:
        print("* "*n,"* "*n,sep="  "*(2*x-2))
        return
    print("* "*n,"* "*n,sep="  "*i)
    toppattern(n-1,i+2,x)

def bottompattern(n,i):
    if i==0:
        print("* "*n,"* "*n,sep="  "*i)
        return 
    print("* "*n,"* "*n,sep="  "*i)
    bottompattern(n+1,i-2)

n=int(input("Enter n: "))
toppattern(n,0,n)
if n>1:
    bottompattern(2,2*n-4)