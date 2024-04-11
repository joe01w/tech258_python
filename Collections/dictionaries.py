# Dictionaries

# key = value pairs
# key is the reference, value is the data storage mechanism you want (int, string etc.)

student1 = {
    "name": "susan",
    "stream": "tech",
    "completed_lessons": 4,
    "completed_lesson_names": ["variables", "data_types", "set_up", "collections"]
}

print(student1["stream"])
print(student1["completed_lesson_names"][0])
student1["completed_lessons"] = 3
print(student1["completed_lessons"])
student1["completed_lesson_names"].remove("collections")
print(student1["completed_lesson_names"])

# getting keys for the dictionary
print(student1.keys())

# Hero Story (Dictionaries Task)

# Define a dictionary called story1. It should have the following keys:
# 'start', 'middle' and 'end'

story1 = {
    "start": "It's 10am on a sunday, and you're starving.",
    "middle": "Luckily, Fry-up man is here to save the day!",
    "end": "Fry-up man makes you a delicious fry-up. The end.",
    "hero": "Fry-up man"
}

# Print the entire dictionary

print(story1)

# Print the type of your dictionary

print(type(story1))

# Print only the keys

print(story1.keys())

# Print only the values

print(story1.values())

# Print the individual values using the keys (individually, lots of print commands)

print(story1["start"])
print(story1["middle"])
print(story1["end"])

# Now, let's add a new key:value pair:
# 'hero': yourSuperHero

print(story1["hero"])