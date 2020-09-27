
str = input('Enter a string: ')

i=0
output=''
while i<=len(str)-1:
    if(str[i].isalpha()):
        output=output+str[i]
    if(str[i].isdigit()):
        output=output+((int(str[i])-1)*str[i-1])
    i=i+1
print(output)
