def upperbound(arr,x):
    n=len(arr)
    for i in range(n):
        if arr[i]> x:
            return i
    return n

if __name__=="__main__":
    arr=[2, 3, 7, 10, 11, 11, 25]
    x=12
    print(upperbound(arr,x))
