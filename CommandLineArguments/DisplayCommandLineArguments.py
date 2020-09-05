
from sys import argv

print("No. of command line arguments are:",len(argv))
print("The list of command line arguments are:",argv)

print("list of command line arguments one by one:")

for i in argv:
    print(i)