# Xor all the elements of the given array, say x, 
# Find the number which gives max xor with x, print the num. 
# Now remove the max element from the array, and do the same till array size is 0.

arr=list(map(int,input().split()))
arr.sort()
xArr=[]
x=arr[0]
for i in range(1,len(arr)):
    x=x ^ arr[i]
    xArr.append(x)
print(xArr)
while(len(arr)>0):
    # print(arr)
    if(len(arr)>1):
        # print("xor value is "+str(x))
        maxx=xArr[len(xArr)-1] ^ arr[0]
        # print("max value is "+str(maxx))
        for i in range(1,len(arr)):
            xval= xArr[len(xArr)-1] ^ arr[i]
            # print("xor ^ "+str(arr[i])+" value is "+str(xval))
            if(xval > maxx):
                maxx=xval
        print(maxx)
    else:
        print(arr[0])
    arr.remove(arr[len(arr)-1])
    if(len(xArr)>1):
        xArr.remove(xArr[len(xArr)-1])
