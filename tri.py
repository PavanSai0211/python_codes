n=5
for i in range(n):
    for j in range(i+1,n):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print()

for i in range(n-2,-1,-1):
    for j in range(i+1,n):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print()