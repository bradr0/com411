# Ask user to enter first number
print("Please enter the first whole number")
first = int(input())

print("Please enter the second whole number")
second = int(input())

print("Please enter the third whole number")
third = int(input())

# Start counters at 0
even = 0
odd = 0

# Check what numbers are even and what ones are odd
if first % 2 == 0:
    even = even + 1
else:
    odd = odd + 1

if second % 2 == 0:
    even = even + 1
else:
    odd = odd + 1

if third % 2 == 0:
    even = even + 1
else:
    odd = odd + 1

# Display output from all 3 numbers
print(f"There were {even} even and {odd} odd numbers")
