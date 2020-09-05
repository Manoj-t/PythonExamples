a = int(input("Enter First Number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number: "))

min = a if a<b and a<c else b if b<c else c
print("Minimum value is:",min,sep="    ")