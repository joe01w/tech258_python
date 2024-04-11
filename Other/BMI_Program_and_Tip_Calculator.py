# BMI Program

height_m = float(input("Enter the height in m: "))
weight_kg = float(input("Enter the weight in kg: "))

bmi = weight_kg / (height_m ** 2)

print(f"Your BMI is {bmi}.")

# Tip Calculator that allows the addition of a tip and splits the bill numerous ways

# Get the bill from the user
initial_bill = float(input("How much is your bill? "))

# Calculate the tip (Assume its 15%)
tip = initial_bill * 0.15

#Calculate the bill with the tip added
total_bill = initial_bill + tip

# Ask how many people they want to split it with
participants = int(input("How many people do you want to split the bill with? "))

# Calculate the bill divided by the split amount
individual_bill = total_bill / participants

# Print the split bill per person, being rounded to 2dp
print(f"Bill per person: {individual_bill:.2f}")