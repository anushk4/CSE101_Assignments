def calculate(cost,sf,r):
    f=sf
    month=1
    while True:
        month+=1
        f+=sf+r*f
        if f>=cost:
            print("Total months: ",month)
            print("Savings remaining: ",f-cost)
            break

cost=float(input("Enter cost of laptop: "))
allowance=20000
sf=0.1*allowance
r=0.005
calculate(cost,sf,r)