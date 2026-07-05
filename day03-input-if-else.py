# Day 3: input() Function + if / elif / else Conditional Branching
# Goal: Learn to get user input and execute different branches based on it

print("Welcome to the conditional judgment practice program.")
print("Enter your choice, and I'll respond accordingly.\n")

# Get user input and strip leading/trailing whitespace
choice = input("Enter a word (happy / tired / hungry / other): ").strip()

# Convert input to lowercase for case-insensitive comparison
choice_lower = choice.lower()

# Use if-elif-else for multi-branch judgment
if choice_lower == "happy":
    print("Great! Keep it up.")
elif choice_lower == "tired":
    print("Take it easy, remember to rest.")
elif choice_lower == "hungry":
    print("Go eat something, don't starve yourself.")
else:
    print(f"Received: {choice}. Noted.")

# Extra interaction: ask if the user wants to try again
again = input("\nWant to try again? (yes/no): ").strip()
if again.lower() in ("yes", "y"):
    print("Restarting... just kidding, this is a simple demo.")
else:
    print("Thanks for playing! Goodbye.")
