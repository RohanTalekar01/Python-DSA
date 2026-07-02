def diagonalTraversal(mat):
    n=len(mat) # length of mat
    diag = [[] for _ in range(2*n-1)] 

    for i in range(n): # rows
        for j in range(n): # columns
            diag[i+j].append(mat[i][j]) # values add in the diag

    for d in range(2*n-1):
        for val in diag[d]:
            print(val, end=" ")



if __name__ == "__main__":
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

diagonalTraversal(mat)
