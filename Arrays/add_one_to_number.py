def add_one(arr):
    a=[]
    str1=""
    for ele in arr:
        str1+=str(ele)
    str1=str(int(str1)+1)
    for i in range(len(str1)):
        a.append(int(str1[i]))
    return a

arr=list(map(int,input().split()))
print(add_one(arr))