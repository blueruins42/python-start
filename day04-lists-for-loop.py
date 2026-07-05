# Day 4: Lists + for Loop — while Loop Basics
# Goal: Learn to create lists, add elements, iterate, and collect user input with loops

print("Enter items one by one. Type 'done' to stop.")

# Create an empty list
items = []

# Use while True for "infinite input until exit"
while True:
    user_input = input("Enter an item (type 'done' to exit): ").strip()

    if user_input.lower() == "done":
        break  # Exit the loop

    if user_input:  # Avoid adding empty strings
        items.append(user_input)
        print(f"Added: {user_input}")
    else:
        print("Input is empty, please try again.")

# Iterate over the list and print with index
print("\nYour entries:")
if items:
    for index, value in enumerate(items, start=1):
        print(f"  {index}. {value}")
else:
    print("  (No entries)")
