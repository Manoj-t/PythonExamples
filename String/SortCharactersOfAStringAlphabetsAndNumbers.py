#Program to sort characters of a string and then first Aplhabets and followed by Numbers

str = input('Enter a string to sort: ')

i=0
alph = ''
digi = ''
while i<=len(str)-1:
    if(str[i].isalpha()):
        alph=alph+str[i]
    if(str[i].isdigit()):
        digi=digi+str[i]
    i = i+1

soralph=''
sordig =''

for x in sorted(alph):
    soralph=soralph+x
for x in sorted(digi):
    sordig=sordig+x
print(soralph+sordig)