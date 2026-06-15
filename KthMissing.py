def kthmissing(arr,k):
    n=len(arr)
    for i in range(n):
        if arr[i] > (k+i):
            return k+i
    return k+n

if __name__ == "__main__":
    arr = [2, 3, 4, 7, 11]
    k = 5
    print(kthmissing(arr, k))
    
