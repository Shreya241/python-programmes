"""square of a matrix"""


# 3x3 matrix
X = [[12,7,3],
    [4,5,6],
    [7,8,9]]
# 3x3 matrix
Y = [[12,7,3],
    [4,5,6],
    [7,8,9]]
# 3x4 matrix
# result is 3x3
result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(X)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)