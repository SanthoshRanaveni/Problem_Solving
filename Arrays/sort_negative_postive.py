def sort_neg_post(arr):
    low=0
    high=len(arr)-1
    while(low<high):
        if(arr[low]<0):
            low+=1
        if(arr[high]>0):
            high-=1
        if(arr[low]>0 and arr[high]<0):
            arr[low],arr[high]=arr[high],arr[low]
            low+=1
            high -=1

    return arr

arr=list(map(int,input().split()))
print(sort_neg_post(arr))