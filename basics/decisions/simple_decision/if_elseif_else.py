# Ask user what direction they want Beep to paint
print("Towards which direction should I paint (up, down, left or right)?")
direction = input()

# Check the users input and output depending on input
if direction == "up":
    print("I am painting in the upward direction!")
elif direction == "down":
    print("I am painting in the downward direction!")
elif direction == "left":
    print("I am painting in the leftward direction!")
elif direction == "right":
    print("I am painting in the rightward direction!")
else:
    print("Not sure which direction in am painting in!")
