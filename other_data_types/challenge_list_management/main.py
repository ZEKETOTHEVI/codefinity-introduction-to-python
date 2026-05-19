#Deli item by initialising, updating and organising them across different categories
meat = ["Ham", 3.99, 50, "Sliced"] #meat list
cheese = ["Cheddar", 5.49, 75, "Spicy"]
condiment = ["Mustard", 1.99, 75, "Spicy"]
deli_dept = [meat, cheese, condiment]
#print(deli_dept)
#list(deli_dept).sort() conversion string to list and sort.() method
#print(deli_dept)
# 3. Restock item
if "Ham" in meat and meat[2] < 100: #restock item
    meat[2] = 100 # Update the quanity for ham selection
    #print(meat)
# 4. Add Seasonal meat
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
deli_dept.append(seasonal_meat)
#print(deli_dept)
# 5. Remove Condiment 
deli_dept.remove(condiment)
print(f"Initial Deli List: {deli_dept}")
# 6.Sort list
deli_dept.sort()
#print(deli_dept)
#OUTPUT
print(f"Updated Deli List: {deli_dept}")
