s1='manoj'
s2=s1
print("address of s1:",id(s1))
print("address of s1:",id(s2))
del s1
print(s2)
print("address of s2:",id(s2))
