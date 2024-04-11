# Task 1: Waiter Helper
# Script should act like a waiter at a restaurant taking orders

# Greet the user
print("Welcome to the restaurant! Let's take your order.")

# Print a list of starters
starters = ["Soup", "Salad", "Bread"]
print("Our starters are " + str(starters))

# Take an input for the user for their starter
starter_choice = int(input("Please enter the number of your starter choice: "))
selected_starter = starters[starter_choice - 1]

# Print a list of mains
mains = ["Pie", "Pasta", "Cheeseburger"]
print("Our mains are " + str(mains))

# Take an input for the user for their main course
main_choice = int(input("Please enter the number of your main choice: "))
selected_main = mains[main_choice - 1]

# Print a list of desserts
desserts = ["Ice Cream", "Crumble", "Cheese Board"]
print("Our desserts are " + str(desserts))

# Take an input for the user for their dessert
dessert_choice = int(input("Please enter the number of your dessert choice: "))
selected_dessert = desserts[dessert_choice - 1]

# Print all of the user's choices
print("You have ordered: " + selected_starter + ", " + selected_main + " and " + selected_dessert + ".")

# level 2
# Use at least one f-string
print("\nYour order:")
print(f"Starter: {selected_starter}")
print(f"Main course: {selected_main}")
print(f"Dessert: {selected_dessert}")

# Add each item ordered to a list called 'customer_order_list'

customer_order_list = []
customer_order_list.append(selected_starter)
customer_order_list.append(selected_main)
customer_order_list.append(selected_dessert)
print(customer_order_list)