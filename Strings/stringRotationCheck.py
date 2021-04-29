def strRotation(str1,str2):
    str1=str1+str1
    if str2 in str1:
        return True
    return False

str1=input()
str2=input()
if(strRotation(str1,str2)):
    print("String 2 is a rotation of String 1")
else:
    print("String 2 is not a rotation of String 1")