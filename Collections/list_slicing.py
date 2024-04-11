# List Slicing

mixture = [1, 2, 3, "one", "two", "three"]
print(mixture)

print(mixture[1:3]) # --> This will return [2, 3]
print(mixture[::2]) # --> This will return [1, 3, "two"] This is everyone other item in the list.

# String Slicing Game

# Guess the word with 4 hints to help
# Rationale: Practice word slicing
# Type of exercise: Finish the code
original_word = "recommendation"
scrambled_word = "eoommandretnic"
# Create the hint slices...
hint1_slice = original_word[4:6]  # Create the word slice according to the clue below
hint2_slice = original_word[-3:]  # Create the word slice according to the clue below
hint3_slice = original_word[7:10]  # Create the word slice according to the clue below
hint4_slice = original_word[:2]  # Create the word slice according to the clue below

# Game instructions
print("Scrambled word:", scrambled_word)
print("Guess the original word from the scrambled version.")
print("Here are some hints:")

# Hints based on list slicing
print("Hint 1: The 5th and 6th letters are:", hint1_slice)
print("Hint 2: The last 3 letters are:", hint2_slice)
print("Hint 3: The 8th to 10th letters are:", hint3_slice)
print("Hint 4: The first two letters are:", hint4_slice)
# Game ends here
print("What's your guess?")
user_guess = input()
if user_guess == original_word:
    print("That's correct")
else:
    print("Sorry, that's not correct, please play again")

