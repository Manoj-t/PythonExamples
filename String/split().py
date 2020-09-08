#Split method in String
# split() method seperates the string based on given seperator

#default seperator is space
#return type of split() is List

str = input("Enter a string: ")
sep = input("Enter a sepeartor: ")

l = str.split(sep)

for s in l:
    print(s)