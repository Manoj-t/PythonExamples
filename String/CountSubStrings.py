#String's count() method is used to get count of number of occurences of a given substring in a string

str = input("Enter a string: ")
substr = input("Enter a substring: ")

print("substr '{x}' is found {y} times in a given string '{z}'".format(x=substr,y=str.count(substr),z=str))

#we can specify our own boundaries in count() method i.e. we can set our own begin and end indices
print("substr '{x}' is found {y} times in a given string '{z}'".format(x=substr,y=str.count(substr,5,10),z=str)) #beginindex = 5 and end = 10-1 = 9
