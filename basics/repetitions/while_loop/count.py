# Ask how many cables Beep needs to avoid
print("How many lives cables must I avoid?")
cables = int(input())

cables_avoided = 0

# Avoid the cables
while cables_avoided < cables:
    print("Avoiding...", end="")
    cables_avoided = cables_avoided + 1
    print(f"Done! {cables_avoided} cables avoided.")
