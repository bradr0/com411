# Ask the user what the book cover is
print("What type of cover does the book have?")
cover = input()

# Show user output
if cover == "soft":
    print("Is the book perfect-bound?")
    perfect = input()

    if perfect == "yes":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")
else:
    print("Books with hard covers can be more expensive!")
