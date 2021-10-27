# Ask the user to enter the type of adventure
print("What type of adventure should Beep go on?")
adventure = input()

# Display output from user input
if (adventure == "scary") or (adventure == "short"):
    print("Entering the dark forest!")
elif (adventure == "safe") or (adventure == "long"):
    print("Taking the safe route!")
else:
    print("Not sure which route to take.")
