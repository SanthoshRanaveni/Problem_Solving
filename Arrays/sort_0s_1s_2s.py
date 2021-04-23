def sort012(arr):
        count={}
        for i in range(len(arr)):
            if arr[i] in count:
                count[arr[i]]+=1
            else:
                count[arr[i]]=1
        arr=[]
        print(arr)
        print(count)
        for i in range(count[0]):
            arr.append(0)
        for i in range(count[1]):
            arr.append(1)
        for i in range(count[2]):
            arr.append(2)
        return arr

arr=list(map(int,input().split()))
print(sort012(arr))