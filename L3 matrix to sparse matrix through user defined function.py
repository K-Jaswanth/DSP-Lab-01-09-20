# sparse matrix representation with User defined funtion

# function display a matrix
def printing_matrix(matrix) :
    for i in matrix:
        for j in i:
            print(j, end =" ")
        print()
    
matri=[[2,0,0,0],
        [9,0,77,0],
        [0,0,5,0],
        [0,44,0,6]]
print('Input Matrix : ')

printing_matrix(matri)
sparseMatrix=[]
for i in range(len(matri)):
    for j in range(len(matri[1])):
        if matri[i][j]!=0:
            temp=[]
            temp.append(i)
            temp.append(j)
            temp.append(matri[i][j])
            sparseMatrix.append(temp)
print("\nsparsematrix:")

printing_matrix(sparseMatrix)
