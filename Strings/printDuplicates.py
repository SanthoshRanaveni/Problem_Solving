def duplicate(str):
    a={}
    for i in range(len(str)):
        if str[i] in a:
            a[str[i]]+=1
        else:
            a[str[i]]=1
    return a
str1=input()
count=duplicate(str1)
for k,v in count.items():
    if v>1:
        print(k+" is repeated "+str(v)+" times")