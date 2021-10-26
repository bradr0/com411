# Ask user to input a whole number
print("Please input a whole number")
number = int(input())

# Print output to user
if number % 2 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")
