#There are total 4 functions in Python String to find substrings

#1. find() method - which returns the index of first occurence of the given substring. If substring not present, it returns -1

s = input("Enter a string: ")
substr = input("Enter substring: ")

print(s.find(substr))
#we can specify our own boundaries for find method to search within
print(s.find(substr,5,10)) #beginIndex = 5, endIndex = end-1 i.e. 9

