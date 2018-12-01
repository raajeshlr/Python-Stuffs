import itertools

A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[1,2,3],[4,5,6],[7,8,9]]
result = [[0,0,0],[0,0,0],[0,0,0]]
transposea = [[0,0,0],[0,0,0],[0,0,0]]

print(len(A))
print(len(A[0]))

#print(list(itertools.product(A,B)))

for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] * B[i][j]
        transposea[i][j]= A[j][i]
for r in result,transposea:
    print(r)
