from math import exp as e
def D(p):
    demand=round(e(a-b*p),2)
    return demand

def S(p):
    supply=round(e(c+d*p),2)
    return supply

a=10
b=1.05
c=1
d=1.06
p=1.0
eq=0
while True:
    if D(p)-S(p)==0:
        eq=p
        print("Equilibrium price: ",eq)
        print("Demand: ",D(p))
        print("Supply: ",S(p))
        break
    elif S(p)>D(p):
        print("Price: ",p)
        print("Demand: ",D(p))
        print("Supply: ",S(p))
        print("Hence, no equilibrium price is possible")
        break
    p+=0.05*p