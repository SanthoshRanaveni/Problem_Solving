def maxSubArray(arr):
    size=len(arr)
    max_so_far=arr[0]
    max_end_here=0
    start_idx=0
    end_idx=0
    k=0

    for i in range(size):
        max_end_here += arr[i]

        if max_so_far < max_end_here:
            max_so_far = max_end_here
            start_idx=k
            end_idx=i
        if max_end_here < 0:
            max_end_here = 0
            k+=1

    return max_so_far,start_idx,end_idx

arr=list(map(int,input().split()))
max,s_idx,e_idx=maxSubArray(arr)
print("The max possible sum is "+str(max)+" in the subarray"+str(arr[s_idx:e_idx+1]))