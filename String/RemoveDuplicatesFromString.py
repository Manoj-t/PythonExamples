#Program to remove duplicates from a string

str = input('Enter a string: ')
l = []
output=''
for x in str:
    if x not in l:
        l.append(x)
        output=output+x
    else:
        pass
print(output)