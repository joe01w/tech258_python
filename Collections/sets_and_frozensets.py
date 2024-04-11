# Sets and Frozen Sets

# Create a set

fruits = {"apple", "banana", "cherry"}
print(fruits)

# Sets are UNORDERED and UNINDEXED

fruits.add("orange")
print(fruits)

# Remove an element
fruits.remove("apple")
print(fruits)

# Attempt to add a duplicate
# There can be no duplicates in a set
fruits.add("banana")
print(fruits)

# Convert list to a set to remove duplicates
example = ["one", "two", "three", "one"]
no_dupes = set(example)
print(no_dupes)

# Set Operations
set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}

print(set_a - set_b)