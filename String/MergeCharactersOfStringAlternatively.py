 # Program to merge characters of two strings into a single string by taking characters alternatively

str1= input("Enter string1: ")
str2 = input("Enter string 2: ")
str3 = ''
i,j=0,0
while i<len(str1) or j<len(str2):
    if i<len(str1):
        str3 = str3 + str1[i]
        i=i+1
    if j<len(str2):
        str3 = str3 + str2[j]
        j=j+1
print(str3)