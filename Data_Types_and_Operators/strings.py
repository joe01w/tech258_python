# Strings

# single_quotes = 'Look! Single Quotes'
# double_quotes - "Look! Double quotes!"

# Generally prefer double quotes, as single quotes are used for other things

# bad_string = 'It's not right''
# good_string = "It's not right"

# String Slicing

Hw = "Hello World!"

#How many characters are in this string
#use len()
print(len(Hw))

# how to target a character in a string
print(Hw[0])
# The number in the square brackets dictates which character is printed
# The first character of any string is 0

# how to target the last character of the string
print(Hw[-1])
# the negative means it starts from the end of the string

#Use negative indexing to get the second to last character
print(Hw[-2])

#Use string slicing to get the first 3 characters only
print(Hw[:3])

print(Hw[5:])
# Very useful website : https://www.codecademy.com/learn/dacp-python-fundamentals/modules/dscp-python-strings/cheatsheet

# String Methods
White_space = "lot's of white space at the end                                        "
print(len(White_space))
print(len(White_space.strip()))

example_string = "Here's some text with lots of text"
# Count a substring within a string
print(example_string.count("text"))

# Make a string lowercase
print(example_string.lower())

#Make a string uppercase
print(example_string.upper())

# Make a string capitalised
print(example_string.capitalize())

#Replacing text
print(example_string.replace("with ", ","))

#Concatenation and Casting

a = "here "
b = "more "
c = "much more "

print(a + b +c)

x = 2
y = 5.4
z = " there's now a number 25.4 unless we put a space in!"
w = "30"

print(str(x) + " " + str(y) + z)
print(x + y + int(w))

# F-string

name = "Lassie"
years = 7
height_cm = 60.2

print(f"{name} is {years} years old and {height_cm} cm tall")

name = "Snoopy"
years = 52

print(f"{name.upper()} IS {years * 7} YEARS OLD IN DOG YEARS")

# Using F-Strings to format numbers

pi = 3.14159265359

# Use an f-string to print pi to 3 decimal places
print(f"{pi:.3f}")

# Use an f-string to print pi to 5 decimal places
print(f"{pi:.5f}")

score = 16
max_score = 26

print(f"You scored {score/max_score}")
print(f"You scored {score/max_score:%}")
print(f"You scored {score/max_score:.2%}")
print(f"You scored {score/max_score:.0%}")

name = "Joe"
years = 23
height_cm = 10
address = "7 Birstal Green"
hobbies = "Music and Carrot Cake"

print(f"{name} is {years} years old and {height_cm} cm tall")
print(f"{name} is {years * 7} years old in dog years.")
print(name + " lives at " + address + " and his hobbies are " + hobbies + ".")