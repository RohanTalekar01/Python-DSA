def countfreq(arr,target):
    res=0
    n=len(arr)
    for i in range(n):
        if arr[i]==target:
            res +=1
    return res

if __name__=="__main__":

    arr = [1, 1, 2, 2, 2, 2, 3]
    target = 2
    print(countfreq(arr, target))
    
