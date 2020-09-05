
cart = [10,20,30,30,520,46]

for item in cart:
    if item > 500:
        print("Needs insurance for this item because item value is",item)
        break
    print("item processed",item)
else:
    print("Congratulations. All items have been successfully processed.")