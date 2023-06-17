n=int(input("Enter N: "))
coordinates=[]
for i in range(n):
    coordinates.append(tuple(map(int,input("Enter coordinates: ").split(","))))
for i in range(len(coordinates)):
    coordinates[i]+=(1,)
cx=int(input("Enter scaling parameter cx: "))
cy=int(input("Enter scaling parameter cy: "))
matrix=[(cx,0,0),(0,cy,0),(0,0,1)]
scaled_matrix=[]
i=0
m=0
t=[]
while i<n:
    k=0
    sum1=0
    for j in range(3):
        sum1+=coordinates[i][k]*matrix[j][m]
        k+=1
    t.append(sum1)
    m+=1
    if len(t)==3:
        t.remove(1)
        scaled_matrix.append(tuple(t))
        i+=1
        m=0
        t=[]
print("Scaled matrix is:",scaled_matrix)