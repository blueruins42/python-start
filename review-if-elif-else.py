# version 1
year = int(input("Enter a year: "))

if year < 1582:
    print("Not within the Gregorian calendar period")
else:
    if year % 4 != 0:
        print("common year")
    elif year % 100 != 0:
        print("leap year")
    elif year % 400 != 0:
        print("common year")
    else:
        print("leap year")

# optimize version
year = int(input("Enter a year: "))

if year < 1582:
    print("Not within the Gregorian calendar period")
elif year % 4 != 0:
    print("common year")
elif year % 100 != 0:
    print("leap year")
elif year % 400 != 0:
    print("common year")
else:
    print("leap year")

# if and if-elif-else
x = 10
 
if x == 10:          # ← if
    print("x == 10")
 
if x > 15:           # ← new if
    print("x > 15")
elif x > 10:
    print("x > 10")
elif x > 5:
    print("x > 5")
else:
    print("else will not be executed")

# Nested if-elif-else
x = 10

if x > 5: # True
    if x == 6: # False
        print("nested: x == 6")
    elif x == 10: # True
        print("nested: x == 10")
    else:
        print("nested: else")
else:
    print("else")

