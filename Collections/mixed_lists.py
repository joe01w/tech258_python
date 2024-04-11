# Mixed Lists

# Lists can hold different data types, for example:

mixture = [1, 2, 3, "one", "two", "three"]
print(mixture)

# 1. Use your code from the "Task: Get name, age and DOB details from a user".
# 2. Mix the name, age and DOB into one list user_details_list
# 3. Print the user's name, age and DOB from the list
# 4. Check the age is saved as an integer in the list. If it's not, work out how to convert it to an integer and add the age integer to the list.
# 5. Ask the user for their height in cm and save it to the variable height
# 6. Save height as a float in the list, and print the height from the list.

name = input("What is your name? ")
age = input("What is your age? ")
dob = input("What is your date of birth? ")
height = input("What is your height in cm? ")
user_details_list = [name, int(age), dob, float(height)]
print(user_details_list)
print("Hi " + user_details_list[0])
print(user_details_list[1])
print(user_details_list[2])
print(user_details_list[3])