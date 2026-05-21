# List of products on promotion for each weekday
daily_promotions = ["Milk", "Eggs", "Bread", "Apples", "Oranges"]

# List of weekdays corresponding to the promotions
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
#Variable created for loop
for day in range (5):
    current_weekday = weekdays[day]
    current_promotions = daily_promotions[day]
    print(f"{current_weekday}: Promotion on {current_promotions}")
    

# # Announce store opening every day for 7 days
# for day in range(7):
#     print(f"Good morning! The store is now open on day {day}.")
# # Planning seasonal sale days in the last week of December
# for day in range(25, 32):
#     print(f"Seasonal sale on December {day}.") 
# Schedule staff shifts every three hours throughout a 12-hour day
# for hour in range(1, 13, 3):
#     print(f"Staff shift starts at hour {hour}.")
# List of daily tasks for a week
# weekly_tasks = [
#     "Restock Fruits",
#     "Clean Dairy Section",
#     "Review Meat Inventory",
#     "Restock Vegetables",
#     "Check Bakery Expiry Dates",
#     "Organize Front Displays",
#     "Prepare Weekly Sales Report"
# ]

# # List of weekdays corresponding to each task
# weekdays = [
#     "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
# ]

# # Loop through each day using the range function
# for day in range(7):
#     task = weekly_tasks[day]  # Access the task corresponding to the current day
#     weekday = weekdays[day]   # Access the corresponding weekday
#     print(f"{weekday} Task: {task}")