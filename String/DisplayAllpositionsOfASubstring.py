str = input("Enter a string: ")
substr = input("Enter a substring: ")

index=-1;
flag = False
length = len(str)

while True:
    index = str.find(substr,index+1,length)
    if index == -1:
        break
    print("substring {x} found at index {y} in string {z}".format(x=substr,y=index,z=str))
    flag = True

if flag == False:
    print("Substring {x} is not found in string {y}".format(x=substr,y=str))