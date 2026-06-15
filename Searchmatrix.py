def search(mat,x):
    n=len(mat)
    m=len(mat[0])

    for i in range(n):
        for j in range(m):
            if mat[i][j]==x:
                return True
    return False

if __name__ == "__main__":
    mat = [
        [1, 5, 9],
        [14, 20, 21],
        [30, 34, 43]
    ]
    x = 14
    print("true" if search(mat, x) else "false")
