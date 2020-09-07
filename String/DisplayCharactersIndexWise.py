# print characters in a string index wise

string = input("Enter a string:")
i=0
for ch in string:
    print("The character present at positive index {x} and negative index {y} is {z}".format(x=i,y=i-len(string),z=ch))
    i = i+1


