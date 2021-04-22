def reverse(arr):
    high=len(arr)-1
    low=0
    while(low<high):
        arr[low],arr[high]=arr[high],arr[low]
        low+=1
        high-=1
    return arr

arr=list(map(int,input().split()))
print(reverse(arr))