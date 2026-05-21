# Loop through the list using indices (use range(len(prices))). 
# For each index i, take the current price as prices[i], apply a discount, update the value in the list, and print the result.
prices = [29.99, 45.50, 12.75, 38.20]
updated_price = []
# discount rules:

# Index 0 → 10% discount
# Index 1 → 20% discount
# Index 2 → 15% discount
# Index 3 → 5% discount
discount_factor = [0.1,0.2,0.15,0.05]
for i in  range(len(prices)):
    original_price =  prices[i] 
    discount = discount_factor[i]
    index = discount_factor[i] * 100
    new_price = original_price *(1 - discount)
    updated_price.append(new_price)
    prices[i] = new_price
    # print(updated_price)
    print(f"Updated price for item {i}: ${new_price:.2f}")
# # List of grocery items
# grocery_list = ["Apples", "Bananas", "Carrots", "Cucumbers"]

# # Initialize a for loop to iterate over indexes
# for item in range(len(grocery_list)):
#     print("Index:", item)
#     print("Item:", grocery_list[item])
#     print("----")  # Printing a divider line for clarity
# List of original prices of grocery items
# prices = [1.50, 2.00, 0.75, 3.25]

# # Discount factor (10% off each item)
# discount_factor = 0.10

# # Iterate over the list of prices using range(len())
# for cost in range(len(prices)):
#     # Apply the discount by reducing the price
#     prices[cost] -= prices[cost] * discount_factor
#     print(f"New price of item {cost + 1}: ${prices[cost]}")

# print("Updated prices:", prices)
