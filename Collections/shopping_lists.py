# Lists

# Collections are a way to store multiple pieces of data in one reference/object
# Lists are the most common/simplest collection

# Lists are often known as arrays in other languages

# Create a list called 'shopping_list' with the following items:
# eggs
# bread
# bananas
# biscuits
# milk

shopping_list = ["eggs", "bread", "bananas", "biscuits", "milk"]

# Print the list to the screen
print(shopping_list)
# or another way is
print("The shopping list is: " + str(shopping_list))
# Print the data type of 'shopping_list'
print(type(shopping_list))
# Print the first item in the list
print(shopping_list[0])
# Print the last item in the list
print(shopping_list[-1])

# Change the second item in the list (i.e. 'bread') to 'rice' instead, then print the second item to the screen to prove it's been changed

shopping_list.insert(2, "rice")
shopping_list.remove("bread")
print(shopping_list)

# Use the list's method to add the item 'carrots' to the list (you should not re-assign the list using '='), then check the length of the list (which should now have 6 rather than 5)

shopping_list.append("carrots")
print(len(shopping_list))

#  Add another list with two items ('toffee' and 'coffee') to the 'shopping_list' list. Use one of the list's methods to add the two items in at the same time.

shopping_list_extra = ["toffee", "coffee"]
shopping_list.extend(shopping_list_extra)
print(shopping_list)

# Remove "bananas" from 'shopping_list'. Print 'shopping_list' to check it's been removed.

shopping_list.remove("bananas")
print(shopping_list)

# Remove the last item ('coffee') from 'shopping_list' using the pop method. Check it worked by printing 'shopping_list'

shopping_list.pop()
print(shopping_list)

# Use the "append" method to add an item to your list

shopping_list.append("lettuce")
print(shopping_list)