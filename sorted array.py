"""selection sort"""

A = [64, 25, 12, 22, 11]
for i in range(len(A)):
    x = i
    for j in range(i+1, len(A)):
        if A[x] > A[j]:
            x = j

    A[i], A[x] = A[x], A[i]
print ("The Sorted array are:") 
for i in range(len(A)): 
    print(A[i])
