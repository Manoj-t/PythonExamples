a = int(input("Enter First Number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number: "))

Max = a if a>b and a>c else b if b>c else c

print("Maximum number is:",Max,sep="   ")