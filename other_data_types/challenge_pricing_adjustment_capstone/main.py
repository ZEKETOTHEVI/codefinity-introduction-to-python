#managing grocery store's sytem and need to maintain a decision making inventory, track prices and perfom check to deterime if action like restocking and removing items from inventory
#Create grocery store inventory dictionary
grocery_inventory = {
    "Milk": ("Dairy", 3.50,  8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)
    
}
print(grocery_inventory)
update_egg_price = grocery_inventory["Eggs"][1]
if update_egg_price > 5:
    category, price, stock = grocery_inventory["Eggs"]
    grocery_inventory["Eggs"] = (category, price - 1, stock) 
    print("Eggs are too expensive, reducing the price by $1.")
else:
    print("The price of Eggs is reasonable.")
#New inventory entry Tomatoes
grocery_inventory["Tomatoes"] = ("Produce", 1.20, 30)
print("Inventory after adding Tomatoes:", grocery_inventory["Tomatoes"])
#Restock Milk
restock_milk = grocery_inventory["Milk"][2]
if restock_milk < 10:
    category, price, stock = grocery_inventory["Milk"]
    grocery_inventory["Milk"] = (category, price, stock + 20)
    print("Milk needs to be restocked. Increasing stock by 20 units.")
else:
    print("Milk has sufficient stock.")
remove_apples = grocery_inventory["Apples"][1]
if remove_apples > 2:
    print("Apples removed from inventory due to high price")
print("Updated inventory:", grocery_inventory)