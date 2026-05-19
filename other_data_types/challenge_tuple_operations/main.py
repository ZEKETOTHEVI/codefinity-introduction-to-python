# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")
#Count to deterime how many time apple appear in tuples to check current stock
apple_count = shelf.count("apples")
#The position in the iex for the first occurence of bananna
banana_index = shelf.index("bananas")
#Check the stock of apples is less than 5
print("Number of Apples:", apple_count)
if apple_count < 5:
    print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked.")
print("First Banana Index:", banana_index)
#Check the stocks on grapes, stock control
grape_count = shelf.count("grapes")
if grape_count == 1:
    print("Grapes need to be restocked.")
else:
    print("Grapes are sufficiently stocked.")
#Check if oranges exist in the shelf inventory 
orange_index = shelf.index("oranges")
if "oranges" in shelf:
    print("Oranges are at index:", orange_index)
else:
    print("Oranges are out of stock", orange_index)
#Output inventory stock 

print()