arr=[9,8,7,6,5]
n=len(arr)

for i in range(n):
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
##            arr[j],arr[j+1]=arr[j+1],arr[j]
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp

print(arr)
        
