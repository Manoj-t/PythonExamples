#Program to find out number of occurences of each character in a string

str = input('Enter a string: ')
dict={}

for x in str:
    if x not in dict:
        dict[x] =1
    else:
        count = dict.get(x)
        dict[x]=count+1

for k,v in dict.items():
    print("occurence of {x} in {y} is {z} no. of times".format(x=k, y=str, z=v))


