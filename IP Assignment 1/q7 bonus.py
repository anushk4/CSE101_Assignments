def calculate(r,m,sf):
    f=sf
    month=0
    while month<m:
        month+=1
        f+=sf+r*f
    return f-sf

cost=float(input("Enter cost of laptop: "))
m=int(input("Enter months: "))
allowance=20000
r=0.005
sf=0.01
while sf<=1:
    if calculate(r,m,sf*allowance)>=cost:
        print("Saving fraction: ",round(sf,2))
        print("Saving rate: ",str(round(sf,2)*100)+"%")
        break
    sf+=0.01