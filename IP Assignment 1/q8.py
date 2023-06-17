def population(pop,g):
    p=0
    for i in range(7):
        pop[i]=pop[i]+pop[i]*g[i]
        p=sum(pop)
    return p

pop=[50,1450,1400,1700,1500,600,1200]
m=sum(pop)
g=[0.025,0.021,0.017,0.013,0.009,0.005,0.001]
y=1
max=sum(pop)
while True:
    l=population(pop,g)
    if l<=max:
        break
    else:
        max=l
        for i in range(7):
            g[i]=g[i]-0.001
        y+=1
print("Current total population: ",m,"million")
print("Number of years: ",y-1)
print("Maximum population: ",max,"million")