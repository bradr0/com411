# Ask user their name
print("What is your name human?")
name = input()

# Ask user their age
print("How old are you (in years)?")
age = int(input())

# Ask user how tall they are
print("How tall are you (in meters)?")
height = float(input())

# Are user how much they weigh
print("How much do you weigh (in kilograms)?")
weight = float(input())

# Calculate the users bmi
bmi = weight / (height ** 2)

# Print message to the user with all inputs
print(f"{name} you are {age} years old and your bmi is {bmi}")
