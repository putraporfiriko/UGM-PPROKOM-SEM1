matrix1 = [[5,0],
           [2,6]]

matrix2 = [[1,0],
           [4,2]]

matrix3 = []

for x in range(0, len(matrix1)):
    row = []
    for y in range(0, len(matrix1[0])):
        total = 0
        for z in range(0,len(matrix1)):
            total = total + (matrix1[x][z] * matrix2[z][y])
        row.append(total)
    matrix3.append(row)

for x in range(0, len(matrix3)):
    for y in range(0, len(matrix3[x])):
        print(matrix3[x][y], end=' ')
    print()