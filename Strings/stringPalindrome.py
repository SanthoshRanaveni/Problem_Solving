def check(str):
    low=0
    high=len(str)-1
    while(low<high):
        if(str[low]==str[high]):
            low+=1
            high-=1
        else:
            return False
    return True

str=input().lower()
print(check(str))