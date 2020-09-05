list = [10,20,30,40]
list[0] = 33
for i in list:
    print(i)

list.append(45)
list.remove(30)

print("List after appending and removing values")
for i in list:
    print(i)