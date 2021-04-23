def reverseString(str):
    stack=[]
    for i in range(len(str)):
        stack.append(str[i])
    for i in range(len(str)):
        print(stack.pop(),end="")

str=input()
reverseString(str)