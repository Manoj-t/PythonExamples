# for i in range(10):
#     if i==7:
#         print("Processing is enough. please break!")
#         break
#     print(i)


# Another Example for break
#processing of all items added in the cart

cart = [10,20,25,200,35,65]

#processing starts
for item in cart:
    if item>100:
        print("This item price is",str(item)+".","Any item > 100 requires insurance." )
        break
    print(item)

