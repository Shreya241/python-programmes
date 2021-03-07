R=int(input("enter the number of rows:"))
C=int(input("enter the number of columns:"))
M=[]
SM=[]
for i in range(R):
    a=[]
    for j in range(C):
        a.append(int(input()))
    M.append(a)
for i in M:
    print(i)
print("\nSquare of Matrix is :\n")
if R==C:
    for i in range(R):
        a=[]
        for k in range(C):
            s=0
            for j in range(R):
                s+=(M[i][j]*M[j][k])
            a.append(s)
        SM.append(a)
    for i in SM:
        print(i)
