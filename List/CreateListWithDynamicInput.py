#Creating a list with dynamic input

list1 = eval((input('Enter a list: ')))
print(list1)
print(type(list1))

#Creating a list using list() function

list2 = list(range(0,10,2))
print(list2)
print(type(list2))

#Creating a list using split() function

str = 'Learning Python is very easy!'
list3 = str.split()
print(list3)
print(type(list3))
