# Program to print reverse words in a string

str = input('Enter a string: ')

list = str.split()

i=len(list)-1
revstr=''
while i>=0:
    revstr = revstr+list[i]+" "
    i = i-1
print(revstr)