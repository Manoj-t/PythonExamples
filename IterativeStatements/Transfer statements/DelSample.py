# Del Keyword is used to delete unused variables so that object referenced by that variable is eligible for GC



a = 10
print(a)
del a

# del can be used for mutable and immutable objects but in immutable objects we can only delete the variables referenced by them but not elements present in them

#Example of deleting elements in mutable object i.e. List
list = [10,20,30,40]
del list[0]
print(list) # prints [20,30,40]

#Example trying to delete elements in immutable object
name = 'manoj'
# del name[1] throws error saying 'str' doesn't support item deletion
del name # valid
