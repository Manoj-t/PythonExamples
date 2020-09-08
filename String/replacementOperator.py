# replace() function in String
#We can replace a substring with a new substring in a given string using replace() method

str = input("Enter a string: ")
oldstr = input("Enter old string: ")
newstr = input("Enter a new string: ")

s1 = str.replace(oldstr,newstr)
print("Old string '{x}' is replaced with new string '{y}' in '{str}' and resultant is '{z}'".format(x=oldstr,y=newstr,z=s1,str=str))
