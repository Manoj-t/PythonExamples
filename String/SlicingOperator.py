str = 'Learning Python is very easy!!'

#forward slicing
print(str[:]) # prints whole string in forward direction

print(str[:6]) # prints string from index 0 to 5

#backward direction
print(str[::-1]) # prints complete string in backward direction

print(str[-2:-9:-1]) # prints string from index in backward direction from index -2 to -8


#Program to access each charcter in a string in forward direction and backward direction

string = input('Enter a string')
length = len(string)

#printing characters in a string in forward direction
i=0;
print("Printing characters in forward direction:")
while i<=length-1:
    print("character at index {x} in forward direction is {y}".format(x=i,y=string[i]))
    i = i+1

i=-1
print("Printing characters in backward direction:")
while i>-(length+1):
    print("character at index {x} in backward direction is {y}".format(x=i, y=string[i]))
    i = i-1