n = 7

for i in range(0,n):
    for j in range(0,i+1):
        print (n-i+j,j)


for i in range(0,n+1):
    for j in range(0,n-i+1):
        print (j,i+j)
