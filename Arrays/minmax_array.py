def minmaxArr(arr,min,max):
    for i in range(len(arr)):
        if arr[i]>max:
            max=arr[i]
        elif arr[i]<min:
            min=arr[i]
    return min,max

arr=list(map(int,input().split()))
min=arr[0]
max=min
min,max=minmaxArr(arr,min,max)
print(min,max)