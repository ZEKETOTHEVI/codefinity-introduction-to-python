start_number = 5
countdown_values = []
# # Handling a queue at a grocery store checkout
# queue_length = 5  # Initial number of people in the queue
# while queue_length > 0:  # Start the `while` loop as long as the queue isn't empty
#     print(f"Current queue size: {queue_length}")
    
#     # Simulate serving a customer
#     print("Serving the next customer...")
    
#     # Decrease the queue length by 1 as a customer leaves
#     # The `-=` operator is a shortcut for `queue_length = queue_length - 1`
#     queue_length -= 1
# Initial amount of milk in stock
milk_stock = 15
# Minimum stock level before restocking is necessary
min_stock = 50
# Quantity a worker can restock at one time
restock_quantity = 20

# # Start the loop to restock milk until the stock exceeds the minimum required level
# while milk_stock < min_stock:
#     # If the loop is running, the condition is `True`, indicating we need more milk
#     print(f"Milk stock is low: {milk_stock} units remaining.")
#     # Simulate the process of restocking milk
#     print("Restocking milk...")
#     # Increase the stock by the quantity the worker can bring in one trip
#     milk_stock += restock_quantity
    
# # Output the final stock level after restocking is complete
# print(f"Milk stock updated: {milk_stock} units, which is now sufficient.")


# My task
# Use a while loop to count down from start_number to 1 (inclusive), decrementing by 1 each iteration
start_number = 5
countdown_values = []
while start_number >= 1:
    countdown_values.append(start_number)
    start_number -= 1
print("Discount countdown complete!", countdown_values)