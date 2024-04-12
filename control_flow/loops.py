# Loops

list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1, 2, 3], [4, 5, 6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"},
             3: {"name": "Roscoe", "money": "$1.14"}}

# For Loops

# 1. Under the starter code, write a loop to print double each number in the list "list_data"
for num in list_data:
    print(num * 2)

# 2. Write another loop on the next line, this one should print items inside of the "embedded_lists" list.
print("New Question")
for sublist in embedded_lists:
    for item in sublist:
        print(item)

# 3. Create another loop inside of the "embedded_lists" for loop to list each individual item in each list.
print("New Question")
for l in embedded_lists:
    print(l)
    for num in l:
        print(num)

# 4. Write a new loop on a new line. This one should loop through the dictionary "dict_data".
print("New Question")
for key, value in dict_data.items():
    print(f"Key: {key}, Value: {value}")

# 6. Copy and paste your last loop on a newline. Create an embedded loop (loop inside the loop you pasted) to extract and print the values within the dictionary of each ittem WITHIN THAT dictionary.
print("New Question")
for value in dict_data.values():
    print(value.get("money"))

# While Loops
print("new question")
x = 0

while x < 10:
    print(f"x is {x}")
    # x = x + 1
    x += 1  # infinite loop without this
    if x > 4:
        break

# fizzbuzz

x = 0
while x < 101:

    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("fizz")
    elif x % 5 == 0:
        print("buzz")
    else:
        print(x)
    x += 1