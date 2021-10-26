# Ask user to input numbers
print("Please enter the first number")
first = int(input())

print("Please enter the second number")
second = int(input())

# Output message depending on inputs
if first < second:
    print("The first number is the smallest!")
elif first > second:
    print("The second number is the smallest!")
else:
    print("Both are equal!")
