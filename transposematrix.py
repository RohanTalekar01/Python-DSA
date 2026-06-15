def transpose(mat):
    n = len(mat)  

    for i in range(n):
        for j in range(i + 1, n):

            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    return mat  

if __name__ == "__main__":
    mat = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
    res = transpose(mat)  
    for row in res:
        print(" ".join(map(str, row)))
