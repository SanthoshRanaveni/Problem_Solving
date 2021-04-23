def kth_smallest_element(arr,k):
    arr.sort()    
    return arr[k-1]

arr=list(map(int,input().split()))
k=int(input())
print(kth_smallest_element(arr,k))