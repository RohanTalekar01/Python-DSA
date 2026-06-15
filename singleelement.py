def single(arr):
    n=len(arr)

    for i in range(0 ,n-1,2):
        if arr[i] != arr[i+1]:
            return arr[i]

    return arr[n-1]

if __name__=="__main__":
    arr=[1, 1, 2, 2, 3, 4, 4]
    print(single(arr))


def single(arr):
    XOR = 0

    for i in arr:
        XOR^=i
    return XOR

if __name__=="__main__":
    arr=[1, 1, 2, 2, 3, 4, 4]
    print(single(arr))
