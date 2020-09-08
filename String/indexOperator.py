# index() function of string
# It is the same method like find() method to find the substring in a given string except it throws ValueError if specified substring is not found.

str = input("Enter a string: ")
substr = input("Enter a substring: ")

try:
    index = str.index(substr)
except ValueError:
    print("Substring '{x}' not found in '{y}'".format(x=substr,y=str))
else:
    print("substring '{x}' found at index {y} in string '{z}'".format(x=substr,y=index,z=str))