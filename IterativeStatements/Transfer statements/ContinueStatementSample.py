
#print odd numbers between 0 to 10
# for i in range(11):
#     if i%2 == 0:
#         continue
#     print(i)

#Another example for processing items in cart by skipping the items greater than 500 saying it needs insurance

cart = [100,250,75,525,300,675,45]
for item in cart:
    if item > 500:
        print("Cost of this item is {}.".format(item),"Need insurance for this item")
        continue
    print("processed",item)