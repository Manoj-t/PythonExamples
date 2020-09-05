# print Equilateral Triangle

lines = int(input("Enter number of lines in a triangle:"))

#First Way
#logic starts
for i in range(1,lines+1):
    for j in range(1,lines-i+1): #Number of spaces required to print
        print(" ",end="") # print spaces
    print(i*"* ") # print *s


# Alternative way (Same logic)
for i in range(1, lines+1):
    print((lines-i)*" ",end="") #Prints number of spaces required
    print("* "*i)
