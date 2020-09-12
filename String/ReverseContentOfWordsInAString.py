#Program to reverse content of words in a string

str = input("Enter a string: ")

list = str.split();

revstr = ''
i=0

while i<=len(list)-1:
    l1 = list[i]
    revstr = revstr + l1[::-1] + " "
    i = i+1
print(revstr)