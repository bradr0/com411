# Print message to user
print("Calculating the sum of the first 100 numbers...")

number = 1
answer = 0

# Calculate the sum of the numbers
while number <= 100:
    answer = answer + number
    number = number + 1

# Print answer to user
print(f"Done... The answer is {answer}")
