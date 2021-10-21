# User input for amount of lives
print("Please enter the number of lives.")
lives = int(input())

# User input for energy level
print("Please enter the energy level.")
energy = int(input())

# User input for shield level
print("Please enter the shield level.")
shield = int(input())

# Print all outputs with inputs
print(f"Lives: {'♥' * lives}")
print(f"Energy {'♦' * energy}")
print(f"Shield {'♦' * shield}")
