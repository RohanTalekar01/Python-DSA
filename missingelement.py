def missing(arr):
    n=len(arr)+1

    for i in range(n-1):
        if arr[i] !=i+1:
            return i+1

    return n

if __name__=="__main__":
    arr=[1, 2, 3, 4, 6, 7, 8]
    print(missing(arr))
