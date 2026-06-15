# Python program to search an element in row-wise
# and column-wise sorted matrix

def matSearch(mat, x):
    n = len(mat)
    m = len(mat[0])
  
    for i in range(n):
        for j in range(m):
            if mat[i][j] == x:
                return True
  
    # If x was not found, return false
    return False

if __name__ == "__main__":
    mat = [[3, 30, 38],
		   [20, 52, 54],
           [35, 60, 69]]
    x = 35
    if matSearch(mat, x):
        print("true")
    else:
        print("false")
