#We have three methods to remove spaces from the string
#rstrip() --> to remove spaces at the right hand side.
#lstrip() --> to remove spaces at the left hand side.
#strip() --> to remove spaces at both sides.

str = input("Enter a string: ")

print("Given string is {x} and it's length is {y}".format(x=str,y=len(str)))
print("string is left stripped and now it is {x} and it's length is {y}".format(x=str.lstrip(),y=len(str.lstrip())))
print("string is right stripped and now it is {x} and it's length is {y}".format(x=str.rstrip(),y=len(str.rstrip())))
print("string is stripped on both sides now it is {x} and it's length is {y}".format(x=str.strip(),y=len(str.strip())))