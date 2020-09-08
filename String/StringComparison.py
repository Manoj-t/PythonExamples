#Strings in python can be compared using <,>,<=,>=(comparison operators) and ==,!=(Equality operators)

# Comparison will be performed based on alphabetical order. Characters in both strings are compared one by one when there is mismatch,
#then their Unicode values will be compared. Character with lower unicode value will be considered as smaller.

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if s1 > s2:
    print("s1 is greater than s2")
elif s1 < s2:
    print("s2 is greater than s1")
else:
    print("Both s1 '{s1}' and s2 '{s2}' are equal".format(s1=s1,s2=s2))

#Unicode value of smaller case aplhabets starts from (a=97-z=122) and
#Unicode value of Capital alphabets starts from (A=65-Z=90)