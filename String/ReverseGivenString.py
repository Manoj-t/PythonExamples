#Program to reverse the given string

#There are several ways to reverse the string

str = input("Enter a string: ")
#1st way (using slice operator backward direction)
print(str[::-1])

#2nd way (using join() and reversed() method which returns an iterator that accesses the given sequence in reverse order
print(''.join(reversed(str)))

#3rd way
i = len(str)-1
rev=''
while i>=0:
    rev = rev + str[i]
    i = i-1
print(rev)
