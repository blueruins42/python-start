# Day 2: Variables + f-strings
my_name = "shooting"  # String — must be quoted
my_age = 35           # Integer — no quotes
message = "I'm about to write my first Python syntax."

print(f"My name is {my_name}, I just turned {my_age}, and {message}")

# Define the current year (number, no quotes)
current_year = 2026

# Calculate how many years until I turn 100
years_to_wait = 100 - my_age

# Calculate the year I'll turn 100
year_of_100 = current_year + years_to_wait

# Print the result
print("When I turn 100, it will be:")
print(year_of_100)

# Alternative: comma-separated output
print("When I turn 100, it will be:", year_of_100)

# Alternative: f-string formatting
print(f"When I turn 100, it will be: {year_of_100}")
