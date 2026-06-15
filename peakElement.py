def peakElement(arr):

    n = len(arr)

    for i in range(n):
        if i == 0:
            if arr[i] > arr[i + 1]:
                return i

        elif i == n - 1:
            if arr[i] > arr[i - 1]:
                return i

        else:
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                return i

arr = [1, 2, 4, 5, 7, 8, 3]

print(peakElement(arr))
