import functools    
def cmp(a,b):
    if(int(a+b) < int(b+a)):
        return 1
    else:
        return -1
    
def largestNumber(A):
    A=sorted(A,key=functools.cmp_to_key(cmp))
    ans=""
    for c in A:
        ans+=str(c)
    return int(ans)

arr=list(map(str,input().split()))
print(largestNumber(arr))