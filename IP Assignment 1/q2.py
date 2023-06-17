def P(x1,x2,M):
    if x1<M and x2<M:
        P=90*M+25*M
    elif x1<M:
        P=90*M+25*M+30*(x2-M)
    elif x2<M:
        P=90*M+25*M+100*(x1-M)
    else:
        P=90*M+25*M+100*(x1-M)+30*(x2-M)
    return P

#x1=no of tables
#x2=no of chairs

M=int(input())
x1_min,x2_min,x1_max,x2_max=0,0,50,120
max_P=0
f_x1=0
f_x2=0

#x1>=0,x2>=0,8x1+2x2<=400,2x1+x2<=120

for i in range(x1_max+1):
    for j in range(x2_max+1):
        if i>=0 and j>=0 and 8*i+2*j<=400 and 2*i+j<=120:
            profit=P(i,j,M)
            if profit>max_P:
                max_P=profit
                f_x1=i
                f_x2=j

print("For maximum profit:")
print("No of tables: ",f_x1)
print("No of chairs: ",f_x2)
print("Maximum profit: ",max_P)