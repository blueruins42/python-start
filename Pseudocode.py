# the elif statement
if the_weather_is_good:
    go_for_a_walk()
elif tickets_are_available:
    go_to_the_theater()
elif table_is_available:
    go_for_lunch()
else:
    play_chess_at_home()

# code exercies
Number1 = int(input("Enter the first number:"))
Number2 = int(input("Enter the second number:"))
Number3 = int(input("Enter the third number:"))
the_largest_number = Number1
if Number2 > the_largest_number:
        the_largest_number = Number2
if Number3 > the_largest_number:
        the_largest_number = Number3
print("The largest number is:", the_largest_number)

# Pseudocode
largest_number = -999999999
number = int(input())
if number == -1:
    print(largest_number)
    exit()
if number > largest_number:
    largest_number = number
# Go to line 02

