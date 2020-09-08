# in and not in are called membership opertaors

# Membership operator checks if substring is part of another string

#in operator returns true if substring is present otherwise false and
# not in operator works vice versa it returns true if substring is not present in another or main string.

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if s2 in s1:
    print("s2 '{x}' is present in s1 '{y}'".format(x=s2,y=s1))
else:
    print("s2 '{x}' is not present in s1 '{y}'".format(x=s2,y=s1))