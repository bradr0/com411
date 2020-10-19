# Ask user to imput data
print("What is your name?")
name = input()

print("How old are you?")
age = int(input())

print("How tall are you?")
height = float(input())

print("How much do you weigh?")
weight = float(input())

bmi = weight / (height * 2)

print(name, "you are", age, "years old and your bmi is", bmi)
