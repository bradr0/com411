# How many numbers should I sum up?
print("How many numbers should I sum up?")
numbers = int(input())

summed = 0
answer = 0

while summed < numbers:
    summed = summed + 1
    print(f"Please enter number {summed} of {numbers}")
    number = int(input())
    answer = answer + number

# Print answer to user
print(f"The answer is {answer}")
