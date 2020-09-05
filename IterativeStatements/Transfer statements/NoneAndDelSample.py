#In case of del, variable is not deleted and object is referenced by variable is eligible for GC Hence, variable can't be accessed after executing del
# name = 'manoj'
# print(name)
# del name
# print(name)

#None: variable is not deleted and object referenced by it is eligible for GC
name1 = 'kumar'
print(name1)
name1 = None
print(name1)